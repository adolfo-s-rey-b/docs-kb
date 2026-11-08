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
 / [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 / Minimum layer

Minimum layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/merging/minimum.py#L26)

### `Minimum` class

Copied!

`tf_keras.layers.Minimum(**kwargs)`

Layer that computes the minimum (element-wise) a list of inputs.

It takes as input a list of tensors, all of the same shape, and returns a single tensor (also of the same shape).

Copied!

`>>> tf.keras.layers.Minimum()([np.arange(5).reshape(5, 1), ...                            np.arange(5, 10).reshape(5, 1)]) <tf.Tensor: shape=(5, 1), dtype=int64, numpy= array([[0],      [1],      [2],      [3],      [4]])>`

Copied!

`>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2)) >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2)) >>> minned = tf.keras.layers.Minimum()([x1, x2]) >>> minned.shape TensorShape([5, 8])`

* * *

[Minimum layer](https://keras.io/2/api/layers/merging_layers/minimum/#minimum-layer)

[`Minimum` class](https://keras.io/2/api/layers/merging_layers/minimum/#minimum-class)