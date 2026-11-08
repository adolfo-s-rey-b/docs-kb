[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/truediv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/truediv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/truediv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Ftruediv&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/truediv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/truediv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/truediv#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.truediv Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/truediv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/truediv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/truediv#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1509-L1561)

Divides x / y elementwise (using Python 3 division operator semantics).

#### View aliases

**Main aliases**

[`tf.truediv`](https://www.tensorflow.org/api_docs/python/tf/math/truediv)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.truediv`](https://www.tensorflow.org/api_docs/python/tf/math/truediv)
, [`tf.compat.v1.truediv`](https://www.tensorflow.org/api_docs/python/tf/math/truediv)

tf.math.truediv(
        x, y, name=None
    )

This function forces Python 3 division operator semantics where all integer arguments are cast to floating types first. If you want integer division that rounds down, use `x // y` or `tf.math.floordiv`.

`x` and `y` must have the same numeric type. If the inputs are floating point, the output will have the same type. If the inputs are integral, the inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32` and `int64` (matching the behavior of Numpy).

#### Example:

    # Division with integer tensors (returns float)

    # Division with different shaped tensors (broadcasting)

Handling potential division by zero (returns inf)
=================================================

>>> x3 = tf.constant(5, dtype=tf.float32)
    >>> y3 = tf.constant(0, dtype=tf.float32)
    >>> result3 = tf.math.truediv(x3, y3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor` numerator of numeric type. |
| `y` | `Tensor` denominator of numeric type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| `x / y` evaluated in floating point. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `x` and `y` have different dtypes. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.