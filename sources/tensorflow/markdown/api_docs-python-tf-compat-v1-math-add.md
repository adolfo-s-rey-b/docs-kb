[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/add#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/add#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.add Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/add#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3916-L3994)

Returns x + y element-wise.

tf.compat.v1.math.add(
        x, y, name=None
    )

Example usages below.

Add a scalar and a list:

    x = [1, 2, 3, 4, 5]

Note that binary `+` operator can be used instead:

    x = tf.convert_to_tensor([1, 2, 3, 4, 5])

Add a tensor and a list of same shape:

    x = [1, 2, 3, 4, 5]

For example,

    x = tf.constant([1, 2], dtype=tf.int8)

When adding two input values of different shapes, `Add` follows NumPy broadcasting rules. The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.

For example,

    x = np.ones(6).reshape(1, 2, 1, 3)

Another example with two arrays of different dimension.

    x = np.ones([1, 2, 1, 4])

The reduction version of this elementwise operation is [`tf.math.reduce_sum`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must be one of the following types: bfloat16, half, float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16, int32, int64, complex64, complex128, string. |
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must have the same type as x. |
| `name` | A name for the operation (optional) |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.