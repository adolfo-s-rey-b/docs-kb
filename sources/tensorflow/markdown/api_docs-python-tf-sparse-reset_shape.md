[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Freset_shape&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.reset\_shape Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L2004-L2106)

Resets the shape of a `SparseTensor` with indices and values unchanged.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.reset_shape`](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape)
, [`tf.compat.v1.sparse_reset_shape`](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape)

tf.sparse.reset_shape(
        sp_input, new_shape=None
    )

If `new_shape` is None, returns a copy of `sp_input` with its shape reset to the tight bounding box of `sp_input`. This will be a shape consisting of all zeros if sp\_input has no values.

If `new_shape` is provided, then it must be larger or equal in all dimensions compared to the shape of `sp_input`. When this condition is met, the returned SparseTensor will have its shape reset to `new_shape` and its indices and values unchanged from that of `sp_input.`

|     |
| --- |
| For example<br>----------- |     |
| Consider a `sp_input` with shape \[2, 3, 5\]:<br><br>*   It is an error to set `new_shape` as \[3, 7\] since this represents a rank-2 tensor while `sp_input` is rank-3. This is either a ValueError during graph construction (if both shapes are known) or an OpError during run time.<br>    <br>*   Setting `new_shape` as \[2, 3, 6\] will be fine as this shape is larger or equal in every dimension compared to the original shape \[2, 3, 5\].<br>    <br>*   On the other hand, setting new\_shape as \[2, 3, 4\] is also an error: The third dimension is smaller than the original shape [2, 3, 5](https://www.tensorflow.org/api_docs/python/tf/sparse/and%20an%0A%60InvalidArgumentError%60%20will%20be%20raised)<br>    .<br>    <br>*   If `new_shape` is None, the returned SparseTensor will have a shape \[2, 3, 4\], which is the tight bounding box of `sp_input`. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The input `SparseTensor`. |
| `new_shape` | None or a vector representing the new shape for the returned `SparseTensor`. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` indices and values unchanged from `sp_input`. Its shape is `new_shape` if that is set. Otherwise it is the tight bounding box of `sp_input` |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |
| `ValueError` | If `new_shape` represents a tensor with a different rank from that of `sp_input` (if shapes are known when graph is constructed). |
| `ValueError` | If `new_shape` is determined during graph build to have dimension sizes that are too small. |
| `OpError` | *   If `new_shape` has dimension sizes that are too small.<br>*   If shapes are not known during graph construction time, and during run time it is found out that the ranks do not match. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.