# This file is generated by objective.metadata
#
# Last update: Fri Jun  8 16:58:06 2012

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'CATransform3D': objc.createStructType('CATransform3D', sel32or64(b'{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}'), ['m11', 'm12', 'm13', 'm14', 'm21', 'm22', 'm23', 'm24', 'm31', 'm32', 'm33', 'm34', 'm41', 'm42', 'm43', 'm44'])})
constants = '''$CIDetectorAccuracy$CIDetectorAccuracyHigh$CIDetectorAccuracyLow$CIDetectorTypeFace$CIFeatureTypeFace$kCAAlignmentCenter$kCAAlignmentJustified$kCAAlignmentLeft$kCAAlignmentNatural$kCAAlignmentRight$kCAAnimationCubic$kCAAnimationCubicPaced$kCAAnimationDiscrete$kCAAnimationLinear$kCAAnimationPaced$kCAAnimationRotateAuto$kCAAnimationRotateAutoReverse$kCAEmitterLayerAdditive$kCAEmitterLayerBackToFront$kCAEmitterLayerCircle$kCAEmitterLayerCuboid$kCAEmitterLayerLine$kCAEmitterLayerOldestFirst$kCAEmitterLayerOldestLast$kCAEmitterLayerOutline$kCAEmitterLayerPoint$kCAEmitterLayerPoints$kCAEmitterLayerRectangle$kCAEmitterLayerSphere$kCAEmitterLayerSurface$kCAEmitterLayerUnordered$kCAEmitterLayerVolume$kCAFillModeBackwards$kCAFillModeBoth$kCAFillModeForwards$kCAFillModeFrozen$kCAFillModeRemoved$kCAFillRuleEvenOdd$kCAFillRuleNonZero$kCAFilterLinear$kCAFilterNearest$kCAFilterTrilinear$kCAGradientLayerAxial$kCAGravityBottom$kCAGravityBottomLeft$kCAGravityBottomRight$kCAGravityCenter$kCAGravityLeft$kCAGravityResize$kCAGravityResizeAspect$kCAGravityResizeAspectFill$kCAGravityRight$kCAGravityTop$kCAGravityTopLeft$kCAGravityTopRight$kCALineCapButt$kCALineCapRound$kCALineCapSquare$kCALineJoinBevel$kCALineJoinMiter$kCALineJoinRound$kCAMediaTimingFunctionDefault$kCAMediaTimingFunctionEaseIn$kCAMediaTimingFunctionEaseInEaseOut$kCAMediaTimingFunctionEaseOut$kCAMediaTimingFunctionLinear$kCAOnOrderIn$kCAOnOrderOut$kCAScrollBoth$kCAScrollHorizontally$kCAScrollNone$kCAScrollVertically$kCATransactionAnimationDuration$kCATransactionAnimationTimingFunction$kCATransactionCompletionBlock$kCATransactionDisableActions$kCATransition$kCATransitionFade$kCATransitionFromBottom$kCATransitionFromLeft$kCATransitionFromRight$kCATransitionFromTop$kCATransitionMoveIn$kCATransitionPush$kCATransitionReveal$kCATruncationEnd$kCATruncationMiddle$kCATruncationNone$kCATruncationStart$kCAValueFunctionRotateX$kCAValueFunctionRotateY$kCAValueFunctionRotateZ$kCAValueFunctionScale$kCAValueFunctionScaleX$kCAValueFunctionScaleY$kCAValueFunctionScaleZ$kCAValueFunctionTranslate$kCAValueFunctionTranslateX$kCAValueFunctionTranslateY$kCAValueFunctionTranslateZ$kCIActiveKeys$kCIApplyOptionColorSpace$kCIApplyOptionDefinition$kCIApplyOptionExtent$kCIApplyOptionUserInfo$kCIAttributeClass$kCIAttributeDefault$kCIAttributeDescription$kCIAttributeDisplayName$kCIAttributeFilterCategories$kCIAttributeFilterDisplayName$kCIAttributeFilterName$kCIAttributeIdentity$kCIAttributeMax$kCIAttributeMin$kCIAttributeName$kCIAttributeReferenceDocumentation$kCIAttributeSliderMax$kCIAttributeSliderMin$kCIAttributeType$kCIAttributeTypeAngle$kCIAttributeTypeBoolean$kCIAttributeTypeCount$kCIAttributeTypeDistance$kCIAttributeTypeGradient$kCIAttributeTypeInteger$kCIAttributeTypeOffset$kCIAttributeTypeOpaqueColor$kCIAttributeTypePosition$kCIAttributeTypePosition3$kCIAttributeTypeRectangle$kCIAttributeTypeScalar$kCIAttributeTypeTime$kCICategoryBlur$kCICategoryBuiltIn$kCICategoryColorAdjustment$kCICategoryColorEffect$kCICategoryCompositeOperation$kCICategoryDistortionEffect$kCICategoryFilterGenerator$kCICategoryGenerator$kCICategoryGeometryAdjustment$kCICategoryGradient$kCICategoryHalftoneEffect$kCICategoryHighDynamicRange$kCICategoryInterlaced$kCICategoryNonSquarePixels$kCICategoryReduction$kCICategorySharpen$kCICategoryStillImage$kCICategoryStylize$kCICategoryTileEffect$kCICategoryTransition$kCICategoryVideo$kCIContextOutputColorSpace$kCIContextUseSoftwareRenderer$kCIContextWorkingColorSpace$kCIFilterGeneratorExportedKey$kCIFilterGeneratorExportedKeyName$kCIFilterGeneratorExportedKeyTargetObject$kCIFormatARGB8@i$kCIFormatRGBA16@i$kCIFormatRGBAf@i$kCIFormatRGBAh@i$kCIImageColorSpace$kCIImageProviderTileSize$kCIImageProviderUserInfo$kCIInputAllowDraftModeKey$kCIInputAngleKey$kCIInputAspectRatioKey$kCIInputBackgroundImageKey$kCIInputBiasKey$kCIInputBoostKey$kCIInputBoostShadowAmountKey$kCIInputBrightnessKey$kCIInputCenterKey$kCIInputColorKey$kCIInputContrastKey$kCIInputDecoderVersionKey$kCIInputEVKey$kCIInputEnableChromaticNoiseTrackingKey$kCIInputEnableSharpeningKey$kCIInputExtentKey$kCIInputGradientImageKey$kCIInputIgnoreImageOrientationKey$kCIInputImageKey$kCIInputImageOrientationKey$kCIInputIntensityKey$kCIInputLinearSpaceFilter$kCIInputMaskImageKey$kCIInputNeutralChromaticityXKey$kCIInputNeutralChromaticityYKey$kCIInputNeutralLocationKey$kCIInputNeutralTemperatureKey$kCIInputNeutralTintKey$kCIInputNoiseReductionAmountKey$kCIInputRadiusKey$kCIInputRefractionKey$kCIInputSaturationKey$kCIInputScaleFactorKey$kCIInputScaleKey$kCIInputShadingImageKey$kCIInputSharpnessKey$kCIInputTargetImageKey$kCIInputTimeKey$kCIInputTransformKey$kCIInputWidthKey$kCIOutputImageKey$kCIOutputNativeSizeKey$kCISamplerAffineMatrix$kCISamplerColorSpace$kCISamplerFilterLinear$kCISamplerFilterMode$kCISamplerFilterNearest$kCISamplerWrapBlack$kCISamplerWrapClamp$kCISamplerWrapMode$kCISupportedDecoderVersionsKey$kCIUIParameterSet$kCIUISetAdvanced$kCIUISetBasic$kCIUISetDevelopment$kCIUISetIntermediate$'''
constants = constants + '$CATransform3DIdentity@%s$'%(sel32or64('{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}'),)
enums = '''$CA_WARN_DEPRECATED@1$kCAConstraintHeight@7$kCAConstraintMaxX@2$kCAConstraintMaxY@6$kCAConstraintMidX@1$kCAConstraintMidY@5$kCAConstraintMinX@0$kCAConstraintMinY@4$kCAConstraintWidth@3$kCALayerBottomEdge@4$kCALayerHeightSizable@16$kCALayerLeftEdge@1$kCALayerMaxXMargin@4$kCALayerMaxYMargin@32$kCALayerMinXMargin@1$kCALayerMinYMargin@8$kCALayerNotSizable@0$kCALayerRightEdge@2$kCALayerTopEdge@8$kCALayerWidthSizable@2$'''
misc.update({})
functions={'CATransform3DIsAffine': (sel32or64(b'B{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DInvert': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DIsIdentity': (sel32or64(b'B{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeScale': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DTranslate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DEqualToTransform': (sel32or64(b'B{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DRotate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}dddd'),), 'CACurrentMediaTime': (b'd',), 'CATransform3DMakeRotation': (sel32or64(b'{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}dddd'),), 'CATransform3DConcat': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DScale': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DMakeTranslation': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'CATransform3DGetAffineTransform': (sel32or64(b'{CGAffineTransform=ffffff}{CATransform3D=ffffffffffffffff}', b'{CGAffineTransform=dddddd}{CATransform3D=dddddddddddddddd}'),), 'CATransform3DMakeAffineTransform': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CGAffineTransform=ffffff}', b'{CATransform3D=dddddddddddddddd}{CGAffineTransform=dddddd}'),)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CAAnimation', b'isRemovedOnCompletion', {'retval': {'type': b'Z'}})
    r(b'CAAnimation', b'setRemovedOnCompletion:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAAnimation', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CAEmitterCell', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'CAEmitterCell', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAEmitterCell', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CAEmitterLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r(b'CAEmitterLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'containsPoint:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'contentsAreFlipped', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isDoubleSided', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isGeometryFlipped', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isHidden', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'isOpaque', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'masksToBounds', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplay', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplayForKey:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsDisplayOnBoundsChange', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'needsLayout', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'setDoubleSided:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setGeometryFlipped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setHidden:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setMasksToBounds:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setNeedsDisplayOnBoundsChange:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setOpaque:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'setShouldRasterize:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CALayer', b'shouldArchiveValueForKey:', {'retval': {'type': b'Z'}})
    r(b'CALayer', b'shouldRasterize', {'retval': {'type': b'Z'}})
    r(b'CAOpenGLLayer', b'canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CAOpenGLLayer', b'drawInCGLContext:pixelFormat:forLayerTime:displayTime:', {'arguments': {5: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CAOpenGLLayer', b'isAsynchronous', {'retval': {'type': b'Z'}})
    r(b'CAOpenGLLayer', b'setAsynchronous:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAPropertyAnimation', b'isAdditive', {'retval': {'type': b'Z'}})
    r(b'CAPropertyAnimation', b'isCumulative', {'retval': {'type': b'Z'}})
    r(b'CAPropertyAnimation', b'setAdditive:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAPropertyAnimation', b'setCumulative:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CARenderer', b'beginFrameAtTime:timeStamp:', {'arguments': {3: {'type': sel32or64(b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}', b'^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}'), 'type_modifier': b'n'}}})
    r(b'CARenderer', b'rendererWithCGLContext:options:', {'arguments': {2: {'type': '^{_CGLContextObject=}'}}})
    r(b'CAReplicatorLayer', b'preservesDepth', {'retval': {'type': b'Z'}})
    r(b'CAReplicatorLayer', b'setPreservesDepth:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CATextLayer', b'font', {'retval': {'type': b'@'}})
    r(b'CATextLayer', b'isWrapped', {'retval': {'type': b'Z'}})
    r(b'CATextLayer', b'setFont:', {'arguments': {2: {'type': b'@'}}})
    r(b'CATextLayer', b'setWrapped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CATransaction', b'completionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'CATransaction', b'disableActions', {'retval': {'type': b'Z'}})
    r(b'CATransaction', b'setCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'CATransaction', b'setDisableActions:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CIColor', b'components', {'retval': {'c_array_of_variable_length': True}})
    r(b'CIContext', b'render:toBitmap:rowBytes:bounds:format:colorSpace:', {'arguments': {3: {'type_modifier': b'o', 'c_array_of_variable_length': True}}})
    r(b'CIFaceFeature', b'hasLeftEyePosition', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasMouthPosition', {'retval': {'type': b'Z'}})
    r(b'CIFaceFeature', b'hasRightEyePosition', {'retval': {'type': b'Z'}})
    r(b'CIFilter', b'apply:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIFilter', b'filterWithName:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIFilter', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'CIFilter', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CIFilterGenerator', b'writeToURL:atomically:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}}})
    r(b'CIFilterShape', b'transformBy:interior:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CIImage', b'imageWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIImage', b'initWithTexture:size:flipped:colorSpace:', {'arguments': {4: {'type': b'Z'}}})
    r(b'CIKernel', b'setROISelector:', {'arguments': {2: {'sel_of_type': sel32or64(b'{CGRect={CGPoint=ff}{CGSize=ff}}@:i{CGRect={CGPoint=ff}{CGSize=ff}}@', b'{CGRect={CGPoint=dd}{CGSize=dd}}@:i{CGRect={CGPoint=dd}{CGSize=dd}}@')}}})
    r(b'CIPlugIn', b'loadPlugIn:allowExecutableCode:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CIPlugIn', b'loadPlugIn:allowNonExecutable:', {'arguments': {3: {'type': b'Z'}}})
    r(b'CISampler', b'initWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CISampler', b'samplerWithImage:keysAndValues:', {'c_array_delimited_by_null': True, 'variadic': True})
    r(b'CIVector', b'initWithValues:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'CIVector', b'vectorWithValues:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'NSObject', b'animationDidStop:finished:', {'arguments': {3: {'type': b'Z'}}})
    r(b'NSObject', b'provideImageData:bytesPerRow:origin::size::userInfo:', {'arguments': {2: {'type_modifier': b'o', 'c_array_of_variable_length': True}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'autoreverses', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'beginTime', {'retval': {'type': b'd'}})
    r(b'NSObject', b'duration', {'retval': {'type': b'd'}})
    r(b'NSObject', b'fillMode', {'retval': {'type': b'@'}})
    r(b'NSObject', b'filterWithName:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'load:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^v'}}})
    r(b'NSObject', b'repeatCount', {'retval': {'type': b'f'}})
    r(b'NSObject', b'repeatDuration', {'retval': {'type': b'd'}})
    r(b'NSObject', b'runActionForKey:object:arguments:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'setAutoreverses:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setBeginTime:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setDuration:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setFillMode:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setRepeatCount:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'f'}}})
    r(b'NSObject', b'setRepeatDuration:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setSpeed:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'f'}}})
    r(b'NSObject', b'setTimeOffset:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'speed', {'retval': {'type': b'f'}})
    r(b'NSObject', b'timeOffset', {'retval': {'type': b'd'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'actionForLayer:forKey:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'animationDidStart:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'animationDidStop:finished:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'Z'}}})
    r(b'NSObject', b'displayLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'drawLayer:inContext:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'^{CGContext=}'}}})
    r(b'NSObject', b'invalidateLayoutOfLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'layoutSublayersOfLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'layoutSublayersOfLayer:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'preferredSizeOfLayer:', {'retval': {'type': sel32or64(b'{CGSize=ff}', b'{CGSize=dd}')}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'provideImageData:bytesPerRow:origin::size::userInfo:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^v', 'type_modifier': b'o', 'c_array_of_variable_length': True}, 3: {'type': b'L'}, 4: {'type': b'L'}, 5: {'type': b'L'}, 6: {'type': b'L'}, 7: {'type': b'L'}, 8: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'CAAnimationDelegate': objc.informal_protocol('CAAnimationDelegate', [objc.selector(None, b'animationDidStart:', b'v@:@', isRequired=False), objc.selector(None, b'animationDidStop:finished:', b'v@:@Z', isRequired=False)]), 'CALayerDelegate': objc.informal_protocol('CALayerDelegate', [objc.selector(None, b'drawLayer:inContext:', b'v@:@^{CGContext=}', isRequired=False), objc.selector(None, b'actionForLayer:forKey:', b'@@:@@', isRequired=False), objc.selector(None, b'displayLayer:', b'v@:@', isRequired=False), objc.selector(None, b'layoutSublayersOfLayer:', b'v@:@', isRequired=False)]), 'CIImageProvider': objc.informal_protocol('CIImageProvider', [objc.selector(None, b'provideImageData:bytesPerRow:origin::size::userInfo:', b'v@:^vLLLLL@', isRequired=False)]), 'CALayoutManager': objc.informal_protocol('CALayoutManager', [objc.selector(None, b'preferredSizeOfLayer:', sel32or64(b'{CGSize=ff}@:@', b'{CGSize=dd}@:@'), isRequired=False), objc.selector(None, b'layoutSublayersOfLayer:', b'v@:@', isRequired=False), objc.selector(None, b'invalidateLayoutOfLayer:', b'v@:@', isRequired=False)])}
expressions = {}

# END OF FILE
