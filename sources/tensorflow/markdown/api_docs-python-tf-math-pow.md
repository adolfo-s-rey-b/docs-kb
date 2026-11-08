[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/pow#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.pow Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L697-L723)

Computes the power of one value to another.

#### View aliases

**Main aliases**

[`tf.pow`](https://www.tensorflow.org/api_docs/python/tf/math/pow)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.pow`](https://www.tensorflow.org/api_docs/python/tf/math/pow)
, [`tf.compat.v1.pow`](https://www.tensorflow.org/api_docs/python/tf/math/pow)

tf.math.pow(
        x, y, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs) |

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for corresponding elements in `x` and `y`. For example:

x = tf.constant([[2, 2], [3, 3]])
    y = tf.constant([[8, 16], [2, 3]])
    tf.pow(x, y)  # [[256, 65536], [9, 27]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |
| `y` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`, `complex64`, or `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.