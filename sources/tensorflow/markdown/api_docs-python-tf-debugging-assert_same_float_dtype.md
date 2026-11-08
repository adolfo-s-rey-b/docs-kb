[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_same\_float\_dtype Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L2126-L2158)

Validate and return float type based on `tensors` and `dtype`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.assert_same_float_dtype`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype)
, [`tf.compat.v1.debugging.assert_same_float_dtype`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype)

tf.debugging.assert_same_float_dtype(
        tensors=None, dtype=None
    )

For ops such as matrix multiplication, inputs and weights must be of the same float type. This function validates that all `tensors` are the same type, validates that type is `dtype` (if supplied), and returns the type. Type must be a floating point type. If neither `tensors` nor `dtype` is supplied, the function will return [`dtypes.float32`](https://www.tensorflow.org/api_docs/python/tf/dtypes#float32)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors` | Tensors of input values. Can include `None` elements, which will be ignored. |
| `dtype` | Expected type. |

|     |
| --- |
| Returns<br>------- |     |
| Validated type. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if neither `tensors` nor `dtype` is supplied, or result is not float, or the common type of the inputs is not a floating point type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.