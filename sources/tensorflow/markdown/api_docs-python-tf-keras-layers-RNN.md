[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#reset_states)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.RNN Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN?version=stable#reset_states)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L12-L498)

Base class for recurrent layers.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.RNN(
        cell,
        return_sequences=False,
        return_state=False,
        go_backwards=False,
        stateful=False,
        unroll=False,
        zero_output_for_mask=False,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cell` | A RNN cell instance or a list of RNN cell instances. A RNN cell is a class that has:<br><br>*   A `call(input_at_t, states_at_t)` method, returning `(output_at_t, states_at_t_plus_1)`. The call method of the cell can also take the optional argument `constants`, see section "Note on passing external constants" below.<br>*   A `state_size` attribute. This can be a single integer (single state) in which case it is the size of the recurrent state. This can also be a list/tuple of integers (one size per state).<br>*   A `output_size` attribute, a single integer.<br>*   A `get_initial_state(batch_size=None)` method that creates a tensor meant to be fed to `call()` as the initial state, if the user didn't specify any initial state via other means. The returned initial state should have shape `(batch_size, cell.state_size)`. The cell might choose to create a tensor full of zeros, or other values based on the cell's implementation. `inputs` is the input tensor to the RNN layer, with shape `(batch_size, timesteps, features)`. If this method is not implemented by the cell, the RNN layer will create a zero filled tensor with shape `(batch_size, cell.state_size)`. In the case that `cell` is a list of RNN cell instances, the cells will be stacked on top of each other in the RNN, resulting in an efficient stacked RNN. |
| `return_sequences` | Boolean (default `False`). Whether to return the last output in the output sequence, or the full sequence. |
| `return_state` | Boolean (default `False`). Whether to return the last state in addition to the output. |
| `go_backwards` | Boolean (default `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default `False`). If True, the last state for each sample at index `i` in a batch will be used as initial state for the sample of index `i` in the following batch. |
| `unroll` | Boolean (default `False`). If True, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |
| `zero_output_for_mask` | Boolean (default `False`). Whether the output should use zeros for the masked timesteps. Note that this field is only used when `return_sequences` is `True` and `mask` is provided. It can useful if you want to reuse the raw output sequence of the RNN without interference from the masked timesteps, e.g., merging bidirectional RNNs. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `sequences` | A 3-D tensor with shape `(batch_size, timesteps, features)`. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell. |
| `mask` | Binary tensor of shape `[batch_size, timesteps]` indicating whether a given timestep should be masked. An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is for use with cells that use dropout. |

#### Output shape:

*   If `return_state`: a list of tensors. The first tensor is the output. The remaining tensors are the last states, each with shape `(batch_size, state_size)`, where `state_size` could be a high dimension tensor shape.
*   If `return_sequences`: 3D tensor with shape `(batch_size, timesteps, output_size)`.

#### Masking:

This layer supports masking for input data with a variable number of timesteps. To introduce masks to your data, use a [`keras.layers.Embedding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)
 layer with the `mask_zero` parameter set to `True`.

Note on using statefulness in RNNs:

You can set RNN layers to be 'stateful', which means that the states computed for the samples in one batch will be reused as initial states for the samples in the next batch. This assumes a one-to-one mapping between samples in different successive batches.

To enable statefulness:

*   Specify `stateful=True` in the layer constructor.
*   Specify a fixed batch size for your model, by passing `batch_size=...` to the `Input` layer(s) of your model. Remember to also specify the same `batch_size=...` when calling `fit()`, or otherwise use a generator-like data source like a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)
     or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    .
*   Specify `shuffle=False` when calling `fit()`, since your batches are expected to be temporally ordered.

To reset the states of your model, call `.reset_state()` on either a specific layer, or on your entire model.

Note on specifying the initial state of RNNs:

You can specify the initial state of RNN layers symbolically by calling them with the keyword argument `initial_state`. The value of `initial_state` should be a tensor or list of tensors representing the initial state of the RNN layer.

You can specify the initial state of RNN layers numerically by calling `reset_state()` with the keyword argument `states`. The value of `states` should be a numpy array or list of numpy arrays representing the initial state of the RNN layer.

#### Examples:

from keras.layers import RNN
    from keras import ops
    
    # First, let's define a RNN Cell, as a layer subclass.
    class MinimalRNNCell(keras.Layer):
    
        def __init__(self, units, **kwargs):
            super().__init__(**kwargs)
            self.units = units
            self.state_size = units
    
        def build(self, input_shape):
            self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                          initializer='uniform',
                                          name='kernel')
            self.recurrent_kernel = self.add_weight(
                shape=(self.units, self.units),
                initializer='uniform',
                name='recurrent_kernel')
    
        def call(self, inputs, states):
            prev_output = states[0]
            h = ops.matmul(inputs, self.kernel)
            output = h + ops.matmul(prev_output, self.recurrent_kernel)
            return output, [output]
    
    # Let's use this cell in a RNN layer:
    
    cell = MinimalRNNCell(32)
    x = keras.Input((None, 5))
    layer = RNN(cell)
    y = layer(x)
    
    # Here's how to use the cell to build a stacked RNN:
    
    cells = [MinimalRNNCell(32), MinimalRNNCell(64)]
    x = keras.Input((None, 5))
    layer = RNN(cells)
    y = layer(x)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L492-L498)

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