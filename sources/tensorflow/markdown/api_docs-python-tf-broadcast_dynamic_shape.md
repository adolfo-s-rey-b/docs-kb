[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fbroadcast_dynamic_shape&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.broadcast\_dynamic\_shape Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L528-L559)

Computes the shape of a broadcast given symbolic shapes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.broadcast_dynamic_shape`](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape)

tf.broadcast_dynamic_shape(
        shape_x, shape_y
    )

When `shape_x` and `shape_y` are Tensors representing shapes (i.e. the result of calling tf.shape on another Tensor) this computes a Tensor which is the shape of the result of a broadcasting op applied in tensors of shapes `shape_x` and `shape_y`.

This is useful when validating the result of a broadcasting operation when the tensors do not have statically known shapes.

#### Example:

    shape_x = (1, 2, 3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape_x` | A rank 1 integer `Tensor`, representing the shape of x. |
| `shape_y` | A rank 1 integer `Tensor`, representing the shape of y. |

|     |
| --- |
| Returns<br>------- |     |
| A rank 1 integer `Tensor` representing the broadcasted shape. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | If the two shapes are incompatible for broadcasting. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.