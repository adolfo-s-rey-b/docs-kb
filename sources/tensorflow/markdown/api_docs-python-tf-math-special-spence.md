[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/special/spence)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/special/spence?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.special.spence Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/special/spence#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/special_math_ops.py#L223-L250)

Computes Spence's integral of `x` element-wise.

tf.math.special.spence(
        x, name=None
    )

Spence's integral is defined as the integral of `log(t) / (1 - t)` from `1` to `x`, with the domain of definition all non-negative real numbers.

    tf.math.special.spence([0.5, 1., 2., 3.]).numpy()

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

Equivalent to scipy.special.spence

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.