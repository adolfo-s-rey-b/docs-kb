[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#initialize)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.DatasetInitializer Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer#initialize)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/lookup_ops.py#L54-L99)

Creates a table initializer from a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.DatasetInitializer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DatasetInitializer)

tf.data.experimental.DatasetInitializer(
        dataset
    )

#### Sample usage:

    keys = tf.data.Dataset.range(100)

Raises: ValueError if `dataset` doesn't conform to specifications.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object that produces tuples of scalars. The first scalar is treated as a key and the second as value. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object that produces tuples of scalars. The first scalar is treated as a key and the second as value. |
| `key_dtype` | The expected table key dtype. |
| `value_dtype` | The expected table value dtype. |

Methods
-------

### `initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/lookup_ops.py#L94-L99)

initialize(
        table
    )

Returns the table initialization op.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.