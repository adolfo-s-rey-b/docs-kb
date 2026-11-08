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
 / [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 / TimeDistributed layer

TimeDistributed layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/time_distributed.py#L10)

### `TimeDistributed` class

Copied!

`keras.layers.TimeDistributed(layer, **kwargs)`

This wrapper allows to apply a layer to every temporal slice of an input.

Every input should be at least 3D, and the dimension of index one of the first input will be considered to be the temporal dimension.

Consider a batch of 32 video samples, where each sample is a 128x128 RGB image with `channels_last` data format, across 10 timesteps. The batch input shape is `(32, 10, 128, 128, 3)`.

You can then use `TimeDistributed` to apply the same `Conv2D` layer to each of the 10 timesteps, independently:

Copied!

`>>> inputs = layers.Input(shape=(10, 128, 128, 3), batch_size=32) >>> conv_2d_layer = layers.Conv2D(64, (3, 3)) >>> outputs = layers.TimeDistributed(conv_2d_layer)(inputs) >>> outputs.shape (32, 10, 126, 126, 64)`

Because `TimeDistributed` applies the same instance of `Conv2D` to each of the timestamps, the same set of weights are used at each timestamp.

**Arguments**

*   **layer**: a `keras.layers.Layer` instance.

**Call arguments**

*   **inputs**: Input tensor of shape (batch, time, ...) or nested tensors, and each of which has shape (batch, time, ...).
*   **training**: Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the wrapped layer (only if the layer supports this argument).
*   **mask**: Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked. This argument is passed to the wrapped layer (only if the layer supports this argument).

* * *

[TimeDistributed layer](https://keras.io/api/layers/recurrent_layers/time_distributed/#timedistributed-layer)

[`TimeDistributed` class](https://keras.io/api/layers/recurrent_layers/time_distributed/#timedistributed-class)