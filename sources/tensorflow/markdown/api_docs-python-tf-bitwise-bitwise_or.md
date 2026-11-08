[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fbitwise%2Fbitwise_or&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.bitwise.bitwise\_or Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or#returns)
    

Elementwise computes the bitwise OR of `x` and `y`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.bitwise.bitwise_or`](https://www.tensorflow.org/api_docs/python/tf/bitwise/bitwise_or)

tf.bitwise.bitwise_or(
        x: Annotated[Any, TV_BitwiseOr_T],
        y: Annotated[Any, TV_BitwiseOr_T],
        name=None
    ) -> Annotated[Any, TV_BitwiseOr_T]

The result will have those bits set, that are set in `x`, `y` or both. The computation is performed on the underlying representations of `x` and `y`.

#### For example:

import tensorflow as tf
    from tensorflow.python.ops import bitwise_ops
    dtype_list = [tf.int8, tf.int16, tf.int32, tf.int64,\
                  tf.uint8, tf.uint16, tf.uint32, tf.uint64]
    
    for dtype in dtype_list:
      lhs = tf.constant([0, 5, 3, 14], dtype=dtype)
      rhs = tf.constant([5, 0, 7, 11], dtype=dtype)
      exp = tf.constant([5, 5, 7, 15], dtype=tf.float32)
    
      res = bitwise_ops.bitwise_or(lhs, rhs)
      tf.assert_equal(tf.cast(res,  tf.float32), exp)  # TRUE

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`. |
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

Last updated 2024-04-26 UTC.