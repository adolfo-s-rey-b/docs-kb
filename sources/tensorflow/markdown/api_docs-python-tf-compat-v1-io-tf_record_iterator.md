[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.io.tf\_record\_iterator Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/tf_record.py#L148-L167)

An iterator that read the records from a TFRecords file. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.python_io.tf_record_iterator`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator)

tf.compat.v1.io.tf_record_iterator(
        path, options=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | The path to the TFRecords file. |
| `options` | (optional) A TFRecordOptions object. |

|     |
| --- |
| Returns<br>------- |     |
| An iterator of serialized TFRecords. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `IOError` | If `path` cannot be opened for reading. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.