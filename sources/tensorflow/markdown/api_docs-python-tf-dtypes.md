[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dtypes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dtypes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dtypes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdtypes&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/dtypes#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/dtypes#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/dtypes#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/dtypes#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.dtypes Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/dtypes#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/dtypes#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/dtypes#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/dtypes#other-members)
    

Public API for tf.\_api.v2.dtypes namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/dtypes/experimental)
 module: Public API for tf.\_api.v2.dtypes.experimental namespace

Classes
-------

[`class DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
: Represents the type of the elements in a `Tensor`.

Functions
---------

[`as_dtype(...)`](https://www.tensorflow.org/api_docs/python/tf/dtypes/as_dtype)
: Converts the given `type_value` to a [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
.

[`cast(...)`](https://www.tensorflow.org/api_docs/python/tf/cast)
: Casts a tensor to a new type.

[`complex(...)`](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex)
: Converts two real numbers to a complex number.

[`saturate_cast(...)`](https://www.tensorflow.org/api_docs/python/tf/dtypes/saturate_cast)
: Performs a safe saturating cast of `value` to `dtype`.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| QUANTIZED\_DTYPES | {<br>     tf.qint16,<br>     tf.qint16_ref,<br>     tf.qint32,<br>     tf.qint32_ref,<br>     tf.qint8,<br>     tf.qint8_ref,<br>     tf.quint16,<br>     tf.quint16_ref,<br>     tf.quint8,<br>     tf.quint8_ref<br>    } |
| bfloat16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>16-bit bfloat (brain floating point). |
| bool | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Boolean. |
| complex128 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>128-bit complex. |
| complex64 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>64-bit complex. |
| double | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>64-bit (double precision) floating-point. |
| float16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>16-bit (half precision) floating-point. |
| float32 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>32-bit (single precision) floating-point. |
| float64 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>64-bit (double precision) floating-point. |
| half | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>16-bit (half precision) floating-point. |
| int16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 16-bit integer. |
| int32 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 32-bit integer. |
| int64 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 64-bit integer. |
| int8 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 8-bit integer. |
| qint16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed quantized 16-bit integer. |
| qint32 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>signed quantized 32-bit integer. |
| qint8 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed quantized 8-bit integer. |
| quint16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned quantized 16-bit integer. |
| quint8 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned quantized 8-bit integer. |
| resource | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Handle to a mutable, dynamically allocated resource. |
| string | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Variable-length string, represented as byte array. |
| uint16 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 16-bit (word) integer. |
| uint32 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 32-bit (dword) integer. |
| uint64 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 64-bit (qword) integer. |
| uint8 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 8-bit (byte) integer. |
| variant | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Data of arbitrary type (known at runtime). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.