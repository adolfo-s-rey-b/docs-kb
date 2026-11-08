[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2Fservice%2FWorkerServer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#methods)
    *   [join](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#start)
        
    *   [stop](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#stop)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.service.WorkerServer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#methods)
    *   [join](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#join)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#start)
        
    *   [stop](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer#stop)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L348-L478)

An in-process tf.data service worker server.

tf.data.experimental.service.WorkerServer(
        config, start=True
    )

A [`tf.data.experimental.service.WorkerServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerServer)
 performs [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 processing for user-defined datasets, and provides the resulting elements over RPC. A worker is associated with a single [`tf.data.experimental.service.DispatchServer`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatchServer)
.

    dispatcher = tf.data.experimental.service.DispatchServer()

When starting a dedicated tf.data worker process, use join() to block after starting up the worker, until the worker terminates.

worker = tf.data.experimental.service.WorkerServer(
        port=5051, dispatcher_address="localhost:5050")
    worker.join()

Call stop() to gracefully terminate the worker. The worker automatically stops when all reference to it have been deleted.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | A [`tf.data.experimental.service.WorkerConfig`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/WorkerConfig)<br> configuration. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to True. |

Methods
-------

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L419-L436)

join() -> None

Blocks until the server has shut down.

This is useful when starting a dedicated worker process.

worker_server = tf.data.experimental.service.WorkerServer(
        port=5051, dispatcher_address="localhost:5050")
    worker_server.join()

This method currently blocks forever.

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while joining the server. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L410-L417)

start() -> None

Starts this server.

|     |     |
| --- | --- |
| Raises |     |
| [`tf.errors.OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while starting the server. |

### `stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L438-L445)

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