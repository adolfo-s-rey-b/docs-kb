[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/cumsum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/cumsum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fcumsum&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.cumsum Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumsum#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4248-L4317)

Compute the cumulative sum of the tensor `x` along `axis`.

#### View aliases

**Main aliases**

[`tf.cumsum`](https://www.tensorflow.org/api_docs/python/tf/math/cumsum)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cumsum`](https://www.tensorflow.org/api_docs/python/tf/math/cumsum)
, [`tf.compat.v1.math.cumsum`](https://www.tensorflow.org/api_docs/python/tf/math/cumsum)

tf.math.cumsum(
        x, axis=0, exclusive=False, reverse=False, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core) |

By default, this op performs an inclusive cumsum, which means that the first element of the input is identical to the first element of the output: For example:

    # tf.cumsum([a, b, c])   # [a, a + b, a + b + c]

    # using varying `axis` values

By setting the `exclusive` kwarg to `True`, an exclusive cumsum is performed instead:

    # tf.cumsum([a, b, c], exclusive=True)  => [0, a, a + b]

By setting the `reverse` kwarg to `True`, the cumsum is performed in the opposite direction:

    # tf.cumsum([a, b, c], reverse=True)  # [a + b + c, b + c, c]

This is more efficient than using separate [`tf.reverse`](https://www.tensorflow.org/api_docs/python/tf/reverse)
 ops. The `reverse` and `exclusive` kwargs can also be combined:

    # tf.cumsum([a, b, c], exclusive=True, reverse=True)  # [b + c, c, 0]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. |
| `axis` | A `Tensor` of type `int32` (default: 0). Must be in the range `[-rank(x), rank(x))`. |\
| `exclusive` | If `True`, perform exclusive cumsum. |\
| `reverse` | A `bool` (default: False). |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `x`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.