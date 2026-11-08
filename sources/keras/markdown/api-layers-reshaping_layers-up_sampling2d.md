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
 / UpSampling2D layer

UpSampling2D layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/up_sampling2d.py#L9)

### `UpSampling2D` class

Copied!

`keras.layers.UpSampling2D(     size=(2, 2), data_format=None, interpolation="nearest", **kwargs )`

Upsampling layer for 2D inputs.

The implementation uses interpolative resizing, given the resize method (specified by the `interpolation` argument). Use `interpolation=nearest` to repeat the rows and columns of the data.

**Example**

Copied!

`>>> input_shape = (2, 2, 1, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> print(x) [[[[ 0  1  2]]   [[ 3  4  5]]]  [[[ 6  7  8]]   [[ 9 10 11]]]] >>> y = keras.layers.UpSampling2D(size=(1, 2))(x) >>> print(y) [[[[ 0  1  2]    [ 0  1  2]]   [[ 3  4  5]    [ 3  4  5]]]  [[[ 6  7  8]    [ 6  7  8]]   [[ 9 10 11]    [ 9 10 11]]]]`

**Arguments**

*   **size**: Int, or tuple of 2 integers. The upsampling factors for rows and columns.
*   **data\_format**: A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists) else `"channels_last"`. Defaults to `"channels_last"`.
*   **interpolation**: A string, one of `"bicubic"`, `"bilinear"`, `"lanczos3"`, `"lanczos5"`, `"nearest"`.

**Input shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, rows, cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, rows, cols)`

**Output shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, upsampled_rows, upsampled_cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, upsampled_rows, upsampled_cols)`

* * *

[UpSampling2D layer](https://keras.io/api/layers/reshaping_layers/up_sampling2d/#upsampling2d-layer)

[`UpSampling2D` class](https://keras.io/api/layers/reshaping_layers/up_sampling2d/#upsampling2d-class)