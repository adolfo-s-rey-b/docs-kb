[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#used-in-the-notebooks)
    
*   [Batching:](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#batching)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.gather Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#used-in-the-notebooks)
    
*   [Batching:](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#batching)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gather#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4781-L4994)

Gather slices from params axis `axis` according to indices. (deprecated arguments)

tf.compat.v1.gather(
        params, indices, validate_indices=None, name=None, axis=None, batch_dims=0
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

Gather slices from `params` axis `axis` according to `indices`. `indices` must be an integer tensor of any dimension (often 1-D).

[`Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)
 works for scalars, [`tf.newaxis`](https://www.tensorflow.org/api_docs/python/tf#newaxis)
, and [python slices](https://numpy.org/doc/stable/reference/arrays.indexing.html#basic-slicing-and-indexing)

[`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
 extends indexing to handle tensors of indices.

In the simplest case it's identical to scalar indexing:

    params = tf.constant(['p0', 'p1', 'p2', 'p3', 'p4', 'p5'])

The most common case is to pass a single axis tensor of indices (this can't be expressed as a python slice because the indices are not sequential):

    indices = [2, 0, 2, 5]

![](https://www.tensorflow.org/images/Gather.png)

The indices can have any shape. When the `params` has 1 axis, the output shape is equal to the input shape:

    tf.gather(params, [[2, 0], [2, 5]]).numpy()

The `params` may also have any shape. `gather` can select slices across any axis depending on the `axis` argument (which defaults to 0). Below it is used to gather first rows, then columns from a matrix:

    params = tf.constant([[0, 1.0, 2.0],\
\
More generally: The output shape has the same shape as the input, with the indexed-axis replaced by the shape of the indices.\
\
    def result_shape(p_shape, i_shape, axis=0):\
\
Here are some examples:\
\
    params.shape.as_list()\
\
    params = tf.random.normal(shape=(5, 6, 7, 8))\
\
This is because each index takes a slice from `params`, and places it at the corresponding location in the output. For the above example\
\
    # For any location in indices\
\
### Batching:\
\
The `batch_dims` argument lets you gather different items from each element of a batch.\
\
Using `batch_dims=1` is equivalent to having an outer loop over the first axis of `params` and `indices`:\
\
    params = tf.constant([\
\
    tf.gather(params, indices, axis=1, batch_dims=1).numpy()\
\
#### This is equivalent to:\
\
    def manually_batched_gather(params, indices, axis):\
\
Higher values of `batch_dims` are equivalent to multiple nested loops over the outer axes of `params` and `indices`. So the overall shape function is\
\
    def batched_result_shape(p_shape, i_shape, axis=0, batch_dims=0):\
\
    tf.gather(params, indices, axis=1, batch_dims=1).shape.as_list()\
\
This comes up naturally if you need to use the indices of an operation like [`tf.argsort`](https://www.tensorflow.org/api_docs/python/tf/argsort)\
, or [`tf.math.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)\
 where the last dimension of the indices indexes into the last dimension of input, at the corresponding location. In this case you can use `tf.gather(values, indices, batch_dims=-1)`.\
\
#### See also:\
\
*   [`tf.Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)\
    : The direct tensor index operation (`t[]`), handles scalars and python-slices `tensor[..., 7, 1:-1]`\
*   `tf.scatter`: A collection of operations similar to `__setitem__` (`t[i] = x`)\
*   [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd)\
    : An operation similar to [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)\
     but gathers across multiple axis at once (it can gather elements of a matrix instead of rows or columns)\
*   [`tf.boolean_mask`](https://www.tensorflow.org/api_docs/python/tf/boolean_mask)\
    , [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
    : Binary indexing.\
*   [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice)\
     and [`tf.strided_slice`](https://www.tensorflow.org/api_docs/python/tf/strided_slice)\
    : For lower level access to the implementation of `__getitem__`'s python-slice handling (`t[1:-1:2]`)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `params` | The `Tensor` from which to gather values. Must be at least rank `axis + 1`. |\
| `indices` | The index `Tensor`. Must be one of the following types: `int32`, `int64`. The values must be in range `[0, params.shape[axis])`. |\
| `validate_indices` | Deprecated, does nothing. Indices are always validated on CPU, never validated on GPU. |\
| `axis` | A `Tensor`. Must be one of the following types: `int32`, `int64`. The `axis` in `params` to gather `indices` from. Must be greater than or equal to `batch_dims`. Defaults to the first non-batch dimension. Supports negative indexes. |\
| `batch_dims` | An `integer`. The number of batch dimensions. Must be less than or equal to `rank(indices)`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `params`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.