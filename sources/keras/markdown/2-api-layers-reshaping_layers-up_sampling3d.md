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
 / UpSampling3D layer

UpSampling3D layer
==================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/up_sampling3d.py#L29)

### `UpSampling3D` class

Copied!

`tf_keras.layers.UpSampling3D(size=(2, 2, 2), data_format=None, **kwargs)`

Upsampling layer for 3D inputs.

Repeats the 1st, 2nd and 3rd dimensions of the data by `size[0]`, `size[1]` and `size[2]` respectively.

**Examples**

Copied!

`>>> input_shape = (2, 1, 2, 1, 3) >>> x = tf.constant(1, shape=input_shape) >>> y = tf.keras.layers.UpSampling3D(size=2)(x) >>> print(y.shape) (2, 2, 4, 2, 3)`

**Arguments**

*   **size**: Int, or tuple of 3 integers. The upsampling factors for dim1, dim2 and dim3.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.

**Input shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, dim1, dim2, dim3, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, dim1, dim2, dim3)`

**Output shape**

5D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, upsampled_dim1, upsampled_dim2, upsampled_dim3, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, upsampled_dim1, upsampled_dim2, upsampled_dim3)`

* * *

[UpSampling3D layer](https://keras.io/2/api/layers/reshaping_layers/up_sampling3d/#upsampling3d-layer)

[`UpSampling3D` class](https://keras.io/2/api/layers/reshaping_layers/up_sampling3d/#upsampling3d-class)