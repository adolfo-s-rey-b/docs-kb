[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fbitwise%2Finvert&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.bitwise.invert Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert#returns)
    

Invert (flip) each bit of supported types; for example, type `uint8` value 01010101 becomes 10101010.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.bitwise.invert`](https://www.tensorflow.org/api_docs/python/tf/bitwise/invert)

tf.bitwise.invert(
        x: Annotated[Any, TV_Invert_T], name=None
    ) -> Annotated[Any, TV_Invert_T]

Flip each bit of supported types. For example, type `int8` (decimal 2) binary 00000010 becomes (decimal -3) binary 11111101. This operation is performed on each element of the tensor argument `x`.

#### Example:

import tensorflow as tf
    from tensorflow.python.ops import bitwise_ops
    
    # flip 2 (00000010) to -3 (11111101)
    tf.assert_equal(-3, bitwise_ops.invert(2))
    
    dtype_list = [dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,\
                  dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64]
    
    inputs = [0, 5, 3, 14]
    for dtype in dtype_list:
      # Because of issues with negative numbers, let's test this indirectly.
      # 1. invert(a) and a = 0
      # 2. invert(a) or a = invert(0)
      input_tensor = tf.constant([0, 5, 3, 14], dtype=dtype)
      not_a_and_a, not_a_or_a, not_0 = [bitwise_ops.bitwise_and(\
                                          input_tensor, bitwise_ops.invert(input_tensor)),\
                                        bitwise_ops.bitwise_or(\
                                          input_tensor, bitwise_ops.invert(input_tensor)),\
                                        bitwise_ops.invert(\
                                          tf.constant(0, dtype=dtype))]
    
      expected = tf.constant([0, 0, 0, 0], dtype=tf.float32)
      tf.assert_equal(tf.cast(not_a_and_a, tf.float32), expected)
    
      expected = tf.cast([not_0] * 4, tf.float32)
      tf.assert_equal(tf.cast(not_a_or_a, tf.float32), expected)
    
      # For unsigned dtypes let's also check the result directly.
      if dtype.is_unsigned:
        inverted = bitwise_ops.invert(input_tensor)
        expected = tf.constant([dtype.max - x for x in inputs], dtype=tf.float32)
        tf.assert_equal(tf.cast(inverted, tf.float32), tf.cast(expected, tf.float32))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`. |
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