[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.dot Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2940-L2966)

Dot product of two tensors.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.dot`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot)

tf.keras.ops.dot(
        x1, x2
    )

*   If both `x1` and `x2` are 1-D tensors, it is inner product of vectors (without complex conjugation).
*   If both `x1` and `x2` are 2-D tensors, it is matrix multiplication.
*   If either `x1` or `x2` is 0-D (scalar), it is equivalent to `x1 * x2`.
*   If `x1` is an N-D tensor and `x2` is a 1-D tensor, it is a sum product over the last axis of `x1` and `x2`.
*   If `x1` is an N-D tensor and `x2` is an M-D tensor (where `M>=2`), it is a sum product over the last axis of `x1` and the second-to-last axis of `x2`: `dot(x1, x2)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First argument. |
| `x2` | Second argument. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend does not accept 0-D tensors as arguments. |     |

|     |
| --- |
| Returns<br>------- |     |
| Dot product of `x1` and `x2`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.