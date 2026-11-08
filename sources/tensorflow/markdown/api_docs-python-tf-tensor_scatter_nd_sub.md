[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tensor\_scatter\_nd\_sub Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub#returns)
    

Subtracts sparse `updates` from an existing tensor according to `indices`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tensor_scatter_nd_sub`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub)
, [`tf.compat.v1.tensor_scatter_sub`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub)

tf.tensor_scatter_nd_sub(
        tensor: Annotated[Any, TV_TensorScatterSub_T],
        indices: Annotated[Any, TV_TensorScatterSub_Tindices],
        updates: Annotated[Any, TV_TensorScatterSub_T],
        bad_indices_policy: str = '',
        name=None
    ) -> Annotated[Any, TV_TensorScatterSub_T]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) |

This operation creates a new tensor by subtracting sparse `updates` from the passed in `tensor`. This operation is very similar to `tf.scatter_nd_sub`, except that the updates are subtracted from an existing tensor (as opposed to a variable). If the memory for the existing tensor cannot be re-used, a copy is made and updated.

`indices` is an integer tensor containing indices into a new tensor of shape `shape`. The last dimension of `indices` can be at most the rank of `shape`:

indices.shape[-1] <= shape.rank

The last dimension of `indices` corresponds to indices into elements (if `indices.shape[-1] = shape.rank`) or slices (if `indices.shape[-1] < shape.rank`) along dimension `indices.shape[-1]` of `shape`. `updates` is a tensor with shape

indices.shape[:-1] + shape[indices.shape[-1]:]

The simplest form of tensor\_scatter\_sub is to subtract individual elements from a tensor by index. For example, say we want to insert 4 scattered elements in a rank-1 tensor with 8 elements.

In Python, this scatter subtract operation would look like this:

    indices = tf.constant([[4], [3], [1], [7]])
        updates = tf.constant([9, 10, 11, 12])
        tensor = tf.ones([8], dtype=tf.int32)
        updated = tf.tensor_scatter_nd_sub(tensor, indices, updates)
        print(updated)

The resulting tensor would look like this:

[1, -10, 1, -9, -8, 1, 1, -11]

We can also, insert entire slices of a higher rank tensor all at once. For example, if we wanted to insert two slices in the first dimension of a rank-3 tensor with two matrices of new values.

In Python, this scatter add operation would look like this:

    indices = tf.constant([[0], [2]])
        updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],\
                                [7, 7, 7, 7], [8, 8, 8, 8]],\
                               [[5, 5, 5, 5], [6, 6, 6, 6],\
                                [7, 7, 7, 7], [8, 8, 8, 8]]])
        tensor = tf.ones([4, 4, 4],dtype=tf.int32)
        updated = tf.tensor_scatter_nd_sub(tensor, indices, updates)
        print(updated)

The resulting tensor would look like this:

[[[-4, -4, -4, -4], [-5, -5, -5, -5], [-6, -6, -6, -6], [-7, -7, -7, -7]],\
     [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],\
     [[-4, -4, -4, -4], [-5, -5, -5, -5], [-6, -6, -6, -6], [-7, -7, -7, -7]],\
     [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]

Note that on CPU, if an out of bound index is found, an error is returned. On GPU, if an out of bound index is found, the index is ignored.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. Tensor to copy/update. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `updates` | A `Tensor`. Must have the same type as `tensor`. Updates to scatter into output. |
| `bad_indices_policy` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.