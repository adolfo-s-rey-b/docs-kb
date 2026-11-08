[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.batch\_scatter\_update Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/batch_scatter_update#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/state_ops.py#L946-L1043)

Generalization of [`tf.compat.v1.scatter_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_update)
 to axis different than 0. (deprecated)

tf.compat.v1.batch_scatter_update(
        ref, indices, updates, use_locking=True, name=None
    )

Analogous to `batch_gather`. This assumes that `ref`, `indices` and `updates` have a series of leading dimensions that are the same for all of them, and the updates are performed on the last dimension of indices. In other words, the dimensions should be the following:

`num_prefix_dims = indices.ndims - 1` `batch_dim = num_prefix_dims + 1` `updates.shape = indices.shape + var.shape[batch_dim:]`

where

`updates.shape[:num_prefix_dims]` `== indices.shape[:num_prefix_dims]` `== var.shape[:num_prefix_dims]`

And the operation performed can be expressed as:

`var[i_1, ..., i_n, indices[i_1, ..., i_n, j]] = updates[i_1, ..., i_n, j]`

When indices is a 1D tensor, this operation is equivalent to [`tf.compat.v1.scatter_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_update)
.

To avoid this operation there would be 2 alternatives:

1) Reshaping the variable by merging the first `ndims` dimensions. However, this is not possible because [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)
 returns a Tensor, which we cannot use [`tf.compat.v1.scatter_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_update)
 on. 2) Looping over the first `ndims` of the variable and using [`tf.compat.v1.scatter_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_update)
 on the subtensors that result of slicing the first dimension. This is a valid option for `ndims = 1`, but less efficient than this implementation.

See also [`tf.compat.v1.scatter_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_update)
 and [`tf.compat.v1.scatter_nd_update`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_update)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ref` | `Variable` to scatter onto. |
| `indices` | Tensor containing indices as described above. |
| `updates` | Tensor of updates to apply to `ref`. |
| `use_locking` | Boolean indicating whether to lock the writing operation. |
| `name` | Optional scope name string. |

|     |
| --- |
| Returns<br>------- |     |
| Ref to `variable` after it has been modified. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the initial `ndims` of `ref`, `indices`, and `updates` are not the same. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.