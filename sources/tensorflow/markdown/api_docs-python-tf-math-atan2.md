Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/atan2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/atan2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/atan2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fatan2&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/atan2#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/atan2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/atan2#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.atan2 Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/atan2#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/atan2#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/atan2#returns)
    

Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

#### View aliases

**Main aliases**

[`tf.atan2`](https://www.tensorflow.org/api_docs/python/tf/math/atan2)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.atan2`](https://www.tensorflow.org/api_docs/python/tf/math/atan2)
, [`tf.compat.v1.math.atan2`](https://www.tensorflow.org/api_docs/python/tf/math/atan2)

tf.math.atan2(
        y: Annotated[Any, tf.raw_ops.Any],
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

This is the angle θ∈\[−π,π\] such that x\=rcos(θ) and y\=rsin(θ) where r\=√x2+y2.

#### For example:

    x = [1., 1.]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `x` | A `Tensor`. Must have the same type as `y`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `y`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.