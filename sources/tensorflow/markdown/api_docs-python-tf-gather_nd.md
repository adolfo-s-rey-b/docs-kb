[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/gather_nd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/gather_nd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/gather_nd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/gather_nd#used-in-the-notebooks)
    
*   [Gathering scalars](https://www.tensorflow.org/api_docs/python/tf/gather_nd#gathering_scalars)
    
*   [Gathering slices](https://www.tensorflow.org/api_docs/python/tf/gather_nd#gathering_slices)
    
*   [Batches](https://www.tensorflow.org/api_docs/python/tf/gather_nd#batches)
    *   [More examples](https://www.tensorflow.org/api_docs/python/tf/gather_nd#more_examples)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/gather_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/gather_nd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.gather\_nd Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/gather_nd#used-in-the-notebooks)
    
*   [Gathering scalars](https://www.tensorflow.org/api_docs/python/tf/gather_nd#gathering_scalars)
    
*   [Gathering slices](https://www.tensorflow.org/api_docs/python/tf/gather_nd#gathering_slices)
    
*   [Batches](https://www.tensorflow.org/api_docs/python/tf/gather_nd#batches)
    *   [More examples](https://www.tensorflow.org/api_docs/python/tf/gather_nd#more_examples)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/gather_nd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/gather_nd#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L5429-L5440)

Gather slices from `params` into a Tensor with shape specified by `indices`.

tf.gather_nd(
        params, indices, batch_dims=0, name=None, bad_indices_policy=''
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing) | *   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning) |

`indices` is a `Tensor` of indices into `params`. The index vectors are arranged along the last axis of `indices`.

This is similar to [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
, in which `indices` defines slices into the first dimension of `params`. In [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd)
, `indices` defines slices into the first `N` dimensions of `params`, where `N = indices.shape[-1]`.

Gathering scalars
-----------------

In the simplest case the vectors in `indices` index the full rank of `params`:

    tf.gather_nd(

In this case the result has 1-axis fewer than `indices`, and each index vector is replaced by the scalar indexed from `params`.

In this case the shape relationship is:

index_depth = indices.shape[-1]
    assert index_depth == params.shape.rank
    result_shape = indices.shape[:-1]

If `indices` has a rank of `K`, it is helpful to think `indices` as a (K-1)-dimensional tensor of indices into `params`.

Gathering slices
----------------

If the index vectors do not index the full rank of `params` then each location in the result contains a slice of params. This example collects rows from a matrix:

    tf.gather_nd(

Here `indices` contains `[2]` index vectors, each with a length of `1`. The index vectors each refer to rows of the `params` matrix. Each row has a shape of `[3]` so the output shape is `[2, 3]`.

In this case, the relationship between the shapes is:

index_depth = indices.shape[-1]
    outer_shape = indices.shape[:-1]
    assert index_depth <= params.shape.rank
    inner_shape = params.shape[index_depth:]
    output_shape = outer_shape + inner_shape

It is helpful to think of the results in this case as tensors-of-tensors. The shape of the outer tensor is set by the leading dimensions of `indices`. While the shape of the inner tensors is the shape of a single slice.

Batches
-------

Additionally, both `params` and `indices` can have `M` leading batch dimensions that exactly match. In this case `batch_dims` must be set to `M`.

For example, to collect one row from each of a batch of matrices you could set the leading elements of the index vectors to be their location in the batch:

    tf.gather_nd(

The `batch_dims` argument lets you omit those leading location dimensions from the index:

    tf.gather_nd(

This is equivalent to caling a separate `gather_nd` for each location in the batch dimensions.

    params=tf.zeros([5, 7, 3])

### More examples

Indexing into a 3-tensor:

    tf.gather_nd(

    tf.gather_nd(

    tf.gather_nd(

The examples below are for the case when only indices have leading extra dimensions. If both 'params' and 'indices' have leading batch dimensions, use the 'batch\_dims' parameter to run gather\_nd in batch mode.

Batched indexing into a matrix:

    tf.gather_nd(

Batched slice indexing into a matrix:

    tf.gather_nd(

Batched indexing into a 3-tensor:

    tf.gather_nd(

    tf.gather_nd(

    tf.gather_nd(

Examples with batched 'params' and 'indices':

    tf.gather_nd(

    tf.gather_nd(

    tf.gather_nd(

See also [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A `Tensor`. The tensor from which to gather values. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Index tensor. |
| `name` | A name for the operation (optional). |
| `batch_dims` | An integer or a scalar 'Tensor'. The number of batch dimensions. |
| `bad_indices_policy` | A string. If `""` or `"DEFAULT"`, the default behavior is used (error on CPU and ignore on GPU). If `"IGNORE"`, the bad indices are ignored and 0 is stored in the corresponding output value. If `"ERROR"`, an error is raised. Accelerators generally don't support `"ERROR"`. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `params`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.