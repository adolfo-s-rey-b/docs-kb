[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/clip_by_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/clip_by_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.clip\_by\_value Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_value#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/clip_ops.py#L34-L125)

Clips tensor values to a specified min and max.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.clip_by_value`](https://www.tensorflow.org/api_docs/python/tf/clip_by_value)

tf.clip_by_value(
        t, clip_value_min, clip_value_max, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core) | *   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

Given a tensor `t`, this operation returns a tensor of the same type and shape as `t` with its values clipped to `clip_value_min` and `clip_value_max`. Any values less than `clip_value_min` are set to `clip_value_min`. Any values greater than `clip_value_max` are set to `clip_value_max`.

#### For example:

Basic usage passes a scalar as the min and max value.

    t = tf.constant([[-10., -1., 0.], [0., 2., 10.]])

The min and max can be the same size as `t`, or broadcastable to that size.

    t = tf.constant([[-1, 0., 10.], [-1, 0, 10]])

Broadcasting fails, intentionally, if you would expand the dimensions of `t`

    t = tf.constant([[-1, 0., 10.], [-1, 0, 10]])

It throws a `TypeError` if you try to clip an `int` to a `float` value ([`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
 the input to `float` first).

    t = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t` | A `Tensor` or `IndexedSlices`. |
| `clip_value_min` | The minimum value to clip to. A scalar `Tensor` or one that is broadcastable to the shape of `t`. |
| `clip_value_max` | The maximum value to clip to. A scalar `Tensor` or one that is broadcastable to the shape of `t`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A clipped `Tensor` or `IndexedSlices`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)<br>: If the clip tensors would trigger array broadcasting that would make the returned tensor larger than the input. |     |
| `TypeError` | If dtype of the input is `int32` and dtype of the `clip_value_min` or `clip_value_max` is `float32` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.