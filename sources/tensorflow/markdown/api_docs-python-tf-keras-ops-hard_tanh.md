[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fhard_tanh&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.hard\_tanh Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L798-L823)

Applies the HardTanh function element-wise.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.hard_tanh`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/hard_tanh)

tf.keras.ops.hard_tanh(
        x
    )

#### It is defined as:

`f(x) = -1 for x < -1`, `f(x) = x for -1 <= x <= 1`, `f(x) = 1 for x > 1`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor of same shape as `x` where values are clamped between -1 and 1. |     |

#### Example:

    x = np.array([-2., -1., 0., 1., 2.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.