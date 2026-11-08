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
 / Base RNN layer

Base RNN layer
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/rnn.py#L12)

### `RNN` class

Copied!

`keras.layers.RNN(     cell,     return_sequences=False,     return_state=False,     go_backwards=False,     stateful=False,     unroll=False,     zero_output_for_mask=False,     **kwargs )`

Base class for recurrent layers.

**Arguments**

*   **cell**: A RNN cell instance or a list of RNN cell instances. A RNN cell is a class that has:
    *   A `call(input_at_t, states_at_t)` method, returning `(output_at_t, states_at_t_plus_1)`. The call method of the cell can also take the optional argument `constants`, see section "Note on passing external constants" below.
    *   A `state_size` attribute. This can be a single integer (single state) in which case it is the size of the recurrent state. This can also be a list/tuple of integers (one size per state).
    *   A `output_size` attribute, a single integer.
    *   A `get_initial_state(batch_size=None)` method that creates a tensor meant to be fed to `call()` as the initial state, if the user didn't specify any initial state via other means. The returned initial state should have shape `(batch_size, cell.state_size)`. The cell might choose to create a tensor full of zeros, or other values based on the cell's implementation. `inputs` is the input tensor to the RNN layer, with shape `(batch_size, timesteps, features)`. If this method is not implemented by the cell, the RNN layer will create a zero filled tensor with shape `(batch_size, cell.state_size)`. In the case that `cell` is a list of RNN cell instances, the cells will be stacked on top of each other in the RNN, resulting in an efficient stacked RNN.
*   **return\_sequences**: Boolean (default `False`). Whether to return the last output in the output sequence, or the full sequence.
*   **return\_state**: Boolean (default `False`). Whether to return the last state in addition to the output.
*   **go\_backwards**: Boolean (default `False`). If `True`, process the input sequence backwards and return the reversed sequence.
*   **stateful**: Boolean (default `False`). If True, the last state for each sample at index `i` in a batch will be used as initial state for the sample of index `i` in the following batch.
*   **unroll**: Boolean (default `False`). If True, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.
*   **zero\_output\_for\_mask**: Boolean (default `False`). Whether the output should use zeros for the masked timesteps. Note that this field is only used when `return_sequences` is `True` and `mask` is provided. It can useful if you want to reuse the raw output sequence of the RNN without interference from the masked timesteps, e.g., merging bidirectional RNNs.

**Call arguments**

*   **sequences**: A 3-D tensor with shape `(batch_size, timesteps, features)`.
*   **initial\_state**: List of initial state tensors to be passed to the first call of the cell.
*   **mask**: Binary tensor of shape `[batch_size, timesteps]` indicating whether a given timestep should be masked. An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored.
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is for use with cells that use dropout.

**Output shape**

*   If `return_state`: a list of tensors. The first tensor is the output. The remaining tensors are the last states, each with shape `(batch_size, state_size)`, where `state_size` could be a high dimension tensor shape.
*   If `return_sequences`: 3D tensor with shape `(batch_size, timesteps, output_size)`.

Masking:

This layer supports masking for input data with a variable number of timesteps. To introduce masks to your data, use a [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 layer with the `mask_zero` parameter set to `True`.

Note on using statefulness in RNNs:

You can set RNN layers to be 'stateful', which means that the states computed for the samples in one batch will be reused as initial states for the samples in the next batch. This assumes a one-to-one mapping between samples in different successive batches.

To enable statefulness:

*   Specify `stateful=True` in the layer constructor.
*   Specify a fixed batch size for your model, by passing `batch_size=...` to the `Input` layer(s) of your model. Remember to also specify the same `batch_size=...` when calling `fit()`, or otherwise use a generator-like data source like a [`keras.utils.PyDataset`](https://keras.io/api/utils/preprocessing_utils#pydataset-class)
     or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    .
*   Specify `shuffle=False` when calling `fit()`, since your batches are expected to be temporally ordered.

To reset the states of your model, call `.reset_state()` on either a specific layer, or on your entire model.

Note on specifying the initial state of RNNs:

You can specify the initial state of RNN layers symbolically by calling them with the keyword argument `initial_state`. The value of `initial_state` should be a tensor or list of tensors representing the initial state of the RNN layer.

You can specify the initial state of RNN layers numerically by calling `reset_state()` with the keyword argument `states`. The value of `states` should be a numpy array or list of numpy arrays representing the initial state of the RNN layer.

**Examples**

Copied!

`from keras.layers import RNN from keras import ops  # First, let's define a RNN Cell, as a layer subclass. class MinimalRNNCell(keras.Layer):      def __init__(self, units, **kwargs):         super().__init__(**kwargs)         self.units = units         self.state_size = units      def build(self, input_shape):         self.kernel = self.add_weight(shape=(input_shape[-1], self.units),                                       initializer='uniform',                                       name='kernel')         self.recurrent_kernel = self.add_weight(             shape=(self.units, self.units),             initializer='uniform',             name='recurrent_kernel')      def call(self, inputs, states):         prev_output = states[0]         h = ops.matmul(inputs, self.kernel)         output = h + ops.matmul(prev_output, self.recurrent_kernel)         return output, [output]  # Let's use this cell in a RNN layer:  cell = MinimalRNNCell(32) x = keras.Input((None, 5)) layer = RNN(cell) y = layer(x)  # Here's how to use the cell to build a stacked RNN:  cells = [MinimalRNNCell(32), MinimalRNNCell(64)] x = keras.Input((None, 5)) layer = RNN(cells) y = layer(x)`

* * *

[Base RNN layer](https://keras.io/api/layers/recurrent_layers/rnn/#base-rnn-layer)

[`RNN` class](https://keras.io/api/layers/recurrent_layers/rnn/#rnn-class)