[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/squeeze#main-content)

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
    

tf.squeeze Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4288-L4361)

Removes dimensions of size 1 from the shape of a tensor.

tf.squeeze(
        input, axis=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) | *   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Generate music with an RNN](https://www.tensorflow.org/tutorials/audio/music_generation)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio) |

Given a tensor `input`, this operation returns a tensor of the same type with all dimensions of size 1 removed. If you don't want to remove all size 1 dimensions, you can remove specific size 1 dimensions by specifying `axis`.

#### For example:

# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
    tf.shape(tf.squeeze(t))  # [2, 3]

Or, to remove specific size 1 dimensions:

# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
    tf.shape(tf.squeeze(t, [2, 4]))  # [1, 2, 3, 1]

Unlike the older op [`tf.compat.v1.squeeze`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/squeeze)
, this op does not accept a deprecated `squeeze_dims` argument.

@tf.function
    def func(x):
      print('x.shape:', x.shape)
      known_axes = [i for i, size in enumerate(x.shape) if size == 1]
      y = tf.squeeze(x, axis=known_axes)
      print('shape of tf.squeeze(x, axis=known_axes):', y.shape)
      y = tf.squeeze(x)
      print('shape of tf.squeeze(x):', y.shape)
      return 0
    
    _ = func.get_concrete_function(tf.TensorSpec([None, 1, 2], dtype=tf.int32))
    # Output is.
    # x.shape: (None, 1, 2)
    # shape of tf.squeeze(x, axis=known_axes): (None, 2)
    # shape of tf.squeeze(x): <unknown>

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. The `input` to squeeze. |
| `axis` | An optional list of `ints`. Defaults to `[]`. If specified, only squeezes the dimensions listed. The dimension index starts at 0. It is an error to squeeze a dimension that is not 1. Must be in the range `[-rank(input), rank(input))`. Must be specified if `input` is a `RaggedTensor`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `input`. Contains the same data as `input`, but has one or more dimensions of size 1 removed. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | The input cannot be converted to a tensor, or the specified axis cannot be squeezed. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.