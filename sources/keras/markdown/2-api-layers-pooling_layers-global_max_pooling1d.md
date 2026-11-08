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
 / GlobalMaxPooling1D layer

GlobalMaxPooling1D layer
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/pooling/global_max_pooling1d.py#L25)

### `GlobalMaxPooling1D` class

Copied!

`tf_keras.layers.GlobalMaxPooling1D(     data_format="channels_last", keepdims=False, **kwargs )`

Global max pooling operation for 1D temporal data.

Downsamples the input representation by taking the maximum value over the time dimension.

For example:

Copied!

`>>> x = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]) >>> x = tf.reshape(x, [3, 3, 1]) >>> x <tf.Tensor: shape=(3, 3, 1), dtype=float32, numpy= array([[[1.], [2.], [3.]],        [[4.], [5.], [6.]],        [[7.], [8.], [9.]]], dtype=float32)> >>> max_pool_1d = tf.keras.layers.GlobalMaxPooling1D() >>> max_pool_1d(x) <tf.Tensor: shape=(3, 1), dtype=float32, numpy= array([[3.],        [6.],        [9.], dtype=float32)>`\
\
**Arguments**\
\
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch, steps, features)` while `channels_first` corresponds to inputs with shape `(batch, features, steps)`.\
*   **keepdims**: A boolean, whether to keep the temporal dimension or not. If `keepdims` is `False` (default), the rank of the tensor is reduced for spatial dimensions. If `keepdims` is `True`, the temporal dimension are retained with length 1. The behavior is the same as for [`tf.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/reduce_max)\
     or `np.max`.\
\
**Input shape**\
\
*   If `data_format='channels_last'`: 3D tensor with shape: `(batch_size, steps, features)`\
*   If `data_format='channels_first'`: 3D tensor with shape: `(batch_size, features, steps)`\
\
**Output shape**\
\
*   If `keepdims`\=False: 2D tensor with shape `(batch_size, features)`.\
*   If `keepdims`\=True:\
    *   If `data_format='channels_last'`: 3D tensor with shape `(batch_size, 1, features)`\
    *   If `data_format='channels_first'`: 3D tensor with shape `(batch_size, features, 1)`\
\
* * *\
\
[GlobalMaxPooling1D layer](https://keras.io/2/api/layers/pooling_layers/global_max_pooling1d/#globalmaxpooling1d-layer)\
\
[`GlobalMaxPooling1D` class](https://keras.io/2/api/layers/pooling_layers/global_max_pooling1d/#globalmaxpooling1d-class)