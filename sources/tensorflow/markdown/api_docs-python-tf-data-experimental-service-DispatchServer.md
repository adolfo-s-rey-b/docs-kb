[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#methods)
    *   [join](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#start)
        
    *   [stop](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#stop)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.service.DispatchServer Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#methods)
    *   [join](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#start)
        
    *   [stop](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer#stop)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L130-L289)

An in-process tf.data service dispatch server.

tf.data.experimental.service.DispatchServer(
        config=None, start=True
    )

A [`tf.data.experimental.service.DispatchServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer)
 coordinates a cluster of [`tf.data.experimental.service.WorkerServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer)
s. When the workers start, they register themselves with the dispatcher.

    dispatcher = tf.data.experimental.service.DispatchServer()

When starting a dedicated tf.data dispatch process, use join() to block after starting up the server, until the server terminates.

dispatcher = tf.data.experimental.service.DispatchServer(
        tf.data.experimental.service.DispatcherConfig(port=5050))
    dispatcher.join()

Call stop() to gracefully terminate the dispatcher. The server automatically stops when all reference to it have been deleted.

To start a `DispatchServer` in fault-tolerant mode, set `work_dir` and `fault_tolerant_mode` like below:

dispatcher = tf.data.experimental.service.DispatchServer(
        tf.data.experimental.service.DispatcherConfig(
            port=5050,
            work_dir="gs://my-bucket/dispatcher/work_dir",
            fault_tolerant_mode=True))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | (Optional.) A [`tf.data.experimental.service.DispatcherConfig`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig)<br> configuration. If `None`, the dispatcher will use default configuration values. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to True. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `target` | Returns a target that can be used to connect to the server.<br><br>    dispatcher = tf.data.experimental.service.DispatchServer()<br><br>The returned string will be in the form protocol://address, e.g. "grpc://localhost:5050". |

Methods
-------

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L221-L236)

join() -> None

Blocks until the server has shut down.

This is useful when starting a dedicated dispatch process.

dispatcher = tf.data.experimental.service.DispatchServer(
        tf.data.experimental.service.DispatcherConfig(port=5050))
    dispatcher.join()

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while joining the server. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L209-L219)

start()

Starts this server.

    dispatcher = tf.data.experimental.service.DispatchServer(start=False)

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while starting the server. |

### `stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L238-L245)

stop() -> None

Stops the server.

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while stopping the server. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.