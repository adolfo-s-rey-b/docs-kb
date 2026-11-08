[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Operation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#call)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#compute_output_spec)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#get_config)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#rematerialized_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Operation Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#call)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#compute_output_spec)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#get_config)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#rematerialized_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Operation#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L20-L442)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.Operation(
        name=None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L97-L98)

call(
        *args, **kwargs
    )

### `compute_output_spec`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L139-L152)

compute_output_spec(
        *args, **kwargs
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L245-L320)

get_config()

Returns the config of the object.

An object config is a Python dictionary (serializable) containing the information needed to re-instantiate it.

### `quantized_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L100-L101)

quantized_call(
        *args, **kwargs
    )

### `rematerialized_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L103-L137)

rematerialized_call(
        fn, *args, **kwargs
    )

Enable rematerialization dynamically for an operation's call method.

|     |     |
| --- | --- |
| Args |     |
| `fn` | The original `call` or `quantized_call` method of an operation. |

|     |
| --- |
| Returns |     |
| Rematerialized method. |     |

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L83-L95)

symbolic_call(
        *args, **kwargs
    )

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L36-L81)

__call__(
        *args, **kwargs
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.