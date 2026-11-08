[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.bitwise.right\_shift Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift#returns)
    

Elementwise computes the bitwise right-shift of `x` and `y`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.bitwise.right_shift`](https://www.tensorflow.org/api_docs/python/tf/bitwise/right_shift)

tf.bitwise.right_shift(
        x: Annotated[Any, TV_RightShift_T],
        y: Annotated[Any, TV_RightShift_T],
        name=None
    ) -> Annotated[Any, TV_RightShift_T]

Performs a logical shift for unsigned integer types, and an arithmetic shift for signed integer types.

If `y` is negative, or greater than or equal to than the width of `x` in bits the result is implementation defined.

#### Example:

import tensorflow as tf
    from tensorflow.python.ops import bitwise_ops
    import numpy as np
    dtype_list = [tf.int8, tf.int16, tf.int32, tf.int64]
    
    for dtype in dtype_list:
      lhs = tf.constant([-1, -5, -3, -14], dtype=dtype)
      rhs = tf.constant([5, 0, 7, 11], dtype=dtype)
    
      right_shift_result = bitwise_ops.right_shift(lhs, rhs)
    
      print(right_shift_result)
    
    # This will print:
    # tf.Tensor([-1 -5 -1 -1], shape=(4,), dtype=int8)
    # tf.Tensor([-1 -5 -1 -1], shape=(4,), dtype=int16)
    # tf.Tensor([-1 -5 -1 -1], shape=(4,), dtype=int32)
    # tf.Tensor([-1 -5 -1 -1], shape=(4,), dtype=int64)
    
    lhs = np.array([-2, 64, 101, 32], dtype=np.int8)
    rhs = np.array([-1, -5, -3, -14], dtype=np.int8)
    bitwise_ops.right_shift(lhs, rhs)
    # <tf.Tensor: shape=(4,), dtype=int8, numpy=array([ -2,  64, 101,  32], dtype=int8)>

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