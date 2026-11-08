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
 / Simple RNN cell layer

Simple RNN cell layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/simple_rnn.py#L14)

### `SimpleRNNCell` class

Copied!

`keras.layers.SimpleRNNCell(     units,     activation="tanh",     use_bias=True,     kernel_initializer="glorot_uniform",     recurrent_initializer="orthogonal",     bias_initializer="zeros",     kernel_regularizer=None,     recurrent_regularizer=None,     bias_regularizer=None,     kernel_constraint=None,     recurrent_constraint=None,     bias_constraint=None,     dropout=0.0,     recurrent_dropout=0.0,     seed=None,     **kwargs )`

Cell class for SimpleRNN.

This class processes one step within the whole time sequence input, whereas `keras.layer.SimpleRNN` processes the whole sequence.

**Arguments**

*   **units**: Positive integer, dimensionality of the output space.
*   **activation**: Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **use\_bias**: Boolean, (default `True`), whether the layer should use a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`.
*   **recurrent\_initializer**: Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`.
*   **bias\_initializer**: Initializer for the bias vector. Default: `"zeros"`.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_regularizer**: Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_regularizer**: Regularizer function applied to the bias vector. Default: `None`.
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_constraint**: Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_constraint**: Constraint function applied to the bias vector. Default: `None`.
*   **dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0.
*   **recurrent\_dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0.
*   **seed**: Random seed for dropout.

**Call arguments**

*   **sequence**: A 2D tensor, with shape `(batch, features)`.
*   **states**: A 2D tensor with shape `(batch, units)`, which is the state from the previous time step.
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. Only relevant when `dropout` or `recurrent_dropout` is used.

**Example**

Copied!

``inputs = np.random.random([32, 10, 8]).astype(np.float32) rnn = keras.layers.RNN(keras.layers.SimpleRNNCell(4)) output = rnn(inputs)  # The output has shape `(32, 4)`. rnn = keras.layers.RNN(     keras.layers.SimpleRNNCell(4),     return_sequences=True,     return_state=True ) # whole_sequence_output has shape `(32, 10, 4)`. # final_state has shape `(32, 4)`. whole_sequence_output, final_state = rnn(inputs)``

* * *

[Simple RNN cell layer](https://keras.io/api/layers/recurrent_layers/simple_rnn_cell/#simple-rnn-cell-layer)

[`SimpleRNNCell` class](https://keras.io/api/layers/recurrent_layers/simple_rnn_cell/#simplernncell-class)