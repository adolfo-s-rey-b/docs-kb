[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/where#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.where Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4445-L4654)

Returns the indices of non-zero elements, or multiplexes `x` and `y`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.where_v2`](https://www.tensorflow.org/api_docs/python/tf/where)

tf.where(
        condition, x=None, y=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) | *   [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2)<br>    <br>*   [TFP Release Notes notebook (0.11.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_11_0)<br>    <br>*   [Bayesian Switchpoint Analysis](https://www.tensorflow.org/probability/examples/Bayesian_Switchpoint_Analysis) |

This operation has two modes:

1.  **Return the indices of non-zero elements** - When only `condition` is provided the result is an `int64` tensor where each row is the index of a non-zero element of `condition`. The result's shape is `[tf.math.count_nonzero(condition), tf.rank(condition)]`.
2.  **Multiplex `x` and `y`** - When both `x` and `y` are provided the result has the shape of `x`, `y`, and `condition` broadcast together. The result is taken from `x` where `condition` is non-zero or `y` where `condition` is zero.

#### 1\. Return the indices of non-zero elements

If `x` and `y` are not provided (both are None):

[`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)
 will return the indices of `condition` that are non-zero, in the form of a 2-D tensor with shape `[n, d]`, where `n` is the number of non-zero elements in `condition` (`tf.count_nonzero(condition)`), and `d` is the number of axes of `condition` ([`tf.rank(condition)`](https://www.tensorflow.org/api_docs/python/tf/rank)
).

Indices are output in row-major order. The `condition` can have a `dtype` of [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)
, or any numeric `dtype`.

Here `condition` is a 1-axis `bool` tensor with 2 `True` values. The result has a shape of `[2,1]`

    tf.where([True, False, False, True]).numpy()

Here `condition` is a 2-axis integer tensor, with 3 non-zero values. The result has a shape of `[3, 2]`.

    tf.where([[1, 0, 0], [1, 0, 1]]).numpy()

Here `condition` is a 3-axis float tensor, with 5 non-zero values. The output shape is `[5, 3]`.

    float_tensor = [[[0.1, 0], [0, 2.2], [3.5, 1e6]],\
\
These indices are the same that [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
 would use to represent the condition tensor:\
\
    sparse = tf.sparse.from_dense(float_tensor)\
\
A complex number is considered non-zero if either the real or imaginary component is non-zero:\
\
    tf.where([complex(0.), complex(1.), 0+1j, 1+1j]).numpy()\
\
#### 2\. Multiplex `x` and `y`\
\
If `x` and `y` are also provided (both have non-None values) the `condition` tensor acts as a mask that chooses whether the corresponding element / row in the output should be taken from `x` (if the element in `condition` is `True`) or `y` (if it is `False`).\
\
The shape of the result is formed by [broadcasting](https://docs.scipy.org/doc/numpy/reference/ufuncs.html)\
 together the shapes of `condition`, `x`, and `y`.\
\
When all three inputs have the same size, each is handled element-wise.\
\
    tf.where([True, False, False, True],\
\
There are two main rules for broadcasting:\
\
1.  If a tensor has fewer axes than the others, length-1 axes are added to the left of the shape.\
2.  Axes with length-1 are streched to match the coresponding axes of the other tensors.\
\
A length-1 vector is streched to match the other vectors:\
\
    tf.where([True, False, False, True], [1, 2, 3, 4], [100]).numpy()\
\
A scalar is expanded to match the other arguments:\
\
    tf.where([[True, False], [False, True]], [[1, 2], [3, 4]], 100).numpy()\
\
A scalar `condition` returns the complete `x` or `y` tensor, with broadcasting applied.\
\
    tf.where(True, [1, 2, 3, 4], 100).numpy()\
\
For a non-trivial example of broadcasting, here `condition` has a shape of `[3]`, `x` has a shape of `[3,3]`, and `y` has a shape of `[3,1]`. Broadcasting first expands the shape of `condition` to `[1,3]`. The final broadcast shape is `[3,3]`. `condition` will select columns from `x` and `y`. Since `y` only has one column, all columns from `y` will be identical.\
\
    tf.where([True, False, True],\
\
Note that if the gradient of either branch of the [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
 generates a `NaN`, then the gradient of the entire [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
 will be `NaN`. This is because the gradient calculation for [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
 combines the two branches, for performance reasons.\
\
A workaround is to use an inner [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
 to ensure the function has no asymptote, and to avoid computing a value whose gradient is `NaN` by replacing dangerous inputs with safe inputs.\
\
Instead of this,\
\
    x = tf.constant(0., dtype=tf.float32)\
\
Although, the `1. / x` values are never used, its gradient is a `NaN` when `x = 0`. Instead, we should guard that with another [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
\
    x = tf.constant(0., dtype=tf.float32)\
\
#### See also:\
\
*   [`tf.sparse`](https://www.tensorflow.org/api_docs/python/tf/sparse)\
     - The indices returned by the first form of [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
     can be useful in [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
     objects.\
*   [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd)\
    , [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)\
    , and related ops - Given the list of indices returned from [`tf.where`](https://www.tensorflow.org/api_docs/python/tf/where)\
     the `scatter` and `gather` family of ops can be used fetch values or insert values at those indices.\
*   [`tf.strings.length`](https://www.tensorflow.org/api_docs/python/tf/strings/length)\
     - [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)\
     is not an allowed dtype for the `condition`. Use the string length instead.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `condition` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of dtype bool, or any numeric dtype. `condition` must have dtype `bool` when `x` and `y` are provided. |\
| `x` | If provided, a Tensor which is of the same type as `y`, and has a shape broadcastable with `condition` and `y`. |\
| `y` | If provided, a Tensor which is of the same type as `x`, and has a shape broadcastable with `condition` and `x`. |\
| `name` | A name of the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| If `x` and `y` are provided: A `Tensor` with the same type as `x` and `y`, and shape that is broadcast from `condition`, `x`, and `y`. Otherwise, a `Tensor` with shape `[tf.math.count_nonzero(condition), tf.rank(condition)]`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | When exactly one of `x` or `y` is non-None, or the shapes are not all broadcastable. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.