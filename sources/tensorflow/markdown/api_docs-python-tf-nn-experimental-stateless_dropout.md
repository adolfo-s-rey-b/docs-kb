[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fexperimental%2Fstateless_dropout&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.experimental.stateless\_dropout Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5525-L5666)

Computes dropout: randomly sets elements to zero to prevent overfitting.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.experimental.stateless_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout)

tf.nn.experimental.stateless_dropout(
        x, rate, seed, rng_alg=None, noise_shape=None, name=None
    )

[Dropout](https://arxiv.org/abs/1207.0580)
 is useful for regularizing DNN models. Inputs elements are randomly set to zero (and the other elements are rescaled). This encourages each node to be independently useful, as it cannot rely on the output of other nodes.

More precisely: With probability `rate` elements of `x` are set to `0`. The remaining elements are scaled up by `1.0 / (1 - rate)`, so that the expected value is preserved.

    x = tf.ones([3,5])

    x = tf.ones([3,5])

    tf.nn.experimental.stateless_dropout(x, rate=0.0, seed=[1, 0]) == x

This function is a stateless version of [`tf.nn.dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
, in the sense that no matter how many times you call this function, the same `seed` will lead to the same results, and different `seed` will lead to different results.

    x = tf.ones([3,5])

Compare the above results to those of [`tf.nn.dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
 below. The second time [`tf.nn.dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
 is called with the same seed, it will give a different output.

    tf.random.set_seed(0)

The difference between this function and [`tf.nn.dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
 is analogous to the difference between [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)
 and [`tf.random.uniform`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
. Please see [Random number generation](https://www.tensorflow.org/guide/random_numbers)
 guide for a detailed description of the various RNG systems in TF. As the guide states, legacy stateful RNG ops like [`tf.random.uniform`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
 and [`tf.nn.dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
 are not deprecated yet but highly discouraged, because their states are hard to control.

By default, each element is kept or dropped independently. If `noise_shape` is specified, it must be [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]` will make independent decisions. This is useful for dropping whole channels from an image or sequence. For example:

    x = tf.ones([3,10])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A floating point tensor. |
| `rate` | A scalar `Tensor` with the same type as x. The probability that each element is dropped. For example, setting rate=0.1 would drop 10% of input elements. |
| `seed` | An integer tensor of shape `[2]`. The seed of the random numbers. |
| `rng_alg` | The algorithm used to generate the random numbers (default to `"auto_select"`). See the `alg` argument of [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for the supported values. |
| `noise_shape` | A 1-D integer `Tensor`, representing the shape for randomly generated keep/drop flags. |
| `name` | A name for this operation. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor of the same shape and dtype of `x`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `rate` is not in `[0, 1)` or if `x` is not a floating point tensor. `rate=1` is disallowed, because the output would be all zeros, which is likely not what was intended. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.