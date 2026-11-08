[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fstrings%2Flength&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.strings.length Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/strings/length#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L382-L409)

Computes the length of each string given in the input tensor.

tf.compat.v1.strings.length(
        input, name=None, unit='BYTE'
    )

    strings = tf.constant(['Hello','TensorFlow', '🙂'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The strings for which to compute the length for each element. |
| `name` | A name for the operation (optional). |
| `unit` | An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`. The unit that is counted to compute string length. One of: `"BYTE"` (for the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8 encoded Unicode code points in each string). Results are undefined if `unit=UTF8_CHAR` and the `input` strings do not contain structurally valid UTF-8. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`, containing the length of the input string in the same element of the input tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.