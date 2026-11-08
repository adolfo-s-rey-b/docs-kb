[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reciprocal_no_nan#main-content)

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
    

tf.math.reciprocal\_no\_nan Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5533-L5564)

Performs a safe reciprocal operation, element wise.

tf.math.reciprocal_no_nan(
        x, name=None
    )

If a particular element is zero, the reciprocal for that element is also set to zero.

#### For example:

x = tf.constant([2.0, 0.5, 0, 1], dtype=tf.float32)
    tf.math.reciprocal_no_nan(x)  # [ 0.5, 2, 0.0, 1.0 ]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` of type `float16`, `float32`, `float64` `complex64` or `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of same shape and type as `x`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | x must be of a valid dtype. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.