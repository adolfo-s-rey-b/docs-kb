[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fhsplit&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.hsplit Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L4025-L4067)

Split an array into multiple sub-arrays horizontally (column-wise).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.hsplit`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hsplit)

tf.keras.ops.hsplit(
        x, indices_or_sections
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `indices_or_sections` | If an integer, N, the tensor will be split into N equal sections along axis 1 (if ndim >= 2) or axis 0 (if ndim == 1). If a 1-D array of sorted integers, the entries indicate indices at which the tensor will be split along the axis. |

|     |
| --- |
| Returns<br>------- |     |
| A list of sub-arrays. |     |

#### Example:

    x = keras.ops.arange(16.0).reshape((4, 4))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.