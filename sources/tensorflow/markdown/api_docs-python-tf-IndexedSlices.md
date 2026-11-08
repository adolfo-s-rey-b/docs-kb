[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#methods)
    *   [consumers](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#consumers)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#__neg__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.IndexedSlices Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#methods)
    *   [consumers](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#consumers)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices#__neg__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/indexed_slices.py#L54-L196)

A sparse representation of a set of tensor slices at given indices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)

tf.IndexedSlices(
        values, indices, dense_shape=None
    )

This class is a simple wrapper for a pair of `Tensor` objects:

*   `values`: A `Tensor` of any dtype with shape `[D0, D1, ..., Dn]`.
*   `indices`: A 1-D integer `Tensor` with shape `[D0]`.

An `IndexedSlices` is typically used to represent a subset of a larger tensor `dense` of shape `[LARGE0, D1, .. , DN]` where `LARGE0 >> D0`. The values in `indices` are the indices in the first dimension of the slices that have been extracted from the larger tensor.

The dense tensor `dense` represented by an `IndexedSlices` `slices` has

dense[slices.indices[i], :, :, :, ...] = slices.values[i, :, :, :, ...]

The `IndexedSlices` class is used principally in the definition of gradients for operations that have sparse gradients (e.g. [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
).

    v = tf.Variable([[0.,1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 8]])

Contrast this representation with [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
, which uses multi-dimensional indices and scalar values.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dense_shape` | A 1-D `Tensor` containing the shape of the corresponding dense tensor. |
| `device` | The name of the device on which `values` will be produced, or `None`. |
| `dtype` | The `DType` of elements in this tensor. |
| `graph` | The `Graph` that contains the values, indices, and shape tensors. |
| `indices` | A 1-D `Tensor` containing the indices of the slices. |
| `name` | The name of this `IndexedSlices`. |
| `op` | The `Operation` that produces `values` as an output. |
| `shape` | Gets the [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> representing the shape of the dense tensor. |
| `values` | A `Tensor` containing the values of the slices. |

Methods
-------

### `consumers`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/indexed_slices.py#L195-L196)

consumers()

### `__neg__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/indexed_slices.py#L162-L163)

__neg__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.