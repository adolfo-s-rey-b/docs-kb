[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/poisson#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/poisson)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/poisson?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/poisson#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/poisson#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.poisson Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/poisson#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/poisson#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L586-L629)

Draws `shape` samples from each of the given Poisson distribution(s).

tf.random.poisson(
        shape,
        lam,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

`lam` is the rate parameter describing the distribution(s).

#### Example:

samples = tf.random.poisson([10], [0.5, 1.5])
    # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
    # the samples drawn from each distribution
    
    samples = tf.random.poisson([7, 5], [12.2, 3.3])
    # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
    # represents the 7x5 samples drawn from each of the two distributions

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output samples to be drawn per "rate"-parameterized distribution. |
| `lam` | A Tensor or Python value or N-D array of type `dtype`. `lam` provides the rate parameter(s) describing the poisson distribution(s) to sample. |
| `dtype` | The type of the output: `float16`, `float32`, `float64`, `int32` or `int64`. |
| `seed` | A Python integer. Used to create a random seed for the distributions. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | Optional name for the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `samples` | a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)` with values of type `dtype`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.