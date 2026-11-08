[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.roll Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L7367-L7385)

Roll tensor elements along a given axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.roll`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/roll)

tf.keras.ops.roll(
        x, shift, axis=None
    )

Elements that roll beyond the last position are re-introduced at the first.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `shift` | The number of places by which elements are shifted. |
| `axis` | The axis along which elements are shifted. By default, the array is flattened before shifting, after which the original shape is restored. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.