[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.linalg.matrix\_transpose Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1996-L2073)

Transposes last two dimensions of tensor `a`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.transpose`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose)

tf.compat.v1.linalg.matrix_transpose(
        a, name='matrix_transpose', conjugate=False
    )

#### For example:

x = tf.constant([[1, 2, 3], [4, 5, 6]])
    tf.linalg.matrix_transpose(x)  # [[1, 4],\
                                   #  [2, 5],\
                                   #  [3, 6]]
    
    x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],\
                     [4 + 4j, 5 + 5j, 6 + 6j]])
    tf.linalg.matrix_transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],\
                                                   #  [2 - 2j, 5 - 5j],\
                                                   #  [3 - 3j, 6 - 6j]]
    
    # Matrix with two batch dimensions.
    # x.shape is [1, 2, 3, 4]
    # tf.linalg.matrix_transpose(x) is shape [1, 2, 4, 3]

Note that [`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
 provides kwargs allowing for transpose of arguments. This is done with minimal cost, and is preferable to using this function. E.g.

# Good!  Transpose is taken at minimal additional cost.
    tf.matmul(matrix, b, transpose_b=True)
    
    # Inefficient!
    tf.matmul(matrix, tf.linalg.matrix_transpose(b))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | A `Tensor` with `rank >= 2`. |
| `name` | A name for the operation (optional). |
| `conjugate` | Optional bool. Setting it to `True` is mathematically equivalent to tf.math.conj(tf.linalg.matrix\_transpose(input)). |

|     |
| --- |
| Returns<br>------- |     |
| A transposed batch matrix `Tensor`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `a` is determined statically to have `rank < 2`. |

numpy compatibility
-------------------

In `numpy` transposes are memory-efficient constant time operations as they simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, [`linalg.matrix_transpose`](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_transpose)
 returns a new tensor with the items permuted.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.