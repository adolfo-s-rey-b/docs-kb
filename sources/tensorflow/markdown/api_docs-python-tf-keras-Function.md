[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2FFunction&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Function#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Function#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Function#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#call)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/keras/Function#compute_output_shape)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Function#compute_output_spec)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Function#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Function#get_config)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#rematerialized_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Function#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Function Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Function#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Function#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Function#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#call)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/keras/Function#compute_output_shape)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Function#compute_output_spec)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Function#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Function#get_config)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#rematerialized_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Function#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Function#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/function.py#L11-L253)

Class that encapsulates a computation graph of Keras operations.

Inherits From: [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Function`](https://www.tensorflow.org/api_docs/python/tf/keras/Function)

tf.keras.Function(
        inputs, outputs, name=None
    )

You can use a `Function` to capture the computation graph linking some input tensors to some output tensors, and reapply the same computation on new inputs.

A `Function` is similar to a Functional Model, with the difference that it is stateless (it does not track state variables) and does not implement the `Layer` API.

#### Example:

input_1 = keras.KerasTensor(shape=(None, 2, 3))
    input_2 = keras.KerasTensor(shape=(None, 2, 3))
    x = input_1 + input_2
    output = keras.ops.sigmoid(x)
    fn = keras.Function(inputs=[input_1, input_2], outputs=output)
    
    input_1_val = np.random.random((4, 2, 3))
    input_2_val = np.random.random((4, 2, 3))
    output_val = fn([input_1_val, input_2_val])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | `KerasTensor` instance or nested structured of `KerasTensor` instances. |
| `outputs` | `KerasTensor` instance or nested structured of `KerasTensor` instances. They should be computable given only the values of `inputs`. |
| `name` | String. The name of the function. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `inputs` | Flat list of the symbolic inputs of the Function. |
| `operations` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `outputs` | Flat list of the symbolic outputs of the Function. |

Methods
-------

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/function.py#L168-L171)

call(
        inputs
    )

Computes output tensors for new inputs.

### `compute_output_shape`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/function.py#L154-L166)

compute_output_shape(
        input_shape
    )

### `compute_output_spec`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/function.py#L132-L152)

compute_output_spec(
        inputs
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