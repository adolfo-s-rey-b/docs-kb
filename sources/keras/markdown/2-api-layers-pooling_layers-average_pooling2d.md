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
 / [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 / AveragePooling2D layer

AveragePooling2D layer
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/pooling/average_pooling2d.py#L26)

### `AveragePooling2D` class

Copied!

`tf_keras.layers.AveragePooling2D(     pool_size=(2, 2), strides=None, padding="valid", data_format=None, **kwargs )`

Average pooling operation for spatial data.

Downsamples the input along its spatial dimensions (height and width) by taking the average value over an input window (of size defined by `pool_size`) for each channel of the input. The window is shifted by `strides` along each dimension.

The resulting output when using `"valid"` padding option has a shape (number of rows or columns) of: `output_shape = math.floor((input_shape - pool_size) / strides) + 1` (when `input_shape >= pool_size`)

The resulting output shape when using the `"same"` padding option is: `output_shape = math.floor((input_shape - 1) / strides) + 1`

For example, for `strides=(1, 1)` and `padding="valid"`:

Copied!

`>>> x = tf.constant([[1., 2., 3.], ...                  [4., 5., 6.], ...                  [7., 8., 9.]]) >>> x = tf.reshape(x, [1, 3, 3, 1]) >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(1, 1), padding='valid') >>> avg_pool_2d(x) <tf.Tensor: shape=(1, 2, 2, 1), dtype=float32, numpy=   array([[[[3.],            [4.]],           [[6.],            [7.]]]], dtype=float32)>`

For example, for `stride=(2, 2)` and `padding="valid"`:

Copied!

`>>> x = tf.constant([[1., 2., 3., 4.], ...                  [5., 6., 7., 8.], ...                  [9., 10., 11., 12.]]) >>> x = tf.reshape(x, [1, 3, 4, 1]) >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(2, 2), padding='valid') >>> avg_pool_2d(x) <tf.Tensor: shape=(1, 1, 2, 1), dtype=float32, numpy=   array([[[[3.5],            [5.5]]]], dtype=float32)>`

For example, for `strides=(1, 1)` and `padding="same"`:

Copied!

`>>> x = tf.constant([[1., 2., 3.], ...                  [4., 5., 6.], ...                  [7., 8., 9.]]) >>> x = tf.reshape(x, [1, 3, 3, 1]) >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), ...    strides=(1, 1), padding='same') >>> avg_pool_2d(x) <tf.Tensor: shape=(1, 3, 3, 1), dtype=float32, numpy=   array([[[[3.],            [4.],            [4.5]],           [[6.],            [7.],            [7.5]],           [[7.5],            [8.5],            [9.]]]], dtype=float32)>`

**Arguments**

*   **pool\_size**: integer or tuple of 2 integers, factors by which to downscale (vertical, horizontal). `(2, 2)` will halve the input in both spatial dimension. If only one integer is specified, the same window length will be used for both dimensions.
*   **strides**: Integer, tuple of 2 integers, or None. Strides values. If None, it will default to `pool_size`.
*   **padding**: One of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch, channels, height, width)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.

**Input shape**

*   If `data_format='channels_last'`: 4D tensor with shape `(batch_size, rows, cols, channels)`.
*   If `data_format='channels_first'`: 4D tensor with shape `(batch_size, channels, rows, cols)`.

**Output shape**

*   If `data_format='channels_last'`: 4D tensor with shape `(batch_size, pooled_rows, pooled_cols, channels)`.
*   If `data_format='channels_first'`: 4D tensor with shape `(batch_size, channels, pooled_rows, pooled_cols)`.

* * *

[AveragePooling2D layer](https://keras.io/2/api/layers/pooling_layers/average_pooling2d/#averagepooling2d-layer)

[`AveragePooling2D` class](https://keras.io/2/api/layers/pooling_layers/average_pooling2d/#averagepooling2d-class)