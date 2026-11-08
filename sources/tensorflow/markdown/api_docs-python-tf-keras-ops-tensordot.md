[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.tensordot Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L8068-L8087)

Compute the tensor dot product along specified axes.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.tensordot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot)

tf.keras.ops.tensordot(
        x1, x2, axes=2
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First tensor. |
| `x2` | Second tensor. |
| `axes` | *   If an integer, N, sum over the last N axes of `x1` and the first N axes of `x2` in order. The sizes of the corresponding axes must match.<br>*   Or, a list of axes to be summed over, first sequence applying to `x1`, second to `x2`. Both sequences must be of the same length. |

|     |
| --- |
| Returns<br>------- |     |
| The tensor dot product of the inputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.