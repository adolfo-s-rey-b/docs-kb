[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#for-example_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_reduce\_sum Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#for-example_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1559-L1625)

Computes [`tf.sparse.add`](https://www.tensorflow.org/api_docs/python/tf/sparse/add)
 of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.reduce_sum`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_reduce_sum)

tf.compat.v1.sparse_reduce_sum(
        sp_input, axis=None, keepdims=None, reduction_axes=None, keep_dims=None
    )

This is the reduction operation for the elementwise [`tf.sparse.add`](https://www.tensorflow.org/api_docs/python/tf/sparse/add)
 op.

This Op takes a SparseTensor and is the sparse counterpart to [`tf.reduce_sum()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)
. In particular, this Op also returns a dense `Tensor` instead of a sparse one.

Reduces `sp_input` along the dimensions given in `reduction_axes`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `reduction_axes` has no entries, all dimensions are reduced, and a tensor with a single element is returned. Additionally, the axes can be negative, similar to the indexing rules in Python.

|     |
| --- |
| For example<br>----------- |     |
| 'x' represents \[\[1, ?, 1\]<br>============================<br><br>\[?, 1, ?\]\]<br>=============<br><br>where ? is implicitly-zero.<br>===========================<br><br>    x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 1, 1], [2, 3]) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The SparseTensor to reduce. Should have numeric type. |
| `axis` | The dimensions to reduce; list or scalar. If `None` (the default), reduces all dimensions. |
| `keepdims` | If true, retain reduced dimensions with length 1. |
| `reduction_axes` | Deprecated name of `axis`. |
| `keep_dims` | Deprecated alias for `keepdims`. |

|     |
| --- |
| Returns<br>------- |     |
| The reduced Tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.