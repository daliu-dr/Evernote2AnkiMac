#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, subprocess
from datetime import datetime
import time

import envoy

import anki
import aqt
from anki.hooks import wrap
from aqt.preferences import Preferences
from aqt.utils import showInfo, getText, openLink, getOnlyText
from aqt.qt import QLineEdit, QLabel, QVBoxLayout, QGroupBox, SIGNAL, QCheckBox, QComboBox, QSpacerItem, QSizePolicy, QWidget
from aqt import mw, editor
# from pprint import pprint

import re
from BeautifulSoup import BeautifulSoup, Tag


# debugging memory leak; its very ressource-intensive and will slow down the script heavily!
#sys.path.append("" + os.path.dirname(os.path.realpath(__file__)))
#from pympler.tracker import SummaryTracker
#tracker = SummaryTracker()
# use this in code: tracker.print_diff()


# Note: This class was adapted from the Real-Time_Import_for_use_with_the_Rikaisama_Firefox_Extension plug-in
# by cb4960@gmail.com
# .. itself adapted from Yomichan plugin by Alex Yatskov.

PATH = os.path.dirname(os.path.abspath(__file__))
EVERNOTE_NOTETYPE_DEFAULT = 'EvernoteDefault'
EVERNOTE_NOTETYPE_HIGHLIGHTS = 'EvernoteHighlights'
EVERNOTE_TEMPLATE_DEFAULT = 'Review'
EVERNOTE_TEMPLATE_HIGHLIGHTS = 'Highlights'
TITLE_FIELD_NAME = 'title'
CONTENT_FIELD_NAME = 'content'
MODIFIED_FIELD_NAME = 'Evernote modified'
GUID_FIELD_NAME = 'Evernote GUID'

USE_APPLESCRIPT = False
import platform
if platform.system() == "Darwin":
    # add PyObjC to system path so it may be automatically included by py-applescript
    sys.path.append("" + os.path.dirname(os.path.realpath(__file__)) + "/PyObjC")
    import applescript
    if applescript.AppleScript('name of application "Evernote"').run() == "Evernote":
        USE_APPLESCRIPT = {}

SETTING_UPDATE_EXISTING_NOTES = 'evernoteUpdateExistingNotes'
SETTING_TOKEN = 'evernoteToken'
SETTING_KEEP_TAGS = 'evernoteKeepTags'
SETTING_TAGS_TO_IMPORT = 'evernoteTagsToImport'
SETTING_DEFAULT_TAG = 'evernoteDefaultTag'
SETTING_DEFAULT_DECK = 'evernoteDefaultDeck'

class UpdateExistingNotes:
    IgnoreExistingNotes, UpdateNotesInPlace, DeleteAndReAddNotes = range(3)


# Anki-specific
# Adding, updating, deleting notes in Anki
class Anki:
    
    # Update cards
    def update_evernote_cards(self, evernote_cards, tag):
        # We don't provide a 'deck'; in case the user has 
        # moved the card to another deck it stays there
        return self.add_evernote_cards(evernote_cards, None, tag, True)
    
    # Add new cards
    def add_evernote_cards(self, evernote_cards, deck, tag, update=False):
        count = 0
        model_name = EVERNOTE_NOTETYPE_DEFAULT

        for card in evernote_cards:
            #sys.stderr.write(card+"\n")
            # seconds from epoch when this note was last modified in evernote
            # -> so we can check with this value if it has changed since last import
            modified_in_seconds_from_epoch = int((card.modified-datetime.utcfromtimestamp(0)).total_seconds())


            card.tags.append(tag)
            anki_field_info = {TITLE_FIELD_NAME: card.front.decode('utf-8'),
                               CONTENT_FIELD_NAME: card.back.decode('utf-8'),
                               MODIFIED_FIELD_NAME: str(modified_in_seconds_from_epoch),
                               GUID_FIELD_NAME: card.guid}
    
            if update:
                self.update_card(anki_field_info, card.tags, card.attachments)
            else:
                self.add_card(deck, model_name, anki_field_info, card.tags, card.attachments)
            count += 1
        return count

    # TODO: desc
    def delete_anki_cards(self, guid_ids):
        col = self.collection()
        card_ids = []
        for guid in guid_ids:
            card_ids += mw.col.findCards(guid)
        col.remCards(card_ids)
        return len(card_ids)

    # Update a single card
    def update_card(self, fields, tags=list(), attachments=None):
        col = self.collection()
        note_id = col.findNotes(fields[GUID_FIELD_NAME])[0]
        note = anki.notes.Note(col, None, note_id)

        # if note is marked (tag "Marked"), readd "Marked" to new tags also
        if "Marked" in note.tags:
            tags.append("Marked")
            note.tags = tags
        else:
            note.tags = tags

        # TODO: only update when new modified value > old value
        # go through all fields until modified is found
        for fld in note._model['flds']:
            if MODIFIED_FIELD_NAME in fld.get('name'):
                if fields[MODIFIED_FIELD_NAME] > note.fields[fld.get('ord')]:

                    # go through fields again and update
                    for fld in note._model['flds']:
                        if TITLE_FIELD_NAME in fld.get('name'):
                            note.fields[fld.get('ord')] = fields[TITLE_FIELD_NAME]
                        elif CONTENT_FIELD_NAME in fld.get('name'):
                            note.fields[fld.get('ord')] = self.parse_content(fields[CONTENT_FIELD_NAME], attachments, tags)
                        # we dont have to update the evernote guid because if it changes we would not find this note anyway
                        
        note.flush()
        return note.id

    # TODO: desc
    def add_card(self, deck_name, model_name, fields, tags=list(), attachments=None):
        note = self.create_card(deck_name, model_name, fields, tags, attachments)
        if note is not None:
            collection = self.collection()
            collection.addNote(note)
            collection.autosave()
            self.start_editing()
            return note.id

    # TODO: desc
    def create_card(self, deck_name, model_name, fields, tags=list(), attachments=None):
        id_deck = self.decks().id(deck_name)
        model = self.models().byName(model_name)
        col = self.collection()
        note = anki.notes.Note(col, model)
        note.model()['did'] = id_deck
        note.tags = tags

        # parse content
        fields[CONTENT_FIELD_NAME] = self.parse_content(fields[CONTENT_FIELD_NAME], attachments, tags)

        for name, value in fields.items():
            note[name] = value
        return note

    # create Evernote note type to be used by all notes
    def create_note_type_default(self):  # adapted from the IREAD plug-in from Frank
        col = self.collection()
        mm = col.models
        evernote_notetype = mm.byName(EVERNOTE_NOTETYPE_DEFAULT)
        if evernote_notetype is None:
            evernote_notetype = mm.new(EVERNOTE_NOTETYPE_DEFAULT)
            # Field for title:
            model_field = mm.newField(TITLE_FIELD_NAME)
            mm.addField(evernote_notetype, model_field)
            # Field for text:
            text_field = mm.newField(CONTENT_FIELD_NAME)
            mm.addField(evernote_notetype, text_field)
            # Field for source:
            guid_field = mm.newField(GUID_FIELD_NAME)
            guid_field['sticky'] = True
            mm.addField(evernote_notetype, guid_field)
            # Field for Evernote modified date:
            modified_field = mm.newField(MODIFIED_FIELD_NAME)
            modified_field['sticky'] = True
            mm.addField(evernote_notetype, modified_field)
            # CSS
            evernote_notetype["css"] = """.card{}"""

            # Add template
            t = mm.newTemplate(EVERNOTE_TEMPLATE_DEFAULT)
            
            t['qfmt'] = """<h1>
{{""" + TITLE_FIELD_NAME + """}}
</h1>"""
            
            t['afmt'] = """{{FrontSide}}
<hr id=answer>
<div id="evernote2ankiHighlightsLinks" style="display: none;">
    <a href="#" onclick="goToFirstHighlight(); return false;">Go to first highlight</a> &nbsp; 
    <a href="" onclick="showAllHighlights(); return false;">Show all highlights</a> &nbsp; 
    <a href="" onclick="hideAllHighlights(); return false;">Hide all highlights</a>
</div>
{{""" + CONTENT_FIELD_NAME + """}}

<script type="text/javascript">
        var highlights = document.querySelectorAll("[style*=-evernote-highlight]");
        var arrayLength = highlights.length;
        if(arrayLength>0){
            document.getElementById("evernote2ankiHighlightsLinks").style.display = "block";
        }
        
        var hideAllHighlights = function(){
            for (var i = 0; i < arrayLength; i++) {
                var inner = highlights[i].innerHTML;
                highlights[i].innerHTML = "<span style='visibility:hidden'>"+inner+"</span>";
                // add click handler to show
                highlights[i].addEventListener("click", function() {
                    this.innerHTML = this.firstChild.innerHTML;
                });
            }
        }
        hideAllHighlights();

        var goToFirstHighlight = function() {
            highlights[0].scrollIntoView();
        }

        var showAllHighlights = function() {
            for (var i = 0; i < arrayLength; i++) {
                highlights[i].innerHTML = highlights[i].firstChild.innerHTML;
            }
        }
</script>"""
            mm.addTemplate(evernote_notetype, t)
            mm.add(evernote_notetype)
            return evernote_notetype
        else:
            fmap = mm.fieldMap(evernote_notetype)
            title_ord, title_field = fmap[TITLE_FIELD_NAME]
            text_ord, text_field = fmap[CONTENT_FIELD_NAME]
            guid_ord, guid_field = fmap[GUID_FIELD_NAME]
            modified_ord, modified_field = fmap[MODIFIED_FIELD_NAME]
            #TODO: what is sticky?
            guid_field['sticky'] = False

    # TODO: desc
    def get_guids_from_anki_id(self, ids):
        guids = []
        for a_id in ids:
            card = self.collection().getCard(a_id)
            items = card.note().items()
            # TODO: refactor!
            # wie komme ich sicher & zuverlässig an GUID?
            # [(u'title', u'highlight test'),
            #  (u'content',
            #   u'\n<div id="en-note">\n<div>ahjfdkla jklsdfjdlsk\xf6 ajsdflk\xf6:</div>\n<ul>\n<li>jadkslf fajdklfjsl\xf6</li>\n<li>adfjkl\xf6dsfsd sdsdfsd</li>\n<li>afdsjkl\xf6sd sfdjklfsdl\xf6</li>\n<li>Frage: ANTWORT</li>\n</ul>\n<div><br /></div>\n<div>jetzt noch eine Tabelle:</div>\n<div><br /></div>\n<table style="-evernote-table:true;border-collapse:collapse;width:100%;table-layout:fixed;margin-left:0px;">\n<tr>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div>ffff</div>\n</td>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div><span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">fajsdkl ajfkl\xf6sfdjl</span></div>\n</td>\n</tr>\n<tr>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div>fadsas fsdafjsdaf</div>\n</td>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div><span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">fdsafas fdsdsa</span></div>\n<div><span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">adfasdfd fdsfsafsa</span></div>\n<div><span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dsfasf</span></div>\n</td>\n</tr>\n<tr>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div>dfafaf sadfafsas</div>\n</td>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div><span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">asdfjalk\xf6f fadsadsfas</span></div>\n</td>\n</tr>\n<tr>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div>afjaklf sklfadf jklf sdfjkl</div>\n</td>\n<td style="border-style:solid;border-width:1px;border-color:rgb(219,219,219);padding:10px;margin:0px;width:50%;">\n<div>afsfklafjkl fdskljfaslk</div>\n</td>\n</tr>\n</table>\n<div><br /></div>\n<div><br /></div>\n<div><br /></div>\n</div>\n'),
            #  (u'Evernote GUID', u'80f8e492-fa45-4775-93e1-f70635d81cdd'),
            #  (u'Evernote modified', u'1460502874')]
            #  
            guids.append(items[2][1])  # not a very smart access
        return guids

    # TODO: desc
    def can_add_note(self, deck_name, model_name, fields):
        return bool(self.create_note(deck_name, model_name, fields))

    # TODO: desc
    def get_cards_id_from_tag(self, tag):
        query = "tag:" + tag
        ids = self.collection().findCards(query)
        return ids

    # import file to anki media library
    def import_file(self, filename):
        return aqt.mw.col.media.addFile(filename)

    # TODO: parse evernote content
    def parse_content(self, content, attachments, tags):

        soup = BeautifulSoup(content)
        pattern = re.compile(r'<.*?src="\?hash=(\w+?)".*?>')

        # images
        for match in soup.findAll('img'):

            filehashmatch = pattern.search(str(match))
            if filehashmatch:
                filehash = filehashmatch.group(1)
                filename = next((l['filename'] for l in attachments if l['hash'] == filehash), None)

                if filename is not None:
                    importedname = self.import_file(filename)
                    match.replaceWith(Tag(soup, 'img', [('src', importedname)]))


        # pdfs
        for match in soup.findAll('embed', {"type": "evernote/x-pdf"}):

            filehashmatch = pattern.search(str(match))
            if filehashmatch:
                filehash = filehashmatch.group(1)
                filename = next((l['filename'] for l in attachments if l['hash'] == filehash), None)

                if filename is not None:
                    # convert pdf -> image
                    images = pdf2image(filename)

                    # import each jpg
                    imageTags = Tag(soup, "span")
                    for image in images:
                        importedname = self.import_file(image)
                        # add new image tag
                        imageTags.insert(images.index(image), Tag(soup, 'img', [('src', importedname)]))

                    # replace embed with <img src...> for each image
                    match.replaceWith(imageTags)

        # TODO: audio
        # TODO: video


        #plugins          

        # TODO: qa-format as in Supermemo
        #for match in soup.find(string=re.compile("A:")):
        #    match['class'] = match.get('class', []) + ['Evernote2Anki-Highlight']
        


        return str(soup).decode('utf-8')

    # TODO: desc
    def start_editing(self):
        self.window().requireReset()

    # TODO: desc
    def stop_editing(self):
        if self.collection():
            self.window().maybeReset()


    # TODO: are these helper functions needed?
    def window(self):
        return aqt.mw

    def collection(self):
        return self.window().col

    def models(self):
        return self.collection().models

    def decks(self):
        return self.collection().decks



# TODO: desc
class EvernoteCard:
    front = ""
    back = ""
    guid = ""
    attachments = []
    modified = ""

    def __init__(self, q, a, g, tags, attachments, modified):
        self.front = q
        self.back = a
        self.guid = g
        self.tags = tags
        self.attachments = attachments
        self.modified = modified


# TODO: desc
class Evernote:
    def __init__(self):

        # TODO: display error message if evernote not installed?
        pass


    # TODO: desc
    def find_tag_guid(self, tag):
        list_tags = self.noteStore.listTags()
        for evernote_tag in list_tags:
            if str(evernote_tag.name).strip() == str(tag).strip():
                return evernote_tag.guid

    # TODO: desc
    def create_evernote_cards(self, guid_set):
        cards = []
        for guid in guid_set:
            note_info = self.get_note_information(guid)
            if note_info is None:
                return cards
            title, content, tags, attachments, modified = note_info
            cards.append(EvernoteCard(title, content, guid, tags, attachments, modified))
        return cards

    # TODO: desc
    def find_notes_filter_by_tag_guids(self, guids_list):
        evernote_filter = NoteFilter()
        evernote_filter.ascending = False
        evernote_filter.tagGuids = guids_list
        spec = NotesMetadataResultSpec()
        spec.includeTitle = True
        note_list = self.noteStore.findNotesMetadata(self.token, evernote_filter, 0, 10000, spec)
        guids = []
        for note in note_list.notes:
            guids.append(note.guid)
        return guids

    def get_note_information(self, note_guid):
        whole_note = next((l for l in USE_APPLESCRIPT['notes'] if l['guid'] == note_guid), None)
        if mw.col.conf.get(SETTING_KEEP_TAGS, False):
            tags = whole_note['tags']
        #raise NameError(whole_note)
        
        return whole_note['title'].encode('utf-8'), whole_note['content'].encode('utf-8'), tags, whole_note['attachments'], whole_note['modified']


class Controller:
    def __init__(self):
        self.evernoteTags = mw.col.conf.get(SETTING_TAGS_TO_IMPORT, "").split(",")
        self.ankiTag = mw.col.conf.get(SETTING_DEFAULT_TAG, "evernote")
        self.deck = mw.col.conf.get(SETTING_DEFAULT_DECK, "Default")
        self.updateExistingNotes = mw.col.conf.get(SETTING_UPDATE_EXISTING_NOTES,
                                                   UpdateExistingNotes.UpdateNotesInPlace)
        self.anki = Anki()
        self.anki.create_note_type_default()
        self.evernote = Evernote()

    def proceed(self):

        anki_ids = self.anki.get_cards_id_from_tag(self.ankiTag)
        anki_guids = self.anki.get_guids_from_anki_id(anki_ids)

        # get all Evernote notes
        USE_APPLESCRIPT['notes'] = applescript.AppleScript('''
            on run {arg1}
            tell application "Evernote"
                set myNotes to find notes "tag:" & arg1
                set noteList to {}
                
                set currentTime to do shell script "date '+%Y%m%d%H%M%S'"

                tell application "Finder"
                    try
                        make new folder at (path to temporary items as string) with properties {name:"Evernote2AnkiMac_"&currentTime}
                    end try
                end tell  
                set temporarypath to (path to temporary items as string) & "Evernote2AnkiMac_" & currentTime


                repeat with counter_variable_name from 1 to count of myNotes
                    set current_note to item counter_variable_name of myNotes
                    set currentTags to tags of current_note
                    set currentGUID to guid of current_note as string
                    set tagList to {}
                    
                    repeat with tag_counter from 1 to count of currentTags
                        set end of tagList to name of item tag_counter of currentTags
                    end repeat
                    
                    set currentAttachments to attachments of current_note
                    set attachmentList to {}                  
                    
                    repeat with counter from 1 to count of currentAttachments
                        set current_attachment to item counter of currentAttachments
                        
                        tell application "Finder"
                            try
                                make new folder at temporarypath with properties {name:currentGUID}
                            end try
                        end tell
                        
                        set current_filename to (temporarypath & ":" & currentGUID & ":" & (hash of current_attachment))

                        try
                            write current_attachment to current_filename
                        end try
                        
                        set end of attachmentList to {|hash|:hash of current_attachment, |filename|:POSIX path of current_filename}
                    end repeat
                    
                    set end of noteList to {|title|:title of current_note, |content|:HTML content of current_note, |modified|:modification date of current_note, |guid|:currentGUID, |link|:note link of current_note, |tags|:tagList, |attachments|:attachmentList}
                    
                end repeat
                noteList
            end tell
        end run

        ''').run(mw.col.conf.get(SETTING_TAGS_TO_IMPORT, ""))
        evernote_guids = [d['guid'] for d in USE_APPLESCRIPT['notes']]

        cards_to_add = set(evernote_guids) - set(anki_guids)
        cards_to_update = set(evernote_guids) - set(cards_to_add)
        cards_to_delete = set(anki_guids) - set(evernote_guids)
        #sys.stderr.write(', '.join(anki_guids)+'\n\n'+', '.join(cards_to_update)+'\n\n'+', '.join(cards_to_update)+'\n')

        self.anki.start_editing()

        # delete
        n = len(cards_to_delete)
        self.anki.delete_anki_cards(cards_to_delete)

        #add
        n1 = self.import_into_anki(cards_to_add, self.deck, self.ankiTag)
        
        if self.updateExistingNotes is UpdateExistingNotes.IgnoreExistingNotes:
            show_tooltip("{} new card(s) imported, {} card(s) deleted. Updating is disabled.".format(str(n1), str(n)))
        else:
            # update
            n2 = len(cards_to_update)
            if self.updateExistingNotes is UpdateExistingNotes.UpdateNotesInPlace:
                update_str = "in-place"
                self.update_in_anki(cards_to_update, self.ankiTag)
            else:
                update_str = "(deleted and re-added)"
                self.anki.delete_anki_cards(cards_to_update)
                self.import_into_anki(cards_to_update, self.deck, self.ankiTag)
            show_tooltip("{} new card(s) imported, {} card(s) updated {} and {} cards deleted."
                         .format(str(n1), str(n2), update_str, str(n)))

        self.anki.stop_editing()
        self.anki.collection().autosave()

    # TODO: desc
    def update_in_anki(self, guid_set, tag):
        cards = self.evernote.create_evernote_cards(guid_set)
        number = self.anki.update_evernote_cards(cards, tag)
        return number

    # TODO: desc
    def import_into_anki(self, guid_set, deck, tag):
        cards = self.evernote.create_evernote_cards(guid_set)
        number = self.anki.add_evernote_cards(cards, deck, tag)
        return number


def show_tooltip(text, time_out=3000):
    aqt.utils.tooltip(text, time_out)


def main():
    controller = Controller()
    controller.proceed()


action = aqt.qt.QAction("Import from Evernote", aqt.mw)
# aqt.mw.connect(action, aqt.qt.SIGNAL("triggered()"), main)
action.triggered.connect(main)
aqt.mw.form.menuTools.addAction(action)


def setup_evernote(self):
    global evernote_default_deck
    global evernote_default_tag
    global evernote_tags_to_import
    global keep_evernote_tags
    global update_existing_notes

    widget = QWidget()
    layout = QVBoxLayout()

    # Default Deck
    evernote_default_deck_label = QLabel("Default Deck for imported Cards:")
    evernote_default_deck = QLineEdit()
    evernote_default_deck.setText(mw.col.conf.get(SETTING_DEFAULT_DECK, ""))
    layout.insertWidget(int(layout.count()) + 1, evernote_default_deck_label)
    layout.insertWidget(int(layout.count()) + 2, evernote_default_deck)
    evernote_default_deck.connect(evernote_default_deck, SIGNAL("editingFinished()"), update_evernote_default_deck)

    # Default Tag
    evernote_default_tag_label = QLabel("Default Tag for imported Cards:")
    evernote_default_tag = QLineEdit()
    evernote_default_tag.setText(mw.col.conf.get(SETTING_DEFAULT_TAG, ""))
    layout.insertWidget(int(layout.count()) + 1, evernote_default_tag_label)
    layout.insertWidget(int(layout.count()) + 2, evernote_default_tag)
    evernote_default_tag.connect(evernote_default_tag, SIGNAL("editingFinished()"), update_evernote_default_tag)

    # Tags to Import
    evernote_tags_to_import_label = QLabel("Evernote Tags to Import:")
    evernote_tags_to_import = QLineEdit()
    evernote_tags_to_import.setText(mw.col.conf.get(SETTING_TAGS_TO_IMPORT, ""))
    layout.insertWidget(int(layout.count()) + 1, evernote_tags_to_import_label)
    layout.insertWidget(int(layout.count()) + 2, evernote_tags_to_import)
    evernote_tags_to_import.connect(evernote_tags_to_import,
                                    SIGNAL("editingFinished()"),
                                    update_evernote_tags_to_import)

    # Keep Evernote Tags
    keep_evernote_tags = QCheckBox("Keep Evernote Tags", self)
    keep_evernote_tags.setChecked(mw.col.conf.get(SETTING_KEEP_TAGS, False))
    keep_evernote_tags.stateChanged.connect(update_evernote_keep_tags)
    layout.insertWidget(int(layout.count()) + 1, keep_evernote_tags)

    # Update Existing Notes
    update_existing_notes = QComboBox()
    update_existing_notes.addItems(["Ignore Existing Notes", "Update Existing Notes In-Place",
                                    "Delete and Re-Add Existing Notes"])
    update_existing_notes.setCurrentIndex(mw.col.conf.get(SETTING_UPDATE_EXISTING_NOTES,
                                                          UpdateExistingNotes.UpdateNotesInPlace))
    update_existing_notes.activated.connect(update_evernote_update_existing_notes)
    layout.insertWidget(int(layout.count()) + 1, update_existing_notes)

    # Vertical Spacer
    vertical_spacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout.addItem(vertical_spacer)

    # Parent Widget
    widget.setLayout(layout)

    # New Tab
    self.form.tabWidget.addTab(widget, "Evernote2AnkiMac")

def update_evernote_default_deck():
    mw.col.conf[SETTING_DEFAULT_DECK] = evernote_default_deck.text()

def update_evernote_default_tag():
    mw.col.conf[SETTING_DEFAULT_TAG] = evernote_default_tag.text()

def update_evernote_tags_to_import():
    mw.col.conf[SETTING_TAGS_TO_IMPORT] = evernote_tags_to_import.text()

def update_evernote_keep_tags():
    mw.col.conf[SETTING_KEEP_TAGS] = keep_evernote_tags.isChecked()

def update_evernote_update_existing_notes(index):
    mw.col.conf[SETTING_UPDATE_EXISTING_NOTES] = index

Preferences.setupOptions = wrap(Preferences.setupOptions, setup_evernote)


# ImageMagick is a requirement, convert needs to be in the path!
# we use envoy to better handle the output (which for whatever reason is actually output to std_err)
def pdf2image(pdfpath, resolution=72):
    # sys.stderr.write("\n"+str('convert -verbose -density 200 pdf:' +pdfpath+ ' ' +pdfpath+ '.png')+"\n"+"\n"+"\n"+pdfpath+"\n")
    r = envoy.run(str('gm convert -verbose -density 200 pdf:' +pdfpath+ ' +adjoin ' +pdfpath+ '-%0d.png'))
    # sys.stderr.write("envoy: "+r.std_err+"\n"+r.std_out+"\n"+"convert pdf:"+pdfpath+" -verbose -density 200 "+ pdfpath+".png"+"\nEND envoy")
    # for whatever reason, convert outputs it as error -> std_err
    num = re.findall(' PDF ', r.std_err)
    # sys.stderr.write(r.std_err)
    if len(num) is 1:
        return [(pdfpath+".png").decode('UTF-8')]
    else:
        images = []
        # there are num/2 files (every PDF page is outputted twice)
        for i in range(0, len(num)/2):
            images.append((pdfpath+"-"+str(i)+".png").decode('UTF-8'))
        return images




