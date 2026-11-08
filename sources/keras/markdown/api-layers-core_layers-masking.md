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
 / [Core layers](https://keras.io/api/layers/core_layers/)
 / Masking layer

Masking layer
=============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/masking.py#L8)

### `Masking` class

Copied!

`keras.layers.Masking(mask_value=0.0, **kwargs)`

Masks a sequence by using a mask value to skip timesteps.

For each timestep in the input tensor (dimension #1 in the tensor), if all values in the input tensor at that timestep are equal to `mask_value`, then the timestep will be masked (skipped) in all downstream layers (as long as they support masking).

If any downstream layer does not support masking yet receives such an input mask, an exception will be raised.

**Example**

Consider a NumPy data array `x` of shape `(samples, timesteps, features)`, to be fed to an LSTM layer. You want to mask timestep #3 and #5 because you lack data for these timesteps. You can:

*   Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
*   Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

Copied!

`samples, timesteps, features = 32, 10, 8 inputs = np.random.random([samples, timesteps, features]).astype(np.float32) inputs[:, 3, :] = 0. inputs[:, 5, :] = 0.  model = keras.models.Sequential() model.add(keras.layers.Masking(mask_value=0.0)) model.add(keras.layers.LSTM(32)) output = model(inputs) # The time step 3 and 5 will be skipped from LSTM calculation.`

Note: in the Keras masking convention, a masked timestep is denoted by a mask value of `False`, while a non-masked (i.e. usable) timestep is denoted by a mask value of `True`.

* * *

[Masking layer](https://keras.io/api/layers/core_layers/masking/#masking-layer)

[`Masking` class](https://keras.io/api/layers/core_layers/masking/#masking-class)