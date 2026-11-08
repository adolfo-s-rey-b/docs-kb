None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Merging layers](https://keras.io/api/layers/merging_layers/)
 / Multiply layer

Multiply layer
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/multiply.py#L7)

### `Multiply` class

Copied!

`keras.layers.Multiply(**kwargs)`

Performs elementwise multiplication.

It takes as input a list of tensors, all of the same shape, and returns a single tensor (also of the same shape).

**Examples**

Copied!

`>>> input_shape = (2, 3, 4) >>> x1 = np.random.rand(*input_shape) >>> x2 = np.random.rand(*input_shape) >>> y = keras.layers.Multiply()([x1, x2])`

Usage in a Keras model:

Copied!

``>>> input1 = keras.layers.Input(shape=(16,)) >>> x1 = keras.layers.Dense(8, activation='relu')(input1) >>> input2 = keras.layers.Input(shape=(32,)) >>> x2 = keras.layers.Dense(8, activation='relu')(input2) >>> # equivalent to `y = keras.layers.multiply([x1, x2])` >>> y = keras.layers.Multiply()([x1, x2]) >>> out = keras.layers.Dense(4)(y) >>> model = keras.models.Model(inputs=[input1, input2], outputs=out)``

* * *

[Multiply layer](https://keras.io/api/layers/merging_layers/multiply/#multiply-layer)

[`Multiply` class](https://keras.io/api/layers/merging_layers/multiply/#multiply-class)