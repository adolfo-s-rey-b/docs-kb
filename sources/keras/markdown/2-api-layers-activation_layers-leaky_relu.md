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
 / LeakyReLU layer

LeakyReLU layer
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/activation/leaky_relu.py#L26)

### `LeakyReLU` class

Copied!

`tf_keras.layers.LeakyReLU(alpha=0.3, **kwargs)`

Leaky version of a Rectified Linear Unit.

It allows a small gradient when the unit is not active:

Copied!

    `f(x) = alpha * x if x < 0     f(x) = x if x >= 0`

Usage:

Copied!

`>>> layer = tf.keras.layers.LeakyReLU() >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [-0.9, -0.3, 0.0, 2.0] >>> layer = tf.keras.layers.LeakyReLU(alpha=0.1) >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [-0.3, -0.1, 0.0, 2.0]`

**Input shape**

Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the batch axis) when using this layer as the first layer in a model.

**Output shape**

Same shape as the input.

**Arguments**

*   **alpha**: Float >= `0.`. Negative slope coefficient. Defaults to `0.3`.

* * *

[LeakyReLU layer](https://keras.io/2/api/layers/activation_layers/leaky_relu/#leakyrelu-layer)

[`LeakyReLU` class](https://keras.io/2/api/layers/activation_layers/leaky_relu/#leakyrelu-class)