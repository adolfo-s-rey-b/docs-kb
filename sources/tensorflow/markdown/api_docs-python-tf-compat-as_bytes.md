[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.as\_bytes Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/compat.py#L57-L82)

Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.as_bytes`](https://www.tensorflow.org/api_docs/python/tf/compat/as_bytes)

tf.compat.as_bytes(
        bytes_or_text, encoding='utf-8'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFX Python function component tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/python_function_component) |

Uses utf-8 encoding for text by default.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes_or_text` | A `bytearray`, `bytes`, `str`, or `unicode` object. |
| `encoding` | A string indicating the charset for encoding unicode. |

|     |
| --- |
| Returns<br>------- |     |
| A `bytes` object. |     |

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