[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.median Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5265-L5282)

Compute the median along the specified axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.median`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/median)

tf.keras.ops.median(
        x, axis=None, keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Axis or axes along which the medians are computed. Defaults to `axis=None` which is to compute the median(s) along a flattened version of the array. |
| `keepdims` | If this is set to `True`, the axes which are reduce are left in the result as dimensions with size one. |

|     |
| --- |
| Returns<br>------- |     |
| The output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.