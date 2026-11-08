[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/cumprod#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/cumprod)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/cumprod?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fcumprod&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumprod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumprod#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.cumprod Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumprod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumprod#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4320-L4371)

Compute the cumulative product of the tensor `x` along `axis`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.cumprod`](https://www.tensorflow.org/api_docs/python/tf/math/cumprod)
, [`tf.compat.v1.math.cumprod`](https://www.tensorflow.org/api_docs/python/tf/math/cumprod)

tf.math.cumprod(
        x, axis=0, exclusive=False, reverse=False, name=None
    )

By default, this op performs an inclusive cumprod, which means that the first element of the input is identical to the first element of the output:

tf.math.cumprod([a, b, c])  # [a, a * b, a * b * c]

By setting the `exclusive` kwarg to `True`, an exclusive cumprod is performed instead:

tf.math.cumprod([a, b, c], exclusive=True)  # [1, a, a * b]

By setting the `reverse` kwarg to `True`, the cumprod is performed in the opposite direction:

tf.math.cumprod([a, b, c], reverse=True)  # [a * b * c, b * c, c]

This is more efficient than using separate [`tf.reverse`](https://www.tensorflow.org/api_docs/python/tf/reverse)
 ops. The `reverse` and `exclusive` kwargs can also be combined:

tf.math.cumprod([a, b, c], exclusive=True, reverse=True)  # [b * c, c, 1]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. |
| `axis` | A `Tensor` of type `int32` (default: 0). Must be in the range `[-rank(x), rank(x))`. |\
| `exclusive` | If `True`, perform exclusive cumprod. |\
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