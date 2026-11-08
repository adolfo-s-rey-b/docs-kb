[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/concat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/concat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/concat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/concat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/concat#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.concat Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/concat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/concat#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1350-L1442)

Concatenates tensors along one dimension.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.concat`](https://www.tensorflow.org/api_docs/python/tf/concat)

tf.concat(
        values, axis, name='concat'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core)<br>    <br>*   [Customizing what happens in \`fit()\` with TensorFlow](https://www.tensorflow.org/guide/keras/custom_train_step_in_tensorflow) | *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Transfer learning for video classification with MoViNet](https://www.tensorflow.org/tutorials/video/transfer_learning_with_movinet)<br>    <br>*   [Video classification with a 3D convolutional neural network](https://www.tensorflow.org/tutorials/video/video_classification) |

See also [`tf.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)
, [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack)
, [`tf.repeat`](https://www.tensorflow.org/api_docs/python/tf/repeat)
.

Concatenates the list of tensors `values` along dimension `axis`. If `values[i].shape = [D0, D1, ... Daxis(i), ...Dn]`, the concatenated result has shape

[D0, D1, ... Raxis, ...Dn]

where

Raxis = sum(Daxis(i))

That is, the data from the input tensors is joined along the `axis` dimension.

The number of dimensions of the input tensors must match, and all dimensions except the `axis` must be equal.

#### For example:

    t1 = [[1, 2, 3], [4, 5, 6]]

    tf.concat([t1, t2], 1)

As in Python, the `axis` could also be negative numbers. Negative `axis` are interpreted as counting from the end of the rank, i.e., `axis + rank(values)`\-th dimension.

#### For example:

    t1 = [[[1, 2], [2, 3]], [[4, 4], [5, 3]]]

tf.concat([tf.expand_dims(t, axis) for t in tensors], axis)

can be rewritten as

tf.stack(tensors, axis=axis)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A list of `Tensor` objects or a single `Tensor`. |
| `axis` | 0-D `int32` `Tensor`. Dimension along which to concatenate. Must be in the range `[-rank(values), rank(values))`. As in Python, indexing for axis is 0-based. Positive axis in the rage of `[0, rank(values))` refers to `axis`\-th dimension. And negative axis refers to `axis + rank(values)`\-th dimension. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` resulting from concatenation of the input tensors. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.