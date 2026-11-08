[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.floor\_div Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/floor_div?version=stable#returns_1)
    

See Stable See Nightly

Returns x // y element-wise.

tf.compat.v1.floor_div(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`. |
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

Last updated 2026-11-01 UTC.