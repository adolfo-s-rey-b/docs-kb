[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.fmod Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5532-L5550)

Returns the element-wise remainder of division with truncation.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.fmod`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmod)

tf.keras.ops.fmod(
        x1, x2
    )

Computes the remainder complementary to the `floor_divide` function, equivalent to the C library function `fmod`. The result has the same sign as the dividend `x1`. This is different from [`keras.ops.mod`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/mod)
 which has the same sign as the divisor `x2`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First tensor, the dividend. |
| `x2` | Second tensor, the divisor. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, element-wise remainder with truncation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.