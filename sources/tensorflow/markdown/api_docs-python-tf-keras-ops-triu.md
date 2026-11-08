[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.triu Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8277-L8294)

Return upper triangle of a tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.triu`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/triu)

tf.keras.ops.triu(
        x, k=0
    )

For tensors with `ndim` exceeding 2, `triu` will apply to the final two axes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `k` | Diagonal below which to zero elements. Defaults to `0`. the main diagonal. `k < 0` is below it, and `k > 0` is above it. |

|     |
| --- |
| Returns<br>------- |     |
| Upper triangle of `x`, of same shape and data type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.