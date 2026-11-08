[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fglu&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.glu Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L725-L751)

Gated Linear Unit (GLU) activation function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.glu`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/glu)

tf.keras.ops.glu(
        x, axis=-1
    )

#### It is defined as:

`f(x) = a * sigmoid(b)` where `x` is split into `a` and `b` along the given axis.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | The axis along which to split the input tensor. Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape as half of the input. |     |

#### Example:

    x = np.array([-1., 0., 1. , 1.])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.