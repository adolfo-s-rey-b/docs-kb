[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/divide#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/divide)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/divide?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/divide#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/divide#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.divide Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/divide#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/divide#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L470-L502)

Computes Python style division of `x` by `y`.

#### View aliases

**Main aliases**

[`tf.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.divide`](https://www.tensorflow.org/api_docs/python/tf/math/divide)

tf.math.divide(
        x, y, name=None
    )

#### For example:

    x = tf.constant([16, 12, 11])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` |
| `y` | A `Tensor` |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with same shape as input |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.