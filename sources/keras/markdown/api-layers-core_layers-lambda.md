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
 / [Core layers](https://keras.io/api/layers/core_layers/)
 / Lambda layer

Lambda layer
============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/lambda_layer.py#L12)

### `Lambda` class

Copied!

`keras.layers.Lambda(function, output_shape=None, mask=None, arguments=None, **kwargs)`

Wraps arbitrary expressions as a `Layer` object.

The `Lambda` layer exists so that arbitrary expressions can be used as a `Layer` when constructing Sequential and Functional API models. `Lambda` layers are best suited for simple operations or quick experimentation. For more advanced use cases, prefer writing new subclasses of `Layer`.

WARNING: `Lambda` layers have (de)serialization limitations!

The main reason to subclass `Layer` instead of using a `Lambda` layer is saving and inspecting a model. `Lambda` layers are saved by serializing the Python bytecode, which is fundamentally non-portable and potentially unsafe. They should only be loaded in the same environment where they were saved. Subclassed layers can be saved in a more portable way by overriding their `get_config()` method. Models that rely on subclassed Layers are also often easier to visualize and reason about.

**Example**

Copied!

`# add a x -> x^2 layer model.add(Lambda(lambda x: x ** 2))`

**Arguments**

*   **function**: The function to be evaluated. Takes input tensor as first argument.
*   **output\_shape**: Expected output shape from function. This argument can usually be inferred if not explicitly provided. Can be a tuple or function. If a tuple, it only specifies the first dimension onward; sample dimension is assumed either the same as the input: `output_shape = (input_shape[0], ) + output_shape` or, the input is `None` and the sample dimension is also `None`: `output_shape = (None, ) + output_shape`. If a function, it specifies the entire shape as a function of the input shape: `output_shape = f(input_shape)`.
*   **mask**: Either None (indicating no masking) or a callable with the same signature as the `compute_mask` layer method, or a tensor that will be returned as output mask regardless of what the input is.
*   **arguments**: Optional dictionary of keyword arguments to be passed to the function.

* * *

[Lambda layer](https://keras.io/api/layers/core_layers/lambda/#lambda-layer)

[`Lambda` class](https://keras.io/api/layers/core_layers/lambda/#lambda-class)