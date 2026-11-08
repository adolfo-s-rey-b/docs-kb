[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.configs.image\_classification Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/image_classification.py)

Image classification configuration definition.

Classes
-------

[`class DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/DataConfig)
: Input config for training.

[`class Evaluation`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/Evaluation)

[`class ImageClassificationModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/ImageClassificationModel)
: The model config.

[`class ImageClassificationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/ImageClassificationTask)
: The task config.

[`class Losses`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/Losses)

Functions
---------

[`image_classification(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification)
: Image classification general.

[`image_classification_imagenet(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet)
: Image classification on imagenet with resnet.

[`image_classification_imagenet_deit_pretrain(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_deit_pretrain)
: Image classification on imagenet with vision transformer.

[`image_classification_imagenet_mobilenet(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_mobilenet)
: Image classification on imagenet with mobilenet.

[`image_classification_imagenet_resnetrs(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_resnetrs)
: Image classification on imagenet with resnet-rs.

[`image_classification_imagenet_revnet(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_revnet)
: Returns a revnet config for image classification on imagenet.

[`image_classification_imagenet_vit_finetune(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_vit_finetune)
: Image classification on imagenet with vision transformer.

[`image_classification_imagenet_vit_pretrain(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_vit_pretrain)
: Image classification on imagenet with vision transformer.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| IMAGENET\_INPUT\_PATH\_BASE | `'imagenet-2012-tfrecord'` |
| IMAGENET\_TRAIN\_EXAMPLES | `1281167` |
| IMAGENET\_VAL\_EXAMPLES | `50000` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.