[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Ffliplr&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.fliplr Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3565-L3581)

Reverse the order of elements along axis 1 (left/right).

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.fliplr`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fliplr)

tf.keras.ops.fliplr(
        x
    )

For a 2-D tensor, this flips the entries in each row in the left/right direction. Columns are preserved, but appear in a different order than before.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor, must be at least 2-D. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor with columns reversed. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.