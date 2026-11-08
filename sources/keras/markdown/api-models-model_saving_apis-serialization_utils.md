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
 / Serialization utilities

Serialization utilities
=======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/serialization_lib.py#L151)

### `serialize_keras_object` function

Copied!

`keras.saving.serialize_keras_object(obj)`

Retrieve the config dict by serializing the Keras object.

`serialize_keras_object()` serializes a Keras object to a python dictionary that represents the object, and is a reciprocal function of `deserialize_keras_object()`. See `deserialize_keras_object()` for more information about the config format.

**Arguments**

*   **obj**: the Keras object to serialize.

**Returns**

A python dict that represents the object. The python dict can be deserialized via `deserialize_keras_object()`.

**Guides and examples using `serialize_keras_object`**

*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    
*   [Consistency training with supervision](https://keras.io/examples/vision/consistency_training/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/serialization_lib.py#L427)

### `deserialize_keras_object` function

Copied!

`keras.saving.deserialize_keras_object(     config, custom_objects=None, safe_mode=True, **kwargs )`

Retrieve the object by deserializing the config dict.

The config dict is a Python dictionary that consists of a set of key-value pairs, and represents a Keras object, such as an `Optimizer`, `Layer`, `Metrics`, etc. The saving and loading library uses the following keys to record information of a Keras object:

*   `class_name`: String. This is the name of the class, as exactly defined in the source code, such as "LossesContainer".
*   `config`: Dict. Library-defined or user-defined key-value pairs that store the configuration of the object, as obtained by `object.get_config()`.
*   `module`: String. The path of the python module. Built-in Keras classes expect to have prefix `keras`.
*   `registered_name`: String. The key the class is registered under via `keras.saving.register_keras_serializable(package, name)` API. The key has the format of '{package}>{name}', where `package` and `name` are the arguments passed to `register_keras_serializable()`. If `name` is not provided, it uses the class name. If `registered_name` successfully resolves to a class (that was registered), the `class_name` and `config` values in the dict will not be used. `registered_name` is only used for non-built-in classes.

For example, the following dictionary represents the built-in Adam optimizer with the relevant config:

Copied!

``dict_structure = {     "class_name": "Adam",     "config": {         "amsgrad": false,         "beta_1": 0.8999999761581421,         "beta_2": 0.9990000128746033,         "decay": 0.0,         "epsilon": 1e-07,         "learning_rate": 0.0010000000474974513,         "name": "Adam"     },     "module": "keras.optimizers",     "registered_name": None } # Returns an `Adam` instance identical to the original one. deserialize_keras_object(dict_structure)``

If the class does not have an exported Keras namespace, the library tracks it by its `module` and `class_name`. For example:

Copied!

``dict_structure = {   "class_name": "MetricsList",   "config": {       ...   },   "module": "keras.trainers.compile_utils",   "registered_name": "MetricsList" }  # Returns a `MetricsList` instance identical to the original one. deserialize_keras_object(dict_structure)``

And the following dictionary represents a user-customized `MeanSquaredError` loss:

Copied!

``@keras.saving.register_keras_serializable(package='my_package') class ModifiedMeanSquaredError(keras.losses.MeanSquaredError):   ...  dict_structure = {     "class_name": "ModifiedMeanSquaredError",     "config": {         "fn": "mean_squared_error",         "name": "mean_squared_error",         "reduction": "auto"     },     "registered_name": "my_package>ModifiedMeanSquaredError" } # Returns the `ModifiedMeanSquaredError` object deserialize_keras_object(dict_structure)``

**Arguments**

*   **config**: Python dict describing the object.
*   **custom\_objects**: Python dict containing a mapping between custom object names the corresponding classes or functions.
*   **safe\_mode**: Boolean, defaults to False. If True, disables unsafe lambda deserialization.
    
    Note that safe\_mode is designed to protect against code serialized within the Keras model file being loaded. It does not provide isolation from the local Python environment and does not guard against modifications made outside of the serialized file.
    

**Returns**

The object described by the `config` dictionary.

**Guides and examples using `deserialize_keras_object`**

*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
    
*   [Consistency training with supervision](https://keras.io/examples/vision/consistency_training/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L10)

### `CustomObjectScope` class

Copied!

`keras.saving.custom_object_scope(custom_objects)`

Exposes custom classes/functions to Keras deserialization internals.

Under a scope `with custom_object_scope(objects_dict)`, Keras methods such as `keras.models.load_model()` or `keras.models.model_from_config()` will be able to deserialize any custom object referenced by a saved config (e.g. a custom layer or metric).

**Example**

Consider a custom regularizer `my_regularizer`:

Copied!

``layer = Dense(3, kernel_regularizer=my_regularizer) # Config contains a reference to `my_regularizer` config = layer.get_config() ... # Later: with custom_object_scope({'my_regularizer': my_regularizer}):     layer = Dense.from_config(config)``

**Arguments**

*   **custom\_objects**: Dictionary of `{str: object}` pairs, where the `str` key is the object name.

**Guides and examples using `custom_object_scope`**

*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L68)

### `get_custom_objects` function

Copied!

`keras.saving.get_custom_objects()`

Retrieves a live reference to the global dictionary of custom objects.

Custom objects set using `custom_object_scope()` are not added to the global dictionary of custom objects, and will not appear in the returned dictionary.

**Example**

Copied!

`get_custom_objects().clear() get_custom_objects()['MyObject'] = MyObject`

**Returns**

Global dictionary mapping registered class names to classes.

**Guides and examples using `get_custom_objects`**

*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L94)

### `register_keras_serializable` function

Copied!

`keras.saving.register_keras_serializable(package="Custom", name=None)`

Registers an object with the Keras serialization framework.

This decorator injects the decorated class or function into the Keras custom object dictionary, so that it can be serialized and deserialized without needing an entry in the user-provided custom object dict. It also injects a function that Keras will call to get the object's serializable string key.

Note that to be serialized and deserialized, classes must implement the `get_config()` method. Functions do not have this requirement.

The object will be registered under the key `'package>name'` where `name`, defaults to the object name if not passed.

**Example**

Copied!

``# Note that `'my_package'` is used as the `package` argument here, and since # the `name` argument is not provided, `'MyDense'` is used as the `name`. @register_keras_serializable('my_package') class MyDense(keras.layers.Dense):     pass  assert get_registered_object('my_package>MyDense') == MyDense assert get_registered_name(MyDense) == 'my_package>MyDense'``

**Arguments**

*   **package**: The package that this class belongs to. This is used for the `key` (which is `"package>name"`) to identify the class. Note that this is the first argument passed into the decorator.
*   **name**: The name to serialize this class under in this package. If not provided or `None`, the class' name will be used (note that this is the case when the decorator is used with only one argument, which becomes the `package`).

**Returns**

A decorator that registers the decorated class with the passed names.

**Guides and examples using `register_keras_serializable`**

*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
    
*   [Writing quantization-compatible layers in Keras](https://keras.io/guides/writing_quantization_compatible_layers/)
    
*   [Denoising Diffusion Implicit Models](https://keras.io/examples/generative/ddim/)
    

* * *

[Serialization utilities](https://keras.io/api/models/model_saving_apis/serialization_utils/#serialization-utilities)

[`serialize_keras_object` function](https://keras.io/api/models/model_saving_apis/serialization_utils/#serializekerasobject-function)

[`deserialize_keras_object` function](https://keras.io/api/models/model_saving_apis/serialization_utils/#deserializekerasobject-function)

[`CustomObjectScope` class](https://keras.io/api/models/model_saving_apis/serialization_utils/#customobjectscope-class)

[`get_custom_objects` function](https://keras.io/api/models/model_saving_apis/serialization_utils/#getcustomobjects-function)

[`register_keras_serializable` function](https://keras.io/api/models/model_saving_apis/serialization_utils/#registerkerasserializable-function)