[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/as_text)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/as_text?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fas_text&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.as\_text Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/as_text#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/compat.py#L85-L108)

Converts any string-like python input types to unicode.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.as_text`](https://www.tensorflow.org/api_docs/python/tf/compat/as_text)

tf.compat.as_text(
        bytes_or_text, encoding='utf-8'
    )

Returns the input as a unicode string. Uses utf-8 encoding for text by default.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes_or_text` | A `bytes`, `str`, or `unicode` object. |
| `encoding` | A string indicating the charset for decoding unicode. |

|     |
| --- |
| Returns<br>------- |     |
| A `unicode` (Python 2) or `str` (Python 3) object. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `bytes_or_text` is not a binary or unicode string. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.