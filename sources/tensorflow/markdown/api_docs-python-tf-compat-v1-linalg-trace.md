[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.linalg.trace Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3431-L3472)

Compute the trace of a tensor `x`.

tf.compat.v1.linalg.trace(
        x, name=None
    )

`trace(x)` returns the sum along the main diagonal of each inner-most matrix in x. If x is of rank `k` with shape `[I, J, K, ..., L, M, N]`, then output is a tensor of rank `k-2` with dimensions `[I, J, K, ..., L]` where

`output[i, j, k, ..., l] = trace(x[i, j, k, ..., l, :, :])`

#### For example:

x = tf.constant([[1, 2], [3, 4]])
    tf.linalg.trace(x)  # 5
    
    x = tf.constant([[1, 2, 3],\
                     [4, 5, 6],\
                     [7, 8, 9]])
    tf.linalg.trace(x)  # 15
    
    x = tf.constant([[[1, 2, 3],\
                      [4, 5, 6],\
                      [7, 8, 9]],\
                     [[-1, -2, -3],\
                      [-4, -5, -6],\
                      [-7, -8, -9]]])
    tf.linalg.trace(x)  # [15, -15]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | tensor. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The trace of input tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.