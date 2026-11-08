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
 / [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 / UpSampling2D layer

UpSampling2D layer
==================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/up_sampling2d.py#L30)

### `UpSampling2D` class

Copied!

`tf_keras.layers.UpSampling2D(     size=(2, 2), data_format=None, interpolation="nearest", **kwargs )`

Upsampling layer for 2D inputs.

Repeats the rows and columns of the data by `size[0]` and `size[1]` respectively.

**Examples**

Copied!

`>>> input_shape = (2, 2, 1, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> print(x) [[[[ 0  1  2]]   [[ 3  4  5]]]  [[[ 6  7  8]]   [[ 9 10 11]]]] >>> y = tf.keras.layers.UpSampling2D(size=(1, 2))(x) >>> print(y) tf.Tensor(   [[[[ 0  1  2]      [ 0  1  2]]     [[ 3  4  5]      [ 3  4  5]]]    [[[ 6  7  8]      [ 6  7  8]]     [[ 9 10 11]      [ 9 10 11]]]], shape=(2, 2, 2, 3), dtype=int64)`

**Arguments**

*   **size**: Int, or tuple of 2 integers. The upsampling factors for rows and columns.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.
*   **interpolation**: A string, one of `"area"`, `"bicubic"`, `"bilinear"`, `"gaussian"`, `"lanczos3"`, `"lanczos5"`, `"mitchellcubic"`, `"nearest"`.

**Input shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, rows, cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, rows, cols)`

**Output shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, upsampled_rows, upsampled_cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, upsampled_rows, upsampled_cols)`

* * *

[UpSampling2D layer](https://keras.io/2/api/layers/reshaping_layers/up_sampling2d/#upsampling2d-layer)

[`UpSampling2D` class](https://keras.io/2/api/layers/reshaping_layers/up_sampling2d/#upsampling2d-class)