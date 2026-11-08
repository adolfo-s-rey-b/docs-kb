[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.weighted\_moments Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_moments#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L1327-L1401)

Returns the frequency-weighted mean and variance of `x`.

tf.compat.v1.nn.weighted_moments(
        x, axes, frequency_weights, name=None, keep_dims=None, keepdims=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A tensor. |
| `axes` | 1-d tensor of int32 values; these are the axes along which to compute mean and variance. |
| `frequency_weights` | A tensor of positive weights which can be broadcast with x. |
| `name` | Name used to scope the operation. |
| `keep_dims` | Produce moments with the same dimensionality as the input. |
| `keepdims` | Alias of keep\_dims. |

|     |
| --- |
| Returns<br>------- |     |
| Two tensors: `weighted_mean` and `weighted_variance`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.