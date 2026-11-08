[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flogging&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.logging Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging#other-members)
    

Public API for tf.\_api.v2.logging namespace

Functions
---------

[`TaskLevelStatusMessage(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/TaskLevelStatusMessage)

[`debug(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/debug)

[`error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/error)

[`fatal(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/fatal)

[`flush(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/flush)

[`get_verbosity(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/get_verbosity)
: Return how much logging output will be produced.

[`info(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/info)

[`log(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log)

[`log_every_n(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_every_n)
: Log 'msg % args' at level 'level' once per 'n' times.

[`log_first_n(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_first_n)
: Log 'msg % args' at level 'level' only first 'n' times.

[`log_if(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/log_if)
: Log 'msg % args' at level 'level' only if condition is fulfilled.

[`set_verbosity(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/set_verbosity)
: Sets the threshold for what messages will be logged.

[`vlog(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/vlog)

[`warn(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/warn)

[`warning(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/warning)

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| DEBUG | `10` |
| ERROR | `40` |
| FATAL | `50` |
| INFO | `20` |
| WARN | `30` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.