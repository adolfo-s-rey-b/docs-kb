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
 / [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 / RMSNormalization layer

RMSNormalization layer
======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/rms_normalization.py#L6)

### `RMSNormalization` class

Copied!

`keras.layers.RMSNormalization(axis=-1, epsilon=1e-06, **kwargs)`

Root Mean Square (RMS) Normalization layer.

This layer normalizes the input tensor based on its RMS value.

The Keras layer performs the operation as described in [Root Mean Square Layer Normalization](https://arxiv.org/pdf/1910.07467)
 by Biao Zhang et al.

If `scale` is enabled, the layer will scale the normalized outputs via a learnable scaling factor.

So, with scaling enabled, the normalization equations are as follows:

Let the intermediate activations for a mini-batch to be the `inputs`.

Copied!

`rms_normalization(x) = x * rsqrt(mean(square(x))) * scale`

For example:

Copied!

`>>> layer = keras.layers.RMSNormalization() >>> layer.build([5, 20, 30, 10]) >>> print(layer.scale.shape) (10,) >>> layer(np.random.rand(1, 10)).numpy() array([[0.35098287, 1.0495652 , 1.4645109 , 1.2944688 , 0.31124955,         1.2768592 , 1.184331  , 0.17474432, 0.49955517, 1.2428929 ]],     dtype=float32)`

**Arguments**

*   **axis**: int. The axis on which to perform the normalization.
*   **epsilon**: float. A small number to add to avoid division by zero.

* * *

[RMSNormalization layer](https://keras.io/api/layers/normalization_layers/rms_normalization/#rmsnormalization-layer)

[`RMSNormalization` class](https://keras.io/api/layers/normalization_layers/rms_normalization/#rmsnormalization-class)