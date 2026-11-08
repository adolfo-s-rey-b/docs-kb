[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Fconfigs%2Fvideo_classification&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision.configs.video\_classification Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/configs/video_classification.py)

Video classification configuration definition.

Classes
-------

[`class DataConfig`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/DataConfig)
: The base configuration for building datasets.

[`class Losses`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/Losses)

[`class Metrics`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/Metrics)

[`class VideoClassificationModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/VideoClassificationModel)
: The model config.

[`class VideoClassificationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/VideoClassificationTask)
: The task config.

Functions
---------

[`add_trainer(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/add_trainer)
: Add and config a trainer to the experiment config.

[`kinetics400(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/kinetics400)
: Generated Kinetics 400 dataset configs.

[`kinetics600(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/kinetics600)
: Generated Kinetics 600 dataset configs.

[`kinetics700(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/kinetics700)
: Generated Kinetics 600 dataset configs.

[`kinetics700_2020(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/kinetics700_2020)
: Generated Kinetics 600 dataset configs.

[`video_classification(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification)
: Video classification general.

[`video_classification_kinetics400(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics400)
: Video classification on Kinetics 400 with resnet.

[`video_classification_kinetics600(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics600)
: Video classification on Kinetics 600 with resnet.

[`video_classification_kinetics700(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics700)
: Video classification on Kinetics 700 with resnet.

[`video_classification_kinetics700_2020(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics700_2020)
: Video classification on Kinetics 700 2020 with resnet.

[`video_classification_ucf101(...)`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_ucf101)
: Video classification on UCF-101 with resnet.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.