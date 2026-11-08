[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.table\_from\_dataset Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/lookup_ops.py#L102-L187)

Returns a lookup table based on the given dataset.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.table_from_dataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/table_from_dataset)

tf.data.experimental.table_from_dataset(
        dataset=None,
        num_oov_buckets=0,
        vocab_size=None,
        default_value=None,
        hasher_spec=lookup_ops.FastHashSpec,
        key_dtype=tf.dtypes.string,
        name=None
    )

This operation constructs a lookup table based on the given dataset of pairs of (key, value).

Any lookup of an out-of-vocabulary token will return a bucket ID based on its hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the `default_value`. The bucket ID range is `[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

#### Sample Usages:

    keys = tf.data.Dataset.range(100)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A dataset containing (key, value) pairs. |
| `num_oov_buckets` | The number of out-of-vocabulary buckets. |
| `vocab_size` | Number of the elements in the vocabulary, if known. |
| `default_value` | The value to use for out-of-vocabulary feature values. Defaults to -1. |
| `hasher_spec` | A `HasherSpec` to specify the hash function to use for assignation of out-of-vocabulary buckets. |
| `key_dtype` | The `key` data type. |
| `name` | A name for this op (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The lookup table based on the given dataset. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If<br><br>*   `dataset` does not contain pairs<br>*   The 2nd item in the `dataset` pairs has a dtype which is incompatible with `default_value`<br>*   `num_oov_buckets` is negative<br>*   `vocab_size` is not greater than zero<br>*   The `key_dtype` is not integer or string |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.