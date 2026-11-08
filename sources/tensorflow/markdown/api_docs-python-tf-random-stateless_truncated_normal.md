[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_truncated\_normal Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L695-L746)

Outputs deterministic pseudorandom values, truncated normally distributed.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal)

tf.random.stateless_truncated_normal(
        shape,
        seed,
        mean=0.0,
        stddev=1.0,
        dtype=tf.dtypes.float32,
        name=None,
        alg='auto_select'
    )

This is a stateless version of [`tf.random.truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

The generated values follow a normal distribution with specified mean and standard deviation, except that values whose magnitude is more than 2 standard deviations from the mean are dropped and re-picked.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `mean` | A 0-D Tensor or Python value of type `dtype`. The mean of the truncated normal distribution. |
| `stddev` | A 0-D Tensor or Python value of type `dtype`. The standard deviation of the normal distribution, before truncation. |
| `dtype` | The type of the output. |
| `name` | A name for the operation (optional). |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for a detailed explanation. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of the specified shape filled with random truncated normal values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.