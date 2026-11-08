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
 / GlobalAveragePooling2D layer

GlobalAveragePooling2D layer
============================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/pooling/global_average_pooling2d.py#L25)

### `GlobalAveragePooling2D` class

Copied!

`tf_keras.layers.GlobalAveragePooling2D(data_format=None, keepdims=False, **kwargs)`

Global average pooling operation for spatial data.

**Examples**

Copied!

`>>> input_shape = (2, 4, 5, 3) >>> x = tf.random.normal(input_shape) >>> y = tf.keras.layers.GlobalAveragePooling2D()(x) >>> print(y.shape) (2, 3)`

**Arguments**

*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch, channels, height, width)`. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.
*   **keepdims**: A boolean, whether to keep the spatial dimensions or not. If `keepdims` is `False` (default), the rank of the tensor is reduced for spatial dimensions. If `keepdims` is `True`, the spatial dimensions are retained with length 1. The behavior is the same as for [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/reduce_mean)
     or `np.mean`.

**Input shape**

*   If `data_format='channels_last'`: 4D tensor with shape `(batch_size, rows, cols, channels)`.
*   If `data_format='channels_first'`: 4D tensor with shape `(batch_size, channels, rows, cols)`.

**Output shape**

*   If `keepdims`\=False: 2D tensor with shape `(batch_size, channels)`.
*   If `keepdims`\=True:
    *   If `data_format='channels_last'`: 4D tensor with shape `(batch_size, 1, 1, channels)`
    *   If `data_format='channels_first'`: 4D tensor with shape `(batch_size, channels, 1, 1)`

* * *

[GlobalAveragePooling2D layer](https://keras.io/2/api/layers/pooling_layers/global_average_pooling2d/#globalaveragepooling2d-layer)

[`GlobalAveragePooling2D` class](https://keras.io/2/api/layers/pooling_layers/global_average_pooling2d/#globalaveragepooling2d-class)