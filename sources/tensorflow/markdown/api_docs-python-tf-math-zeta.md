[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/zeta#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/zeta)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/zeta?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fzeta&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/zeta#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/zeta#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.zeta Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/zeta#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/zeta#returns)
    

Compute the Hurwitz zeta function ζ(x,q).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.zeta`](https://www.tensorflow.org/api_docs/python/tf/math/zeta)
, [`tf.compat.v1.zeta`](https://www.tensorflow.org/api_docs/python/tf/math/zeta)

tf.math.zeta(
        x: Annotated[Any, tf.raw_ops.Any],
        q: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

The Hurwitz zeta function is defined as:

ζ(x,q)\=∑∞n\=0(q+n)−x

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `q` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.