[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.saved\_model Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model#other-members)
    

Public API for tf.\_api.v2.saved\_model namespace

Modules
-------

[`builder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/builder)
 module: Public API for tf.\_api.v2.saved\_model.builder namespace

[`constants`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/constants)
 module: Public API for tf.\_api.v2.saved\_model.constants namespace

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/experimental)
 module: Public API for tf.\_api.v2.saved\_model.experimental namespace

[`loader`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/loader)
 module: Public API for tf.\_api.v2.saved\_model.loader namespace

[`main_op`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op)
 module: Public API for tf.\_api.v2.saved\_model.main\_op namespace

[`signature_constants`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants)
 module: Public API for tf.\_api.v2.saved\_model.signature\_constants namespace

[`signature_def_utils`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_def_utils)
 module: Public API for tf.\_api.v2.saved\_model.signature\_def\_utils namespace

[`tag_constants`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/tag_constants)
 module: Public API for tf.\_api.v2.saved\_model.tag\_constants namespace

[`utils`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/utils)
 module: Public API for tf.\_api.v2.saved\_model.utils namespace

Classes
-------

[`class Asset`](https://www.tensorflow.org/api_docs/python/tf/saved_model/Asset)
: Represents a file asset to hermetically include in a SavedModel.

[`class Builder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/Builder)
: Builds the `SavedModel` protocol buffer and saves variables and assets.

[`class SaveOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)
: Options for saving to SavedModel.

Functions
---------

[`build_signature_def(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_signature_def)
: Utility function to build a SignatureDef protocol buffer.

[`build_tensor_info(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info)
: Utility function to build TensorInfo proto from a Tensor. (deprecated)

[`classification_signature_def(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/classification_signature_def)
: Creates classification signature from given examples and predictions.

[`contains_saved_model(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/contains_saved_model)
: Checks whether the provided export directory could contain a SavedModel.

[`get_tensor_from_tensor_info(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info)
: Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

[`is_valid_signature(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/is_valid_signature)
: Determine whether a SignatureDef can be served by TensorFlow Serving.

[`load(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/load)
: Loads the model from a SavedModel as specified by tags. (deprecated)

[`load_v2(...)`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
: Load a SavedModel from `export_dir`.

[`main_op_with_restore(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore)
: Returns a main op to init variables, tables and restore the graph. (deprecated)

[`maybe_saved_model_directory(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/contains_saved_model)
: Checks whether the provided export directory could contain a SavedModel.

[`predict_signature_def(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/predict_signature_def)
: Creates prediction signature from given inputs and outputs.

[`regression_signature_def(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/regression_signature_def)
: Creates regression signature from given examples and predictions.

[`save(...)`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
: Exports a [tf.Module](https://www.tensorflow.org/api_docs/python/tf/Module)
 (and subclasses) `obj` to [SavedModel format](https://www.tensorflow.org/guide/saved_model#the_savedmodel_format_on_disk)
.

[`simple_save(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/simple_save)
: Convenience function to build a SavedModel suitable for serving. (deprecated)

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| ASSETS\_DIRECTORY | `'assets'` |
| ASSETS\_KEY | `'saved_model_assets'` |
| CLASSIFY\_INPUTS | `'inputs'` |
| CLASSIFY\_METHOD\_NAME | `'tensorflow/serving/classify'` |
| CLASSIFY\_OUTPUT\_CLASSES | `'classes'` |
| CLASSIFY\_OUTPUT\_SCORES | `'scores'` |
| DEBUG\_DIRECTORY | `'debug'` |
| DEBUG\_INFO\_FILENAME\_PB | `'saved_model_debug_info.pb'` |
| DEFAULT\_SERVING\_SIGNATURE\_DEF\_KEY | `'serving_default'` |
| GPU | `'gpu'` |
| LEGACY\_INIT\_OP\_KEY | `'legacy_init_op'` |
| MAIN\_OP\_KEY | `'saved_model_main_op'` |
| PREDICT\_INPUTS | `'inputs'` |
| PREDICT\_METHOD\_NAME | `'tensorflow/serving/predict'` |
| PREDICT\_OUTPUTS | `'outputs'` |
| REGRESS\_INPUTS | `'inputs'` |
| REGRESS\_METHOD\_NAME | `'tensorflow/serving/regress'` |
| REGRESS\_OUTPUTS | `'outputs'` |
| SAVED\_MODEL\_FILENAME\_PB | `'saved_model.pb'` |
| SAVED\_MODEL\_FILENAME\_PBTXT | `'saved_model.pbtxt'` |
| SAVED\_MODEL\_SCHEMA\_VERSION | `1` |
| SERVING | `'serve'` |
| TPU | `'tpu'` |
| TRAINING | `'train'` |
| VARIABLES\_DIRECTORY | `'variables'` |
| VARIABLES\_FILENAME | `'variables'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.