[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/floordiv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.floordiv Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/floordiv?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1704-L1731)

Divides `x / y` elementwise, rounding toward the most negative integer.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.floordiv`](https://www.tensorflow.org/api_docs/python/tf/math/floordiv)
, [`tf.compat.v1.math.floordiv`](https://www.tensorflow.org/api_docs/python/tf/math/floordiv)

tf.math.floordiv(
        x, y, name=None
    )

Mathematically, this is equivalent to floor(x / y). For example: floor(8.4 / 4.0) = floor(2.1) = 2.0 floor(-8.4 / 4.0) = floor(-2.1) = -3.0 This is equivalent to the '//' operator in Python 3.0 and above.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor` numerator of real numeric type. |
| `y` | `Tensor` denominator of real numeric type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| `x / y` rounded toward -infinity. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the inputs are complex. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-01 UTC.