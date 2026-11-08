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
 / Keras weights file editor

Keras weights file editor
=========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L38)

### `KerasFileEditor` class

Copied!

`keras.saving.KerasFileEditor(filepath)`

Utility to inspect, edit, and resave Keras weights files.

You will find this class useful when adapting an old saved weights file after having made architecture changes to a model.

**Arguments**

*   **filepath**: The path to a local file to inspect and edit.

**Examples**

Copied!

`editor = KerasFileEditor("my_model.weights.h5")  # Displays current contents editor.summary()  # Remove the weights of an existing layer editor.delete_object("layers/dense_2")  # Add the weights of a new layer editor.add_object("layers/einsum_dense", weights={"0": ..., "1": ...})  # Save the weights of the edited model editor.resave_weights("edited_model.weights.h5")`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L112)

### `summary` method

Copied!

`KerasFileEditor.summary()`

Prints the weight structure of the opened file.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L116)

### `compare` method

Copied!

`KerasFileEditor.compare(reference_model)`

Compares the opened file to a reference model.

This method will list all mismatches between the currently opened file and the provided reference model.

**Arguments**

*   **reference\_model**: Model instance to compare to.

**Returns**

*   **Dict with the following keys**: `'status'`, `'error_count'`, `'match_count'`. Status can be `'success'` or `'error'`. `'error_count'` is the number of mismatches found. `'match_count'` is the number of matching weights found.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L416)

### `save` method

Copied!

`KerasFileEditor.save(filepath)`

Save the edited weights file.

**Arguments**

*   **filepath**: Path to save the file to. Must be a `.weights.h5` file.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L306)

### `rename_object` method

Copied!

`KerasFileEditor.rename_object(object_name, new_name)`

Rename an object in the file (e.g. a layer).

**Arguments**

*   **object\_name**: String, name or path of the object to rename (e.g. `"dense_2"` or `"layers/dense_2"`).
*   **new\_name**: String, new name of the object.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L322)

### `delete_object` method

Copied!

`KerasFileEditor.delete_object(object_name)`

Removes an object from the file (e.g. a layer).

**Arguments**

*   **object\_name**: String, name or path of the object to delete (e.g. `"dense_2"` or `"layers/dense_2"`).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L336)

### `add_object` method

Copied!

`KerasFileEditor.add_object(object_path, weights)`

Add a new object to the file (e.g. a layer).

**Arguments**

*   **object\_path**: String, full path of the object to add (e.g. `"layers/dense_2"`).
*   **weights**: Dict mapping weight names to weight values (arrays), e.g. `{"0": kernel_value, "1": bias_value}`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L369)

### `delete_weight` method

Copied!

`KerasFileEditor.delete_weight(object_name, weight_name)`

Removes a weight from an existing object.

**Arguments**

*   **object\_name**: String, name or path of the object from which to remove the weight (e.g. `"dense_2"` or `"layers/dense_2"`).
*   **weight\_name**: String, name of the weight to delete (e.g. `"0"`).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/file_editor.py#L392)

### `add_weights` method

Copied!

`KerasFileEditor.add_weights(object_name, weights)`

Add one or more new weights to an existing object.

**Arguments**

*   **object\_name**: String, name or path of the object to add the weights to (e.g. `"dense_2"` or `"layers/dense_2"`).
*   **weights**: Dict mapping weight names to weight values (arrays), e.g. `{"0": kernel_value, "1": bias_value}`.

* * *

[Keras weights file editor](https://keras.io/api/models/model_saving_apis/keras_file_editor/#keras-weights-file-editor)

[`KerasFileEditor` class](https://keras.io/api/models/model_saving_apis/keras_file_editor/#kerasfileeditor-class)

[`summary` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#summary-method)

[`compare` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#compare-method)

[`save` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#save-method)

[`rename_object` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#renameobject-method)

[`delete_object` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#deleteobject-method)

[`add_object` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#addobject-method)

[`delete_weight` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#deleteweight-method)

[`add_weights` method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#addweights-method)