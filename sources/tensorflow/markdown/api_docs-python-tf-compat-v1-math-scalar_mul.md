[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.scalar\_mul Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/scalar_mul#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L620-L659)

Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

tf.compat.v1.math.scalar_mul(
        scalar, x, name=None
    )

This is a special case of [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
, where the first value must be a `scalar`. Unlike the general form of [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
, this is operation is guaranteed to be efficient for [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
.

    x = tf.reshape(tf.range(30, dtype=tf.float32), [10, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scalar` | A 0-D scalar `Tensor`. Must have known shape. |
| `x` | A `Tensor` or `IndexedSlices` to be scaled. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| `scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if scalar is not a 0-D `scalar`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.