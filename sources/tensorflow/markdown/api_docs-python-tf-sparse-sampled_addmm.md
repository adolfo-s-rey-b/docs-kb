[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.sampled\_addmm Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4762-L4953)

Performs the sampled matrix multiplication of two dense matrices.

tf.sparse.sampled_addmm(
        indices,
        values,
        dense_shape,
        mat1,
        mat2,
        beta=1.0,
        alpha=1.0,
        output_type=tf.dtypes.float32
    )

Multiplies matrix `mat1` by matrix `mat2` at the locations defined by `indices`. The product is scaled and added to `values`, producing `alpha` \* (`mat1` @ `mat2`) \* spy(`indices`) + `beta` \* `values`.

The function `spy(indices)` is the sparsity pattern matrix derived from `indices`.

The `mat1` and `mat2` inputs must be tensors of rank >= 2 where the inner 2 dimensions specify valid matrix multiplication dimensions, and any further dimensions specify matching batch size.

The `indices`, `values`, and `dense_shape` inputs make up the components of a `SparseTensor` which defines the sparsity pattern of the output. The sparsity pattern has values of 1 at the positions defined by the `SparseTensor`, and 0 elsewhere.

The `alpha` and `beta` inputs are the scaling factors.

The supported types for `values`, `mat1`, and `mat2` are: `bfloat16`, `float16`, `float32`, `float64`.

A simple 2-D tensor operation:

    indices = tf.constant([0, 0, 1, 1], shape=[2, 2])

#### A batch operation:

    indices = tf.constant([0, 1, 1, 0, 0, 0, 1, 0], shape=[2, 2, 2])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing coordinates for the rows and columns to be multiplied. Must have rank > 1. |
| `values` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the values to be scaled and added to the sampled dot product. |
| `dense_shape` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> defining the dense shape of the output. |
| `mat1` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> to be multiplied. Must have rank > 1. |
| `mat2` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> to be multiplied. Must have rank > 1. |
| `beta` | Number to be multiplied with `values`. Defaults to 1.0. |
| `alpha` | Number to be multiplied with the sampled dot product of `mat1` and `mat2`. Defaults to 1.0. |
| `output_type` | The output datatype if needed. Defaults to float32. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple representing the `SparseTensor` components of the result of the operation. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `dense_shape` does not match the shape of the product. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.