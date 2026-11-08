[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fshape&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/shape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/shape#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.shape Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/shape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/shape#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L598-L656)

Returns a tensor containing the shape of the input tensor.

tf.shape(
        input, out_type=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Customizing what happens in \`fit()\` with TensorFlow](https://www.tensorflow.org/guide/keras/custom_train_step_in_tensorflow)<br>    <br>*   [Customizing what happens in \`fit()\`](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic) |

See also [`tf.size`](https://www.tensorflow.org/api_docs/python/tf/size)
, [`tf.rank`](https://www.tensorflow.org/api_docs/python/tf/rank)
.

[`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape)
 returns a 1-D integer tensor representing the shape of `input`. For a scalar input, the tensor returned has a shape of (0,) and its value is the empty vector (i.e. \[\]).

#### For example:

    tf.shape(1.)

    t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])

    a = tf.keras.layers.Input((None, 10))

In these cases, using [`tf.Tensor.shape`](https://www.tensorflow.org/api_docs/python/tf/Tensor#shape)
 will return more informative results.

    a.shape

(The first `None` represents the as yet unknown batch size.)

[`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape)
 and [`Tensor.shape`](https://www.tensorflow.org/api_docs/python/tf/Tensor#shape)
 should be identical in eager mode. Within [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 or within a [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 context, not all dimensions may be known until execution time. Hence, when defining custom layers and models for graph mode, prefer the dynamic [`tf.shape(x)`](https://www.tensorflow.org/api_docs/python/tf/shape)
 over the static `x.shape`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` or `SparseTensor`. |
| `out_type` | (Optional) The specified output type of the operation (`int32` or `int64`). Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. (Note: there is an experimental flag, `tf_shape_default_int64` that changes the default to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. This is an unsupported, experimental setting that causes known breakages.) |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `out_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.