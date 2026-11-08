[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.float\_power Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/numpy.py#L9299-L9322)

First tensor elements raised to powers from second tensor, in floats.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.float_power`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/float_power)

tf.keras.ops.float_power(
        x1, x2
    )

This is `power` with the operands promoted to a float dtype first, so a negative exponent has a well defined result for integer inputs, where `power` either raises an error or returns an integer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | The bases. |
| `x2` | The exponents. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, the bases in `x1` raised to the exponents in `x2`. |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([2, 3, 4])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.