[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.to\_hash\_bucket Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L505-L533)

Converts each string in the input Tensor to its hash mod by a number of buckets.

tf.strings.to_hash_bucket(
        input, num_buckets, name=None
    )

The hash function is deterministic on the content of the string within the process.

Note that the hash function may change from time to time. This functionality will be deprecated and it's recommended to use [`tf.strings.to_hash_bucket_fast()`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast)
 or [`tf.strings.to_hash_bucket_strong()`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong)
.

#### Examples:

    tf.strings.to_hash_bucket(["Hello", "TensorFlow", "2.x"], 3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. |
| `num_buckets` | An `int` that is `>= 1`. The number of buckets. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int64`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.