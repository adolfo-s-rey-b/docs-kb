None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 / ConvLSTM1D layer

ConvLSTM1D layer
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/conv_lstm1d.py#L5)

### `ConvLSTM1D` class

Copied!

`keras.layers.ConvLSTM1D(     filters,     kernel_size,     strides=1,     padding="valid",     data_format=None,     dilation_rate=1,     activation="tanh",     recurrent_activation="sigmoid",     use_bias=True,     kernel_initializer="glorot_uniform",     recurrent_initializer="orthogonal",     bias_initializer="zeros",     unit_forget_bias=True,     kernel_regularizer=None,     recurrent_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     recurrent_constraint=None,     bias_constraint=None,     dropout=0.0,     recurrent_dropout=0.0,     seed=None,     return_sequences=False,     return_state=False,     go_backwards=False,     stateful=False,     **kwargs )`

1D Convolutional LSTM.

Similar to an LSTM layer, but the input transformations and recurrent transformations are both convolutional.

**Arguments**

*   **filters**: int, the dimension of the output space (the number of filters in the convolution).
*   **kernel\_size**: int or tuple/list of 1 integer, specifying the size of the convolution window.
*   **strides**: int or tuple/list of 1 integer, specifying the stride length of the convolution. `strides > 1` is incompatible with `dilation_rate > 1`.
*   **padding**: string, `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dilation\_rate**: int or tuple/list of 1 integers, specifying the dilation rate to use for dilated convolution.
*   **activation**: Activation function to use. By default hyperbolic tangent activation function is applied (`tanh(x)`).
*   **recurrent\_activation**: Activation function to use for the recurrent step.
*   **use\_bias**: Boolean, whether the layer uses a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs.
*   **recurrent\_initializer**: Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state.
*   **bias\_initializer**: Initializer for the bias vector.
*   **unit\_forget\_bias**: Boolean. If `True`, add 1 to the bias of the forget gate at initialization. Use in combination with `bias_initializer="zeros"`. This is recommended in [Jozefowicz et al., 2015](http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
    
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix.
*   **recurrent\_regularizer**: Regularizer function applied to the `recurrent_kernel` weights matrix.
*   **bias\_regularizer**: Regularizer function applied to the bias vector.
*   **activity\_regularizer**: Regularizer function applied to.
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix.
*   **recurrent\_constraint**: Constraint function applied to the `recurrent_kernel` weights matrix.
*   **bias\_constraint**: Constraint function applied to the bias vector.
*   **dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs.
*   **recurrent\_dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state.
*   **seed**: Random seed for dropout.
*   **return\_sequences**: Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`.
*   **return\_state**: Boolean. Whether to return the last state in addition to the output. Default: `False`.
*   **go\_backwards**: Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence.
*   **stateful**: Boolean (default False). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch.
*   **unroll**: Boolean (default: `False`). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.

**Call arguments**

*   **inputs**: A 4D tensor.
*   **initial\_state**: List of initial state tensors to be passed to the first call of the cell.
*   **mask**: Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked.
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. This is only relevant if `dropout` or `recurrent_dropout` are set.

**Input shape**

*   If `data_format="channels_first"`: 4D tensor with shape: `(samples, time, channels, rows)`
*   If `data_format="channels_last"`: 4D tensor with shape: `(samples, time, rows, channels)`

**Output shape**

*   If `return_state`: a list of tensors. The first tensor is the output. The remaining tensors are the last states, each 3D tensor with shape: `(samples, filters, new_rows)` if `data_format='channels_first'` or shape: `(samples, new_rows, filters)` if `data_format='channels_last'`. `rows` values might have changed due to padding.
*   If `return_sequences`: 4D tensor with shape: `(samples, timesteps, filters, new_rows)` if data\_format='channels\_first' or shape: `(samples, timesteps, new_rows, filters)` if `data_format='channels_last'`.
*   Else, 3D tensor with shape: `(samples, filters, new_rows)` if `data_format='channels_first'` or shape: `(samples, new_rows, filters)` if `data_format='channels_last'`.

**References**

*   [Shi et al., 2015](http://arxiv.org/abs/1506.04214v1)
     (the current implementation does not include the feedback loop on the cells output).

* * *

[ConvLSTM1D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm1d/#convlstm1d-layer)

[`ConvLSTM1D` class](https://keras.io/api/layers/recurrent_layers/conv_lstm1d/#convlstm1d-class)