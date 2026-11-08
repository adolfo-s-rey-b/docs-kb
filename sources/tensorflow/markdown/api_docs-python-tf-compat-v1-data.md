[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.data Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data#other-members)
    

Public API for tf.\_api.v2.data namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/experimental)
 module: Public API for tf.\_api.v2.data.experimental namespace

Classes
-------

[`class Dataset`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/Dataset)
: Represents a potentially large set of elements.

[`class DatasetSpec`](https://www.tensorflow.org/api_docs/python/tf/data/DatasetSpec)
: Type specification for [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

[`class FixedLengthRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/FixedLengthRecordDataset)
: A `Dataset` of fixed-length records from one or more binary files.

[`class Iterator`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/Iterator)
: Represents the state of iterating through a `Dataset`.

[`class NumpyIterator`](https://www.tensorflow.org/api_docs/python/tf/data/NumpyIterator)
: Iterator over a dataset with elements converted to numpy.

[`class Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
: Represents options for [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

[`class TFRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/TFRecordDataset)
: A `Dataset` comprising records from one or more TFRecord files.

[`class TextLineDataset`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/TextLineDataset)
: A `Dataset` comprising lines from one or more text files.

[`class ThreadingOptions`](https://www.tensorflow.org/api_docs/python/tf/data/ThreadingOptions)
: Represents options for dataset threading.

Functions
---------

[`get_output_classes(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/get_output_classes)
: Returns the output classes for elements of the input dataset / iterator.

[`get_output_shapes(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/get_output_shapes)
: Returns the output shapes for elements of the input dataset / iterator.

[`get_output_types(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/get_output_types)
: Returns the output shapes for elements of the input dataset / iterator.

[`make_initializable_iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator)
: Creates an iterator for elements of `dataset`.

[`make_one_shot_iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_one_shot_iterator)
: Creates an iterator for elements of `dataset`.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| AUTOTUNE | `-1` |
| INFINITE\_CARDINALITY | `-1` |
| UNKNOWN\_CARDINALITY | `-2` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.