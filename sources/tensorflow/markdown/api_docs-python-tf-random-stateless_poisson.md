[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Fstateless_poisson%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.random.stateless\_poisson Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L584-L641)

Outputs deterministic pseudorandom values from a Poisson distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_poisson`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson)

tf.random.stateless_poisson(
        shape,
        seed,
        lam,
        dtype=tf.dtypes.int32,
        name=None
    )

The generated values follow a Poisson distribution with specified rate parameter.

This is a stateless version of [`tf.random.poisson`](https://www.tensorflow.org/api_docs/python/tf/random/poisson)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware, but may change between versions of TensorFlow or on non-CPU/GPU hardware.

A slight difference exists in the interpretation of the `shape` parameter between `stateless_poisson` and `poisson`: in `poisson`, the `shape` is always prepended to the shape of `lam`; whereas in `stateless_poisson` the shape of `lam` must match the trailing dimensions of `shape`.

#### Example:

samples = tf.random.stateless_poisson([10, 2], seed=[12, 34], lam=[5, 15])
    # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
    # the samples drawn from each distribution
    
    samples = tf.random.stateless_poisson([7, 5, 2], seed=[12, 34], lam=[5, 15])
    # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
    # represents the 7x5 samples drawn from each of the two distributions
    
    rate = tf.constant([[1.], [3.], [5.]])
    samples = tf.random.stateless_poisson([30, 3, 1], seed=[12, 34], lam=rate)
    # samples has shape [30, 3, 1], with 30 samples each of 3x1 distributions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `lam` | Tensor. The rate parameter "lambda" of the Poisson distribution. Shape must match the rightmost dimensions of `shape`. |
| `dtype` | Dtype of the samples (int or float dtypes are permissible, as samples are discrete). Default: int32. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `samples` | A Tensor of the specified shape filled with random Poisson values. For each i, each `samples[..., i]` is an independent draw from the Poisson distribution with rate `lam[i]`. |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.