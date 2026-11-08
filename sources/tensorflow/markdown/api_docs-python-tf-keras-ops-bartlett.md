[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fbartlett&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.bartlett Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1399-L1420)

Bartlett window function.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.bartlett`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/bartlett)

tf.keras.ops.bartlett(
        x
    )

The Bartlett window is a triangular window that rises then falls linearly.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Scalar or 1D Tensor. Window length. |

|     |
| --- |
| Returns<br>------- |     |
| A 1D tensor containing the Bartlett window values. |     |

#### Example:

    x = keras.ops.convert_to_tensor(5)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.