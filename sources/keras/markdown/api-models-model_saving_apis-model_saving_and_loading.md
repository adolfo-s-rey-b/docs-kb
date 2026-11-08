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
 / Whole model saving & loading

Whole model saving & loading
============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L273)

### `save` method

Copied!

`Model.save(filepath, overwrite=True, zipped=None, **kwargs)`

Saves a model as a `.keras` file.

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file contains:

*   The model's configuration (architecture)
*   The model's weights
*   The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. The path where to save the model. Must end in `.keras` (unless saving the model as an unzipped directory via `zipped=False`).
*   **overwrite**: Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt.
*   **zipped**: Whether to save the model as a zipped `.keras` archive (default when saving locally), or as an unzipped directory (default when saving on the Hugging Face Hub).

**Example**

Copied!

`model = keras.Sequential(     [         keras.layers.Dense(5, input_shape=(3,)),         keras.layers.Softmax(),     ], ) model.save("model.keras") loaded_model = keras.saving.load_model("model.keras") x = keras.random.uniform((10, 3)) assert np.allclose(model.predict(x), loaded_model.predict(x))`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/saving_api.py#L19)

### `save_model` function

Copied!

`keras.saving.save_model(model, filepath, overwrite=True, zipped=None, **kwargs)`

Saves a model as a `.keras` file.

**Arguments**

*   **model**: Keras model instance to be saved.
*   **filepath**: `str` or `pathlib.Path` object. Path where to save the model.
*   **overwrite**: Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt.
*   **zipped**: Whether to save the model as a zipped `.keras` archive (default when saving locally), or as an unzipped directory (default when saving on the Hugging Face Hub).

**Example**

Copied!

`model = keras.Sequential(     [         keras.layers.Dense(5, input_shape=(3,)),         keras.layers.Softmax(),     ], ) model.save("model.keras") loaded_model = keras.saving.load_model("model.keras") x = keras.random.uniform((10, 3)) assert np.allclose(model.predict(x), loaded_model.predict(x))`

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file is a `zip` archive that contains:

*   The model's configuration (architecture)
*   The model's weights
*   The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/saving_api.py#L125)

### `load_model` function

Copied!

`keras.saving.load_model(filepath, custom_objects=None, compile=True, safe_mode=True)`

Loads a model saved via `model.save()` or from an Orbax checkpoint.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object, path to the saved model file or Orbax checkpoint directory.
*   **custom\_objects**: Optional dictionary mapping names (strings) to custom classes or functions to be considered during deserialization.
*   **compile**: Boolean, whether to compile the model after loading.
*   **safe\_mode**: Boolean, whether to disallow unsafe `lambda` deserialization. When `safe_mode=False`, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the Keras v3 model format. Defaults to `True`.

**Returns**

A Keras model instance. If the original model was compiled, and the argument `compile=True` is set, then the returned model will be compiled. Otherwise, the model will be left uncompiled.

**Example**

Copied!

`model = keras.Sequential([     keras.layers.Dense(5, input_shape=(3,)),     keras.layers.Softmax()]) model.save("model.keras") loaded_model = keras.saving.load_model("model.keras")`

Note that the model variables may have different name values (`var.name` property, e.g. `"dense_1/kernel:0"`) after being reloaded. It is recommended that you use layer attributes to access specific variables, e.g. `model.get_layer("dense_1").kernel`.

**Guides and examples using `load_model`**

*   [Orbax Checkpointing in Keras](https://keras.io/guides/orbax_checkpoint/)
    
*   [8-bit integer quantization in Keras](https://keras.io/guides/int8_quantization_in_keras/)
    
*   [4-bit integer quantization in Keras](https://keras.io/guides/int4_quantization_in_keras/)
    
*   [Writing quantization-compatible layers in Keras](https://keras.io/guides/writing_quantization_compatible_layers/)
    
*   [The Functional API](https://keras.io/guides/functional_api/)
    
*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
    
*   [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
    
*   [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
    

* * *

[Whole model saving & loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#whole-model-saving-amp-loading)

[`save` method](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#save-method)

[`save_model` function](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#savemodel-function)

[`load_model` function](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#loadmodel-function)