[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.configs.retinanet Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/retinanet.py)

RetinaNet configuration definition.

Classes
-------

[`class Anchor`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/Anchor)

[`class AttributeHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/AttributeHead)

[`class DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/DataConfig)
: Input config for training.

[`class DataDecoder`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/DataDecoder)
: Data decoder config.

[`class DetectionGenerator`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/DetectionGenerator)

[`class ExportConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/ExportConfig)

[`class Losses`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/Losses)

[`class Parser`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/Parser)

[`class RetinaNet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/RetinaNet)

[`class RetinaNetHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/RetinaNetHead)

[`class RetinaNetTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/RetinaNetTask)

[`class TfExampleDecoder`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/TfExampleDecoder)
: A simple TF Example decoder config.

[`class TfExampleDecoderLabelMap`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/TfExampleDecoderLabelMap)
: TF Example decoder with label map config.

Functions
---------

[`retinanet(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet)
: RetinaNet general config.

[`retinanet_resnetfpn_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_resnetfpn_coco)
: COCO object detection with RetinaNet.

[`retinanet_spinenet_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_spinenet_coco)
: COCO object detection with RetinaNet using SpineNet backbone.

[`retinanet_spinenet_mobile_coco(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_spinenet_mobile_coco)
: COCO object detection with mobile RetinaNet.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| COCO\_INPUT\_PATH\_BASE | `'coco'` |
| COCO\_TRAIN\_EXAMPLES | `118287` |
| COCO\_VAL\_EXAMPLES | `5000` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.