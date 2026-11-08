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
 / [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 / ZeroPadding3D layer

ZeroPadding3D layer
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/zero_padding3d.py#L9)

### `ZeroPadding3D` class

Copied!

`keras.layers.ZeroPadding3D(     padding=((1, 1), (1, 1), (1, 1)), data_format=None, **kwargs )`

Zero-padding layer for 3D data (spatial or spatio-temporal).

**Example**

Copied!

`>>> input_shape = (1, 1, 2, 2, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> y = keras.layers.ZeroPadding3D(padding=2)(x) >>> y.shape (1, 5, 6, 6, 3)`

**Arguments**

*   **padding**: Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
    *   If int: the same symmetric padding is applied to depth, height, and width.
    *   If tuple of 3 ints: interpreted as three different symmetric padding values for depth, height, and width: `(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad)`.
    *   If tuple of 3 tuples of 2 ints: interpreted as `((left_dim1_pad, right_dim1_pad), (left_dim2_pad, right_dim2_pad), (left_dim3_pad, right_dim3_pad))`.
*   **data\_format**: A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`.

**Input shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad, depth)` - If `data_format` is `"channels_first"`: `(batch_size, depth, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad)`

**Output shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, first_padded_axis, second_padded_axis, third_axis_to_pad, depth)` - If `data_format` is `"channels_first"`: `(batch_size, depth, first_padded_axis, second_padded_axis, third_axis_to_pad)`

* * *

[ZeroPadding3D layer](https://keras.io/api/layers/reshaping_layers/zero_padding3d/#zeropadding3d-layer)

[`ZeroPadding3D` class](https://keras.io/api/layers/reshaping_layers/zero_padding3d/#zeropadding3d-class)