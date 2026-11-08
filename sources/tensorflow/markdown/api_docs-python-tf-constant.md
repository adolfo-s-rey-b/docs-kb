[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/constant)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/constant?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconstant%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.constant Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/constant?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/constant_op.py#L177-L277)

Creates a constant tensor from a tensor-like object.

tf.constant(
        value, dtype=None, shape=None, name='Const'
    ) -> Union[tf.Operation, ops._EagerTensorBase]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [TF-NumPy Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs)<br>    <br>*   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl) |

If the argument `dtype` is not specified, then the type is inferred from the type of `value`.

    # Constant 1-D Tensor from a python list.

If `dtype` is specified, the resulting tensor values are cast to the requested `dtype`.

    tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.float64)

If `shape` is set, the `value` is reshaped to match. Scalars are expanded to fill the `shape`:

    tf.constant(0, shape=(2, 3))

[`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
 has no effect if an eager Tensor is passed as the `value`, it even transmits gradients:

    v = tf.Variable([0.0])

But, since [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
 embeds the value in the [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
 this fails for symbolic tensors:

    with tf.compat.v1.Graph().as_default():

[`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
 will create tensors on the current device. Inputs which are already tensors maintain their placements unchanged.

#### Related Ops:

*   [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
     is similar but:
    
    *   It has no `shape` argument.
    *   Symbolic tensors are allowed to pass through.
    
    with tf.compat.v1.Graph().as_default():
      
*   [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
    : differs in a few ways:
    
    *   [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)
         supports arbitrary constants, not just uniform scalar Tensors like [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
        .
    *   [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
         creates an Op in the graph that is expanded at runtime, so it can efficiently represent large tensors.
    *   Since [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
         does not embed the value, it can produce dynamically sized outputs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A constant value (or list) of output type `dtype`. |
| `dtype` | Optional type of the elements of the resulting tensor. |
| `shape` | Optional dimensions of resulting tensor. |
| `name` | Optional name for the tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A Constant Tensor. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if shape is incorrectly specified or unsupported. |
| `ValueError` | if called on a symbolic tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.