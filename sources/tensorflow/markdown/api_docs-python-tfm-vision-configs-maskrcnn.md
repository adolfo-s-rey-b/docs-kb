[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.configs.maskrcnn Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/maskrcnn.py)

R-CNN(-RS) configuration definition.

Classes
-------

[`class Anchor`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/Anchor)

[`class DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DataConfig)
: Input config for training.

[`class DetectionGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionGenerator)

[`class DetectionHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/DetectionHead)

[`class Losses`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/Losses)

[`class MaskHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/MaskHead)

[`class MaskRCNN`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/MaskRCNN)

[`class MaskRCNNTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/MaskRCNNTask)

[`class MaskROIAligner`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/MaskROIAligner)

[`class MaskSampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/MaskSampler)

[`class Parser`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/Parser)

[`class ROIAligner`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROIAligner)

[`class ROIGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROIGenerator)

[`class ROISampler`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/ROISampler)

[`class RPNHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/RPNHead)

Functions
---------

[`cascadercnn_spinenet_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/cascadercnn_spinenet_coco)
: COCO object detection with Cascade RCNN-RS with SpineNet backbone.

[`fasterrcnn_resnetfpn_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/fasterrcnn_resnetfpn_coco)
: COCO object detection with Faster R-CNN.

[`maskrcnn_mobilenet_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_mobilenet_coco)
: COCO object detection with Mask R-CNN with MobileNet backbone.

[`maskrcnn_resnetfpn_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_resnetfpn_coco)
: COCO object detection with Mask R-CNN.

[`maskrcnn_spinenet_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_spinenet_coco)
: COCO object detection with Mask R-CNN with SpineNet backbone.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| COCO\_INPUT\_PATH\_BASE | `'coco'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.