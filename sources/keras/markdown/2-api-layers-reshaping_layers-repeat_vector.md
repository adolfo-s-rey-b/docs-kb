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
 / RepeatVector layer

RepeatVector layer
==================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/repeat_vector.py#L28)

### `RepeatVector` class

Copied!

`tf_keras.layers.RepeatVector(n, **kwargs)`

Repeats the input n times.

**Example**

Copied!

``model = Sequential() model.add(Dense(32, input_dim=32)) # now: model.output_shape == (None, 32) # note: `None` is the batch dimension  model.add(RepeatVector(3)) # now: model.output_shape == (None, 3, 32)``

**Arguments**

*   **n**: Integer, repetition factor.

**Input shape 2D tensor of shape `(num_samples, features)`**

.

**Output shape 3D tensor of shape `(num_samples, n, features)`.**

* * *

[RepeatVector layer](https://keras.io/2/api/layers/reshaping_layers/repeat_vector/#repeatvector-layer)

[`RepeatVector` class](https://keras.io/2/api/layers/reshaping_layers/repeat_vector/#repeatvector-class)