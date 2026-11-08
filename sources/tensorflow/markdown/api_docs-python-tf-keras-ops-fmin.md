[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Ffmin&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.fmin Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5456-L5479)

Element-wise minimum of tensor elements, ignoring NaNs.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.fmin`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/fmin)

tf.keras.ops.fmin(
        x1, x2
    )

Compare two tensors element-wise and return the minimum. If one of the elements being compared is a NaN, the non-NaN element is returned. If both elements are NaNs, the NaN is returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First input tensor. |
| `x2` | Second input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, element-wise minimum of `x1` and `x2`. |     |

#### Examples:

    x1 = keras.ops.convert_to_tensor([2.0, float("nan")])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.