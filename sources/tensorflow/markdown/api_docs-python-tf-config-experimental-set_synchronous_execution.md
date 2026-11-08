[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.set\_synchronous\_execution Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L403-L425)

Specifies whether operations are executed synchronously or asynchronously.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.set_synchronous_execution`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution)

tf.config.experimental.set_synchronous_execution(
        enable
    )

TensorFlow can execute operations synchronously or asynchronously. If asynchronous execution is enabled, operations may return "non-ready" handles.

When `enable` is set to None, an appropriate value will be picked automatically. The value picked may change between TensorFlow releases.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `enable` | Whether operations should be dispatched synchronously. Valid values:<br><br>*   None: sets the system default.<br>*   True: executes each operation synchronously.<br>*   False: executes each operation asynchronously. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.