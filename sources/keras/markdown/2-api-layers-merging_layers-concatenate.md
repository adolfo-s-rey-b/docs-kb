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
 / Concatenate layer

Concatenate layer
=================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/merging/concatenate.py#L28)

### `Concatenate` class

Copied!

`tf_keras.layers.Concatenate(axis=-1, **kwargs)`

Layer that concatenates a list of inputs.

It takes as input a list of tensors, all of the same shape except for the concatenation axis, and returns a single tensor that is the concatenation of all inputs.

Copied!

`>>> x = np.arange(20).reshape(2, 2, 5) >>> print(x) [[[ 0  1  2  3  4]   [ 5  6  7  8  9]]  [[10 11 12 13 14]   [15 16 17 18 19]]] >>> y = np.arange(20, 30).reshape(2, 1, 5) >>> print(y) [[[20 21 22 23 24]]  [[25 26 27 28 29]]] >>> tf.keras.layers.Concatenate(axis=1)([x, y]) <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy= array([[[ 0,  1,  2,  3,  4],         [ 5,  6,  7,  8,  9],         [20, 21, 22, 23, 24]],        [[10, 11, 12, 13, 14],         [15, 16, 17, 18, 19],         [25, 26, 27, 28, 29]]])>`

Copied!

`>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2)) >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2)) >>> concatted = tf.keras.layers.Concatenate()([x1, x2]) >>> concatted.shape TensorShape([5, 16])`

* * *

[Concatenate layer](https://keras.io/2/api/layers/merging_layers/concatenate/#concatenate-layer)

[`Concatenate` class](https://keras.io/2/api/layers/merging_layers/concatenate/#concatenate-class)