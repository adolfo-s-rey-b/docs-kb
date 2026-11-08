[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.polar Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L3207-L3241)

Constructs a complex tensor whose elements are Cartesian coordinates corresponding to the polar coordinates with absolute value `abs` and angle `angle`.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.polar`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/polar)

tf.keras.ops.polar(
        abs_, angle
    )

The operation is numerically equivalent to `torch.polar()`. It is not equivalent to `scipy.lingalg.polar()` which performs Singular Value Decomposition.

Given the magnitude (`abs_`) and angle (`angle`), this function computes the corresponding complex number in the form of `real + imaginary * 1j`, where:

*   `real = abs_ * cos(angle)`
*   `imaginary = abs_ * sin(angle)`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `abs_` | The magnitude (absolute value) of the complex number. |
| `angle` | The angle (in radians) of the complex number. |

|     |
| --- |
| Returns<br>------- |     |
| A complex number (or array of complex numbers) with the same shape as `abs_` and `angle`. |     |

#### Example:

    abs_ = keras.random.normal((1, 2))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.