[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_raw Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_raw#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L840-L965)

Convert raw bytes from input tensor into numeric tensors.

tf.io.decode_raw(
        input_bytes, out_type, little_endian=True, fixed_length=None, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor) |

Every component of the input tensor is interpreted as a sequence of bytes. These bytes are then decoded as numbers in the format specified by `out_type`.

    tf.io.decode_raw(tf.constant("1"), tf.uint8)

Note that the rank of the output tensor is always one more than the input one:

    tf.io.decode_raw(tf.constant(["1","2"]), tf.uint8).shape

This is because each byte in the input is converted to a new value on the output (if output type is `uint8` or `int8`, otherwise chunks of inputs get converted to a new value):

    tf.io.decode_raw(tf.constant("123"), tf.uint8)

The operation allows specifying endianness via the `little_endian` parameter.

    tf.io.decode_raw(tf.constant("\x0a\x0b"), tf.int16)

If the elements of `input_bytes` are of different length, you must specify `fixed_length`:

    tf.io.decode_raw(tf.constant([["1"],["23"]]), tf.uint8, fixed_length=4)

If the `fixed_length` value is larger that the length of the `out_type` dtype, multiple values are generated:

    tf.io.decode_raw(tf.constant(["1212"]), tf.uint16, fixed_length=4)

If the input value is larger than `fixed_length`, it is truncated:

    x=''.join([chr(1), chr(2), chr(3), chr(4)])

If `little_endian` and `fixed_length` are specified, truncation to the fixed length occurs before endianness conversion:

    x=''.join([chr(1), chr(2), chr(3), chr(4)])

If input values all have the same length, then specifying `fixed_length` equal to the size of the strings should not change output:

    x = ["12345678", "87654321"]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_bytes` | Each element of the input Tensor is converted to an array of bytes. Currently, this must be a tensor of strings (bytes), although semantically the operation should support any input. |
| `out_type` | `DType` of the output. Acceptable types are `half`, `float`, `double`, `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`. |
| `little_endian` | Whether the `input_bytes` data is in little-endian format. Data will be converted into host byte order if necessary. |
| `fixed_length` | If set, the first `fixed_length` bytes of each element will be converted. Data will be zero-padded or truncated to the specified length. `fixed_length` must be a multiple of the size of `out_type`. `fixed_length` must be specified if the elements of `input_bytes` are of variable length. |
| `name` | A name for the operation (optional). |

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