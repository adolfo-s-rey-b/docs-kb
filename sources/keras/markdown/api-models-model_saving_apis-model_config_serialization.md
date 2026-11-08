None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [The Model class](https://keras.io/api/models/model/)
 [The Sequential class](https://keras.io/api/models/sequential/)
 [Model training APIs](https://keras.io/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/api/models/model_saving_apis/)
 [Knowledge distillation](https://keras.io/api/models/distillation/)
 [Layers API](https://keras.io/api/layers/)
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
 / [Models API](https://keras.io/api/models/)
 / [Saving & serialization](https://keras.io/api/models/model_saving_apis/)
 / Model config serialization

Model config serialization
==========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1743)

### `get_config` method

Copied!

`Model.get_config()`

Returns the config of the object.

An object config is a Python dictionary (serializable) containing the information needed to re-instantiate it.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L864)

### `from_config` method

Copied!

`Model.from_config(config, custom_objects=None)`

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

Note: If you override this method, you might receive a serialized dtype config, which is a `dict`. You can deserialize it as follows:

Copied!

`if "dtype" in config and isinstance(config["dtype"], dict):     policy = dtype_policies.deserialize(config["dtype"])`

**Arguments**

*   **config**: A Python dictionary, typically the output of `get_config`.

**Returns**

An operation instance.

**Guides and examples using `from_config`**

*   [The Functional API](https://keras.io/guides/functional_api/)
    
*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/cloning.py#L13)

### `clone_model` function

Copied!

`keras.models.clone_model(     model,     input_tensors=None,     clone_function=None,     call_function=None,     recursive=False,     **kwargs )`

Clone a Functional or Sequential `Model` instance.

Model cloning is similar to calling a model on new inputs, except that it creates new layers (and thus new weights) instead of sharing the weights of the existing layers.

Note that `clone_model` will not preserve the uniqueness of shared objects within the model (e.g. a single variable attached to two distinct layers will be restored as two separate variables).

**Arguments**

*   **model**: Instance of `Model` (could be a Functional model or a Sequential model).
*   **input\_tensors**: optional list of input tensors or InputLayer objects to build the model upon. If not provided, new `Input` objects will be created.
*   **clone\_function**: Callable with signature `fn(layer)` to be used to clone each layer in the target model (except `Input` instances). It takes as argument the layer instance to be cloned, and returns the corresponding layer instance to be used in the model copy. If unspecified, this callable defaults to the following serialization/deserialization function: `lambda layer: layer.__class__.from_config(layer.get_config())`. By passing a custom callable, you can customize your copy of the model, e.g. by wrapping certain layers of interest (you might want to replace all `LSTM` instances with equivalent `Bidirectional(LSTM(...))` instances, for example). Defaults to `None`.
*   **call\_function**: Callable with signature `fn(layer, *args, **kwargs)` to be used to call each cloned layer and a set of inputs. It takes the layer instance, the call arguments and keyword arguments, and returns the call outputs. If unspecified, this callable defaults to the regular `__call__()` method: `def fn(layer, *args, **kwargs): return layer(*args, **kwargs)`. By passing a custom callable, you can insert new layers before or after a given layer. Note: this argument can only be used with Functional models.
*   **recursive**: Boolean. Whether to recursively clone any Sequential or Functional models encountered in the original Sequential/Functional model. If `False`, then inner models are cloned by calling `clone_function()`. If `True`, then inner models are cloned by calling `clone_model()` with the same `clone_function`, `call_function`, and `recursive` arguments. Note that in this case, `call_function` will not be propagated to any Sequential model (since it is not applicable to Sequential models).

**Returns**

An instance of `Model` reproducing the behavior of the original model, on top of new inputs tensors, using newly instantiated weights. The cloned model may behave differently from the original model if a custom `clone_function` or `call_function` modifies a layer or layer call.

**Example**

Copied!

`# Create a test Sequential model. model = keras.Sequential([     keras.layers.Input(shape=(728,)),     keras.layers.Dense(32, activation='relu'),     keras.layers.Dense(1, activation='sigmoid'), ]) # Create a copy of the test model (with freshly initialized weights). new_model = clone_model(model)`

Using a `clone_function` to make a model deterministic by setting the random seed everywhere:

Copied!

`def clone_function(layer):     config = layer.get_config()     if "seed" in config:         config["seed"] = 1337     return layer.__class__.from_config(config)  new_model = clone_model(model, clone_function=clone_function)`

Using a `call_function` to add a `Dropout` layer after each `Dense` layer (without recreating new layers):

Copied!

`def call_function(layer, *args, **kwargs):     out = layer(*args, **kwargs)     if isinstance(layer, keras.layers.Dense):         out = keras.layers.Dropout(0.5)(out)     return out  new_model = clone_model(     model,     clone_function=lambda x: x,  # Reuse the same layers.     call_function=call_function, )`

Note that subclassed models cannot be cloned by default, since their internal layer structure is not known. To achieve equivalent functionality as `clone_model` in the case of a subclassed model, simply make sure that the model class implements `get_config()` (and optionally `from_config()`), and call:

Copied!

`new_model = model.__class__.from_config(model.get_config())`

In the case of a subclassed model, you cannot using a custom `clone_function`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L1098)

### `model_from_json` function

Copied!

`keras.models.model_from_json(json_string, custom_objects=None)`

Parses a JSON model configuration string and returns a model instance.

**Example**

Copied!

`>>> model = keras.Sequential([ ...     keras.layers.Dense(5, input_shape=(3,)), ...     keras.layers.Softmax()]) >>> config = model.to_json() >>> loaded_model = keras.models.model_from_json(config)`

**Arguments**

*   **json\_string**: JSON string encoding a model configuration.
*   **custom\_objects**: Optional dictionary mapping names (strings) to custom classes or functions to be considered during deserialization.

**Returns**

A Keras model instance (uncompiled).

* * *

[Model config serialization](https://keras.io/api/models/model_saving_apis/model_config_serialization/#model-config-serialization)

[`get_config` method](https://keras.io/api/models/model_saving_apis/model_config_serialization/#getconfig-method)

[`from_config` method](https://keras.io/api/models/model_saving_apis/model_config_serialization/#fromconfig-method)

[`clone_model` function](https://keras.io/api/models/model_saving_apis/model_config_serialization/#clonemodel-function)

[`model_from_json` function](https://keras.io/api/models/model_saving_apis/model_config_serialization/#modelfromjson-function)