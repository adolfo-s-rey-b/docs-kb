[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/floormod#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/floormod)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/floormod?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/floormod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/floormod#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.floormod Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/floormod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/floormod#returns)
    

Returns element-wise remainder of division.

#### View aliases

**Main aliases**

[`tf.math.mod`](https://www.tensorflow.org/api_docs/python/tf/math/floormod)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.floormod`](https://www.tensorflow.org/api_docs/python/tf/math/floormod)
, [`tf.compat.v1.mod`](https://www.tensorflow.org/api_docs/python/tf/math/floormod)

tf.math.floormod(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

This follows Python semantics in that the result here is consistent with a flooring divide. E.g. `floor(x / y) * y + floormod(x, y) = x`, regardless of the signs of x and y.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `bfloat16`, `half`, `float32`, `float64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
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