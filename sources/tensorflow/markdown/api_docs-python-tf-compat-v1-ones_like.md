[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fones_like&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ones\_like Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_like#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2815-L2846)

Creates a tensor with all elements set to 1.

tf.compat.v1.ones_like(
        tensor, dtype=None, name=None, optimize=True
    )

See also [`tf.ones`](https://www.tensorflow.org/api_docs/python/tf/ones)
.

Given a single tensor (`tensor`), this operation returns a tensor of the same type and shape as `tensor` with all elements set to 1. Optionally, you can specify a new type (`dtype`) for the returned tensor.

#### For example:

tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    tf.ones_like(tensor)  # [[1, 1, 1], [1, 1, 1]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. |
| `dtype` | A type for the returned `Tensor`. Must be `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `complex64`, `complex128` or `bool`. |
| `name` | A name for the operation (optional). |
| `optimize` | if true, attempt to statically determine the shape of 'tensor' and encode it as a constant. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with all elements set to 1. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.