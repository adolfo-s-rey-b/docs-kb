[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.transpose Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/transpose#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1907-L1992)

Transposes `a`.

tf.compat.v1.transpose(
        a, perm=None, name='transpose', conjugate=False
    )

Permutes the dimensions according to `perm`.

The returned tensor's dimension i will correspond to the input dimension `perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank of the input tensor. Hence, by default, this operation performs a regular matrix transpose on 2-D input Tensors. If conjugate is True and `a.dtype` is either `complex64` or `complex128` then the values of `a` are conjugated and transposed.

#### For example:

x = tf.constant([[1, 2, 3], [4, 5, 6]])
    tf.transpose(x)  # [[1, 4]\
                     #  [2, 5]\
                     #  [3, 6]]
    
    # Equivalently
    tf.transpose(x, perm=[1, 0])  # [[1, 4]\
                                  #  [2, 5]\
                                  #  [3, 6]]
    
    # If x is complex, setting conjugate=True gives the conjugate transpose
    x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],\
                     [4 + 4j, 5 + 5j, 6 + 6j]])
    tf.transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],\
                                     #  [2 - 2j, 5 - 5j],\
                                     #  [3 - 3j, 6 - 6j]]
    
    # 'perm' is more useful for n-dimensional tensors, for n > 2
    x = tf.constant([[[ 1,  2,  3],\
                      [ 4,  5,  6]],\
                     [[ 7,  8,  9],\
                      [10, 11, 12]]])
    
    # Take the transpose of the matrices in dimension-0
    # (this common operation has a shorthand `linalg.matrix_transpose`)
    tf.transpose(x, perm=[0, 2, 1])  # [[[1,  4],\
                                     #   [2,  5],\
                                     #   [3,  6]],\
                                     #  [[7, 10],\
                                     #   [8, 11],\
                                     #   [9, 12]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | A `Tensor`. |
| `perm` | A permutation of the dimensions of `a`. |
| `name` | A name for the operation (optional). |
| `conjugate` | Optional bool. Setting it to `True` is mathematically equivalent to tf.math.conj(tf.transpose(input)). |

|     |
| --- |
| Returns<br>------- |     |
| A transposed `Tensor`. |     |

numpy compatibility
-------------------

In `numpy` transposes are memory-efficient constant time operations as they simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, so `transpose` returns a new tensor with the items permuted.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.