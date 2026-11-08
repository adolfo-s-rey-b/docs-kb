[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/saved_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/saved_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/saved_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsaved_model&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/saved_model#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/saved_model#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/saved_model#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/saved_model#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.saved\_model Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/saved_model#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/saved_model#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/saved_model#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/saved_model#other-members)
    

Public API for tf.\_api.v2.saved\_model namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental)
 module: Public API for tf.\_api.v2.saved\_model.experimental namespace

Classes
-------

[`class Asset`](https://www.tensorflow.org/api_docs/python/tf/saved_model/Asset)
: Represents a file asset to hermetically include in a SavedModel.

[`class LoadOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/LoadOptions)
: Options for loading a SavedModel.

[`class SaveOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)
: Options for saving to SavedModel.

Functions
---------

[`contains_saved_model(...)`](https://www.tensorflow.org/api_docs/python/tf/saved_model/contains_saved_model)
: Checks whether the provided export directory could contain a SavedModel.

[`load(...)`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
: Load a SavedModel from `export_dir`.

[`save(...)`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
: Exports a [tf.Module](https://www.tensorflow.org/api_docs/python/tf/Module)
 (and subclasses) `obj` to [SavedModel format](https://www.tensorflow.org/guide/saved_model#the_savedmodel_format_on_disk)
.

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