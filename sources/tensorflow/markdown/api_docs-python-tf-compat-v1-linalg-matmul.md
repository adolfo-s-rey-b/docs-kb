[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flinalg%2Fmatmul%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.linalg.matmul Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3475-L3740)

Multiplies matrix `a` by matrix `b`, producing `a` \* `b`.

tf.compat.v1.linalg.matmul(
        a,
        b,
        transpose_a=False,
        transpose_b=False,
        adjoint_a=False,
        adjoint_b=False,
        a_is_sparse=False,
        b_is_sparse=False,
        output_type=None,
        grad_a=False,
        grad_b=False,
        name=None
    )

The inputs must, following any transpositions, be tensors of rank >= 2 where the inner 2 dimensions specify valid matrix multiplication dimensions, and any further outer dimensions specify matching batch size.

Both matrices must be of the same type. The supported types are: `bfloat16`, `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.

Either matrix can be transposed or adjointed (conjugated and transposed) on the fly by setting one of the corresponding flag to `True`. These are `False` by default.

If one or both of the matrices contain a lot of zeros, a more efficient multiplication algorithm can be used by setting the corresponding `a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default. This optimization is only available for plain matrices (rank-2 tensors) with datatypes `bfloat16` or `float32`.

A simple 2-D tensor matrix multiplication:

    a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

A batch matrix multiplication with batch shape \[2\]:

    a = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])

Since python >= 3.5 the @ operator is supported (see [PEP 465](https://www.python.org/dev/peps/pep-0465/)
). In TensorFlow, it simply calls the [`tf.matmul()`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)
 function, so the following lines are equivalent:

    d = a @ b @ [[10], [11]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type `float16`, `float32`, `float64`, `int32`, `complex64`, `complex128` and rank > 1. |
| `b` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with same type and rank as `a`. |
| `transpose_a` | If `True`, `a` is transposed before multiplication. |
| `transpose_b` | If `True`, `b` is transposed before multiplication. |
| `adjoint_a` | If `True`, `a` is conjugated and transposed before multiplication. |
| `adjoint_b` | If `True`, `b` is conjugated and transposed before multiplication. |
| `a_is_sparse` | If `True`, `a` is treated as a sparse matrix. Notice, this **does not support [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>**, it just makes optimizations that assume most values in `a` are zero. See [`tf.sparse.sparse_dense_matmul`](https://www.tensorflow.org/api_docs/python/tf/sparse/sparse_dense_matmul)<br> for some support for [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> multiplication. |
| `b_is_sparse` | If `True`, `b` is treated as a sparse matrix. Notice, this **does not support [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>**, it just makes optimizations that assume most values in `b` are zero. See [`tf.sparse.sparse_dense_matmul`](https://www.tensorflow.org/api_docs/python/tf/sparse/sparse_dense_matmul)<br> for some support for [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> multiplication. |
| `output_type` | The output datatype if needed. Defaults to None in which case the output\_type is the same as input type. Currently only works when input tensors are type (u)int8 and output\_type can be int32. |
| `grad_a` | Set it to `True` to hint that Tensor `a` is for the backward pass. |
| `grad_b` | Set it to `True` to hint that Tensor `b` is for the backward pass. |
| `name` | Name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the same type as `a` and `b` where each inner-most matrix is the product of the corresponding matrices in `a` and `b`, e.g. if all transpose or adjoint attributes are `False`:<br><br>`output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j])`, for all indices `i`, `j`. |     |
| `Note` | This is matrix product, not element-wise product. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `transpose_a` and `adjoint_a`, or `transpose_b` and `adjoint_b` are both set to `True`. |
| `TypeError` | If output\_type is specified but the types of `a`, `b` and `output_type` is not (u)int8, (u)int8 and int32. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.