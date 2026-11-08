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
 / Cropping3D layer

Cropping3D layer
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/cropping3d.py#L28)

### `Cropping3D` class

Copied!

`tf_keras.layers.Cropping3D(     cropping=((1, 1), (1, 1), (1, 1)), data_format=None, **kwargs )`

Cropping layer for 3D data (e.g. spatial or spatio-temporal).

\# Examples

Copied!

`>>> input_shape = (2, 28, 28, 10, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> y = tf.keras.layers.Cropping3D(cropping=(2, 4, 2))(x) >>> print(y.shape) (2, 24, 20, 6, 3)`

**Arguments**

*   **cropping**: Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
    *   If int: the same symmetric cropping is applied to depth, height, and width.
    *   If tuple of 3 ints: interpreted as two different symmetric cropping values for depth, height, and width: `(symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop)`.
    *   If tuple of 3 tuples of 2 ints: interpreted as `((left_dim1_crop, right_dim1_crop), (left_dim2_crop, right_dim2_crop), (left_dim3_crop, right_dim3_crop))`
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.

**Input shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, first_axis_to_crop, second_axis_to_crop, third_axis_to_crop, depth)` - If `data_format` is `"channels_first"`: `(batch_size, depth, first_axis_to_crop, second_axis_to_crop, third_axis_to_crop)`

**Output shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, first_cropped_axis, second_cropped_axis, third_cropped_axis, depth)` - If `data_format` is `"channels_first"`: `(batch_size, depth, first_cropped_axis, second_cropped_axis, third_cropped_axis)`

* * *

[Cropping3D layer](https://keras.io/2/api/layers/reshaping_layers/cropping3d/#cropping3d-layer)

[`Cropping3D` class](https://keras.io/2/api/layers/reshaping_layers/cropping3d/#cropping3d-class)