[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/conj#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/conj)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/conj?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/conj#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/conj#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/conj#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/conj#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.conj Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/conj#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/conj#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/conj#raises)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/conj#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4430-L4486)

Returns the complex conjugate of a complex number.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.conj`](https://www.tensorflow.org/api_docs/python/tf/math/conj)

tf.math.conj(
        x, name=None
    )

Given a tensor `x` of complex numbers, this operation returns a tensor of complex numbers that are the complex conjugate of each element in `x`. The complex numbers in `x` must be of the form a+bj, where `a` is the real part and `b` is the imaginary part.

The complex conjugate returned by this operation is of the form a−bj.

#### For example:

    x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])

If `x` is real, it is returned unchanged.

#### For example:

    x = tf.constant([-2.25, 3.25])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor` to conjugate. Must have numeric or variant type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` that is the conjugate of `x` (with the same type). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `x` is not a numeric tensor. |

numpy compatibility
-------------------

Equivalent to numpy.conj.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.