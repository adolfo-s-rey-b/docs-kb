[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/gamma#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/gamma)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/gamma?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Fgamma&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/gamma#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/gamma#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/random/gamma#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.gamma Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/gamma#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/gamma#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/random/gamma#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L451-L542)

Draws `shape` samples from each of the given Gamma distribution(s).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.gamma`](https://www.tensorflow.org/api_docs/python/tf/random/gamma)
, [`tf.compat.v1.random_gamma`](https://www.tensorflow.org/api_docs/python/tf/random/gamma)

tf.random.gamma(
        shape,
        alpha,
        beta=None,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

`alpha` is the shape parameter describing the distribution(s), and `beta` is the inverse scale parameter(s).

The samples are differentiable w.r.t. alpha and beta. The derivatives are computed using the approach described in (Figurnov et al., 2018).

#### Example:

samples = tf.random.gamma([10], [0.5, 1.5])
    # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
    # the samples drawn from each distribution
    
    samples = tf.random.gamma([7, 5], [0.5, 1.5])
    # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
    # represents the 7x5 samples drawn from each of the two distributions
    
    alpha = tf.constant([[1.],[3.],[5.]])
    beta = tf.constant([[3., 4.]])
    samples = tf.random.gamma([30], alpha=alpha, beta=beta)
    # samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.
    
    loss = tf.reduce_mean(tf.square(samples))
    dloss_dalpha, dloss_dbeta = tf.gradients(loss, [alpha, beta])
    # unbiased stochastic derivatives of the loss function
    alpha.shape == dloss_dalpha.shape  # True
    beta.shape == dloss_dbeta.shape  # True

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output samples to be drawn per alpha/beta-parameterized distribution. |
| `alpha` | A Tensor or Python value or N-D array of type `dtype`. `alpha` provides the shape parameter(s) describing the gamma distribution(s) to sample. Must be broadcastable with `beta`. |
| `beta` | A Tensor or Python value or N-D array of type `dtype`. Defaults to 1. `beta` provides the inverse scale parameter(s) of the gamma distribution(s) to sample. Must be broadcastable with `alpha`. |
| `dtype` | The type of alpha, beta, and the output: `float16`, `float32`, or `float64`. |
| `seed` | A Python integer. Used to create a random seed for the distributions. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | Optional name for the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `samples` | a `Tensor` of shape `tf.concat([shape, tf.shape(alpha + beta)], axis=0)` with values of type `dtype`. |

|     |
| --- |
| References<br>---------- |     |
| Implicit Reparameterization Gradients: [Figurnov et al., 2018](http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)<br> ([pdf](http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.