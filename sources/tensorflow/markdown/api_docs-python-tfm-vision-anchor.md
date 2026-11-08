[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fanchor&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.anchor Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/anchor.py)

Anchor box and labeler definition.

Classes
-------

[`class Anchor`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/Anchor)
: Anchor class for anchor-based object detectors.

[`class AnchorGeneratorv2`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/AnchorGeneratorv2)
: Utility to generate anchors for a multiple feature maps.

[`class AnchorLabeler`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/AnchorLabeler)
: Labeler for dense object detector.

[`class RpnAnchorLabeler`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/RpnAnchorLabeler)
: Labeler for Region Proposal Network.

Functions
---------

[`build_anchor_generator(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/build_anchor_generator)
: Build anchor generator from levels.

[`unpack_targets(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor/unpack_targets)
: Unpacks an array of labels into multi-scales labels.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.