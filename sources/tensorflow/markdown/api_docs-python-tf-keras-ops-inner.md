[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.inner Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8394-L8418)

Return the inner product of two tensors.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.inner`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/inner)

tf.keras.ops.inner(
        x1, x2
    )

Ordinary inner product of vectors for 1-D tensors (without complex conjugation), in higher dimensions a sum product over the last axes.

Multidimensional arrays are treated as vectors by flattening all but their last axes. The resulting dot product is performed over their last axes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First input tensor. |
| `x2` | Second input tensor. The last dimension of `x1` and `x2` must match. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor. The shape of the output is determined by broadcasting the shapes of `x1` and `x2` after removing their last axes. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.