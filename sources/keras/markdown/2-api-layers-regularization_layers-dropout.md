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
 / [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 / Dropout layer

Dropout layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/regularization/dropout.py#L29)

### `Dropout` class

Copied!

`tf_keras.layers.Dropout(rate, noise_shape=None, seed=None, **kwargs)`

Applies Dropout to the input.

The Dropout layer randomly sets input units to 0 with a frequency of `rate` at each step during training time, which helps prevent overfitting. Inputs not set to 0 are scaled up by 1/(1 - rate) such that the sum over all inputs is unchanged.

Note that the Dropout layer only applies when `training` is set to True such that no values are dropped during inference. When using `model.fit`, `training` will be appropriately set to True automatically, and in other contexts, you can set the kwarg explicitly to True when calling the layer.

(This is in contrast to setting `trainable=False` for a Dropout layer. `trainable` does not affect the layer's behavior, as Dropout does not have any variables/weights that can be frozen during training.)

Copied!

`>>> tf.random.set_seed(0) >>> layer = tf.keras.layers.Dropout(.2, input_shape=(2,)) >>> data = np.arange(10).reshape(5, 2).astype(np.float32) >>> print(data) [[0. 1.]  [2. 3.]  [4. 5.]  [6. 7.]  [8. 9.]] >>> outputs = layer(data, training=True) >>> print(outputs) tf.Tensor( [[ 0.    1.25]  [ 2.5   3.75]  [ 5.    6.25]  [ 7.5   8.75]  [10.    0.  ]], shape=(5, 2), dtype=float32)`

**Arguments**

*   **rate**: Float between 0 and 1. Fraction of the input units to drop.
*   **noise\_shape**: 1D integer tensor representing the shape of the binary dropout mask that will be multiplied with the input. For instance, if your inputs have shape `(batch_size, timesteps, features)` and you want the dropout mask to be the same for all timesteps, you can use `noise_shape=(batch_size, 1, features)`.
*   **seed**: A Python integer to use as random seed.

**Call arguments**

*   **inputs**: Input tensor (of any rank).
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing).

* * *

[Dropout layer](https://keras.io/2/api/layers/regularization_layers/dropout/#dropout-layer)

[`Dropout` class](https://keras.io/2/api/layers/regularization_layers/dropout/#dropout-class)