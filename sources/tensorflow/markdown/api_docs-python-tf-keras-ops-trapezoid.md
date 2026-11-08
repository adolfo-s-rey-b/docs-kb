[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Ftrapezoid&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.trapezoid Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9026-L9047)

Integrate along the given axis using the composite trapezoidal rule.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.trapezoid`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/trapezoid)

tf.keras.ops.trapezoid(
        y, x=None, dx=1.0, axis=-1
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y` | Input tensor. |
| `x` | Optional tensor specifying sample points corresponding to `y`. If `None`, spacing is assumed to be `dx`. |
| `dx` | Spacing between sample points when `x` is `None`. |
| `axis` | Axis along which to integrate. Default is the last axis. |

|     |
| --- |
| Returns<br>------- |     |
| The approximate integral of `y` along the given axis. |     |

#### Example:

    y = keras.ops.convert_to_tensor([[1, 2, 3], [4, 5, 6]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.