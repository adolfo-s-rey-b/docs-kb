[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#methods)
    *   [create](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#create)
        
    *   [register](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#register)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#start)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.rpc.Server Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#methods)
    *   [create](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#create)
        
    *   [register](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#register)
        
    *   [start](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server#start)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L50-L114)

A Server base class for accepting RPCs for registered tf.functions.

Functions can be registered on the server and are exposed via RPCs.

Methods
-------

### `create`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L57-L91)

@staticmethod

Create TF RPC server at given address.

|     |     |
| --- | --- |
| Args |     |
| `rpc_layer` | Communication layer between client and server. Only "grpc" rpc layer is supported at the moment. |
| `address` | Address where RPC server is hosted. |

|     |
| --- |
| Returns |     |
| An instance of [`tf.distribute.experimental.rpc.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Server)<br> class. |     |

|     |
| --- |
| Raises |     |
| A ValueError if rpc\_layer other than "grpc" is used. Only GRPC is supported at the moment. |     |

|     |
| --- |
| Example usage |     |
| >>> import portpicker<br>    >>> @tf.function(input_signature=[<br>    ...      tf.TensorSpec([], tf.int32),<br>    ...      tf.TensorSpec([], tf.int32)])<br>    ... def remote_fn(a, b):<br>    ...   return tf.add(a, b)<br><br>    port = portpicker.pick_unused_port() |     |

### `register`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L93-L106)

register(
        method_name: str,
        func: Union[def_function.Function, tf_function.ConcreteFunction]
    )

Method for registering tf.function on server.

Registered methods can be invoked remotely from clients.

|     |     |
| --- | --- |
| Args |     |
| `method_name` | Name of the tf.function. Clients use this method\_name to make RPCs. |
| `func` | A [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> or ConcreteFunction to register. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L108-L114)

start()

Starts the RPC server on provided address.

Server listens for new requests from client, once it is started.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.