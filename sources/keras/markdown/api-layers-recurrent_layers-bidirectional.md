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
 / Bidirectional layer

Bidirectional layer
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/bidirectional.py#L13)

### `Bidirectional` class

Copied!

`keras.layers.Bidirectional(     layer, merge_mode="concat", weights=None, backward_layer=None, **kwargs )`

Bidirectional wrapper for RNNs.

**Arguments**

*   **layer**: [`keras.layers.RNN`](https://keras.io/api/layers/recurrent_layers/rnn#rnn-class)
     instance, such as [`keras.layers.LSTM`](https://keras.io/api/layers/recurrent_layers/lstm#lstm-class)
     or [`keras.layers.GRU`](https://keras.io/api/layers/recurrent_layers/gru#gru-class)
    . It could also be a `keras.layers.Layer` instance that meets the following criteria:
    1.  Be a sequence-processing layer (accepts 3D+ inputs).
    2.  Have a `go_backwards`, `return_sequences` and `return_state` attribute (with the same semantics as for the `RNN` class).
    3.  Have an `input_spec` attribute.
    4.  Implement serialization via `get_config()` and `from_config()`. Note that the recommended way to create new RNN layers is to write a custom RNN cell and use it with [`keras.layers.RNN`](https://keras.io/api/layers/recurrent_layers/rnn#rnn-class)
        , instead of subclassing `keras.layers.Layer` directly. When `return_sequences` is `True`, the output of the masked timestep will be zero regardless of the layer's original `zero_output_for_mask` value.
*   **merge\_mode**: Mode by which outputs of the forward and backward RNNs will be combined. One of `{"sum", "mul", "concat", "ave", None}`. If `None`, the outputs will not be combined, they will be returned as a list. Defaults to `"concat"`.
*   **backward\_layer**: Optional [`keras.layers.RNN`](https://keras.io/api/layers/recurrent_layers/rnn#rnn-class)
    , or `keras.layers.Layer` instance to be used to handle backwards input processing. If `backward_layer` is not provided, the layer instance passed as the `layer` argument will be used to generate the backward layer automatically. Note that the provided `backward_layer` layer should have properties matching those of the `layer` argument, in particular it should have the same values for `stateful`, `return_states`, `return_sequences`, etc. In addition, `backward_layer` and `layer` should have different `go_backwards` argument values. A `ValueError` will be raised if these requirements are not met.

**Call arguments**

The call arguments for this layer are the same as those of the wrapped RNN layer. Beware that when passing the `initial_state` argument during the call of this layer, the first half in the list of elements in the `initial_state` list will be passed to the forward RNN call and the last half in the list of elements will be passed to the backward RNN call.

Note: instantiating a `Bidirectional` layer from an existing RNN layer instance will not reuse the weights state of the RNN layer instance – the `Bidirectional` layer will have freshly initialized weights.

**Examples**

Copied!

`model = Sequential([     Input(shape=(5, 10)),     Bidirectional(LSTM(10, return_sequences=True),     Bidirectional(LSTM(10)),     Dense(5, activation="softmax"), ]) model.compile(loss='categorical_crossentropy', optimizer='rmsprop')  # With custom backward layer forward_layer = LSTM(10, return_sequences=True) backward_layer = LSTM(10, activation='relu', return_sequences=True,                       go_backwards=True) model = Sequential([     Input(shape=(5, 10)),     Bidirectional(forward_layer, backward_layer=backward_layer),     Dense(5, activation="softmax"), ]) model.compile(loss='categorical_crossentropy', optimizer='rmsprop')`

* * *

[Bidirectional layer](https://keras.io/api/layers/recurrent_layers/bidirectional/#bidirectional-layer)

[`Bidirectional` class](https://keras.io/api/layers/recurrent_layers/bidirectional/#bidirectional-class)