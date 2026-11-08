[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/dropout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.dropout Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/dropout#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5430-L5522)

Computes dropout: randomly sets elements to zero to prevent overfitting.

tf.nn.dropout(
        x, rate, noise_shape=None, seed=None, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Automatically rewrite TF 1.x and compat.v1 API symbols](https://www.tensorflow.org/guide/migrate/upgrade) |

See also: [`tf.keras.layers.Dropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout)
 for a dropout layer.

[Dropout](https://arxiv.org/abs/1207.0580)
 is useful for regularizing DNN models. Inputs elements are randomly set to zero (and the other elements are rescaled). This encourages each node to be independently useful, as it cannot rely on the output of other nodes.

More precisely: With probability `rate` elements of `x` are set to `0`. The remaining elements are scaled up by `1.0 / (1 - rate)`, so that the expected value is preserved.

    tf.random.set_seed(0)

    tf.random.set_seed(0)

    tf.nn.dropout(x, rate = 0.0) == x

By default, each element is kept or dropped independently. If `noise_shape` is specified, it must be [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]` will make independent decisions. This is useful for dropping whole channels from an image or sequence. For example:

    tf.random.set_seed(0)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A floating point tensor. |
| `rate` | A scalar `Tensor` with the same type as x. The probability that each element is dropped. For example, setting rate=0.1 would drop 10% of input elements. |
| `noise_shape` | A 1-D integer `Tensor`, representing the shape for randomly generated keep/drop flags. |
| `seed` | A Python integer. Used to create random seeds. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor of the same shape of `x`. |     |

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