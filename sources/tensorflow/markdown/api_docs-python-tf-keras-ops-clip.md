[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.clip Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2047-L2064)

Clip (limit) the values in a tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.clip`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/clip)

tf.keras.ops.clip(
        x, x_min, x_max
    )

Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of `[0, 1]` is specified, values smaller than 0 become 0, and values larger than 1 become 1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `x_min` | Minimum value. |
| `x_max` | Maximum value. |

|     |
| --- |
| Returns<br>------- |     |
| The clipped tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.