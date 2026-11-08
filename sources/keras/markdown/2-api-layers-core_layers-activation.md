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
 / [Core layers](https://keras.io/2/api/layers/core_layers/)
 / Activation layer

Activation layer
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/core/activation.py#L25)

### `Activation` class

Copied!

`tf_keras.layers.Activation(activation, **kwargs)`

Applies an activation function to an output.

**Arguments**

*   **activation**: Activation function, such as [`tf.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
    , or string name of built-in activation function, such as "relu".

Usage:

Copied!

`>>> layer = tf.keras.layers.Activation('relu') >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [0.0, 0.0, 0.0, 2.0] >>> layer = tf.keras.layers.Activation(tf.nn.relu) >>> output = layer([-3.0, -1.0, 0.0, 2.0]) >>> list(output.numpy()) [0.0, 0.0, 0.0, 2.0]`

**Input shape**

Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the batch axis) when using this layer as the first layer in a model.

**Output shape**

Same shape as input.

* * *

[Activation layer](https://keras.io/2/api/layers/core_layers/activation/#activation-layer)

[`Activation` class](https://keras.io/2/api/layers/core_layers/activation/#activation-class)