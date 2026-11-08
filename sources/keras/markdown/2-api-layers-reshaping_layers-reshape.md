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
 / Reshape layer

Reshape layer
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/reshape.py#L27)

### `Reshape` class

Copied!

`tf_keras.layers.Reshape(target_shape, **kwargs)`

Layer that reshapes inputs into the given shape.

**Input shape**

Arbitrary, although all dimensions in the input shape must be known/fixed. Use the keyword argument `input_shape` (tuple of integers, does not include the samples/batch size axis) when using this layer as the first layer in a model.

**Output shape**

`(batch_size,) + target_shape`

**Example**

Copied!

``>>> # as first layer in a Sequential model >>> model = tf.keras.Sequential() >>> model.add(tf.keras.layers.Reshape((3, 4), input_shape=(12,))) >>> # model.output_shape == (None, 3, 4), `None` is the batch size. >>> model.output_shape (None, 3, 4)``

Copied!

`>>> # as intermediate layer in a Sequential model >>> model.add(tf.keras.layers.Reshape((6, 2))) >>> model.output_shape (None, 6, 2)`

Copied!

``>>> # also supports shape inference using `-1` as dimension >>> model.add(tf.keras.layers.Reshape((-1, 2, 2))) >>> model.output_shape (None, 3, 2, 2)``

* * *

[Reshape layer](https://keras.io/2/api/layers/reshaping_layers/reshape/#reshape-layer)

[`Reshape` class](https://keras.io/2/api/layers/reshaping_layers/reshape/#reshape-class)