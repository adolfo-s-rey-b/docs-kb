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
 / Masking layer

Masking layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/core/masking.py#L26)

### `Masking` class

Copied!

`tf_keras.layers.Masking(mask_value=0.0, **kwargs)`

Masks a sequence by using a mask value to skip timesteps.

For each timestep in the input tensor (dimension #1 in the tensor), if all values in the input tensor at that timestep are equal to `mask_value`, then the timestep will be masked (skipped) in all downstream layers (as long as they support masking).

If any downstream layer does not support masking yet receives such an input mask, an exception will be raised.

**Example**

Consider a Numpy data array `x` of shape `(samples, timesteps, features)`, to be fed to an LSTM layer. You want to mask timestep #3 and #5 because you lack data for these timesteps. You can:

*   Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
*   Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

Copied!

`samples, timesteps, features = 32, 10, 8 inputs = np.random.random([samples, timesteps, features]).astype(np.float32) inputs[:, 3, :] = 0. inputs[:, 5, :] = 0.  model = tf.keras.models.Sequential() model.add(tf.keras.layers.Masking(mask_value=0.,                                   input_shape=(timesteps, features))) model.add(tf.keras.layers.LSTM(32))  output = model(inputs) # The time step 3 and 5 will be skipped from LSTM calculation.`

See [the masking and padding guide](https://keras.io/guides/understanding_masking_and_padding)
 for more details.

* * *

[Masking layer](https://keras.io/2/api/layers/core_layers/masking/#masking-layer)

[`Masking` class](https://keras.io/2/api/layers/core_layers/masking/#masking-class)