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
 / Weights-only saving & loading

Weights-only saving & loading
=============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L319)

### `save_weights` method

Copied!

`Model.save_weights(filepath, overwrite=True, max_shard_size=None)`

Saves all weights to a single file or sharded files.

By default, the weights will be saved in a single `.weights.h5` file. If sharding is enabled (`max_shard_size` is not `None`), the weights will be saved in multiple files, each with a size at most `max_shard_size` (in GB). Additionally, a configuration file `.weights.json` will contain the metadata for the sharded files.

The saved sharded files contain:

*   `*.weights.json`: The configuration file containing 'metadata' and 'weight\_map'.
*   `*_xxxxxx.weights.h5`: The sharded files containing only the weights.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`. If `.weights.h5` is provided, it will be overridden.
*   **overwrite**: Whether to overwrite any existing weights at the target location or instead ask the user via an interactive prompt.
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `None`.

**Example**

Copied!

``# Instantiate a EfficientNetV2L model with about 454MB of weights. model = keras.applications.EfficientNetV2L(weights=None)  # Save the weights in a single file. model.save_weights("model.weights.h5")  # Save the weights in sharded files. Use `max_shard_size=0.25` means # each sharded file will be at most ~250MB. model.save_weights("model.weights.json", max_shard_size=0.25)  # Load the weights in a new model with the same architecture. loaded_model = keras.applications.EfficientNetV2L(weights=None) loaded_model.load_weights("model.weights.h5") x = keras.random.uniform((1, 480, 480, 3)) assert np.allclose(model.predict(x), loaded_model.predict(x))  # Load the sharded weights in a new model with the same architecture. loaded_model = keras.applications.EfficientNetV2L(weights=None) loaded_model.load_weights("model.weights.json") x = keras.random.uniform((1, 480, 480, 3)) assert np.allclose(model.predict(x), loaded_model.predict(x))``

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L377)

### `load_weights` method

Copied!

`Model.load_weights(filepath, skip_mismatch=False, **kwargs)`

Load the weights from a single file or sharded files.

Weights are loaded based on the network's topology. This means the architecture should be the same as when the weights were saved. Note that layers that don't have weights are not taken into account in the topological ordering, so adding or removing layers is fine as long as they don't have weights.

**Partial weight loading**

If you have modified your model, for instance by adding a new layer (with weights) or by changing the shape of the weights of a layer, you can choose to ignore errors and continue loading by setting `skip_mismatch=True`. In this case any layer with mismatching weights will be skipped. A warning will be displayed for each skipped layer.

**Sharding**

When loading sharded weights, it is important to specify `filepath` that ends with `*.weights.json` which is used as the configuration file. Additionally, the sharded files `*_xxxxx.weights.h5` must be in the same directory as the configuration file.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`.
*   **skip\_mismatch**: Boolean, whether to skip loading of layers where there is a mismatch in the number of weights, or a mismatch in the shape of the weights.

**Example**

Copied!

`# Load the weights in a single file. model.load_weights("model.weights.h5")  # Load the weights in sharded files. model.load_weights("model.weights.json")`

* * *

[Weights-only saving & loading](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/#weightsonly-saving-amp-loading)

[`save_weights` method](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/#saveweights-method)

[`load_weights` method](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/#loadweights-method)