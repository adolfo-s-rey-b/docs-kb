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
 / Lambda layer

Lambda layer
============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/core/lambda_layer.py#L36)

### `Lambda` class

Copied!

`tf_keras.layers.Lambda(     function, output_shape=None, mask=None, arguments=None, **kwargs )`

Wraps arbitrary expressions as a `Layer` object.

The `Lambda` layer exists so that arbitrary expressions can be used as a `Layer` when constructing Sequential and Functional API models. `Lambda` layers are best suited for simple operations or quick experimentation. For more advanced use cases, follow [this guide](https://keras.io/guides/making_new_layers_and_models_via_subclassing)
 for subclassing [`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer)
.

WARNING: [`tf.keras.layers.Lambda`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda)
 layers have (de)serialization limitations!

The main reason to subclass [`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer)
 instead of using a `Lambda` layer is saving and inspecting a Model. `Lambda` layers are saved by serializing the Python bytecode, which is fundamentally non-portable. They should only be loaded in the same environment where they were saved. Subclassed layers can be saved in a more portable way by overriding their `get_config()` method. Models that rely on subclassed Layers are also often easier to visualize and reason about.

**Examples**

Copied!

`# add a x -> x^2 layer model.add(Lambda(lambda x: x ** 2))`

Copied!

`# add a layer that returns the concatenation # of the positive part of the input and # the opposite of the negative part  def antirectifier(x):     x -= K.mean(x, axis=1, keepdims=True)     x = K.l2_normalize(x, axis=1)     pos = K.relu(x)     neg = K.relu(-x)     return K.concatenate([pos, neg], axis=1)  model.add(Lambda(antirectifier))`

**Note on Variables:**

While it is possible to use Variables with Lambda layers, this practice is discouraged as it can easily lead to bugs. For instance, consider the following layer:

Copied!

`scale = tf.Variable(1.) scale_layer = tf.keras.layers.Lambda(lambda x: x * scale)`

Because `scale_layer` does not directly track the `scale` variable, it will not appear in `scale_layer.trainable_weights` and will therefore not be trained if `scale_layer` is used in a Model.

A better pattern is to write a subclassed Layer:

Copied!

`class ScaleLayer(tf.keras.layers.Layer):     def __init__(self, **kwargs):         super().__init__(**kwargs)         self.scale = tf.Variable(1.)      def call(self, inputs):         return inputs * self.scale`

In general, `Lambda` layers can be convenient for simple stateless computation, but anything more complex should use a subclass Layer instead.

**Arguments**

*   **function**: The function to be evaluated. Takes input tensor as first argument.
*   **output\_shape**: Expected output shape from function. This argument can be inferred if not explicitly provided. Can be a tuple or function. If a tuple, it only specifies the first dimension onward; sample dimension is assumed either the same as the input: `output_shape = (input_shape[0], ) + output_shape` or, the input is `None` and the sample dimension is also `None`: `output_shape = (None, ) + output_shape` If a function, it specifies the entire shape as a function of the input shape: `output_shape = f(input_shape)`
*   **mask**: Either None (indicating no masking) or a callable with the same signature as the `compute_mask` layer method, or a tensor that will be returned as output mask regardless of what the input is.
*   **arguments**: Optional dictionary of keyword arguments to be passed to the function.

**Input shape Arbitrary. Use the keyword argument input\_shape (tuple of**

integers, does not include the samples axis) when using this layer as the first layer in a model.

**Output shape Specified by `output_shape` argument**

* * *

[Lambda layer](https://keras.io/2/api/layers/core_layers/lambda/#lambda-layer)

[`Lambda` class](https://keras.io/2/api/layers/core_layers/lambda/#lambda-class)