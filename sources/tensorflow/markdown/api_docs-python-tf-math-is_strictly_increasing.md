[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/is_strictly_increasing#main-content)

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
    

tf.math.is\_strictly\_increasing Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L2037-L2076)

Returns `True` if `x` is strictly increasing.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.is_strictly_increasing`](https://www.tensorflow.org/api_docs/python/tf/math/is_strictly_increasing)
, [`tf.compat.v1.is_strictly_increasing`](https://www.tensorflow.org/api_docs/python/tf/math/is_strictly_increasing)
, [`tf.compat.v1.math.is_strictly_increasing`](https://www.tensorflow.org/api_docs/python/tf/math/is_strictly_increasing)

tf.math.is_strictly_increasing(
        x, name=None
    )

Elements of `x` are compared in row-major order. The tensor `[x[0],...]` is strictly increasing if for every adjacent pair we have `x[i] < x[i+1]`. If `x` has less than two elements, it is trivially strictly increasing.

See also: `is_non_decreasing`

    x1 = tf.constant([1.0, 2.0, 3.0])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `name` | A name for this operation (optional). Defaults to "is\_strictly\_increasing" |

|     |
| --- |
| Returns<br>------- |     |
| Boolean `Tensor`, equal to `True` iff `x` is strictly increasing. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `x` is not a numeric tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.