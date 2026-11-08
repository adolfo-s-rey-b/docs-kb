[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.tridiagonal\_matmul Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L670-L748)

Multiplies tridiagonal matrix by matrix.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.tridiagonal_matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul)

tf.linalg.tridiagonal_matmul(
        diagonals, rhs, diagonals_format='compact', name=None
    )

`diagonals` is representation of 3-diagonal NxN matrix, which depends on `diagonals_format`.

In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with two inner-most dimensions representing the square tridiagonal matrices. Elements outside of the three diagonals will be ignored.

If `sequence` format, `diagonals` is list or tuple of three tensors: `[superdiag, maindiag, subdiag]`, each having shape \[..., M\]. Last element of `superdiag` first element of `subdiag` are ignored.

In `compact` format the three diagonals are brought together into one tensor of shape `[..., 3, M]`, with last two dimensions containing superdiagonals, diagonals, and subdiagonals, in order. Similarly to `sequence` format, elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

The `sequence` format is recommended as the one with the best performance.

`rhs` is matrix to the right of multiplication. It has shape `[..., M, N]`.

#### Example:

superdiag = tf.constant([-1, -1, 0], dtype=tf.float64)
    maindiag = tf.constant([2, 2, 2], dtype=tf.float64)
    subdiag = tf.constant([0, -1, -1], dtype=tf.float64)
    diagonals = [superdiag, maindiag, subdiag]
    rhs = tf.constant([[1, 1], [1, 1], [1, 1]], dtype=tf.float64)
    x = tf.linalg.tridiagonal_matmul(diagonals, rhs, diagonals_format='sequence')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `diagonals` | A `Tensor` or tuple of `Tensor`s describing left-hand sides. The shape depends of `diagonals_format`, see description above. Must be `float32`, `float64`, `complex64`, or `complex128`. |
| `rhs` | A `Tensor` of shape \[..., M, N\] and with the same dtype as `diagonals`. |
| `diagonals_format` | one of `sequence`, or `compact`. Default is `compact`. |
| `name` | A name to give this `Op` (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape \[..., M, N\] containing the result of multiplication. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | An unsupported type is provided as input, or when the input tensors have incorrect shapes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.