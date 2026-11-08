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
 / AveragePooling1D layer

AveragePooling1D layer
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/pooling/average_pooling1d.py#L27)

### `AveragePooling1D` class

Copied!

`tf_keras.layers.AveragePooling1D(     pool_size=2, strides=None, padding="valid", data_format="channels_last", **kwargs )`

Average pooling for temporal data.

Downsamples the input representation by taking the average value over the window defined by `pool_size`. The window is shifted by `strides`. The resulting output when using "valid" padding option has a shape of: `output_shape = (input_shape - pool_size + 1) / strides)`

The resulting output shape when using the "same" padding option is: `output_shape = input_shape / strides`

For example, for strides=1 and padding="valid":

Copied!

`>>> x = tf.constant([1., 2., 3., 4., 5.]) >>> x = tf.reshape(x, [1, 5, 1]) >>> x <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=   array([[[1.],           [2.],           [3.],           [4.],           [5.]], dtype=float32)> >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2, ...    strides=1, padding='valid') >>> avg_pool_1d(x) <tf.Tensor: shape=(1, 4, 1), dtype=float32, numpy= array([[[1.5],         [2.5],         [3.5],         [4.5]]], dtype=float32)>`\
\
For example, for strides=2 and padding="valid":\
\
Copied!\
\
`>>> x = tf.constant([1., 2., 3., 4., 5.]) >>> x = tf.reshape(x, [1, 5, 1]) >>> x <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=   array([[[1.],           [2.],           [3.],           [4.],           [5.]], dtype=float32)> >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2, ...    strides=2, padding='valid') >>> avg_pool_1d(x) <tf.Tensor: shape=(1, 2, 1), dtype=float32, numpy= array([[[1.5],         [3.5]]], dtype=float32)>`\
\
For example, for strides=1 and padding="same":\
\
Copied!\
\
`>>> x = tf.constant([1., 2., 3., 4., 5.]) >>> x = tf.reshape(x, [1, 5, 1]) >>> x <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=   array([[[1.],           [2.],           [3.],           [4.],           [5.]], dtype=float32)> >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2, ...    strides=1, padding='same') >>> avg_pool_1d(x) <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy= array([[[1.5],         [2.5],         [3.5],         [4.5],         [5.]]], dtype=float32)>`\
\
**Arguments**\
\
*   **pool\_size**: Integer, size of the average pooling windows.\
*   **strides**: Integer, or None. Factor by which to downscale. E.g. 2 will halve the input. If None, it will default to `pool_size`.\
*   **padding**: One of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.\
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch, steps, features)` while `channels_first` corresponds to inputs with shape `(batch, features, steps)`.\
\
**Input shape**\
\
*   If `data_format='channels_last'`: 3D tensor with shape `(batch_size, steps, features)`.\
*   If `data_format='channels_first'`: 3D tensor with shape `(batch_size, features, steps)`.\
\
**Output shape**\
\
*   If `data_format='channels_last'`: 3D tensor with shape `(batch_size, downsampled_steps, features)`.\
*   If `data_format='channels_first'`: 3D tensor with shape `(batch_size, features, downsampled_steps)`.\
\
* * *\
\
[AveragePooling1D layer](https://keras.io/2/api/layers/pooling_layers/average_pooling1d/#averagepooling1d-layer)\
\
[`AveragePooling1D` class](https://keras.io/2/api/layers/pooling_layers/average_pooling1d/#averagepooling1d-class)