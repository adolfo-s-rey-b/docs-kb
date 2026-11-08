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
 / [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 / UnitNormalization layer

UnitNormalization layer
=======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/normalization/unit_normalization.py#L27)

### `UnitNormalization` class

Copied!

`tf_keras.layers.UnitNormalization(axis=-1, **kwargs)`

Unit normalization layer.

Normalize a batch of inputs so that each input in the batch has a L2 norm equal to 1 (across the axes specified in `axis`).

**Example**

Copied!

`>>> data = tf.constant(np.arange(6).reshape(2, 3), dtype=tf.float32) >>> normalized_data = tf.keras.layers.UnitNormalization()(data) >>> print(tf.reduce_sum(normalized_data[0, :] ** 2).numpy()) 1.0`

**Arguments**

*   **axis**: Integer or list/tuple. The axis or axes to normalize across. Typically, this is the features axis or axes. The left-out axes are typically the batch axis or axes. `-1` is the last dimension in the input. Defaults to `-1`.

* * *

[UnitNormalization layer](https://keras.io/2/api/layers/normalization_layers/unit_normalization/#unitnormalization-layer)

[`UnitNormalization` class](https://keras.io/2/api/layers/normalization_layers/unit_normalization/#unitnormalization-class)