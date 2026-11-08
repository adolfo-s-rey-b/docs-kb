[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#call)
        
    *   [create](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#create)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.rpc.Client Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#call)
        
    *   [create](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client#create)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L117-L257)

Client class for invoking RPCs to the server.

Methods
-------

### `call`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L217-L257)

call(
        method_name: str,
        args: Optional[Sequence[core_tf_types.Tensor]] = None,
        output_specs=None,
        timeout_in_ms=0
    )

Method for making RPC calls to remote server.

This invokes RPC to the server, executing the registered method\_name remotely. Args: method\_name: Remote registered method to invoke args: List of arguments for the registered method. output\_specs: Output specs for the output from method. For example, if tf.function is: @tf.function(input\_signature=\[ tf.TensorSpec(\[\], tf.int32), tf.TensorSpec(\[\], tf.int32) \]) def multiply\_fn(a, b): return tf.math.multiply(a, b) output\_spec is: tf.TensorSpec((), tf.int32) If you have access to TF Function, the output specs can be generated from tf.function by calling: output\_specs = tf.nest.map\_structure(tf.type\_spec\_from\_value, tf\_function.get\_concrete\_function().structured\_outputs If output\_specs are not provided, flattened list of tensors will be returned in response. timeout\_in\_ms: Timeout for this call. If 0, default client timeout will be used.

|     |
| --- |
| Returns |     |
| An instance of `StatusOrResult` class with the following available methods.<br><br>*   `is_ok()`: Returns True of RPC was successful.<br>*   `get_error()`: Returns TF error\_code and error message for the RPC.<br>*   `get_value()`: Returns the returned value from remote TF function execution when RPC is successful.<br><br>Calling any of the above methods will block till RPC is completed and result is available. |     |

### `create`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/experimental/rpc/rpc_ops.py#L121-L215)

@staticmethod

Create TF RPC client to connect to the given address.

|     |     |
| --- | --- |
| Args |     |
| `rpc_layer` | Communication layer between client and server. Only "grpc" rpc layer is supported at the moment. |
| `address` | Address of the server to connect the RPC client to. |
| `name` | Name of the RPC Client. You can create multiple clients connecting to same server and distinguish them using different names. |
| `timeout_in_ms` | The default timeout to use for outgoing RPCs from client. 0 indicates no timeout. Exceeding timeout during RPC will raise DeadlineExceeded error. |

|     |
| --- |
| Returns |     |
| An instance of [`tf.distribute.experimental.rpc.Client`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/rpc/Client)<br> with the following dynamically added methods for eagerly created clients:<br><br>*   `Registered methods` e.g. multiply(\*\*args): If Client is created when executing eagerly, client will request the list of registered methods from server during client creation. The convenience methods for RPCs will be dynamically added to the created Client instance.<br>    <br>    For example, when a server has method "multiply" registered, the client object created in eager mode will have 'multiply' method available. Users can use client.multiply(..) to make RPC, instead of client.call("multiply", ...)<br>    <br>    Both "call" and "multiply" methods are non-blocking i.e. they return a StatusOrResult object which should be used to wait for getting value or error.<br>    <br>    Along with the above, blocking versions of the registered methods are also dynamically added to client instance. e.g. multiply\_blocking(\*\*args). These methods block till the RPC is finished and return response for successful RPC. Otherwise raise exception.<br>    <br>    These methods are not available when Client is created inside a tf.function. |     |

|     |
| --- |
| Raises |     |
| A ValueError if rpc\_layer other than "grpc" is used. Only GRPC is supported at the moment. A DeadlineExceeded exception in eager mode if timeout exceeds while creating and listing client methods. |     |

|     |
| --- |
| Example usage |     |
| >>> # Have server already started.<br>    >>> import portpicker<br>    >>> @tf.function(input_signature=[<br>    ...      tf.TensorSpec([], tf.int32),<br>    ...      tf.TensorSpec([], tf.int32)])<br>    ... def remote_fn(a, b):<br>    ...   return tf.add(a, b)<br><br>    port = portpicker.pick_unused_port()<br><br>    # Start client<br><br>    a = tf.constant(2, dtype=tf.int32)<br><br>    result = client.call(<br><br>    if result.is_ok():<br><br>    result = client.addition(a, b)<br><br>    if result.is_ok():<br><br>    value = client.addition_blocking(a, b) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.