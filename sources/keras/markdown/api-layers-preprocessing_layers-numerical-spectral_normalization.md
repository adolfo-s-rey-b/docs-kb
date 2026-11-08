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
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Numerical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/numerical/)
 / Spectral Normalization layer

Spectral Normalization layer
============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/spectral_normalization.py#L9)

### `SpectralNormalization` class

Copied!

`keras.layers.SpectralNormalization(layer, power_iterations=1, **kwargs)`

Performs spectral normalization on the weights of a target layer.

This wrapper controls the Lipschitz constant of the weights of a layer by constraining their spectral norm, which can stabilize the training of GANs.

**Arguments**

*   **layer**: A `keras.layers.Layer` instance that has either a `kernel` (e.g. `Conv2D`, `Dense`...) or an `embeddings` attribute (`Embedding` layer).
*   **power\_iterations**: int, the number of iterations during normalization.
*   **\*\*kwargs**: Base wrapper keyword arguments.

**Examples**

Wrap [`keras.layers.Conv2D`](https://keras.io/api/layers/convolution_layers/convolution2d#conv2d-class)
:

Copied!

`>>> x = np.random.rand(1, 10, 10, 1) >>> conv2d = SpectralNormalization(keras.layers.Conv2D(2, 2)) >>> y = conv2d(x) >>> y.shape (1, 9, 9, 2)`

Wrap [`keras.layers.Dense`](https://keras.io/api/layers/core_layers/dense#dense-class)
:

Copied!

`>>> x = np.random.rand(1, 10, 10, 1) >>> dense = SpectralNormalization(keras.layers.Dense(10)) >>> y = dense(x) >>> y.shape (1, 10, 10, 10)`

**Reference**

*   [Spectral Normalization for GAN](https://arxiv.org/abs/1802.05957)
    .

* * *

[Spectral Normalization layer](https://keras.io/api/layers/preprocessing_layers/numerical/spectral_normalization/#spectral-normalization-layer)

[`SpectralNormalization` class](https://keras.io/api/layers/preprocessing_layers/numerical/spectral_normalization/#spectralnormalization-class)