# Evernote2Anki Importer for Mac (beta)

**Forks and suggestions are very welcome.**

Thanks to https://github.com/brumar/anknotes for most of the code.

## Description
An Anki addon for OS X for importing Evernote (https://www.evernote.com) notes to anki. Very rudimentary for the moment. I wait for suggestions according to the needs of evernote/anki users.

## How to use it
- download everything, move it to your Anki/addons directory
- install ImageMagick library, eg. using [homebrew](https://brew.sh/)
  - ```brew install imagemagick```
- install the Evernote app from the App store or directly from their website
- start Anki and fill in the information in the preferences tab
- use _Tools->Import from Evernote_ to import notes

## Current features
- Import all the notes from evernote with selected tags
- Choose the name of the deck, as well as the default tag in anki
- Only new cards are imported
- Converts pdf-files to images
- Transforms highlights into a cloze deletion format
