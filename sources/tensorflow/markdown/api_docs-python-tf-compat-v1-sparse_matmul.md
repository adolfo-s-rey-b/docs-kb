[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsparse_matmul&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_matmul Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_matmul#returns)
    

Multiply matrix "a" by matrix "b". (deprecated)

tf.compat.v1.sparse_matmul(
        a: Annotated[Any, tf.raw_ops.Any],
        b: Annotated[Any, tf.raw_ops.Any],
        transpose_a: bool = False,
        transpose_b: bool = False,
        a_is_sparse: bool = False,
        b_is_sparse: bool = False,
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

The inputs must be two-dimensional matrices and the inner dimension of "a" must match the outer dimension of "b". Both "a" and "b" must be `Tensor`s not `SparseTensor`s. This op is optimized for the case where at least one of "a" or "b" is sparse, in the sense that they have a large proportion of zero values. The breakeven for using this versus a dense matrix multiply on one platform was 30% zero values in the sparse matrix.

The gradient computation of this operation will only take advantage of sparsity in the input gradient when that gradient comes from a Relu.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `bfloat16`. |
| `b` | A `Tensor`. Must be one of the following types: `float32`, `bfloat16`. |
| `transpose_a` | An optional `bool`. Defaults to `False`. |
| `transpose_b` | An optional `bool`. Defaults to `False`. |
| `a_is_sparse` | An optional `bool`. Defaults to `False`. |
| `b_is_sparse` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.