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
 / [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 / MaxPooling1D layer

MaxPooling1D layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/max_pooling1d.py#L5)

### `MaxPooling1D` class

Copied!

`keras.layers.MaxPooling1D(     pool_size=2, strides=None, padding="valid", data_format=None, name=None, **kwargs )`

Max pooling operation for 1D temporal data.

Downsamples the input representation by taking the maximum value over a spatial window of size `pool_size`. The window is shifted by `strides`.

The resulting output when using the `"valid"` padding option has a shape of: `output_shape = (input_shape - pool_size + 1) / strides)`.

The resulting output shape when using the `"same"` padding option is: `output_shape = input_shape / strides`

**Arguments**

*   **pool\_size**: int, size of the max pooling window.
*   **strides**: int or None. Specifies how much the pooling window moves for each pooling step. If None, it will default to `pool_size`.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.

**Input shape**

*   If `data_format="channels_last"`: 3D tensor with shape `(batch_size, steps, features)`.
*   If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, steps)`.

**Output shape**

*   If `data_format="channels_last"`: 3D tensor with shape `(batch_size, downsampled_steps, features)`.
*   If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, downsampled_steps)`.

**Examples**

`strides=1` and `padding="valid"`:

Copied!

`>>> x = np.array([1., 2., 3., 4., 5.]) >>> x = np.reshape(x, [1, 5, 1]) >>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2, ...    strides=1, padding="valid") >>> max_pool_1d(x)`

`strides=2` and `padding="valid"`:

Copied!

`>>> x = np.array([1., 2., 3., 4., 5.]) >>> x = np.reshape(x, [1, 5, 1]) >>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2, ...    strides=2, padding="valid") >>> max_pool_1d(x)`

`strides=1` and `padding="same"`:

Copied!

`>>> x = np.array([1., 2., 3., 4., 5.]) >>> x = np.reshape(x, [1, 5, 1]) >>> max_pool_1d = keras.layers.MaxPooling1D(pool_size=2, ...    strides=1, padding="same") >>> max_pool_1d(x)`

**Guides and examples using `MaxPooling1D`**

*   [Speaker Recognition](https://keras.io/examples/audio/speaker_recognition_using_cnn/)
    

* * *

[MaxPooling1D layer](https://keras.io/api/layers/pooling_layers/max_pooling1d/#maxpooling1d-layer)

[`MaxPooling1D` class](https://keras.io/api/layers/pooling_layers/max_pooling1d/#maxpooling1d-class)