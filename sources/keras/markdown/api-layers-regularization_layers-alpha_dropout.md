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
 / [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 / AlphaDropout layer

AlphaDropout layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/regularization/alpha_dropout.py#L7)

### `AlphaDropout` class

Copied!

`keras.layers.AlphaDropout(rate, noise_shape=None, seed=None, **kwargs)`

Applies Alpha Dropout to the input.

Alpha Dropout is a `Dropout` that keeps mean and variance of inputs to their original values, in order to ensure the self-normalizing property even after this dropout. Alpha Dropout fits well to Scaled Exponential Linear Units (SELU) by randomly setting activations to the negative saturation value.

**Arguments**

*   **rate**: Float between 0 and 1. The multiplicative noise will have standard deviation `sqrt(rate / (1 - rate))`.
*   **noise\_shape**: 1D integer tensor representing the shape of the binary alpha dropout mask that will be multiplied with the input. For instance, if your inputs have shape `(batch_size, timesteps, features)` and you want the alpha dropout mask to be the same for all timesteps, you can use `noise_shape=(batch_size, 1, features)`.
*   **seed**: A Python integer to use as random seed.

**Call arguments**

*   **inputs**: Input tensor (of any rank).
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding alpha dropout) or in inference mode (doing nothing).

* * *

[AlphaDropout layer](https://keras.io/api/layers/regularization_layers/alpha_dropout/#alphadropout-layer)

[`AlphaDropout` class](https://keras.io/api/layers/regularization_layers/alpha_dropout/#alphadropout-class)