[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/atan#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/atan)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/atan?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fatan&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/atan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/atan#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.atan Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/atan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/atan#returns)
    

Computes the trignometric inverse tangent of x element-wise.

#### View aliases

**Main aliases**

[`tf.atan`](https://www.tensorflow.org/api_docs/python/tf/math/atan)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.atan`](https://www.tensorflow.org/api_docs/python/tf/math/atan)

tf.math.atan(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

The [`tf.math.atan`](https://www.tensorflow.org/api_docs/python/tf/math/atan)
 operation returns the inverse of [`tf.math.tan`](https://www.tensorflow.org/api_docs/python/tf/math/tan)
, such that if `y = tf.math.tan(x)` then, `x = tf.math.atan(y)`.

#### For example:

# Note: [1.047, 0.785] ~= [(pi/3), (pi/4)]
    x = tf.constant([1.047, 0.785])
    y = tf.math.tan(x) # [1.731261, 0.99920404]
    
    tf.math.atan(y) # [1.047, 0.785] = x

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`.<br><br>If `x` is a `SparseTensor`, returns `SparseTensor(x.indices, tf.math.atan(x.values, ...), x.dense_shape)` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.