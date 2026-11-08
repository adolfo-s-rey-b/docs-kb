[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Fstateless_gamma%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_gamma Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L481-L581)

Outputs deterministic pseudorandom values from a gamma distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_gamma`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma)

tf.random.stateless_gamma(
        shape,
        seed,
        alpha,
        beta=None,
        dtype=tf.dtypes.float32,
        name=None
    )

The generated values follow a gamma distribution with specified concentration (`alpha`) and inverse scale (`beta`) parameters.

This is a stateless version of [`tf.random.gamma`](https://www.tensorflow.org/api_docs/python/tf/random/gamma)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

A slight difference exists in the interpretation of the `shape` parameter between `stateless_gamma` and `gamma`: in `gamma`, the `shape` is always prepended to the shape of the broadcast of `alpha` with `beta`; whereas in `stateless_gamma` the `shape` parameter must always encompass the shapes of each of `alpha` and `beta` (which must broadcast together to match the trailing dimensions of `shape`).

The samples are differentiable w.r.t. alpha and beta. The derivatives are computed using the approach described in (Figurnov et al., 2018).

#### Example:

samples = tf.random.stateless_gamma([10, 2], seed=[12, 34], alpha=[0.5, 1.5])
    # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
    # the samples drawn from each distribution
    
    samples = tf.random.stateless_gamma([7, 5, 2], seed=[12, 34], alpha=[.5, 1.5])
    # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
    # represents the 7x5 samples drawn from each of the two distributions
    
    alpha = tf.constant([[1.], [3.], [5.]])
    beta = tf.constant([[3., 4.]])
    samples = tf.random.stateless_gamma(
        [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)
    # samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.
    
    with tf.GradientTape() as tape:
      tape.watch([alpha, beta])
      loss = tf.reduce_mean(tf.square(tf.random.stateless_gamma(
          [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)))
    dloss_dalpha, dloss_dbeta = tape.gradient(loss, [alpha, beta])
    # unbiased stochastic derivatives of the loss function
    alpha.shape == dloss_dalpha.shape  # True
    beta.shape == dloss_dbeta.shape  # True

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `alpha` | Tensor. The concentration parameter of the gamma distribution. Must be broadcastable with `beta`, and broadcastable with the rightmost dimensions of `shape`. |
| `beta` | Tensor. The inverse scale parameter of the gamma distribution. Must be broadcastable with `alpha` and broadcastable with the rightmost dimensions of `shape`. |
| `dtype` | Floating point dtype of `alpha`, `beta`, and the output. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `samples` | A Tensor of the specified shape filled with random gamma values. For each i, each \`samples\[..., i\] is an independent draw from the gamma distribution with concentration alpha\[i\] and scale beta\[i\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.