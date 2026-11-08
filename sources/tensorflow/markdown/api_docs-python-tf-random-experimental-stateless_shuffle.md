[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.experimental.stateless\_shuffle Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L226-L271)

Randomly and deterministically shuffles a tensor along its first dimension.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.stateless_shuffle`](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle)

tf.random.experimental.stateless_shuffle(
        value, seed, alg='auto_select', name=None
    )

The tensor is shuffled along dimension 0, such that each `value[j]` is mapped to one and only one `output[i]`. For example, a mapping that might occur for a 3x2 tensor is:

[[1, 2],       [[5, 6],\
     [3, 4],  ==>   [1, 2],\
     [5, 6]]        [3, 4]]

    v = tf.constant([[1, 2], [3, 4], [5, 6]])

This is a stateless version of [`tf.random.shuffle`](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)
: if run twice with the same `value` and `seed`, it will produce the same result. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A Tensor to be shuffled. |
| `seed` | A shape \[2\] Tensor. The seed to the random number generator. Must have dtype `int32` or `int64`. |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for a detailed explanation. |
| `name` | A name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of same shape and type as `value`, shuffled along its first dimension. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.