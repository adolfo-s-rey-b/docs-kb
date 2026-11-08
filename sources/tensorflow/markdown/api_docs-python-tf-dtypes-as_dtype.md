[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dtypes.as\_dtype Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/dtypes.py#L885-L945)

Converts the given `type_value` to a [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
.

#### View aliases

**Main aliases**

[`tf.as_dtype`](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.as_dtype`](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)
, [`tf.compat.v1.dtypes.as_dtype`](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)

tf.dtypes.as_dtype(
        type_value
    )

Inputs can be existing [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
 objects, a [`DataType` enum](https://www.tensorflow.org/code/tensorflow/core/framework/types.proto)
, a string type name, or a [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html)
.

#### Examples:

    tf.as_dtype(2)  # Enum value for float64.

    tf.as_dtype('float')

    tf.as_dtype(np.int32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `type_value` | A value that can be converted to a [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> object. |

|     |
| --- |
| Returns<br>------- |     |
| A `DType` corresponding to `type_value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `type_value` cannot be converted to a `DType`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.