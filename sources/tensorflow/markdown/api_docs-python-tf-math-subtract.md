[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/subtract#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/subtract)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/subtract?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/subtract#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/subtract#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.subtract Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/subtract#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/subtract#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L571-L575)

Returns x - y element-wise.

#### View aliases

**Main aliases**

[`tf.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)
, [`tf.compat.v1.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)

tf.math.subtract(
        x, y, name=None
    )

Both input and output have a range `(-inf, inf)`.

Example usages below.

Subtract operation between an array and a scalar:

    x = [1, 2, 3, 4, 5]

Note that binary `-` operator can be used instead:

    x = tf.convert_to_tensor([1, 2, 3, 4, 5])

Subtract operation between an array and a tensor of same shape:

    x = [1, 2, 3, 4, 5]

For example,

    x = tf.constant([1, 2], dtype=tf.int8)

When subtracting two input values of different shapes, [`tf.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)
 follows the [general broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules)
 . The two input array shapes are compared element-wise. Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be `1`.

For example,

    x = np.ones(6).reshape(2, 3, 1)

Example with inputs of different dimensions:

    x = np.ones(6).reshape(2, 3, 1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`, `uint64`. |
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

Last updated 2026-10-31 UTC.