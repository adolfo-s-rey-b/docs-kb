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
 / ZeroPadding1D layer

ZeroPadding1D layer
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/zero_padding1d.py#L9)

### `ZeroPadding1D` class

Copied!

`keras.layers.ZeroPadding1D(padding=1, data_format=None, **kwargs)`

Zero-padding layer for 1D input (e.g. temporal sequence).

**Example**

Copied!

`>>> input_shape = (2, 2, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> x [[[ 0  1  2]   [ 3  4  5]]  [[ 6  7  8]   [ 9 10 11]]] >>> y = keras.layers.ZeroPadding1D(padding=2)(x) >>> y [[[ 0  0  0]   [ 0  0  0]   [ 0  1  2]   [ 3  4  5]   [ 0  0  0]   [ 0  0  0]]  [[ 0  0  0]   [ 0  0  0]   [ 6  7  8]   [ 9 10 11]   [ 0  0  0]   [ 0  0  0]]]`

**Arguments**

*   **padding**: Int, or tuple of int (length 2), or dictionary.
    *   If int: how many zeros to add at the beginning and end of the padding dimension (axis 1).
    *   If tuple of 2 ints: how many zeros to add at the beginning and the end of the padding dimension (`(left_pad, right_pad)`).
*   **data\_format**: A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, axis_to_pad, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, axis_to_pad)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`.

**Input shape**

3D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, axis_to_pad, features)` - If `data_format` is `"channels_first"`: `(batch_size, features, axis_to_pad)`

**Output shape**

3D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, padded_axis, features)` - If `data_format` is `"channels_first"`: `(batch_size, features, padded_axis)`

* * *

[ZeroPadding1D layer](https://keras.io/api/layers/reshaping_layers/zero_padding1d/#zeropadding1d-layer)

[`ZeroPadding1D` class](https://keras.io/api/layers/reshaping_layers/zero_padding1d/#zeropadding1d-class)