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
 / [Activation layers](https://keras.io/api/layers/activation_layers/)
 / Softmax layer

Softmax layer
=============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/softmax.py#L14)

### `Softmax` class

Copied!

`keras.layers.Softmax(axis=-1, **kwargs)`

Softmax activation layer.

Formula:

Copied!

`exp_x = exp(x - max(x)) f(x) = exp_x / sum(exp_x)`

**Example**

Copied!

`>>> softmax_layer = keras.layers.Softmax() >>> input = np.array([1.0, 2.0, 1.0]) >>> result = softmax_layer(input) >>> result [0.21194157, 0.5761169, 0.21194157]`

**Arguments**

*   **axis**: Integer, or list of Integers, axis along which the softmax normalization is applied.
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.

**Call arguments**

*   **inputs**: The inputs (logits) to the softmax layer.
*   **mask**: A boolean mask that is broadcastable to `inputs`. The mask specifies 1 to keep and 0 to mask. Each dimension of the mask must either be 1 or match the corresponding dimension of `inputs`; it must not be larger. Defaults to `None`.

**Returns**

Softmaxed output with the same shape as `inputs`.

* * *

[Softmax layer](https://keras.io/api/layers/activation_layers/softmax/#softmax-layer)

[`Softmax` class](https://keras.io/api/layers/activation_layers/softmax/#softmax-class)