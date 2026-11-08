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
 / [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 / FlaxLayer

FlaxLayer
=========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/jax_layer.py#L670)

### `FlaxLayer` class

Copied!

`keras.layers.FlaxLayer(module, method=None, variables=None, **kwargs)`

Keras Layer that wraps a [Flax](https://flax.readthedocs.io/)
 module.

This layer enables the use of Flax components in the form of [`flax.linen.Module`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html)
 instances within Keras when using JAX as the backend for Keras.

The module method to use for the forward pass can be specified via the `method` argument and is `__call__` by default. This method must take the following arguments with these exact names:

*   `self` if the method is bound to the module, which is the case for the default of `__call__`, and `module` otherwise to pass the module.
*   `inputs`: the inputs to the model, a JAX array or a `PyTree` of arrays.
*   `training` _(optional)_: an argument specifying if we're in training mode or inference mode, `True` is passed in training mode.

`FlaxLayer` handles the non-trainable state of your model and required RNGs automatically. Note that the `mutable` parameter of [`flax.linen.Module.apply()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.apply)
 is set to `DenyList(["params"])`, therefore making the assumption that all the variables outside of the "params" collection are non-trainable weights.

This example shows how to create a `FlaxLayer` from a Flax `Module` with the default `__call__` method and no training argument:

Copied!

`class MyFlaxModule(flax.linen.Module):     @flax.linen.compact     def __call__(self, inputs):         x = inputs         x = flax.linen.Conv(features=32, kernel_size=(3, 3))(x)         x = flax.linen.relu(x)         x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))         x = x.reshape((x.shape[0], -1))  # flatten         x = flax.linen.Dense(features=200)(x)         x = flax.linen.relu(x)         x = flax.linen.Dense(features=10)(x)         x = flax.linen.softmax(x)         return x  flax_module = MyFlaxModule() keras_layer = FlaxLayer(flax_module)`

This example shows how to wrap the module method to conform to the required signature. This allows having multiple input arguments and a training argument that has a different name and values. This additionally shows how to use a function that is not bound to the module.

Copied!

`class MyFlaxModule(flax.linen.Module):     @flax.linen.compact     def forward(self, input1, input2, deterministic):         ...         return outputs  def my_flax_module_wrapper(module, inputs, training):     input1, input2 = inputs     return module.forward(input1, input2, not training)  flax_module = MyFlaxModule() keras_layer = FlaxLayer(     module=flax_module,     method=my_flax_module_wrapper, )`

**Arguments**

*   **module**: An instance of `flax.linen.Module` or subclass.
*   **method**: The method to call the model. This is generally a method in the `Module`. If not provided, the `__call__` method is used. `method` can also be a function not defined in the `Module`, in which case it must take the `Module` as the first argument. It is used for both `Module.init` and `Module.apply`. Details are documented in the `method` argument of [`flax.linen.Module.apply()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.apply)
    .
*   **variables**: A `dict` containing all the variables of the module in the same format as what is returned by [`flax.linen.Module.init()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.init)
    . It should contain a "params" key and, if applicable, other keys for collections of variables for non-trainable state. This allows passing trained parameters and learned non-trainable state or controlling the initialization. If `None` is passed, the module's `init` function is called at build time to initialize the variables of the model.

* * *

[FlaxLayer](https://keras.io/api/layers/backend_specific_layers/flax_layer/#flaxlayer)

[`FlaxLayer` class](https://keras.io/api/layers/backend_specific_layers/flax_layer/#flaxlayer-class)