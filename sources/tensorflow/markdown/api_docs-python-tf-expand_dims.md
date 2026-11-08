[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/expand_dims#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/expand_dims)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/expand_dims?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/expand_dims#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/expand_dims#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/expand_dims#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.expand\_dims Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/expand_dims#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/expand_dims#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/expand_dims#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L392-L459)

Returns a tensor with a length 1 axis inserted at index `axis`.

tf.expand_dims(
        input, axis, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding)<br>    <br>*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns) | *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic)<br>    <br>*   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)<br>    <br>*   [Generate music with an RNN](https://www.tensorflow.org/tutorials/audio/music_generation)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream) |

Given a tensor `input`, this operation inserts a dimension of length 1 at the dimension index `axis` of `input`'s shape. The dimension index follows Python indexing rules: It's zero-based, and a negative index is counted backward from the end.

This operation is useful to:

*   Add an outer "batch" dimension to a single element.
*   Align axes for broadcasting.
*   To add an inner vector length axis to a tensor of scalars.

#### For example:

If you have a single image of shape `[height, width, channels]`:

    image = tf.zeros([10,10,3])

You can add an outer `batch` axis by passing `axis=0`:

    tf.expand_dims(image, axis=0).shape.as_list()

The new axis location matches Python `list.insert(axis, 1)`:

    tf.expand_dims(image, axis=1).shape.as_list()

Following standard Python indexing rules, a negative `axis` counts from the end so `axis=-1` adds an inner most dimension:

    tf.expand_dims(image, -1).shape.as_list()

This operation requires that `axis` is a valid index for `input.shape`, following Python indexing rules:

-1-tf.rank(input) <= axis <= tf.rank(input)

This operation is related to:

*   [`tf.squeeze`](https://www.tensorflow.org/api_docs/python/tf/squeeze)
    , which removes dimensions of size 1.
*   [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)
    , which provides more flexible reshaping capability.
*   [`tf.sparse.expand_dims`](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims)
    , which provides this functionality for [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `axis` | Integer specifying the dimension index at which to expand the shape of `input`. Given an input of D dimensions, `axis` must be in range `[-(D+1), D]` (inclusive). |
| `name` | Optional string. The name of the output `Tensor`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same data as `input`, with an additional dimension inserted at the index specified by `axis`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `axis` is not specified. |
| `InvalidArgumentError` | If `axis` is out of range `[-(D+1), D]`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.