[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tensor\_scatter\_nd\_add Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add#returns)
    

Adds sparse `updates` to an existing tensor according to `indices`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tensor_scatter_add`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add)
, [`tf.compat.v1.tensor_scatter_nd_add`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add)

tf.tensor_scatter_nd_add(
        tensor: Annotated[Any, TV_TensorScatterAdd_T],
        indices: Annotated[Any, TV_TensorScatterAdd_Tindices],
        updates: Annotated[Any, TV_TensorScatterAdd_T],
        bad_indices_policy: str = '',
        name=None
    ) -> Annotated[Any, TV_TensorScatterAdd_T]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) |

This operation creates a new tensor by adding sparse `updates` to the passed in `tensor`. This operation is very similar to [`tf.compat.v1.scatter_nd_add`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add)
, except that the updates are added onto an existing tensor (as opposed to a variable). If the memory for the existing tensor cannot be re-used, a copy is made and updated.

`indices` is an integer tensor containing indices into a new tensor of shape `tensor.shape`. The last dimension of `indices` can be at most the rank of `tensor.shape`:

indices.shape[-1] <= tensor.shape.rank

The last dimension of `indices` corresponds to indices into elements (if `indices.shape[-1] = tensor.shape.rank`) or slices (if `indices.shape[-1] < tensor.shape.rank`) along dimension `indices.shape[-1]` of `tensor.shape`. `updates` is a tensor with shape

indices.shape[:-1] + tensor.shape[indices.shape[-1]:]

The simplest form of `tensor_scatter_nd_add` is to add individual elements to a tensor by index. For example, say we want to add 4 elements in a rank-1 tensor with 8 elements.

In Python, this scatter add operation would look like this:

    indices = tf.constant([[4], [3], [1], [7]])

We can also, insert entire slices of a higher rank tensor all at once. For example, if we wanted to insert two slices in the first dimension of a rank-3 tensor with two matrices of new values.

In Python, this scatter add operation would look like this:

    indices = tf.constant([[0], [2]])

If `indices` contains any out-of-bound indices, depending on `bad_indices_policy`, the op will either return an error or ignore the out-of-bound indices. `bad_indices_policy` can be one of the following values:

1.  "" or "DEFAULT": raises on CPU and ignore on GPU. This is because historically on CPU and GPU we handle errors in different ways, and for backward compatibility we keep the default behavior.
2.  "ERROR": raises error; GPU does not support this value.
3.  "IGNORE": ignore the bad indices; supported on both CPU and GPU.

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