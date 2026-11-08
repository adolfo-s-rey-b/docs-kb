[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fnormalize&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.normalize Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2673-L2709)

Normalizes `x` over the specified axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.normalize`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/normalize)

tf.keras.ops.normalize(
        x, axis=-1, order=2, epsilon=None
    )

It is defined as: `normalize(x) = x / max(norm(x), epsilon)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | The axis or axes along which to perform normalization. Default to -1. |
| `order` | The exponent value in the norm formulation. Defaults to 2. |
| `epsilon` | A lower bound value for the norm. Defaults to [`backend.epsilon()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/epsilon)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The normalized array. |     |

#### Example:

    x = keras.ops.convert_to_tensor([[1, 2, 3], [4, 5, 6]])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.