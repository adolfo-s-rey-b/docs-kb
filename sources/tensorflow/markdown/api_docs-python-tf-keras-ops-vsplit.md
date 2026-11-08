[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.vsplit Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8524-L8554)

Split an array into multiple sub-arrays vertically (row-wise).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.vsplit`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vsplit)

tf.keras.ops.vsplit(
        x, indices_or_sections
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `indices_or_sections` | If an integer, N, the tensor will be split into N equal sections along axis 0. If a 1-D array of sorted integers, the entries indicate indices at which the tensor will be split along axis 0. |

|     |
| --- |
| Returns<br>------- |     |
| A list of sub-arrays. |     |

#### Example:

    x = keras.ops.arange(12).reshape((4, 3))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.