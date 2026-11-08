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
 / Cropping2D layer

Cropping2D layer
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/cropping2d.py#L28)

### `Cropping2D` class

Copied!

`tf_keras.layers.Cropping2D(cropping=((0, 0), (0, 0)), data_format=None, **kwargs)`

Cropping layer for 2D input (e.g. picture).

It crops along spatial dimensions, i.e. height and width.

**Examples**

Copied!

`>>> input_shape = (2, 28, 28, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> y = tf.keras.layers.Cropping2D(cropping=((2, 2), (4, 4)))(x) >>> print(y.shape) (2, 24, 20, 3)`

**Arguments**

*   **cropping**: Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
    *   If int: the same symmetric cropping is applied to height and width.
    *   If tuple of 2 ints: interpreted as two different symmetric cropping values for height and width: `(symmetric_height_crop, symmetric_width_crop)`.
    *   If tuple of 2 tuples of 2 ints: interpreted as `((top_crop, bottom_crop), (left_crop, right_crop))`
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.

**Input shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, rows, cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, rows, cols)`

**Output shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, cropped_rows, cropped_cols, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, cropped_rows, cropped_cols)`

* * *

[Cropping2D layer](https://keras.io/2/api/layers/reshaping_layers/cropping2d/#cropping2d-layer)

[`Cropping2D` class](https://keras.io/2/api/layers/reshaping_layers/cropping2d/#cropping2d-class)