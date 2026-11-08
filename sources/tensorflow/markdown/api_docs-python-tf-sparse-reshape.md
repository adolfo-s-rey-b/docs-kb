[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.reshape Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L876-L980)

Reshapes a `SparseTensor` to represent values in a new dense shape.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.reshape`](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape)
, [`tf.compat.v1.sparse_reshape`](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape)

tf.sparse.reshape(
        sp_input, shape, name=None
    )

This operation has the same semantics as `reshape` on the represented dense tensor. The indices of non-empty values in `sp_input` are recomputed based on the new dense shape, and a new `SparseTensor` is returned containing the new indices and new shape. The order of non-empty values in `sp_input` is unchanged.

If one component of `shape` is the special value -1, the size of that dimension is computed so that the total dense size remains constant. At most one component of `shape` can be -1. The number of dense elements implied by `shape` must be the same as the number of dense elements originally represented by `sp_input`.

For example, if `sp_input` has shape `[2, 3, 6]` and `indices` / `values`:

[0, 0, 0]: a
    [0, 0, 1]: b
    [0, 1, 0]: c
    [1, 0, 0]: d
    [1, 2, 3]: e

and `shape` is `[9, -1]`, then the output will be a `SparseTensor` of shape `[9, 4]` and `indices` / `values`:

[0, 0]: a
    [0, 1]: b
    [1, 2]: c
    [4, 2]: d
    [8, 1]: e

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `shape` | A 1-D (vector) int64 `Tensor` specifying the new dense shape of the represented `SparseTensor`. |
| `name` | A name prefix for the returned tensors (optional) |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` with the same non-empty values but with indices calculated by the new dense shape. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |
| `ValueError` | If argument `shape` requests a `SparseTensor` with a different number of elements than `sp_input`. |
| `ValueError` | If `shape` has more than one inferred (== -1) dimension. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.