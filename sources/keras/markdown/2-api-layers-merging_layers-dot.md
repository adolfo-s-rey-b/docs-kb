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
 / Dot layer

Dot layer
=========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/merging/dot.py#L29)

### `Dot` class

Copied!

`tf_keras.layers.Dot(axes, normalize=False, **kwargs)`

Layer that computes a dot product between samples in two tensors.

E.g. if applied to a list of two tensors `a` and `b` of shape `(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)` where each entry `i` will be the dot product between `a[i]` and `b[i]`.

Copied!

`>>> x = np.arange(10).reshape(1, 5, 2) >>> print(x) [[[0 1]   [2 3]   [4 5]   [6 7]   [8 9]]] >>> y = np.arange(10, 20).reshape(1, 2, 5) >>> print(y) [[[10 11 12 13 14]   [15 16 17 18 19]]] >>> tf.keras.layers.Dot(axes=(1, 2))([x, y]) <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy= array([[[260, 360],         [320, 445]]])>`

Copied!

`>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2)) >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2)) >>> dotted = tf.keras.layers.Dot(axes=1)([x1, x2]) >>> dotted.shape TensorShape([5, 1])`

* * *

[Dot layer](https://keras.io/2/api/layers/merging_layers/dot/#dot-layer)

[`Dot` class](https://keras.io/2/api/layers/merging_layers/dot/#dot-class)