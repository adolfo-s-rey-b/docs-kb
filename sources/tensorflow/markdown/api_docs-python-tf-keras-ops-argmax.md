[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.argmax Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1057-L1086)

Returns the indices of the maximum values along an axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.argmax`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/argmax)

tf.keras.ops.argmax(
        x, axis=None, keepdims=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | By default, the index is into the flattened tensor, otherwise along the specified axis. |
| `keepdims` | If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. Defaults to `False`. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of indices. It has the same shape as `x`, with the dimension along `axis` removed. |     |

#### Example:

    x = keras.ops.arange(6).reshape(2, 3) + 10

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.