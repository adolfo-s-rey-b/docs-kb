[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.moments Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/moments#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1224-L1287)

Calculate the mean and variance of `x`.

tf.compat.v1.nn.moments(
        x, axes, shift=None, name=None, keep_dims=None, keepdims=None
    )

The mean and variance are calculated by aggregating the contents of `x` across `axes`. If `x` is 1-D and `axes = [0]` this is just the mean and variance of a vector.

When using these moments for batch normalization (see [`tf.nn.batch_normalization`](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization)
):

*   for so-called "global normalization", used with convolutional filters with shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
*   for simple batch normalization pass `axes=[0]` (batch only).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. |
| `axes` | Array of ints. Axes along which to compute mean and variance. |
| `shift` | Not used in the current implementation |
| `name` | Name used to scope the operations that compute the moments. |
| `keep_dims` | produce moments with the same dimensionality as the input. |
| `keepdims` | Alias to keep\_dims. |

|     |
| --- |
| Returns<br>------- |     |
| Two `Tensor` objects: `mean` and `variance`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.