[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.empty\_like Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L3342-L3365)

Return a new uninitialized tensor with the same shape and dtype as `x`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.empty_like`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/empty_like)

tf.keras.ops.empty_like(
        x, dtype=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor to mimic shape and dtype. |
| `dtype` | Optional data type. If None, uses `x.dtype`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape and dtype as `x`, with arbitrary contents. |     |

#### Example:

    from keras import ops

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.