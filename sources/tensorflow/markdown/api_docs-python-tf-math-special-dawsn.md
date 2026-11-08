[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.special.dawsn Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/special/dawsn#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/special_math_ops.py#L101-L129)

Computes Dawson's integral of `x` element-wise.

tf.math.special.dawsn(
        x, name=None
    )

Dawson's integral is defined as `exp(-x**2)` times the integral of `exp(t**2)` from `0` to `x`, with the domain of definition all real numbers.

Dawson's function is odd.

>>> tf.math.special.dawsn([-1., -0.5, 0.5, 1.]).numpy()
    array([-0.5380795, -0.4244364, 0.4244364,  0.5380795], dtype=float32)

This implementation is based off of the Cephes math library.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `float32`, `float64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. |     |

scipy compatibility
-------------------

Equivalent to scipy.special.dawsn

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.