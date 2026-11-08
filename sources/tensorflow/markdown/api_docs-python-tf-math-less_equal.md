[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/less_equal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/less_equal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/less_equal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/less_equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/less_equal#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.less\_equal Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/less_equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/less_equal#returns)
    

Returns the truth value of (x <= y) element-wise.

#### View aliases

**Main aliases**

[`tf.less_equal`](https://www.tensorflow.org/api_docs/python/tf/math/less_equal)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.less_equal`](https://www.tensorflow.org/api_docs/python/tf/math/less_equal)
, [`tf.compat.v1.math.less_equal`](https://www.tensorflow.org/api_docs/python/tf/math/less_equal)

tf.math.less_equal(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

#### Example:

x = tf.constant([5, 4, 6])
    y = tf.constant([5])
    tf.math.less_equal(x, y) ==> [True, True, False]
    
    x = tf.constant([5, 4, 6])
    y = tf.constant([5, 6, 6])
    tf.math.less_equal(x, y) ==> [True, True, True]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.