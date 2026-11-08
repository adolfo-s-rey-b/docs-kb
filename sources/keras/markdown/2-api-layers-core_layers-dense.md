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
 / [Core layers](https://keras.io/2/api/layers/core_layers/)
 / Dense layer

Dense layer
===========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/core/dense.py#L33)

### `Dense` class

Copied!

`tf_keras.layers.Dense(     units,     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

Just your regular densely-connected NN layer.

`Dense` implements the operation: `output = activation(dot(input, kernel) + bias)` where `activation` is the element-wise activation function passed as the `activation` argument, `kernel` is a weights matrix created by the layer, and `bias` is a bias vector created by the layer (only applicable if `use_bias` is `True`). These are all attributes of `Dense`.

Note: If the input to the layer has a rank greater than 2, then `Dense` computes the dot product between the `inputs` and the `kernel` along the last axis of the `inputs` and axis 0 of the `kernel` (using [`tf.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)
). For example, if input has dimensions `(batch_size, d0, d1)`, then we create a `kernel` with shape `(d1, units)`, and the `kernel` operates along axis 2 of the `input`, on every sub-tensor of shape `(1, 1, d1)` (there are `batch_size * d0` such sub-tensors). The output in this case will have shape `(batch_size, d0, units)`.

Besides, layer attributes cannot be modified after the layer has been called once (except the `trainable` attribute). When a popular kwarg `input_shape` is passed, then keras will create an input layer to insert before the current layer. This can be treated equivalent to explicitly defining an `InputLayer`.

**Example**

Copied!

``>>> # Create a `Sequential` model and add a Dense layer as the first layer. >>> model = tf.keras.models.Sequential() >>> model.add(tf.keras.Input(shape=(16,))) >>> model.add(tf.keras.layers.Dense(32, activation='relu')) >>> # Now the model will take as input arrays of shape (None, 16) >>> # and output arrays of shape (None, 32). >>> # Note that after the first layer, you don't need to specify >>> # the size of the input anymore: >>> model.add(tf.keras.layers.Dense(32)) >>> model.output_shape (None, 32)``

**Arguments**

*   **units**: Positive integer, dimensionality of the output space.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: `a(x) = x`).
*   **use\_bias**: Boolean, whether the layer uses a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix.
*   **bias\_initializer**: Initializer for the bias vector.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix.
*   **bias\_regularizer**: Regularizer function applied to the bias vector.
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation").
*   **kernel\_constraint**: Constraint function applied to the `kernel` weights matrix.
*   **bias\_constraint**: Constraint function applied to the bias vector.

**Input shape**

N-D tensor with shape: `(batch_size, ..., input_dim)`. The most common situation would be a 2D input with shape `(batch_size, input_dim)`.

**Output shape**

N-D tensor with shape: `(batch_size, ..., units)`. For instance, for a 2D input with shape `(batch_size, input_dim)`, the output would have shape `(batch_size, units)`.

* * *

[Dense layer](https://keras.io/2/api/layers/core_layers/dense/#dense-layer)

[`Dense` class](https://keras.io/2/api/layers/core_layers/dense/#dense-class)