[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.logging.log\_every\_n Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/tf_logging.py#L266-L280)

Log 'msg % args' at level 'level' once per 'n' times.

tf.compat.v1.logging.log_every_n(
        level, msg, n, *args
    )

Logs the 1st call, (N+1)st call, (2N+1)st call, etc. Not threadsafe.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `level` | The level at which to log. |
| `msg` | The message to be logged. |
| `n` | The number of times this should be called before it is logged. |
| `*args` | The args to be substituted into the msg. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.