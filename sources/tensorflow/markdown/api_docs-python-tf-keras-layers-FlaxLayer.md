[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.FlaxLayer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/FlaxLayer#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/jax_layer.py#L670-L896)

Keras Layer that wraps a [Flax](https://flax.readthedocs.io/)
 module.

Inherits From: [`JaxLayer`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.FlaxLayer(
        module, method=None, variables=None, **kwargs
    )

This layer enables the use of Flax components in the form of [`flax.linen.Module`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html)
 instances within Keras when using JAX as the backend for Keras.

The module method to use for the forward pass can be specified via the `method` argument and is `__call__` by default. This method must take the following arguments with these exact names:

*   `self` if the method is bound to the module, which is the case for the default of `__call__`, and `module` otherwise to pass the module.
*   `inputs`: the inputs to the model, a JAX array or a `PyTree` of arrays.
*   `training` _(optional)_: an argument specifying if we're in training mode or inference mode, `True` is passed in training mode.

`FlaxLayer` handles the non-trainable state of your model and required RNGs automatically. Note that the `mutable` parameter of [`flax.linen.Module.apply()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.apply)
 is set to `DenyList(["params"])`, therefore making the assumption that all the variables outside of the "params" collection are non-trainable weights.

This example shows how to create a `FlaxLayer` from a Flax `Module` with the default `__call__` method and no training argument:

class MyFlaxModule(flax.linen.Module):
        @flax.linen.compact
        def __call__(self, inputs):
            x = inputs
            x = flax.linen.Conv(features=32, kernel_size=(3, 3))(x)
            x = flax.linen.relu(x)
            x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
            x = x.reshape((x.shape[0], -1))  # flatten
            x = flax.linen.Dense(features=200)(x)
            x = flax.linen.relu(x)
            x = flax.linen.Dense(features=10)(x)
            x = flax.linen.softmax(x)
            return x
    
    flax_module = MyFlaxModule()
    keras_layer = FlaxLayer(flax_module)

This example shows how to wrap the module method to conform to the required signature. This allows having multiple input arguments and a training argument that has a different name and values. This additionally shows how to use a function that is not bound to the module.

class MyFlaxModule(flax.linen.Module):
        @flax.linen.compact
        def forward(self, input1, input2, deterministic):
            ...
            return outputs
    
    def my_flax_module_wrapper(module, inputs, training):
        input1, input2 = inputs
        return module.forward(input1, input2, not training)
    
    flax_module = MyFlaxModule()
    keras_layer = FlaxLayer(
        module=flax_module,
        method=my_flax_module_wrapper,
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `module` | An instance of `flax.linen.Module` or subclass. |
| `method` | The method to call the model. This is generally a method in the `Module`. If not provided, the `__call__` method is used. `method` can also be a function not defined in the `Module`, in which case it must take the `Module` as the first argument. It is used for both `Module.init` and `Module.apply`. Details are documented in the `method` argument of [`flax.linen.Module.apply()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.apply)<br>. |
| `variables` | A `dict` containing all the variables of the module in the same format as what is returned by [`flax.linen.Module.init()`](https://flax.readthedocs.io/en/latest/api_reference/flax.linen/module.html#flax.linen.init)<br>. It should contain a "params" key and, if applicable, other keys for collections of variables for non-trainable state. This allows passing trained parameters and learned non-trainable state or controlling the initialization. If `None` is passed, the module's `init` function is called at build time to initialize the variables of the model. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/jax_layer.py#L887-L896)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.