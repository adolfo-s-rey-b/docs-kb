[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Model function](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#model_function)
    
*   [Model weights initialization](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#model_weights_initialization)
    
*   [Models with non-trainable state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#models_with_non-trainable_state)
    
*   [Models without non-trainable state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#models_without_non-trainable_state)
    
*   [Conforming to the required signature](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#conforming_to_the_required_signature)
    
*   [Usage with Haiku modules](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#usage_with_haiku_modules)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.JaxLayer Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Model function](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#model_function)
    
*   [Model weights initialization](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#model_weights_initialization)
    
*   [Models with non-trainable state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#models_with_non-trainable_state)
    
*   [Models without non-trainable state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#models_without_non-trainable_state)
    
*   [Conforming to the required signature](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#conforming_to_the_required_signature)
    
*   [Usage with Haiku modules](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#usage_with_haiku_modules)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/JaxLayer#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/jax_layer.py#L37-L667)

Keras Layer that wraps a JAX model.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.JaxLayer(
        call_fn,
        init_fn=None,
        params=None,
        state=None,
        seed=None,
        native_serialization_platforms=None,
        **kwargs
    )

This layer enables the use of JAX components within Keras when using JAX as the backend for Keras.

Model function
--------------

This layer accepts JAX models in the form of a function, `call_fn`, which must take the following arguments with these exact names:

*   `params`: trainable parameters of the model.
*   `state` (_optional_): non-trainable state of the model. Can be omitted if the model has no non-trainable state.
*   `rng` (_optional_): a `jax.random.PRNGKey` instance. Can be omitted if the model does not need RNGs, neither during training nor during inference.
*   `inputs`: inputs to the model, a JAX array or a `PyTree` of arrays.
*   `training` (_optional_): an argument specifying if we're in training mode or inference mode, `True` is passed in training mode. Can be omitted if the model behaves the same in training mode and inference mode.

The `inputs` argument is mandatory. Inputs to the model must be provided via a single argument. If the JAX model takes multiple inputs as separate arguments, they must be combined into a single structure, for instance in a `tuple` or a `dict`.

Model weights initialization
----------------------------

The initialization of the `params` and `state` of the model can be handled by this layer, in which case the `init_fn` argument must be provided. This allows the model to be initialized dynamically with the right shape. Alternatively, and if the shape is known, the `params` argument and optionally the `state` argument can be used to create an already initialized model.

The `init_fn` function, if provided, must take the following arguments with these exact names:

*   `rng`: a `jax.random.PRNGKey` instance.
*   `inputs`: a JAX array or a `PyTree` of arrays with placeholder values to provide the shape of the inputs.
*   `training` (_optional_): an argument specifying if we're in training mode or inference mode. `True` is always passed to `init_fn`. Can be omitted regardless of whether `call_fn` has a `training` argument.

Models with non-trainable state
-------------------------------

For JAX models that have non-trainable state:

*   `call_fn` must have a `state` argument
*   `call_fn` must return a `tuple` containing the outputs of the model and the new non-trainable state of the model
*   `init_fn` must return a `tuple` containing the initial trainable params of the model and the initial non-trainable state of the model.

This code shows a possible combination of `call_fn` and `init_fn` signatures for a model with non-trainable state. In this example, the model has a `training` argument and an `rng` argument in `call_fn`.

def stateful_call(params, state, rng, inputs, training):
        outputs = ...
        new_state = ...
        return outputs, new_state
    
    def stateful_init(rng, inputs):
        initial_params = ...
        initial_state = ...
        return initial_params, initial_state

Models without non-trainable state
----------------------------------

For JAX models with no non-trainable state:

*   `call_fn` must not have a `state` argument
*   `call_fn` must return only the outputs of the model
*   `init_fn` must return only the initial trainable params of the model.

This code shows a possible combination of `call_fn` and `init_fn` signatures for a model without non-trainable state. In this example, the model does not have a `training` argument and does not have an `rng` argument in `call_fn`.

def stateless_call(params, inputs):
        outputs = ...
        return outputs
    
    def stateless_init(rng, inputs):
        initial_params = ...
        return initial_params

Conforming to the required signature
------------------------------------

If a model has a different signature than the one required by `JaxLayer`, one can easily write a wrapper method to adapt the arguments. This example shows a model that has multiple inputs as separate arguments, expects multiple RNGs in a `dict`, and has a `deterministic` argument with the opposite meaning of `training`. To conform, the inputs are combined in a single structure using a `tuple`, the RNG is split and used the populate the expected `dict`, and the Boolean flag is negated:

def my_model_fn(params, rngs, input1, input2, deterministic):
        ...
        if not deterministic:
            dropout_rng = rngs["dropout"]
            keep = jax.random.bernoulli(dropout_rng, dropout_rate, x.shape)
            x = jax.numpy.where(keep, x / dropout_rate, 0)
            ...
        ...
        return outputs
    
    def my_model_wrapper_fn(params, rng, inputs, training):
        input1, input2 = inputs
        rng1, rng2 = jax.random.split(rng)
        rngs = {"dropout": rng1, "preprocessing": rng2}
        deterministic = not training
        return my_model_fn(params, rngs, input1, input2, deterministic)
    
    keras_layer = JaxLayer(my_model_wrapper_fn, params=initial_params)

Usage with Haiku modules
------------------------

`JaxLayer` enables the use of [Haiku](https://dm-haiku.readthedocs.io/)
 components in the form of [`haiku.Module`](https://dm-haiku.readthedocs.io/en/latest/api.html#module)
. This is achieved by transforming the module per the Haiku pattern and then passing `module.apply` in the `call_fn` parameter and `module.init` in the `init_fn` parameter if needed.

If the model has non-trainable state, it should be transformed with [`haiku.transform_with_state`](https://dm-haiku.readthedocs.io/en/latest/api.html#haiku.transform_with_state)
. If the model has no non-trainable state, it should be transformed with [`haiku.transform`](https://dm-haiku.readthedocs.io/en/latest/api.html#haiku.transform)
. Additionally, and optionally, if the module does not use RNGs in "apply", it can be transformed with [`haiku.without_apply_rng`](https://dm-haiku.readthedocs.io/en/latest/api.html#without-apply-rng)
.

The following example shows how to create a `JaxLayer` from a Haiku module that uses random number generators via `hk.next_rng_key()` and takes a training positional argument:

class MyHaikuModule(hk.Module):
        def __call__(self, x, training):
            x = hk.Conv2D(32, (3, 3))(x)
            x = jax.nn.relu(x)
            x = hk.AvgPool((1, 2, 2, 1), (1, 2, 2, 1), "VALID")(x)
            x = hk.Flatten()(x)
            x = hk.Linear(200)(x)
            if training:
                x = hk.dropout(rng=hk.next_rng_key(), rate=0.3, x=x)
            x = jax.nn.relu(x)
            x = hk.Linear(10)(x)
            x = jax.nn.softmax(x)
            return x
    
    def my_haiku_module_fn(inputs, training):
        module = MyHaikuModule()
        return module(inputs, training)
    
    transformed_module = hk.transform(my_haiku_module_fn)
    
    keras_layer = JaxLayer(
        call_fn=transformed_module.apply,
        init_fn=transformed_module.init,
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| call\_fn: The function to call the model. See description above for the list of arguments it takes and the outputs it returns. init\_fn: the function to call to initialize the model. See description above for the list of arguments it takes and the outputs it returns. If `None`, then `params` and/or `state` must be provided. |     |
| `params` | A `PyTree` containing all the model trainable parameters. This allows passing trained parameters or controlling the initialization. If both `params` and `state` are `None`, `init_fn` is called at build time to initialize the trainable parameters of the model. |
| `state` | A `PyTree` containing all the model non-trainable state. This allows passing learned state or controlling the initialization. If both `params` and `state` are `None`, and `call_fn` takes a `state` argument, then `init_fn` is called at build time to initialize the non-trainable state of the model. |
| `seed` | Seed for random number generator. Optional. |
| `native_serialization_platforms` | Sequence of platforms ('cpu', 'cuda', 'rocm', 'tpu') to compile for when using `jax2tf.convert` with native serialization. This is only used when the Keras backend is `tensorflow`. If `None`, the function is compiled for the default backend. If multiple platforms are specified, the exported module will be device-polymorphic. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/jax_layer.py#L661-L667)

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