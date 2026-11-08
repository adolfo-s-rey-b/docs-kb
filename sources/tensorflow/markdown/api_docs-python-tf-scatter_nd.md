[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/scatter_nd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.scatter\_nd Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/scatter_nd#returns)
    

Scatters `updates` into a tensor of shape `shape` according to `indices`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.manip.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
, [`tf.compat.v1.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)

tf.scatter_nd(
        indices: Annotated[Any, TV_ScatterNd_Tindices],
        updates: Annotated[Any, TV_ScatterNd_T],
        shape: Annotated[Any, TV_ScatterNd_Tindices],
        bad_indices_policy: str = '',
        name=None
    ) -> Annotated[Any, TV_ScatterNd_T]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) |

Scatter sparse `updates` according to individual values at the specified `indices`. This op returns an output tensor with the `shape` you specify. This op is the inverse of the [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd)
 operator which extracts values or slices from a given tensor.

This operation is similar to [`tf.tensor_scatter_nd_add`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add)
, except that the tensor is zero-initialized. Calling [`tf.scatter_nd(indices, updates, shape)`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
 is identical to calling `tf.tensor_scatter_nd_add(tf.zeros(shape, updates.dtype), indices, updates)`

If `indices` contains duplicates, the associated `updates` are accumulated (summed) into the output tensor.

`indices` is an integer tensor containing indices into the output tensor. The last dimension of `indices` can be at most the rank of `shape`:

indices.shape[-1] <= shape.rank

The last dimension of `indices` corresponds to indices of elements (if `indices.shape[-1] = shape.rank`) or slices (if `indices.shape[-1] < shape.rank`) along dimension `indices.shape[-1]` of `shape`.

`updates` is a tensor with shape:

indices.shape[:-1] + shape[indices.shape[-1]:]

The simplest form of the scatter op is to insert individual elements in a tensor by index. Consider an example where you want to insert 4 scattered elements in a rank-1 tensor with 8 elements.

![](https://www.tensorflow.org/images/ScatterNd1.png)

In Python, this scatter operation would look like this:

    indices = tf.constant([[4], [3], [1], [7]])
        updates = tf.constant([9, 10, 11, 12])
        shape = tf.constant([8])
        scatter = tf.scatter_nd(indices, updates, shape)
        print(scatter)

The resulting tensor would look like this:

[0, 11, 0, 10, 9, 0, 0, 12]

You can also insert entire slices of a higher rank tensor all at once. For example, you can insert two slices in the first dimension of a rank-3 tensor with two matrices of new values.

![](https://www.tensorflow.org/images/ScatterNd2.png)

In Python, this scatter operation would look like this:

    indices = tf.constant([[1], [3]])
        updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],\
                                [7, 7, 7, 7], [8, 8, 8, 8]],\
                               [[5, 5, 5, 5], [6, 6, 6, 6],\
                                [7, 7, 7, 7], [8, 8, 8, 8]]])
        shape = tf.constant([4, 4, 4])
        scatter = tf.scatter_nd(indices, updates, shape)
        print(scatter)

The resulting tensor would look like this:

[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],\
     [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],\
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],\
     [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]]

If `indices` contains any out-of-bound indices, depending on `bad_indices_policy`, the op will either return an error or ignore the out-of-bound indices. `bad_indices_policy` can be one of the following values:

1.  "" or "DEFAULT": raises on CPU and ignore on GPU. This is because historically on CPU and GPU we handle errors in different ways, and for backward compatibility we keep the default behavior.
2.  "ERROR": raises error; GPU does not support this value.
3.  "IGNORE": ignore the bad indices; supported on both CPU and GPU.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. Tensor of indices. |
| `updates` | A `Tensor`. Values to scatter into the output tensor. |
| `shape` | A `Tensor`. Must have the same type as `indices`. 1-D. The shape of the output tensor. |
| `bad_indices_policy` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `updates`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.