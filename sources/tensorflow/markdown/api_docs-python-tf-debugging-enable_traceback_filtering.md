[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.enable\_traceback\_filtering Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/traceback_utils.py#L51-L73)

Enable filtering out TensorFlow-internal frames in exception stack traces.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.enable_traceback_filtering`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering)

tf.debugging.enable_traceback_filtering()

Raw TensorFlow stack traces involve many internal frames, which can be challenging to read through, while not being actionable for end users. By default, TensorFlow filters internal frames in most exceptions that it raises, to keep stack traces short, readable, and focused on what's actionable for end users (their own code).

If you have previously disabled traceback filtering via [`tf.debugging.disable_traceback_filtering()`](https://www.tensorflow.org/api_docs/python/tf/debugging/disable_traceback_filtering)
, you can re-enable it via [`tf.debugging.enable_traceback_filtering()`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering)
.

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If Python version is not at least 3.7. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.