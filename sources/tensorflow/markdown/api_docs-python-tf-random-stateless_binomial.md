[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_binomial#main-content)

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
    

tf.random.stateless\_binomial Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L411-L478)

Outputs deterministic pseudorandom values from a binomial distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_binomial`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_binomial)

tf.random.stateless_binomial(
        shape,
        seed,
        counts,
        probs,
        output_dtype=tf.dtypes.int32,
        name=None
    )

The generated values follow a binomial distribution with specified count and probability of success parameters.

This is a stateless version of [`tf.random.Generator.binomial`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#binomial)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

#### Example:

counts = [10., 20.]
    # Probability of success.
    probs = [0.8]
    
    binomial_samples = tf.random.stateless_binomial(
        shape=[2], seed=[123, 456], counts=counts, probs=probs)
    
    counts = ... # Shape [3, 1, 2]
    probs = ...  # Shape [1, 4, 2]
    shape = [3, 4, 3, 4, 2]
    # Sample shape will be [3, 4, 3, 4, 2]
    binomial_samples = tf.random.stateless_binomial(
        shape=shape, seed=[123, 456], counts=counts, probs=probs)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `counts` | Tensor. The counts of the binomial distribution. Must be broadcastable with `probs`, and broadcastable with the rightmost dimensions of `shape`. |
| `probs` | Tensor. The probability of success for the binomial distribution. Must be broadcastable with `counts` and broadcastable with the rightmost dimensions of `shape`. |
| `output_dtype` | The type of the output. Default: tf.int32 |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `samples` | A Tensor of the specified shape filled with random binomial values. For each i, each samples\[..., i\] is an independent draw from the binomial distribution on counts\[i\] trials with probability of success probs\[i\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.