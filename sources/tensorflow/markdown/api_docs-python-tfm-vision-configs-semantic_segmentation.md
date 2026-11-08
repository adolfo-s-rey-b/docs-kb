[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fconfigs%2Fsemantic_segmentation&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.configs.semantic\_segmentation Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/semantic_segmentation.py)

Semantic segmentation configuration definition.

Classes
-------

[`class DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DataConfig)
: Input config for training.

[`class DenseFeatureConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/DenseFeatureConfig)
: Config for dense features, such as RGB pixels, masks, heatmaps.

[`class Evaluation`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/Evaluation)
: Evaluation config.

[`class ExportConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/ExportConfig)
: Model export config.

[`class Losses`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/Losses)
: Loss function config.

[`class MaskScoringHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/MaskScoringHead)
: Mask Scoring head config.

[`class SegmentationHead`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/SegmentationHead)
: Segmentation head config.

[`class SemanticSegmentationModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/SemanticSegmentationModel)
: Semantic segmentation model config.

[`class SemanticSegmentationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/SemanticSegmentationTask)
: The model config.

Functions
---------

[`mnv2_deeplabv3_cityscapes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3_cityscapes)
: Image segmentation on cityscapes with mobilenetv2 deeplabv3.

[`mnv2_deeplabv3_pascal(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3_pascal)
: Image segmentation on pascal with mobilenetv2 deeplabv3.

[`mnv2_deeplabv3plus_cityscapes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3plus_cityscapes)
: Image segmentation on cityscapes with mobilenetv2 deeplabv3plus.

[`seg_deeplabv3_pascal(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3_pascal)
: Image segmentation on pascal voc with resnet deeplabv3.

[`seg_deeplabv3plus_cityscapes(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3plus_cityscapes)
: Image segmentation on cityscapes with resnet deeplabv3+.

[`seg_deeplabv3plus_pascal(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3plus_pascal)
: Image segmentation on pascal voc with resnet deeplabv3+.

[`seg_resnetfpn_pascal(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_resnetfpn_pascal)
: Image segmentation on pascal voc with resnet-fpn.

[`semantic_segmentation(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/semantic_segmentation)
: Semantic segmentation general.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| CITYSCAPES\_INPUT\_PATH\_BASE | `'cityscapes'` |
| CITYSCAPES\_TRAIN\_EXAMPLES | `2975` |
| CITYSCAPES\_VAL\_EXAMPLES | `500` |
| PASCAL\_INPUT\_PATH\_BASE | `'gs://**/pascal_voc_seg'` |
| PASCAL\_TRAIN\_EXAMPLES | `10582` |
| PASCAL\_VAL\_EXAMPLES | `1449` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.