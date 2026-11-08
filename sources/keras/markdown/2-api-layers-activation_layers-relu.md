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
 / [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 / ReLU layer

ReLU layer
==========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/activation/relu.py#L26)

### `ReLU` class

Copied!

`tf_keras.layers.ReLU(max_value=None, negative_slope=0.0, threshold=0.0, **kwargs)`

Rectified Linear Unit activation function.

With default values, it returns element-wise `max(x, 0)`.

Otherwise, it follows:

Copied!

    `f(x) = max_value if x >= max_value     f(x) = x if threshold <= x < max_value     f(x) = negative_slope * (x - threshold) otherwise`

Usage:

Copied!

`>>> layer = tf.keras.layers.ReLU() >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [0.0, 0.0, 0.0, 2.0] >>> layer = tf.keras.layers.ReLU(max_value=1.0) >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [0.0, 0.0, 0.0, 1.0] >>> layer = tf.keras.layers.ReLU(negative_slope=1.0) >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [-3.0, -1.0, 0.0, 2.0] >>> layer = tf.keras.layers.ReLU(threshold=1.5) >>> output = layer([-3.0, -1.0, 1.0, 2.0]) >>> list(output.numpy()) [0.0, 0.0, 0.0, 2.0]`

**Input shape**

Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the batch axis) when using this layer as the first layer in a model.

**Output shape**

Same shape as the input.

**Arguments**

*   **max\_value**: Float >= 0. Maximum activation value. None means unlimited. Defaults to `None`.
*   **negative\_slope**: Float >= 0. Negative slope coefficient. Defaults to `0.`.
*   **threshold**: Float >= 0. Threshold value for thresholded activation. Defaults to `0.`.

* * *

[ReLU layer](https://keras.io/2/api/layers/activation_layers/relu/#relu-layer)

[`ReLU` class](https://keras.io/2/api/layers/activation_layers/relu/#relu-class)