[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/angle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/angle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/angle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fangle&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/angle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/angle#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.angle Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/angle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/angle#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L897-L936)

Returns the element-wise argument of a complex (or real) tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.angle`](https://www.tensorflow.org/api_docs/python/tf/math/angle)

tf.math.angle(
        input, name=None
    )

Given a tensor `input`, this operation returns a tensor of type `float` that is the argument of each element in `input` considered as a complex number.

The elements in `input` are considered to be complex numbers of the form a+bj, where _a_ is the real part and _b_ is the imaginary part. If `input` is real then _b_ is zero by definition.

The argument returned by this function is of the form atan2(b,a). If `input` is real, a tensor of all zeros is returned.

#### For example:

input = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j], dtype=tf.complex64)
    tf.math.angle(input).numpy()
    # ==> array([2.0131705, 1.056345 ], dtype=float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float`, `double`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float32` or `float64`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.