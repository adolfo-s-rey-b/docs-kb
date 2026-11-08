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
 / Softmax layer

Softmax layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/activation/softmax.py#L48)

### `Softmax` class

Copied!

`tf_keras.layers.Softmax(axis=-1, **kwargs)`

Softmax activation function.

Example without mask:

Copied!

`>>> inp = np.asarray([[1., 2., 1.]]) >>> layer = tf.keras.layers.Softmax() >>> layer(inp).numpy() array([[0.21194157, 0.5761169 , 0.21194157]], dtype=float32) >>> mask = np.asarray([[True, False, True]], dtype=bool) >>> layer(inp, mask).numpy() array([[0.5, 0. , 0.5]], dtype=float32)`

**Input shape**

Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the samples axis) when using this layer as the first layer in a model.

**Output shape**

Same shape as the input.

**Arguments**

*   **axis**: Integer, or list of Integers, axis along which the softmax normalization is applied.

**Call arguments**

*   **inputs**: The inputs, or logits to the softmax layer.
*   **mask**: A boolean mask of the same shape as `inputs`. The mask specifies 1 to keep and 0 to mask. Defaults to `None`.

**Returns**

Softmaxed output with the same shape as `inputs`.

* * *

[Softmax layer](https://keras.io/2/api/layers/activation_layers/softmax/#softmax-layer)

[`Softmax` class](https://keras.io/2/api/layers/activation_layers/softmax/#softmax-class)