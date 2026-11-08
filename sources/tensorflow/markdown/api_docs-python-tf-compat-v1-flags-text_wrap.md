[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.text\_wrap Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/text_wrap#raises)
    

Wraps a given text to a maximum line length and returns it.

tf.compat.v1.flags.text_wrap(
        text: str,
        length: (int | None) = None,
        indent: str = '',
        firstline_indent: (str | None) = None
    ) -> str

It turns lines that only contain whitespace into empty lines, keeps new lines, and expands tabs using 4 spaces.

|     |     |
| --- | --- |
| Args<br>---- |     |
| [`text`](https://www.tensorflow.org/text/api_docs/python/text) | Text to wrap. |
| `length` | Maximum length of a line, includes indentation. If this is `None` then use `get_help_width()`. |
| `indent` | Indent for all but first line. |
| `firstline_indent` | Indent for first line. If `None`, fall back to `indent`. |

|     |
| --- |
| Returns<br>------- |     |
| The wrapped text. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | Raised if indent or firstline\_indent not shorter than length. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.