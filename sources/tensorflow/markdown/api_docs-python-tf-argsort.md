[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/argsort#main-content)

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
    

tf.argsort Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sort_ops.py#L86-L150)

Returns the indices of a tensor that give its sorted order along an axis.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.argsort`](https://www.tensorflow.org/api_docs/python/tf/argsort)

tf.argsort(
        values, axis=-1, direction='ASCENDING', stable=False, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet)<br>    <br>*   [Image Classification with TensorFlow Hub](https://www.tensorflow.org/hub/tutorials/image_classification) |

    values = [1, 10, 26.9, 2.8, 166.32, 62.3]

#### For a 1D tensor:

    sorted = tf.gather(values, sort_order)

For higher dimensions, the output has the same shape as `values`, but along the given axis, values represent the index of the sorted element in that slice of the tensor at the given position.

    mat = [[30,20,10],\
\
If `axis=-1` these indices can be used to apply a sort using `tf.gather`:\
\
    tf.gather(mat, indices, batch_dims=-1).numpy()\
\
|     |\
| --- |\
| See also<br>-------- |     |\
| *   [`tf.sort`](https://www.tensorflow.org/api_docs/python/tf/sort)<br>    : Sort along an axis.<br>*   [`tf.math.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)<br>    : A partial sort that returns a fixed number of top values and corresponding indices. |     |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `values` | 1-D or higher **numeric** `Tensor`. |\
| `axis` | The axis along which to sort. The default is -1, which sorts the last axis. |\
| `direction` | The direction in which to sort the values (`'ASCENDING'` or `'DESCENDING'`). |\
| `stable` | If True, equal elements in the original tensor will not be re-ordered in the returned order. Unstable sort is not yet implemented, but will eventually be the default for performance reasons. If you require a stable order, pass `stable=True` for forwards compatibility. |\
| `name` | Optional name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| An int32 `Tensor` with the same shape as `values`. The indices that would sort each slice of the given `values` along the given `axis`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If axis is not a constant scalar, or the direction is invalid. |\
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError) | If the `values.dtype` is not a `float` or `int` type. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.