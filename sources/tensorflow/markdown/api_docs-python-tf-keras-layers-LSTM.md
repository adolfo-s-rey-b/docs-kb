[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FLSTM%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#reset_states)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.LSTM Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable#reset_states)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/lstm.py#L331-L692)

Long Short-Term Memory layer - Hochreiter 1997.

Inherits From: [`RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.LSTM(
        units,
        activation='tanh',
        recurrent_activation='sigmoid',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros',
        unit_forget_bias=True,
        kernel_regularizer=None,
        recurrent_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        recurrent_constraint=None,
        bias_constraint=None,
        dropout=0.0,
        recurrent_dropout=0.0,
        seed=None,
        return_sequences=False,
        return_state=False,
        go_backwards=False,
        stateful=False,
        unroll=False,
        use_cudnn='auto',
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Generate music with an RNN](https://www.tensorflow.org/tutorials/audio/music_generation)<br>    <br>*   [Text classification with an RNN](https://www.tensorflow.org/text/tutorials/text_classification_rnn)<br>    <br>*   [Load metrics from Prometheus server](https://www.tensorflow.org/io/tutorials/prometheus)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

Based on available runtime hardware and constraints, this layer will choose different implementations (cuDNN-based or backend-native) to maximize the performance. If a GPU is available and all the arguments to the layer meet the requirement of the cuDNN kernel (see below for details), the layer will use a fast cuDNN implementation when using the TensorFlow backend. The requirements to use the cuDNN implementation are:

1.  `activation` == `tanh`
2.  `recurrent_activation` == `sigmoid`
3.  `recurrent_dropout` == 0
4.  `unroll` is `False`
5.  `use_bias` is `True`
6.  Inputs, if use masking, are strictly right-padded.
7.  Eager execution is enabled in the outermost context.

#### For example:

    inputs = np.random.random((32, 10, 8))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `recurrent_activation` | Activation function to use for the recurrent step. Default: sigmoid (`sigmoid`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer should use a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `unit_forget_bias` | Boolean (default `True`). If `True`, add 1 to the bias of the forget gate at initialization. Setting it to `True` will also force `bias_initializer="zeros"`. This is recommended in [Jozefowicz et al.](https://github.com/mlresearch/v37/blob/gh-pages/jozefowicz15.pdf) |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `seed` | Random seed for dropout. |
| `return_sequences` | Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`. |
| `return_state` | Boolean. Whether to return the last state in addition to the output. Default: `False`. |
| `go_backwards` | Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default: `False`). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch. |
| `unroll` | Boolean (default False). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |
| `use_cudnn` | Whether to use a cuDNN-backed implementation. `"auto"` will attempt to use cuDNN when feasible, and will fallback to the default implementation if not. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A 3D tensor, with shape `(batch, timesteps, feature)`. |
| `mask` | Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked (optional). An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. Defaults to `None`. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used (optional). Defaults to `None`. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell (optional, `None` causes creation of zero-filled initial state tensors). Defaults to `None`. |

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
| `recurrent_activation` |     |
| `recurrent_constraint` |     |
| `recurrent_dropout` |     |
| `recurrent_initializer` |     |
| `recurrent_regularizer` |     |
| `unit_forget_bias` |     |
| `units` |     |
| `use_bias` |     |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/lstm.py#L690-L692)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/lstm.py#L529-L580)

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