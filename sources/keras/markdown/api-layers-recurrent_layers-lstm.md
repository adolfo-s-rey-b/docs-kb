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
 / LSTM layer

LSTM layer
==========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/lstm.py#L331)

### `LSTM` class

Copied!

`keras.layers.LSTM(     units,     activation="tanh",     recurrent_activation="sigmoid",     use_bias=True,     kernel_initializer="glorot_uniform",     recurrent_initializer="orthogonal",     bias_initializer="zeros",     unit_forget_bias=True,     kernel_regularizer=None,     recurrent_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     recurrent_constraint=None,     bias_constraint=None,     dropout=0.0,     recurrent_dropout=0.0,     seed=None,     return_sequences=False,     return_state=False,     go_backwards=False,     stateful=False,     unroll=False,     use_cudnn="auto",     **kwargs )`

Long Short-Term Memory layer - Hochreiter 1997.

Based on available runtime hardware and constraints, this layer will choose different implementations (cuDNN-based or backend-native) to maximize the performance. If a GPU is available and all the arguments to the layer meet the requirement of the cuDNN kernel (see below for details), the layer will use a fast cuDNN implementation when using the TensorFlow backend. The requirements to use the cuDNN implementation are:

1.  `activation` == `tanh`
2.  `recurrent_activation` == `sigmoid`
3.  `recurrent_dropout` == 0
4.  `unroll` is `False`
5.  `use_bias` is `True`
6.  Inputs, if use masking, are strictly right-padded.
7.  Eager execution is enabled in the outermost context.

For example:

Copied!

`>>> inputs = np.random.random((32, 10, 8)) >>> lstm = keras.layers.LSTM(4) >>> output = lstm(inputs) >>> output.shape (32, 4) >>> lstm = keras.layers.LSTM( ...     4, return_sequences=True, return_state=True) >>> whole_seq_output, final_memory_state, final_carry_state = lstm(inputs) >>> whole_seq_output.shape (32, 10, 4) >>> final_memory_state.shape (32, 4) >>> final_carry_state.shape (32, 4)`

**Arguments**

*   **units**: Positive integer, dimensionality of the output space.
*   **activation**: Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **recurrent\_activation**: Activation function to use for the recurrent step. Default: sigmoid (`sigmoid`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **use\_bias**: Boolean, (default `True`), whether the layer should use a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`.
*   **recurrent\_initializer**: Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`.
*   **bias\_initializer**: Initializer for the bias vector. Default: `"zeros"`.
*   **unit\_forget\_bias**: Boolean (default `True`). If `True`, add 1 to the bias of the forget gate at initialization. Setting it to `True` will also force `bias_initializer="zeros"`. This is recommended in [Jozefowicz et al.](https://github.com/mlresearch/v37/blob/gh-pages/jozefowicz15.pdf)
    
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_regularizer**: Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_regularizer**: Regularizer function applied to the bias vector. Default: `None`.
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation"). Default: `None`.
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_constraint**: Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_constraint**: Constraint function applied to the bias vector. Default: `None`.
*   **dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0.
*   **recurrent\_dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0.
*   **seed**: Random seed for dropout.
*   **return\_sequences**: Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`.
*   **return\_state**: Boolean. Whether to return the last state in addition to the output. Default: `False`.
*   **go\_backwards**: Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence.
*   **stateful**: Boolean (default: `False`). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch.
*   **unroll**: Boolean (default False). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.
*   **use\_cudnn**: Whether to use a cuDNN-backed implementation. `"auto"` will attempt to use cuDNN when feasible, and will fallback to the default implementation if not.

**Call arguments**

*   **inputs**: A 3D tensor, with shape `(batch, timesteps, feature)`.
*   **mask**: Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked (optional). An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. Defaults to `None`.
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used (optional). Defaults to `None`.
*   **initial\_state**: List of initial state tensors to be passed to the first call of the cell (optional, `None` causes creation of zero-filled initial state tensors). Defaults to `None`.

* * *

[LSTM layer](https://keras.io/api/layers/recurrent_layers/lstm/#lstm-layer)

[`LSTM` class](https://keras.io/api/layers/recurrent_layers/lstm/#lstm-class)