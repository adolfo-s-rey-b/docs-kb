[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/length#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/length)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/length?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/length#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/length#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.length Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/length#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/length#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L412-L416)

String lengths of `input`.

tf.strings.length(
        input, unit='BYTE', name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [word2vec](https://www.tensorflow.org/text/tutorials/word2vec) |

Computes the length of each string given in the input tensor.

    strings = tf.constant(['Hello','TensorFlow', '\U0001F642'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` of type `string`. The strings for which to compute the length for each element. |
| `unit` | An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`. The unit that is counted to compute string length. One of: `"BYTE"` (for the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8 encoded Unicode code points in each string). Results are undefined if `unit=UTF8_CHAR` and the `input` strings do not contain structurally valid UTF-8. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.