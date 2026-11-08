[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fstrings%2Fto_hash_bucket_fast&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.to\_hash\_bucket\_fast Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast#returns)
    

Converts each string in the input Tensor to its hash mod by a number of buckets.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.string_to_hash_bucket_fast`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast)
, [`tf.compat.v1.strings.to_hash_bucket_fast`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_fast)

tf.strings.to_hash_bucket_fast(
        input: Annotated[Any, _atypes.String], num_buckets: int, name=None
    ) -> Annotated[Any, _atypes.Int64]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

The hash function is deterministic on the content of the string within the process and will never change. However, it is not suitable for cryptography. This function may be used when CPU time is scarce and inputs are trusted or unimportant. There is a risk of adversaries constructing inputs that all hash to the same bucket. To prevent this problem, use a strong hash function with `tf.string_to_hash_bucket_strong`.

#### Examples:

    tf.strings.to_hash_bucket_fast(["Hello", "TensorFlow", "2.x"], 3).numpy()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The strings to assign a hash bucket. |
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

Last updated 2024-04-26 UTC.