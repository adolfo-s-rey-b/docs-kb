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
 / Weights-only saving & loading

Weights-only saving & loading
=============================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3035)

### `get_weights` method

Copied!

`Model.get_weights()`

Retrieves the weights of the model.

**Returns**

A flat list of Numpy arrays.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/base_layer.py#L1736)

### `set_weights` method

Copied!

`Model.set_weights(weights)`

Sets the weights of the layer, from NumPy arrays.

The weights of a layer represent the state of the layer. This function sets the weight values from numpy arrays. The weight values should be passed in the order they are created by the layer. Note that the layer's weights must be instantiated before calling this function, by calling the layer.

For example, a `Dense` layer returns a list of two values: the kernel matrix and the bias vector. These can be used to set the weights of another `Dense` layer:

Copied!

`>>> layer_a = tf.keras.layers.Dense(1, ...   kernel_initializer=tf.constant_initializer(1.)) >>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]])) >>> layer_a.get_weights() [array([[1.],        [1.],        [1.]], dtype=float32), array([0.], dtype=float32)] >>> layer_b = tf.keras.layers.Dense(1, ...   kernel_initializer=tf.constant_initializer(2.)) >>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]])) >>> layer_b.get_weights() [array([[2.],        [2.],        [2.]], dtype=float32), array([0.], dtype=float32)] >>> layer_b.set_weights(layer_a.get_weights()) >>> layer_b.get_weights() [array([[1.],        [1.],        [1.]], dtype=float32), array([0.], dtype=float32)]`

**Arguments**

*   **weights**: a list of NumPy arrays. The number of arrays and their shape must match number of the dimensions of the weights of the layer (i.e. it should match the output of `get_weights`).

**Raises**

*   **ValueError**: If the provided weights list does not match the layer's specifications.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3106)

### `save_weights` method

Copied!

`Model.save_weights(filepath, overwrite=True, save_format=None, options=None)`

Saves all layer weights.

Either saves in HDF5 or in TensorFlow format based on the `save_format` argument.

When saving in HDF5 format, the weight file has: - `layer_names` (attribute), a list of strings (ordered names of model layers). - For every layer, a `group` named `layer.name` - For every such layer group, a group attribute `weight_names`, a list of strings (ordered names of weights tensor of the layer). - For every weight in the layer, a dataset storing the weight value, named after the weight tensor.

When saving in TensorFlow format, all objects referenced by the network are saved in the same format as [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
, including any `Layer` instances or `Optimizer` instances assigned to object attributes. For networks constructed from inputs and outputs using `tf.keras.Model(inputs, outputs)`, `Layer` instances used by the network are tracked/saved automatically. For user-defined classes which inherit from [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
, `Layer` instances must be assigned to object attributes, typically in the constructor. See the documentation of [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 and [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 for details.

While the formats are the same, do not mix `save_weights` and [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
. Checkpoints saved by `Model.save_weights` should be loaded using `Model.load_weights`. Checkpoints saved using [`tf.train.Checkpoint.save`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 should be restored using the corresponding [`tf.train.Checkpoint.restore`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
. Prefer [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 over `save_weights` for training checkpoints.

The TensorFlow format matches objects and variables by starting at a root object, `self` for `save_weights`, and greedily matching attribute names. For `Model.save` this is the `Model`, and for `Checkpoint.save` this is the `Checkpoint` even if the `Checkpoint` has a model attached. This means saving a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 using `save_weights` and loading into a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 with a `Model` attached (or vice versa) will not match the `Model`'s variables. See the [guide to training checkpoints](https://www.tensorflow.org/guide/checkpoint)
 for details on the TensorFlow format.

**Arguments**

*   **filepath**: String or PathLike, path to the file to save the weights to. When saving in TensorFlow format, this is the prefix used for checkpoint files (multiple files are generated). Note that the '.h5' suffix causes weights to be saved in HDF5 format.
*   **overwrite**: Whether to silently overwrite any existing file at the target location, or provide the user with a manual prompt.
*   **save\_format**: Either 'tf' or 'h5'. A `filepath` ending in '.h5' or '.keras' will default to HDF5 if `save_format` is `None`. Otherwise, `None` becomes 'tf'. Defaults to `None`.
*   **options**: Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)
     object that specifies options for saving weights.

**Raises**

*   **ImportError**: If `h5py` is not available when attempting to save in HDF5 format.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/engine/training.py#L3178)

### `load_weights` method

Copied!

`Model.load_weights(filepath, skip_mismatch=False, by_name=False, options=None)`

Loads all layer weights from a saved files.

The saved file could be a SavedModel file, a `.keras` file (v3 saving format), or a file created via `model.save_weights()`.

By default, weights are loaded based on the network's topology. This means the architecture should be the same as when the weights were saved. Note that layers that don't have weights are not taken into account in the topological ordering, so adding or removing layers is fine as long as they don't have weights.

**Partial weight loading**

If you have modified your model, for instance by adding a new layer (with weights) or by changing the shape of the weights of a layer, you can choose to ignore errors and continue loading by setting `skip_mismatch=True`. In this case any layer with mismatching weights will be skipped. A warning will be displayed for each skipped layer.

**Weight loading by name**

If your weights are saved as a `.h5` file created via `model.save_weights()`, you can use the argument `by_name=True`.

In this case, weights are loaded into layers only if they share the same name. This is useful for fine-tuning or transfer-learning models where some of the layers have changed.

Note that only topological loading (`by_name=False`) is supported when loading weights from the `.keras` v3 format or from the TensorFlow SavedModel format.

**Arguments**

*   **filepath**: String, path to the weights file to load. For weight files in TensorFlow format, this is the file prefix (the same as was passed to `save_weights()`). This can also be a path to a SavedModel or a `.keras` file (v3 saving format) saved via `model.save()`.
*   **skip\_mismatch**: Boolean, whether to skip loading of layers where there is a mismatch in the number of weights, or a mismatch in the shape of the weights.
*   **by\_name**: Boolean, whether to load weights by name or by topological order. Only topological loading is supported for weight files in the `.keras` v3 format or in the TensorFlow SavedModel format.
*   **options**: Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)
     object that specifies options for loading weights (only valid for a SavedModel file).

* * *

[Weights-only saving & loading](https://keras.io/2/api/models/model_saving_apis/weights_saving_and_loading/#weightsonly-saving-amp-loading)

[`get_weights` method](https://keras.io/2/api/models/model_saving_apis/weights_saving_and_loading/#getweights-method)

[`set_weights` method](https://keras.io/2/api/models/model_saving_apis/weights_saving_and_loading/#setweights-method)

[`save_weights` method](https://keras.io/2/api/models/model_saving_apis/weights_saving_and_loading/#saveweights-method)

[`load_weights` method](https://keras.io/2/api/models/model_saving_apis/weights_saving_and_loading/#loadweights-method)