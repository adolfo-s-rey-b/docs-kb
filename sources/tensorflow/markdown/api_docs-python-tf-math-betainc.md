Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/betainc#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/betainc)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/betainc?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fbetainc&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/betainc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/betainc#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.betainc Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/betainc#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/betainc#returns)
    

Compute the regularized incomplete beta integral Ix(a,b).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.betainc`](https://www.tensorflow.org/api_docs/python/tf/math/betainc)
, [`tf.compat.v1.math.betainc`](https://www.tensorflow.org/api_docs/python/tf/math/betainc)

tf.math.betainc(
        a: Annotated[Any, tf.raw_ops.Any],
        b: Annotated[Any, tf.raw_ops.Any],
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

The regularized incomplete beta integral is defined as:

Ix(a,b)\=B(x;a,b)B(a,b)

where

B(x;a,b)\=∫x0ta−1(1−t)b−1dt

is the incomplete beta function and B(a,b) is the _complete_ beta function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `b` | A `Tensor`. Must have the same type as `a`. |
| `x` | A `Tensor`. Must have the same type as `a`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `a`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.