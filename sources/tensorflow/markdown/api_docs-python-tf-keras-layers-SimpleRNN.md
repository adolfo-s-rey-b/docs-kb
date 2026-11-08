[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#reset_states)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.SimpleRNN Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN?version=stable#reset_states)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/simple_rnn.py#L211-L449)

Fully-connected RNN where the output is to be fed back as the new input.

Inherits From: [`RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.SimpleRNN(
        units,
        activation='tanh',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros',
        kernel_regularizer=None,
        recurrent_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        recurrent_constraint=None,
        bias_constraint=None,
        dropout=0.0,
        recurrent_dropout=0.0,
        return_sequences=False,
        return_state=False,
        go_backwards=False,
        stateful=False,
        unroll=False,
        seed=None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass None, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer uses a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `return_sequences` | Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`. |
| `return_state` | Boolean. Whether to return the last state in addition to the output. Default: `False`. |
| `go_backwards` | Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default: `False`). If `True`, the last state for each sample at index i in a batch will be used as the initial state for the sample of index i in the following batch. |
| `unroll` | Boolean (default: `False`). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up an RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `sequence` | A 3D tensor, with shape `[batch, timesteps, feature]`. |
| `mask` | Binary tensor of shape `[batch, timesteps]` indicating whether a given timestep should be masked. An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell. |

#### Example:

inputs = np.random.random((32, 10, 8))
    simple_rnn = keras.layers.SimpleRNN(4)
    output = simple_rnn(inputs)  # The output has shape `(32, 4)`.
    simple_rnn = keras.layers.SimpleRNN(
        4, return_sequences=True, return_state=True
    )
    # whole_sequence_output has shape `(32, 10, 4)`.
    # final_state has shape `(32, 4)`.
    whole_sequence_output, final_state = simple_rnn(inputs)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `activation` |     |
| `bias_constraint` |     |
| `bias_initializer` |     |
| `bias_regularizer` |     |
| `dropout` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `kernel_constraint` |     |
| `kernel_initializer` |     |
| `kernel_regularizer` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `recurrent_constraint` |     |
| `recurrent_dropout` |     |
| `recurrent_initializer` |     |
| `recurrent_regularizer` |     |
| `units` |     |
| `use_bias` |     |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/simple_rnn.py#L447-L449)

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

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L304-L319)

get_initial_state(
        batch_size
    )

### `inner_loop`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L330-L360)

inner_loop(
        sequences, initial_state, mask, training=False
    )

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L325-L328)

reset_state()

### `reset_states`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L321-L323)

reset_states()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.