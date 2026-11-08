[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#reset_states)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ConvLSTM2D Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#get_initial_state)
        
    *   [inner\_loop](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#inner_loop)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ConvLSTM2D?version=stable#reset_states)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/conv_lstm2d.py#L5-L184)

2D Convolutional LSTM.

Inherits From: [`RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ConvLSTM2D(
        filters,
        kernel_size,
        strides=1,
        padding='valid',
        data_format=None,
        dilation_rate=1,
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
        **kwargs
    )

Similar to an LSTM layer, but the input transformations and recurrent transformations are both convolutional.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filters` | int, the dimension of the output space (the number of filters in the convolution). |
| `kernel_size` | int or tuple/list of 2 integers, specifying the size of the convolution window. |
| `strides` | int or tuple/list of 2 integers, specifying the stride length of the convolution. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. |
| `activation` | Activation function to use. By default hyperbolic tangent activation function is applied (`tanh(x)`). |
| `recurrent_activation` | Activation function to use for the recurrent step. |
| `use_bias` | Boolean, whether the layer uses a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. |
| `bias_initializer` | Initializer for the bias vector. |
| `unit_forget_bias` | Boolean. If `True`, add 1 to the bias of the forget gate at initialization. Use in combination with `bias_initializer="zeros"`. This is recommended in [Jozefowicz et al., 2015](http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf) |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. |
| `bias_regularizer` | Regularizer function applied to the bias vector. |
| `activity_regularizer` | Regularizer function applied to. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. |
| `bias_constraint` | Constraint function applied to the bias vector. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. |
| `seed` | Random seed for dropout. |
| `return_sequences` | Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`. |
| `return_state` | Boolean. Whether to return the last state in addition to the output. Default: `False`. |
| `go_backwards` | Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default False). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch. |
| `unroll` | Boolean (default: `False`). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A 5D tensor. |
| `mask` | Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This is only relevant if `dropout` or `recurrent_dropout` are set. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell. |

#### Input shape:

*   If `data_format='channels_first'`: 5D tensor with shape: `(samples, time, channels, rows, cols)`
*   If `data_format='channels_last'`: 5D tensor with shape: `(samples, time, rows, cols, channels)`

#### Output shape:

*   If `return_state`: a list of tensors. The first tensor is the output. The remaining tensors are the last states, each 4D tensor with shape: `(samples, filters, new_rows, new_cols)` if `data_format='channels_first'` or shape: `(samples, new_rows, new_cols, filters)` if `data_format='channels_last'`. `rows` and `cols` values might have changed due to padding.
*   If `return_sequences`: 5D tensor with shape: `(samples, timesteps, filters, new_rows, new_cols)` if data\_format='channels\_first' or shape: `(samples, timesteps, new_rows, new_cols, filters)` if `data_format='channels_last'`.
*   Else, 4D tensor with shape: `(samples, filters, new_rows, new_cols)` if `data_format='channels_first'` or shape: `(samples, new_rows, new_cols, filters)` if `data_format='channels_last'`.

#### References:

*   [Shi et al., 2015](http://arxiv.org/abs/1506.04214v1)
     (the current implementation does not include the feedback loop on the cells output).

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `activation` |     |
| `bias_constraint` |     |
| `bias_initializer` |     |
| `bias_regularizer` |     |
| `data_format` |     |
| `dilation_rate` |     |
| `dropout` |     |
| `filters` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `kernel_constraint` |     |
| `kernel_initializer` |     |
| `kernel_regularizer` |     |
| `kernel_size` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `padding` |     |
| `recurrent_activation` |     |
| `recurrent_constraint` |     |
| `recurrent_dropout` |     |
| `recurrent_initializer` |     |
| `recurrent_regularizer` |     |
| `strides` |     |
| `unit_forget_bias` |     |
| `use_bias` |     |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/conv_lstm.py#L701-L703)

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