[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/dtypes/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/dtypes/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/dtypes/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/dtypes/experimental#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.dtypes.experimental Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/dtypes/experimental#other-members)
    

Public API for tf.\_api.v2.dtypes.experimental namespace

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| float4\_e2m1fn | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>4-bit float with 2 exponent bits and 1 mantissa bits, with extended finite range. This type has no representation for both inf and NaN. |
| float8\_e4m3b11fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range and 11 bits of bias. This type has no representation for inf, and only one NaN value: 0x80. |
| float8\_e4m3fn | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range. This type has no representation for inf, and only two NaN values: 0xFF for negative NaN, and 0x7F for positive NaN. |
| float8\_e4m3fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 4 exponent bits and 3 mantissa bits, with extended finite range. This type has no representation for inf, and only one NaN value: 0x80. |
| float8\_e5m2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 5 exponent bits and 2 mantissa bits. |
| float8\_e5m2fnuz | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>8-bit float with 5 exponent bits and 2 mantissa bits, with extended finite range. This type has no representation for inf, and only one NaN value: 0x80. |
| int2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 2-bit integer. |
| int4 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Signed 4-bit integer. |
| uint2 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 2-bit integer. |
| uint4 | Instance of [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br><br>Unsigned 4-bit integer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.