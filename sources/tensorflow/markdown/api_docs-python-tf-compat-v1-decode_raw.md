[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fdecode_raw&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.decode\_raw Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L968-L1009)

Convert raw byte strings into tensors. (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.decode_raw`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw)

tf.compat.v1.decode_raw(
        input_bytes=None, out_type=None, little_endian=True, name=None, bytes=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_bytes` | Each element of the input Tensor is converted to an array of bytes. |
| `out_type` | `DType` of the output. Acceptable types are `half`, `float`, `double`, `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`. |
| `little_endian` | Whether the `input_bytes` data is in little-endian format. Data will be converted into host byte order if necessary. |
| `name` | A name for the operation (optional). |
| `bytes` | Deprecated parameter. Use `input_bytes` instead. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` object storing the decoded bytes. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.