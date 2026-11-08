[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/unstack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/unstack)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/unstack?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/unstack#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unstack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unstack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/unstack#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.unstack Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/unstack#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unstack#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unstack#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/unstack#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops_stack.py#L88-L214)

Unpacks the given dimension of a rank-`R` tensor into rank-`(R-1)` tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.unstack`](https://www.tensorflow.org/api_docs/python/tf/unstack)

tf.unstack(
        value, num=None, axis=0, name='unstack'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

Unpacks tensors from `value` by chipping it along the `axis` dimension.

    x = tf.reshape(tf.range(12), (3,4))

    i, j, k, l = tf.unstack(x, axis=1)

This is the opposite of stack.

    x = tf.stack([i, j, k, l], axis=1)

More generally if you have a tensor of shape `(A, B, C, D)`:

    A, B, C, D = [2, 3, 4, 5]

The number of tensor returned is equal to the length of the target `axis`:

    axis = 2

The shape of each result tensor is equal to the shape of the input tensor, with the target `axis` removed.

    items[0].shape.as_list()  # [A, B, D]

The value of each tensor `items[i]` is equal to the slice of `input` across `axis` at index `i`:

    for i in range(len(items)):

#### Python iterable unpacking

With eager execution you _can_ unstack the 0th axis of a tensor using python's iterable unpacking:

    t = tf.constant([1,2,3])

`unstack` is still necessary because Iterable unpacking doesn't work in a [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
: Symbolic tensors are not iterable.

You need to use [`tf.unstack`](https://www.tensorflow.org/api_docs/python/tf/unstack)
 here:

    @tf.function

    @tf.function

#### Unknown shapes

Eager tensors have concrete values, so their shape is always known. Inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 the symbolic tensors may have unknown shapes. If the length of `axis` is unknown [`tf.unstack`](https://www.tensorflow.org/api_docs/python/tf/unstack)
 will fail because it cannot handle an unknown number of tensors:

    @tf.function(input_signature=[tf.TensorSpec([None], tf.float32)])

If you know the `axis` length you can pass it as the `num` argument. But this must be a constant value.

If you actually need a variable number of tensors in a single [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 trace, you will need to use explicit loops and a [`tf.TensorArray`](https://www.tensorflow.org/api_docs/python/tf/TensorArray)
 instead.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A rank `R > 0` `Tensor` to be unstacked. |
| `num` | An `int`. The length of the dimension `axis`. Automatically inferred if `None` (the default). |
| `axis` | An `int`. The axis to unstack along. Defaults to the first dimension. Negative values wrap around, so the valid range is `[-R, R)`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The list of `Tensor` objects unstacked from `value`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `axis` is out of the range `[-R, R)`. |\
| `ValueError` | If `num` is unspecified and cannot be inferred. |\
| `InvalidArgumentError` | If `num` does not match the shape of `value`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.