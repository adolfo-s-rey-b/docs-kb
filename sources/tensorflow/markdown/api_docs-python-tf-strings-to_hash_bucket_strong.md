[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.to\_hash\_bucket\_strong Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong#returns)
    

Converts each string in the input Tensor to its hash mod by a number of buckets.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.string_to_hash_bucket_strong`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong)
, [`tf.compat.v1.strings.to_hash_bucket_strong`](https://www.tensorflow.org/api_docs/python/tf/strings/to_hash_bucket_strong)

tf.strings.to_hash_bucket_strong(
        input: Annotated[Any, _atypes.String], num_buckets: int, key, name=None
    ) -> Annotated[Any, _atypes.Int64]

The hash function is deterministic on the content of the string within the process. The hash function is a keyed hash function, where attribute `key` defines the key of the hash function. `key` is an array of 2 elements.

A strong hash is important when inputs may be malicious, e.g. URLs with additional components. Adversaries could try to make their inputs hash to the same bucket for a denial-of-service attack or to skew the results. A strong hash can be used to make it difficult to find inputs with a skewed hash value distribution over buckets. This requires that the hash function is seeded by a high-entropy (random) "key" unknown to the adversary.

The additional robustness comes at a cost of roughly 4x higher compute time than `tf.string_to_hash_bucket_fast`.

#### Examples:

    tf.strings.to_hash_bucket_strong(["Hello", "TF"], 3, [1, 2]).numpy()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The strings to assign a hash bucket. |
| `num_buckets` | An `int` that is `>= 1`. The number of buckets. |
| `key` | A list of `ints`. The key used to seed the hash function, passed as a list of two uint64 elements. |
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