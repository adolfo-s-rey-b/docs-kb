[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/bitcast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/bitcast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/bitcast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitcast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitcast#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.bitcast Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitcast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitcast#returns)
    

Bitcasts a tensor from one type to another without copying data.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.bitcast`](https://www.tensorflow.org/api_docs/python/tf/bitcast)

tf.bitcast(
        input: Annotated[Any, TV_Bitcast_T], type: TV_Bitcast_type, name=None
    ) -> Annotated[Any, TV_Bitcast_type]

Given a tensor `input`, this operation returns a tensor that has the same buffer data as `input` with datatype `type`.

If the input datatype `T` is larger than the output datatype `type` then the shape changes from \[...\] to \[..., sizeof(`T`)/sizeof(`type`)\].

If `T` is smaller than `type`, the operator requires that the rightmost dimension be equal to sizeof(`type`)/sizeof(`T`). The shape then goes from \[..., sizeof(`type`)/sizeof(`T`)\] to \[...\].

tf.bitcast() and tf.cast() work differently when real dtype is casted as a complex dtype (e.g. tf.complex64 or tf.complex128) as tf.cast() make imaginary part 0 while tf.bitcast() gives module error. For example,

#### Example 1:

    a = [1., 2., 3.]

#### Example 2:

    tf.bitcast(tf.constant(0xffffffff, dtype=tf.uint32), tf.uint8)

#### Example 3:

    x = [1., 2., 3.]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `complex64`, `complex128`, `qint8`, `quint8`, `qint16`, `quint16`, `qint32`. |
| `type` | A [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int64, tf.int32, tf.uint8, tf.uint16, tf.uint32, tf.uint64, tf.int8, tf.int16, tf.complex64, tf.complex128, tf.qint8, tf.quint8, tf.qint16, tf.quint16, tf.qint32`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.