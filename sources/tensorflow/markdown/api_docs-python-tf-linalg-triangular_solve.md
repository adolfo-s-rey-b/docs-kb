[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.triangular\_solve Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L84-L144)

Solve systems of linear equations with upper or lower triangular matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.triangular_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve)
, [`tf.compat.v1.matrix_triangular_solve`](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve)

tf.linalg.triangular_solve(
        matrix, rhs, lower=True, adjoint=False, name=None
    )

`matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form square matrices. If `lower` is `True` then the strictly upper triangular part of each inner-most matrix is assumed to be zero and not accessed. If `lower` is `False` then the strictly lower triangular part of each inner-most matrix is assumed to be zero and not accessed. `rhs` is a tensor of shape `[..., M, N]`.

The output is a tensor of shape `[..., M, N]`. If `adjoint` is `True` then the innermost matrices in output satisfy matrix equations `sum_k matrix[..., i, k] * output[..., k, j] = rhs[..., i, j]`. If `adjoint` is `False` then the innermost matrices in output satisfy matrix equations `sum_k adjoint(matrix[..., i, k]) * output[..., k, j] = rhs[..., i, j]`.

#### Example:

    a = tf.constant([[3,  0,  0,  0],\
\
    b = tf.constant([[4], [2], [4], [2]], dtype=tf.float32)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `matrix` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`. |\
| `rhs` | A `Tensor`. Must have the same type as `matrix`. Shape is `[..., M, N]`. |\
| `lower` | An optional `bool`. Defaults to `True`. Boolean indicating whether the innermost matrices in matrix are lower or upper triangular. |\
| `adjoint` | An optional `bool`. Defaults to `False`. Boolean indicating whether to solve with matrix or its (block-wise) adjoint. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as matrix, and shape is `[..., M, N]`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.