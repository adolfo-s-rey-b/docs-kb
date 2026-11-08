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
 / MaxPooling3D layer

MaxPooling3D layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/max_pooling3d.py#L5)

### `MaxPooling3D` class

Copied!

`keras.layers.MaxPooling3D(     pool_size=(2, 2, 2),     strides=None,     padding="valid",     data_format=None,     name=None,     **kwargs )`

Max pooling operation for 3D data (spatial or spatio-temporal).

Downsamples the input along its spatial dimensions (depth, height, and width) by taking the maximum value over an input window (of size defined by `pool_size`) for each channel of the input. The window is shifted by `strides` along each dimension.

**Arguments**

*   **pool\_size**: int or tuple of 3 integers, factors by which to downscale (dim1, dim2, dim3). If only one integer is specified, the same window length will be used for all dimensions.
*   **strides**: int or tuple of 3 integers, or None. Strides values. If None, it will default to `pool_size`. If only one int is specified, the same stride size will be used for all dimensions.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.

**Input shape**

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

**Output shape**

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, pooled_dim1, pooled_dim2, pooled_dim3, channels)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, channels, pooled_dim1, pooled_dim2, pooled_dim3)`

**Example**

Copied!

`depth = 30 height = 30 width = 30 channels = 3  inputs = keras.layers.Input(shape=(depth, height, width, channels)) layer = keras.layers.MaxPooling3D(pool_size=3) outputs = layer(inputs)  # Shape: (batch_size, 10, 10, 10, 3)`

* * *

[MaxPooling3D layer](https://keras.io/api/layers/pooling_layers/max_pooling3d/#maxpooling3d-layer)

[`MaxPooling3D` class](https://keras.io/api/layers/pooling_layers/max_pooling3d/#maxpooling3d-class)