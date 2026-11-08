[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/nextafter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/nextafter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#returns)
    
*   [cpp compatibility](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#cpp-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.nextafter Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#returns)
    
*   [cpp compatibility](https://www.tensorflow.org/api_docs/python/tf/math/nextafter#cpp-compatibility)
    

Returns the next representable value of `x1` in the direction of `x2`, element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.nextafter`](https://www.tensorflow.org/api_docs/python/tf/math/nextafter)

tf.math.nextafter(
        x1: Annotated[Any, tf.raw_ops.Any],
        x2: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

This operation returns the same result as the C++ std::nextafter function.

It can also return a subnormal number.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | A `Tensor`. Must be one of the following types: `float64`, `float32`. |
| `x2` | A `Tensor`. Must have the same type as `x1`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x1`. |     |

cpp compatibility
-----------------

Equivalent to C++ std::nextafter function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.