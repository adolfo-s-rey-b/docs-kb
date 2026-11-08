[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.kaiser Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1513-L1539)

Kaiser window function.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.kaiser`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/kaiser)

tf.keras.ops.kaiser(
        x, beta
    )

The Kaiser window is defined as: `w[n] = I0(beta * sqrt(1 - (2n / (N - 1) - 1)^2)) / I0(beta)` where I0 is the modified zeroth-order Bessel function of the first kind.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Scalar or 1D Tensor. The window length. |
| `beta` | Float. Shape parameter for the Kaiser window. |

|     |
| --- |
| Returns<br>------- |     |
| A 1D tensor containing the Kaiser window values. |     |

#### Example:

    x = keras.ops.convert_to_tensor(5)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.