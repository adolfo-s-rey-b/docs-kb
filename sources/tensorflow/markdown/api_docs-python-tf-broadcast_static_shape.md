[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fbroadcast_static_shape&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.broadcast\_static\_shape Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L562-L595)

Computes the shape of a broadcast given known shapes.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.broadcast_static_shape`](https://www.tensorflow.org/api_docs/python/tf/broadcast_static_shape)

tf.broadcast_static_shape(
        shape_x, shape_y
    )

When `shape_x` and `shape_y` are fully known `TensorShape`s this computes a `TensorShape` which is the shape of the result of a broadcasting op applied in tensors of shapes `shape_x` and `shape_y`.

For example, if shape\_x is `TensorShape([1, 2, 3])` and shape\_y is `TensorShape([5, 1, 3])`, the result is a TensorShape whose value is `TensorShape([5, 2, 3])`.

This is useful when validating the result of a broadcasting operation when the tensors have statically known shapes.

#### Example:

    shape_x = tf.TensorShape([1, 2, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape_x` | A `TensorShape` |
| `shape_y` | A `TensorShape` |

|     |
| --- |
| Returns<br>------- |     |
| A `TensorShape` representing the broadcasted shape. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the two shapes can not be broadcasted. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.