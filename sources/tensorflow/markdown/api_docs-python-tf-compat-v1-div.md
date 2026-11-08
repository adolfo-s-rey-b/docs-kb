[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.div Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/div#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1564-L1593)

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

tf.compat.v1.div(
        x, y, name=None
    )

Migrate to TF2
--------------

This function is deprecated in TF2. Prefer using the Tensor division operator, [`tf.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)
, or [`tf.math.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)
, which obey the Python 3 division operator semantics.

Description
-----------

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x` and `y` are both integers then the result will be an integer. This is in contrast to Python 3, where division with `/` is always a float while division with `//` is always an integer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor` numerator of real numeric type. |
| `y` | `Tensor` denominator of real numeric type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| `x / y` returns the quotient of x and y. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.