[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.core.base\_trainer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py)

Standard Trainer implementation.

The base trainer implements the Orbit `StandardTrainable` and `StandardEvaluable` interfaces. Trainers inside this project should be interchangable and independent on model architectures and tasks.

Classes
-------

[`class ExperimentConfig`](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/ExperimentConfig)
: Top-level configuration.

[`class Trainer`](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer)
: Implements the common trainer shared for TensorFlow models.

[`class TrainerConfig`](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/TrainerConfig)
: Configuration for trainer.

Functions
---------

[`get_runtime_options(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/get_runtime_options)
: Get tf.distribute.RunOptions from config.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.