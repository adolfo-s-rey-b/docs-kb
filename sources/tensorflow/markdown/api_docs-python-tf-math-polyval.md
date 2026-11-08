[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/polyval#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/polyval)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/polyval?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fpolyval&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/polyval#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/polyval#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/polyval#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.polyval Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/polyval#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/polyval#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/polyval#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5461-L5530)

Computes the elementwise value of a polynomial.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.polyval`](https://www.tensorflow.org/api_docs/python/tf/math/polyval)

tf.math.polyval(
        coeffs, x, name=None
    )

If `x` is a tensor and `coeffs` is a list n + 1 tensors, this function returns the value of the n-th order polynomial

`p(x) = coeffs[n-1] + coeffs[n-2] * x + ... + coeffs[0] * x**(n-1)`

evaluated using Horner's method, i.e.

p(x) = coeffs[n-1] + x * (coeffs[n-2] + ... + x * (coeffs[1] + x * coeffs[0]))

#### Usage Example:

    coefficients = [1.0, 2.5, -4.2]

#### Usage Example:

    tf.math.polyval([2, 1, 0], 3) # evaluates 2 * (3**2) + 1 * (3**1) + 0 * (3**0)

[`tf.math.polyval`](https://www.tensorflow.org/api_docs/python/tf/math/polyval)
 can also be used in polynomial regression. Taking advantage of this function can facilitate writing a polynomial equation as compared to explicitly writing it out, especially for higher degree polynomials.

    x = tf.constant(3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `coeffs` | A list of `Tensor` representing the coefficients of the polynomial. |
| `x` | A `Tensor` representing the variable of the polynomial. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `tensor` of the shape as the expression p(x) with usual broadcasting rules for element-wise addition and multiplication applied. |     |

numpy compatibility
-------------------

Equivalent to numpy.polyval.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.