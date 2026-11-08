[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fconjugate&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.conjugate Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2135-L2152)

Returns the complex conjugate, element-wise.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.conjugate`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conjugate)

tf.keras.ops.conjugate(
        x
    )

The complex conjugate of a complex number is obtained by changing the sign of its imaginary part.

[`keras.ops.conj`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conj)
 is a shorthand for this function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| The complex conjugate of each element in `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.