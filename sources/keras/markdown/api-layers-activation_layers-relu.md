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
 / ReLU layer

ReLU layer
==========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/relu.py#L6)

### `ReLU` class

Copied!

`keras.layers.ReLU(max_value=None, negative_slope=0.0, threshold=0.0, **kwargs)`

Rectified Linear Unit activation function layer.

Formula:

Copied!

`f(x) = max(x,0) f(x) = max_value if x >= max_value f(x) = x if threshold <= x < max_value f(x) = negative_slope * (x - threshold) otherwise`

**Example**

Copied!

`relu_layer = keras.layers.ReLU(     max_value=10,     negative_slope=0.5,     threshold=0, ) input = np.array([-10, -5, 0.0, 5, 10]) result = relu_layer(input) # result = [-5. , -2.5,  0. ,  5. , 10.]`

**Arguments**

*   **max\_value**: Float >= 0. Maximum activation value. `None` means unlimited. Defaults to `None`.
*   **negative\_slope**: Float >= 0. Negative slope coefficient. Defaults to `0.0`.
*   **threshold**: Float >= 0. Threshold value for thresholded activation. Defaults to `0.0`.
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.

* * *

[ReLU layer](https://keras.io/api/layers/activation_layers/relu/#relu-layer)

[`ReLU` class](https://keras.io/api/layers/activation_layers/relu/#relu-class)