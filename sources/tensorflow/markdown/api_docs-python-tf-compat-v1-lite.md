[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.lite Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite#functions)
    

Public API for tf.\_api.v2.lite namespace

Modules
-------

[`constants`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/constants)
 module: Public API for tf.\_api.v2.lite.constants namespace

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/experimental)
 module: Public API for tf.\_api.v2.lite.experimental namespace

Classes
-------

[`class Interpreter`](https://www.tensorflow.org/api_docs/python/tf/lite/Interpreter)
: Interpreter interface for running TensorFlow Lite models.

[`class OpHint`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/OpHint)
: A class that helps build tflite function invocations. (deprecated)

[`class OpsSet`](https://www.tensorflow.org/api_docs/python/tf/lite/OpsSet)
: Enum class defining the sets of ops available to generate TFLite models.

[`class Optimize`](https://www.tensorflow.org/api_docs/python/tf/lite/Optimize)
: Enum defining the optimizations to apply when generating a tflite model.

[`class RepresentativeDataset`](https://www.tensorflow.org/api_docs/python/tf/lite/RepresentativeDataset)
: Representative dataset used to optimize the model.

[`class TFLiteConverter`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/TFLiteConverter)
: Convert a TensorFlow model into `output_format`.

[`class TargetSpec`](https://www.tensorflow.org/api_docs/python/tf/lite/TargetSpec)
: Specification of target device used to optimize the model.

[`class TocoConverter`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/TocoConverter)
: Convert a TensorFlow model into `output_format`.

Functions
---------

[`toco_convert(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/lite/toco_convert)
: Convert a TensorFlow GraphDef to TFLite. (deprecated)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.