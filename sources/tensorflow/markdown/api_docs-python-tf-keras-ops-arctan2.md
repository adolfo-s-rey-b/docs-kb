[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.arctan2 Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L963-L1004)

Element-wise arc tangent of `x1/x2` choosing the quadrant correctly.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.arctan2`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arctan2)

tf.keras.ops.arctan2(
        x1, x2
    )

The quadrant (i.e., branch) is chosen so that `arctan2(x1, x2)` is the signed angle in radians between the ray ending at the origin and passing through the point `(1, 0)`, and the ray ending at the origin and passing through the point `(x2, x1)`. (Note the role reversal: the "y-coordinate" is the first function parameter, the "x-coordinate" is the second.) By IEEE convention, this function is defined for `x2 = +/-0` and for either or both of `x1` and `x2` `= +/-inf`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First input tensor. |
| `x2` | Second input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor of angles in radians, in the range `[-pi, pi]`. |     |

#### Examples:

Consider four points in different quadrants:

>>> x = keras.ops.convert_to_tensor([-1, +1, +1, -1])
    >>> y = keras.ops.convert_to_tensor([-1, -1, +1, +1])
    >>> keras.ops.arctan2(y, x) * 180 / numpy.pi
    array([-135., -45., 45., 135.], dtype=float32)

Note the order of the parameters. `arctan2` is defined also when x2=0 and at several other points, obtaining values in the range `[-pi, pi]`:

>>> keras.ops.arctan2(
    ...     keras.ops.array([1., -1.]),
    ...     keras.ops.array([0., 0.]),
    ... )
    array([ 1.5707964, -1.5707964], dtype=float32)
    >>> keras.ops.arctan2(
    ...     keras.ops.array([0., 0., numpy.inf]),
    ...     keras.ops.array([+0., -0., numpy.inf]),
    ... )
    array([0., 3.1415925, 0.7853982], dtype=float32)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.