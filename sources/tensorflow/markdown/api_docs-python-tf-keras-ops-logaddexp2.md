[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.logaddexp2 Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4868-L4890)

Base-2 logarithm of the sum of exponentiations of the inputs.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.logaddexp2`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/logaddexp2)

tf.keras.ops.logaddexp2(
        x1, x2
    )

Calculates `log2(2**x1 + 2**x2)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | Input tensor. |
| `x2` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, element-wise log base 2 of the sum of 2**x1 and 2**x2. |     |

#### Example:

    from keras import ops

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.