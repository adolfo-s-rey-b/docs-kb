[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_parameterized\_truncated\_normal Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L850-L921)

Outputs random values from a truncated normal distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_parameterized_truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal)

tf.random.stateless_parameterized_truncated_normal(
        shape, seed, means=0.0, stddevs=1.0, minvals=-2.0, maxvals=2.0, name=None
    )

The generated values follow a normal distribution with specified mean and standard deviation, except that values whose magnitude is more than 2 standard deviations from the mean are dropped and re-picked.

#### Examples:

Sample from a Truncated normal, with deferring shape parameters that broadcast.

    means = 0.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer `Tensor` or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `means` | A `Tensor` or Python value of type `dtype`. The mean of the truncated normal distribution. This must broadcast with `stddevs`, `minvals` and `maxvals`, and the broadcasted shape must be dominated by `shape`. |
| `stddevs` | A `Tensor` or Python value of type `dtype`. The standard deviation of the truncated normal distribution. This must broadcast with `means`, `minvals` and `maxvals`, and the broadcasted shape must be dominated by `shape`. |
| `minvals` | A `Tensor` or Python value of type `dtype`. The minimum value of the truncated normal distribution. This must broadcast with `means`, `stddevs` and `maxvals`, and the broadcasted shape must be dominated by `shape`. |
| `maxvals` | A `Tensor` or Python value of type `dtype`. The maximum value of the truncated normal distribution. This must broadcast with `means`, `stddevs` and `minvals`, and the broadcasted shape must be dominated by `shape`. |
| `name` | A name for the operation (optional). |

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