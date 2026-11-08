[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random\_index\_shuffle Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle#returns)
    

Outputs the position of `value` in a permutation of \[0, ..., max\_index\].

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random_index_shuffle`](https://www.tensorflow.org/api_docs/python/tf/random_index_shuffle)

tf.random_index_shuffle(
        index: Annotated[Any, TV_RandomIndexShuffle_dtype],
        seed: Annotated[Any, TV_RandomIndexShuffle_Tseed],
        max_index: Annotated[Any, TV_RandomIndexShuffle_dtype],
        rounds: int = 4,
        name=None
    ) -> Annotated[Any, TV_RandomIndexShuffle_dtype]

Output values are a bijection of the `index` for any combination and `seed` and `max_index`.

If multiple inputs are vectors (matrix in case of seed) then the size of the first dimension must match.

The outputs are deterministic.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `index` | A `Tensor`. Must be one of the following types: `int32`, `uint32`, `int64`, `uint64`. A scalar tensor or a vector of dtype `dtype`. The index (or indices) to be shuffled. Must be within \[0, max\_index\]. |
| `seed` | A `Tensor`. Must be one of the following types: `int32`, `uint32`, `int64`, `uint64`. A tensor of dtype `Tseed` and shape \[3\] or \[n, 3\]. The random seed. |
| `max_index` | A `Tensor`. Must have the same type as `index`. A scalar tensor or vector of dtype `dtype`. The upper bound(s) of the interval (inclusive). |
| `rounds` | An optional `int`. Defaults to `4`. The number of rounds to use the in block cipher. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `index`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.