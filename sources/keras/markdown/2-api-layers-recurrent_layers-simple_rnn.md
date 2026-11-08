None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Layers API](https://keras.io/2/api/layers/)
 / [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 / SimpleRNN layer

SimpleRNN layer
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/rnn/simple_rnn.py#L253)

### `SimpleRNN` class

Copied!

`tf_keras.layers.SimpleRNN(     units,     activation="tanh",     use_bias=True,     kernel_initializer="glorot_uniform",     recurrent_initializer="orthogonal",     bias_initializer="zeros",     kernel_regularizer=None,     recurrent_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     recurrent_constraint=None,     bias_constraint=None,     dropout=0.0,     recurrent_dropout=0.0,     return_sequences=False,     return_state=False,     go_backwards=False,     stateful=False,     unroll=False,     **kwargs )`

Fully-connected RNN where the output is to be fed back to input.

See [the TF-Keras RNN API guide](https://keras.io/guides/working_with_rnns)
 for details about the usage of RNN API.

**Arguments**

*   **units**: Positive integer, dimensionality of the output space.
*   **activation**: Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass None, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **use\_bias**: Boolean, (default `True`), whether the layer uses a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `glorot_uniform`.
*   **recurrent\_initializer**: Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `orthogonal`.
*   **bias\_initializer**: Initializer for the bias vector. Default: `zeros`.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_regularizer**: Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_regularizer**: Regularizer function applied to the bias vector. Default: `None`.
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation"). Default: `None`.
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix. Default: `None`.
*   **recurrent\_constraint**: Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`.
*   **bias\_constraint**: Constraint function applied to the bias vector. Default: `None`.
*   **dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0.
*   **recurrent\_dropout**: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0.
*   **return\_sequences**: Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`.
*   **return\_state**: Boolean. Whether to return the last state in addition to the output. Default: `False`
*   **go\_backwards**: Boolean (default False). If True, process the input sequence backwards and return the reversed sequence.
*   **stateful**: Boolean (default False). If True, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch.
*   **unroll**: Boolean (default False). If True, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.

**Call arguments**

*   **inputs**: A 3D tensor, with shape `[batch, timesteps, feature]`.
*   **mask**: Binary tensor of shape `[batch, timesteps]` indicating whether a given timestep should be masked. An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored.
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used.
*   **initial\_state**: List of initial state tensors to be passed to the first call of the cell.

**Examples**

Copied!

``inputs = np.random.random([32, 10, 8]).astype(np.float32) simple_rnn = tf.keras.layers.SimpleRNN(4)  output = simple_rnn(inputs)  # The output has shape `[32, 4]`.  simple_rnn = tf.keras.layers.SimpleRNN(     4, return_sequences=True, return_state=True)  # whole_sequence_output has shape `[32, 10, 4]`. # final_state has shape `[32, 4]`. whole_sequence_output, final_state = simple_rnn(inputs)``

* * *

[SimpleRNN layer](https://keras.io/2/api/layers/recurrent_layers/simple_rnn/#simplernn-layer)

[`SimpleRNN` class](https://keras.io/2/api/layers/recurrent_layers/simple_rnn/#simplernn-class)