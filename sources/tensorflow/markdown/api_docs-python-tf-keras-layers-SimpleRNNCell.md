[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FSimpleRNNCell%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#from_config)
        
    *   [get\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_dropout_mask)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_initial_state)
        
    *   [get\_recurrent\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_recurrent_dropout_mask)
        
    *   [reset\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#reset_dropout_mask)
        
    *   [reset\_recurrent\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#reset_recurrent_dropout_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.SimpleRNNCell Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#from_config)
        
    *   [get\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_dropout_mask)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_initial_state)
        
    *   [get\_recurrent\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#get_recurrent_dropout_mask)
        
    *   [reset\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#reset_dropout_mask)
        
    *   [reset\_recurrent\_dropout\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNNCell?version=stable#reset_recurrent_dropout_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/simple_rnn.py#L14-L208)

Cell class for SimpleRNN.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.SimpleRNNCell(
        units,
        activation='tanh',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros',
        kernel_regularizer=None,
        recurrent_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        recurrent_constraint=None,
        bias_constraint=None,
        dropout=0.0,
        recurrent_dropout=0.0,
        seed=None,
        **kwargs
    )

This class processes one step within the whole time sequence input, whereas `keras.layer.SimpleRNN` processes the whole sequence.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer should use a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `seed` | Random seed for dropout. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `sequence` | A 2D tensor, with shape `(batch, features)`. |
| `states` | A 2D tensor with shape `(batch, units)`, which is the state from the previous time step. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. Only relevant when `dropout` or `recurrent_dropout` is used. |

#### Example:

inputs = np.random.random([32, 10, 8]).astype(np.float32)
    rnn = keras.layers.RNN(keras.layers.SimpleRNNCell(4))
    output = rnn(inputs)  # The output has shape `(32, 4)`.
    rnn = keras.layers.RNN(
        keras.layers.SimpleRNNCell(4),
        return_sequences=True,
        return_state=True
    )
    # whole_sequence_output has shape `(32, 10, 4)`.
    # final_state has shape `(32, 4)`.
    whole_sequence_output, final_state = rnn(inputs)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

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

### `get_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/dropout_rnn_cell.py#L37-L44)

get_dropout_mask(
        step_input
    )

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/simple_rnn.py#L174-L177)

get_initial_state(
        batch_size=None
    )

### `get_recurrent_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/dropout_rnn_cell.py#L46-L53)

get_recurrent_dropout_mask(
        step_input
    )

### `reset_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/dropout_rnn_cell.py#L55-L63)

reset_dropout_mask()

Reset the cached dropout mask if any.

The RNN layer invokes this in the `call()` method so that the cached mask is cleared after calling `cell.call()`. The mask should be cached across all timestep within the same batch, but shouldn't be cached between batches.

### `reset_recurrent_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/dropout_rnn_cell.py#L65-L66)

reset_recurrent_dropout_mask()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.