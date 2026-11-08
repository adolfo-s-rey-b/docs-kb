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
 / AveragePooling2D layer

AveragePooling2D layer
======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/average_pooling2d.py#L5)

### `AveragePooling2D` class

Copied!

`keras.layers.AveragePooling2D(     pool_size, strides=None, padding="valid", data_format=None, name=None, **kwargs )`

Average pooling operation for 2D spatial data.

Downsamples the input along its spatial dimensions (height and width) by taking the average value over an input window (of size defined by `pool_size`) for each channel of the input. The window is shifted by `strides` along each dimension.

The resulting output when using the `"valid"` padding option has a spatial shape (number of rows or columns) of: `output_shape = math.floor((input_shape - pool_size) / strides) + 1` (when `input_shape >= pool_size`)

The resulting output shape when using the `"same"` padding option is: `output_shape = input_shape`

**Arguments**

*   **pool\_size**: int or tuple of 2 integers, factors by which to downscale (dim1, dim2). If only one integer is specified, the same window length will be used for all dimensions.
*   **strides**: int or tuple of 2 integers, or None. Strides values. If None, it will default to `pool_size`. If only one int is specified, the same stride size will be used for all dimensions.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.

**Input shape**

*   If `data_format="channels_last"`: 4D tensor with shape `(batch_size, height, width, channels)`.
*   If `data_format="channels_first"`: 4D tensor with shape `(batch_size, channels, height, width)`.

**Output shape**

*   If `data_format="channels_last"`: 4D tensor with shape `(batch_size, pooled_height, pooled_width, channels)`.
*   If `data_format="channels_first"`: 4D tensor with shape `(batch_size, channels, pooled_height, pooled_width)`.

**Examples**

`strides=(1, 1)` and `padding="valid"`:

Copied!

`>>> x = np.array([[1., 2., 3.], ...               [4., 5., 6.], ...               [7., 8., 9.]]) >>> x = np.reshape(x, [1, 3, 3, 1]) >>> avg_pool_2d = keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(1, 1), padding="valid") >>> avg_pool_2d(x)`

`strides=(2, 2)` and `padding="valid"`:

Copied!

`>>> x = np.array([[1., 2., 3., 4.], ...              [5., 6., 7., 8.], ...              [9., 10., 11., 12.]]) >>> x = np.reshape(x, [1, 3, 4, 1]) >>> avg_pool_2d = keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(2, 2), padding="valid") >>> avg_pool_2d(x)`

`stride=(1, 1)` and `padding="same"`:

Copied!

`>>> x = np.array([[1., 2., 3.], ...                  [4., 5., 6.], ...                  [7., 8., 9.]]) >>> x = np.reshape(x, [1, 3, 3, 1]) >>> avg_pool_2d = keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(1, 1), padding="same") >>> avg_pool_2d(x)`

**Guides and examples using `AveragePooling2D`**

*   [Distributed hyperparameter tuning with KerasTuner](https://keras.io/keras_tuner/guides/distributed_tuning/)
    
*   [Involutional neural networks](https://keras.io/examples/vision/involution/)
    

* * *

[AveragePooling2D layer](https://keras.io/api/layers/pooling_layers/average_pooling2d/#averagepooling2d-layer)

[`AveragePooling2D` class](https://keras.io/api/layers/pooling_layers/average_pooling2d/#averagepooling2d-class)