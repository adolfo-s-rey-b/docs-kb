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
 / Serialization utilities

Serialization utilities
=======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/saving/serialization_lib.py#L128)

### `serialize_keras_object` function

Copied!

`tf_keras.utils.serialize_keras_object(obj)`

Retrieve the config dict by serializing the TF-Keras object.

`serialize_keras_object()` serializes a TF-Keras object to a python dictionary that represents the object, and is a reciprocal function of `deserialize_keras_object()`. See `deserialize_keras_object()` for more information about the config format.

**Arguments**

*   **obj**: the TF-Keras object to serialize.

**Returns**

A python dict that represents the object. The python dict can be deserialized via `deserialize_keras_object()`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/saving/serialization_lib.py#L405)

### `deserialize_keras_object` function

Copied!

`tf_keras.utils.deserialize_keras_object(     config, custom_objects=None, safe_mode=True, **kwargs )`

Retrieve the object by deserializing the config dict.

The config dict is a Python dictionary that consists of a set of key-value pairs, and represents a TF-Keras object, such as an `Optimizer`, `Layer`, `Metrics`, etc. The saving and loading library uses the following keys to record information of a TF-Keras object:

*   `class_name`: String. This is the name of the class, as exactly defined in the source code, such as "LossesContainer".
*   `config`: Dict. Library-defined or user-defined key-value pairs that store the configuration of the object, as obtained by `object.get_config()`.
*   `module`: String. The path of the python module, such as "keras.engine.compile\_utils". Built-in TF-Keras classes expect to have prefix `keras`.
*   `registered_name`: String. The key the class is registered under via `keras.saving.register_keras_serializable(package, name)` API. The key has the format of '{package}>{name}', where `package` and `name` are the arguments passed to `register_keras_serializable()`. If `name` is not provided, it uses the class name. If `registered_name` successfully resolves to a class (that was registered), the `class_name` and `config` values in the dict will not be used. `registered_name` is only used for non-built-in classes.

For example, the following dictionary represents the built-in Adam optimizer with the relevant config:

Copied!

``dict_structure = {     "class_name": "Adam",     "config": {         "amsgrad": false,         "beta_1": 0.8999999761581421,         "beta_2": 0.9990000128746033,         "decay": 0.0,         "epsilon": 1e-07,         "learning_rate": 0.0010000000474974513,         "name": "Adam"     },     "module": "keras.optimizers",     "registered_name": None } # Returns an `Adam` instance identical to the original one. deserialize_keras_object(dict_structure)``

If the class does not have an exported TF-Keras namespace, the library tracks it by its `module` and `class_name`. For example:

Copied!

``dict_structure = {   "class_name": "LossesContainer",   "config": {       "losses": [...],       "total_loss_mean": {...},   },   "module": "keras.engine.compile_utils",   "registered_name": "LossesContainer" }  # Returns a `LossesContainer` instance identical to the original one. deserialize_keras_object(dict_structure)``

And the following dictionary represents a user-customized `MeanSquaredError` loss:

Copied!

``@keras.saving.register_keras_serializable(package='my_package') class ModifiedMeanSquaredError(keras.losses.MeanSquaredError):   ...  dict_structure = {     "class_name": "ModifiedMeanSquaredError",     "config": {         "fn": "mean_squared_error",         "name": "mean_squared_error",         "reduction": "auto"     },     "registered_name": "my_package>ModifiedMeanSquaredError" } # Returns the `ModifiedMeanSquaredError` object deserialize_keras_object(dict_structure)``

**Arguments**

*   **config**: Python dict describing the object.
*   **custom\_objects**: Python dict containing a mapping between custom object names the corresponding classes or functions.
*   **safe\_mode**: Boolean, whether to disallow unsafe `lambda` deserialization. When `safe_mode=False`, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the TF-Keras v3 model format. Defaults to `True`.

**Returns**

The object described by the `config` dictionary.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/saving/object_registration.py#L29)

### `CustomObjectScope` class

Copied!

`tf_keras.saving.custom_object_scope(*args)`

Exposes custom classes/functions to TF-Keras deserialization internals.

Under a scope `with custom_object_scope(objects_dict)`, TF-Keras methods such as [`tf.keras.models.load_model`](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
 or [`tf.keras.models.model_from_config`](https://www.tensorflow.org/api_docs/python/tf/keras/models/model_from_config)
 will be able to deserialize any custom object referenced by a saved config (e.g. a custom layer or metric).

**Example**

Consider a custom regularizer `my_regularizer`:

Copied!

``layer = Dense(3, kernel_regularizer=my_regularizer) # Config contains a reference to `my_regularizer` config = layer.get_config() ... # Later: with custom_object_scope({'my_regularizer': my_regularizer}):   layer = Dense.from_config(config)``

**Arguments**

*   **\*args**: Dictionary or dictionaries of `{name: object}` pairs.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/saving/object_registration.py#L75)

### `get_custom_objects` function

Copied!

`tf_keras.saving.get_custom_objects()`

Retrieves a live reference to the global dictionary of custom objects.

Custom objects set using using `custom_object_scope` are not added to the global dictionary of custom objects, and will not appear in the returned dictionary.

**Example**

Copied!

`get_custom_objects().clear() get_custom_objects()['MyObject'] = MyObject`

**Returns**

Global dictionary mapping registered class names to classes.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/saving/object_registration.py#L98)

### `register_keras_serializable` function

Copied!

`tf_keras.saving.register_keras_serializable(package="Custom", name=None)`

Registers an object with the TF-Keras serialization framework.

This decorator injects the decorated class or function into the TF-Keras custom object dictionary, so that it can be serialized and deserialized without needing an entry in the user-provided custom object dict. It also injects a function that TF-Keras will call to get the object's serializable string key.

Note that to be serialized and deserialized, classes must implement the `get_config()` method. Functions do not have this requirement.

The object will be registered under the key 'package>name' where `name`, defaults to the object name if not passed.

**Example**

Copied!

``# Note that `'my_package'` is used as the `package` argument here, and since # the `name` argument is not provided, `'MyDense'` is used as the `name`. @keras.saving.register_keras_serializable('my_package') class MyDense(keras.layers.Dense):   pass  assert keras.saving.get_registered_object('my_package>MyDense') == MyDense assert keras.saving.get_registered_name(MyDense) == 'my_package>MyDense'``

**Arguments**

*   **package**: The package that this class belongs to. This is used for the `key` (which is `"package>name"`) to idenfify the class. Note that this is the first argument passed into the decorator.
*   **name**: The name to serialize this class under in this package. If not provided or `None`, the class' name will be used (note that this is the case when the decorator is used with only one argument, which becomes the `package`).

**Returns**

A decorator that registers the decorated class with the passed names.

* * *

[Serialization utilities](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#serialization-utilities)

[`serialize_keras_object` function](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#serializekerasobject-function)

[`deserialize_keras_object` function](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#deserializekerasobject-function)

[`CustomObjectScope` class](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#customobjectscope-class)

[`get_custom_objects` function](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#getcustomobjects-function)

[`register_keras_serializable` function](https://keras.io/2/api/models/model_saving_apis/serialization_utils/#registerkerasserializable-function)