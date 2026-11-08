[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.nextafter Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8844-L8869)

Return the next representable floating-point value after `x1` towards `x2`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.nextafter`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nextafter)

tf.keras.ops.nextafter(
        x1, x2
    )

This function computes the next floating-point value following `x1` in the direction of `x2`, element-wise.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | Input tensor whose values will be moved to the next representable floating-point value. |
| `x2` | Input tensor indicating the direction toward which `x1` is moved. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor |     |

#### Example:

    x1 = keras.ops.convert_to_tensor([1.0, 1.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.