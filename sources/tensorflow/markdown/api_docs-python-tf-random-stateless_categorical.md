[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Fstateless_categorical&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_categorical Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L793-L832)

Draws deterministic pseudorandom samples from a categorical distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_categorical`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical)

tf.random.stateless_categorical(
        logits,
        num_samples,
        seed,
        dtype=tf.dtypes.int64,
        name=None
    )

This is a stateless version of `tf.categorical`: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

#### Example:

# samples has shape [1, 5], where each value is either 0 or 1 with equal
    # probability.
    samples = tf.random.stateless_categorical(
        tf.math.log([[0.5, 0.5]]), 5, seed=[7, 17])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logits` | 2-D Tensor with shape `[batch_size, num_classes]`. Each slice `[i, :]` represents the unnormalized log-probabilities for all classes. |
| `num_samples` | 0-D. Number of independent samples to draw for each row slice. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `dtype` | The integer type of the output: `int32` or `int64`. Defaults to `int64`. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| The drawn samples of shape `[batch_size, num_samples]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.