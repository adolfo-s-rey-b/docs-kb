[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/experimental/index_shuffle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.experimental.index\_shuffle Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L135-L223)

Outputs the position of `index` in a permutation of `[0, ..., max_index]`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.index_shuffle`](https://www.tensorflow.org/api_docs/python/tf/random/experimental/index_shuffle)

tf.random.experimental.index_shuffle(
        index, seed, max_index
    )

For each possible `seed` and `max_index` there is one pseudorandom permutation of the sequence `S=[0, ..., max_index]`. Instead of materializing the full array we can compute the new position of any integer `i` (`0 <= i <= max_index`) in `S`. This can be useful for very large `max_index`s by avoiding allocating large chunks of memory.

In the simplest case, `index` and `max_index` are scalars, and `seed` is a length-2 vector (as typical for stateless RNGs). But you can add a leading batch dimension to all of them. If some of them don't have the batch dimension while others do, `index_shuffle` will add a batch dimension to the former by broadcasting.

The input `index` and output can be used as indices to shuffle a vector. For example:

    vector = tf.constant(['e0', 'e1', 'e2', 'e3'])

More usefully, it can be used in a streaming (aka online) scenario such as [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
, where each element of `vector` is processed individually and the whole `vector` is never materialized in memory.

    dataset = tf.data.Dataset.range(10)

This operation is stateless (like the `tf.random.stateless_*` functions), meaning the output is fully determined by the `seed` (other inputs being equal). Each `seed` choice corresponds to one permutation, so when calling this function multiple times for the same shuffling, please make sure to use the same `seed`. For example:

    seed = [5, 9]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `index` | An integer scalar tensor or vector with values in `[0, max_index]`. It can be seen as either a value `v` in the sequence `S=[0, ..., max_index]` to be permutated, or as an index of an element `e` in a shuffled vector. |
| `seed` | A tensor of shape \[2\] or \[n, 2\] with dtype `int32`, `uint32`, `int64` or `uint64`. The RNG seed. If the rank is unknown during graph-building time it must be 1 at runtime. |
| `max_index` | A non-negative tensor with the same shape and dtype as `index`. The upper bound (inclusive). |

|     |
| --- |
| Returns<br>------- |     |
| If all inputs were scalar (shape \[2\] for `seed`), the output will be a scalar with the same dtype as `index`. The output can be seen as the new position of `v` in `S`, or as the index of `e` in the vector before shuffling. If one or multiple inputs were vectors (shape \[n, 2\] for `seed`), then the output will be a vector of the same size which each element shuffled independently. Scalar values are broadcasted in this case. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.