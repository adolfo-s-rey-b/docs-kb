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
 / [Merging layers](https://keras.io/api/layers/merging_layers/)
 / Concatenate layer

Concatenate layer
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/concatenate.py#L8)

### `Concatenate` class

Copied!

`keras.layers.Concatenate(axis=-1, **kwargs)`

Concatenates a list of inputs.

It takes as input a list of tensors, all of the same shape except for the concatenation axis, and returns a single tensor that is the concatenation of all inputs.

**Examples**

Copied!

`>>> x = np.arange(20).reshape(2, 2, 5) >>> y = np.arange(20, 30).reshape(2, 1, 5) >>> keras.layers.Concatenate(axis=1)([x, y])`

Usage in a Keras model:

Copied!

`>>> x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2)) >>> x2 = keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2)) >>> y = keras.layers.Concatenate()([x1, x2])`

**Arguments**

*   **axis**: Axis along which to concatenate.
*   **\*\*kwargs**: Standard layer keyword arguments.

**Returns**

A tensor, the concatenation of the inputs alongside axis `axis`.

* * *

[Concatenate layer](https://keras.io/api/layers/merging_layers/concatenate/#concatenate-layer)

[`Concatenate` class](https://keras.io/api/layers/merging_layers/concatenate/#concatenate-class)