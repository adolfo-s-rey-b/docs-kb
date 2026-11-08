None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [The Model class](https://keras.io/2/api/models/model/)
 [The Sequential class](https://keras.io/2/api/models/sequential/)
 [Model training APIs](https://keras.io/2/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/2/api/models/model_saving_apis/)
 [Layers API](https://keras.io/2/api/layers/)
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
 / [Models API](https://keras.io/2/api/models/)
 / [Saving & serialization](https://keras.io/2/api/models/model_saving_apis/)
 / Model config serialization

Model config serialization
==========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3255)

### `get_config` method

Copied!

`Model.get_config()`

Returns the config of the `Model`.

Config is a Python dictionary (serializable) containing the configuration of an object, which in this case is a `Model`. This allows the `Model` to be be reinstantiated later (without its trained weights) from this configuration.

Note that `get_config()` does not guarantee to return a fresh copy of dict every time it is called. The callers should make a copy of the returned dict if they want to modify it.

Developers of subclassed `Model` are advised to override this method, and continue to update the dict from `super(MyModel, self).get_config()` to provide the proper configuration of this `Model`. The default config will return config dict for init parameters if they are basic types. Raises `NotImplementedError` when in cases where a custom `get_config()` implementation is required for the subclassed model.

**Returns**

Python dictionary containing the configuration of this `Model`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3295)

### `from_config` method

Copied!

`Model.from_config(config, custom_objects=None)`

Creates a layer from its config.

This method is the reverse of `get_config`, capable of instantiating the same layer from the config dictionary. It does not handle layer connectivity (handled by Network), nor weights (handled by `set_weights`).

**Arguments**

*   **config**: A Python dictionary, typically the output of get\_config.

**Returns**

A layer instance.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/models/cloning.py#L464)

### `clone_model` function

Copied!

`tf_keras.models.clone_model(model, input_tensors=None, clone_function=None)`

Clone a Functional or Sequential `Model` instance.

Model cloning is similar to calling a model on new inputs, except that it creates new layers (and thus new weights) instead of sharing the weights of the existing layers.

Note that `clone_model` will not preserve the uniqueness of shared objects within the model (e.g. a single variable attached to two distinct layers will be restored as two separate variables).

**Arguments**

*   **model**: Instance of `Model` (could be a Functional model or a Sequential model).
*   **input\_tensors**: optional list of input tensors or InputLayer objects to build the model upon. If not provided, new `Input` objects will be created.
*   **clone\_function**: Callable to be used to clone each layer in the target model (except `InputLayer` instances). It takes as argument the layer instance to be cloned, and returns the corresponding layer instance to be used in the model copy. If unspecified, this callable becomes the following serialization/deserialization function: `lambda layer: layer.__class__.from_config(layer.get_config())`. By passing a custom callable, you can customize your copy of the model, e.g. by wrapping certain layers of interest (you might want to replace all `LSTM` instances with equivalent `Bidirectional(LSTM(...))` instances, for example). Defaults to `None`.

**Returns**

An instance of `Model` reproducing the behavior of the original model, on top of new inputs tensors, using newly instantiated weights. The cloned model may behave differently from the original model if a custom `clone_function` modifies the layer.

**Example**

Copied!

`# Create a test Sequential model. model = keras.Sequential([     keras.Input(shape=(728,)),     keras.layers.Dense(32, activation='relu'),     keras.layers.Dense(1, activation='sigmoid'), ]) # Create a copy of the test model (with freshly initialized weights). new_model = clone_model(model)`

Note that subclassed models cannot be cloned, since their internal layer structure is not known. To achieve equivalent functionality as `clone_model` in the case of a subclassed model, simply make sure that the model class implements `get_config()` (and optionally `from_config()`), and call:

Copied!

`new_model = model.__class__.from_config(model.get_config())`

* * *

[Model config serialization](https://keras.io/2/api/models/model_saving_apis/model_config_serialization/#model-config-serialization)

[`get_config` method](https://keras.io/2/api/models/model_saving_apis/model_config_serialization/#getconfig-method)

[`from_config` method](https://keras.io/2/api/models/model_saving_apis/model_config_serialization/#fromconfig-method)

[`clone_model` function](https://keras.io/2/api/models/model_saving_apis/model_config_serialization/#clonemodel-function)