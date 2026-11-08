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
 / Model export for inference

Model export for inference
==========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L654)

### `export` method

Copied!

`Model.export(     filepath, format="tf_saved_model", verbose=None, input_signature=None, **kwargs )`

Export the model as an artifact for inference.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. The path to save the artifact.
*   **format**: `str`. The export format. Supported values: `"tf_saved_model"`, `"onnx"`, `"openvino"`, `"litert"`, and `"torch"`. Defaults to `"tf_saved_model"`.
*   **verbose**: `bool`. Whether to print a message during export. Defaults to `None`, which uses the default value set by different backends and formats.
*   **input\_signature**: Optional. Specifies the shape and dtype of the model inputs. Can be a structure of [`keras.InputSpec`](https://keras.io/api/layers/core_layers/input_spec#inputspec-class)
    , [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
    , `backend.KerasTensor`, or backend tensor. If not provided, it will be automatically computed. Defaults to `None`. Note: With `format="litert"` and the PyTorch backend, dynamic input shapes are not supported. Any dynamic dimensions (i.e., `None` in input shapes) will be automatically replaced with `1` during export, which may cause runtime failures for other shapes. You must explicitly pass a fixed static `input_signature` matching your maximum runtime shape.
*   **\*\*kwargs**: Additional keyword arguments.
    *   `is_static`: Optional `bool`. Specific to the JAX backend and `format="tf_saved_model"`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds and counters).
    *   `jax2tf_kwargs`: Optional `dict`. Specific to the JAX backend and `format="tf_saved_model"`. Arguments for `jax2tf.convert`. See the documentation for [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)
        . If `native_serialization` and `polymorphic_shapes` are not provided, they will be automatically computed.
    *   `opset_version`: Optional `int`. Specific to `format="onnx"`. An integer value that specifies the ONNX opset version.
    *   LiteRT-specific options: Optional keyword arguments specific to `format="litert"`. These are passed directly to the TensorFlow Lite converter on the TensorFlow backend and include options like `optimizations`, `representative_dataset`, `experimental_new_quantizer`, `allow_custom_ops`, `enable_select_tf_ops`, etc. On the PyTorch backend, LiteRT export accepts `optimizations` plus the installed `litert_torch.convert()` keyword arguments such as `strict_export`, `dynamic_shapes` (note that standard ops do not support dynamic shapes, as noted below), `lightweight_conversion`, `enable_x64`, `runtime_constant_folding`, and `quant_config`.
    *   PyTorch export options: Optional keyword arguments specific to `format="torch"`. These are passed directly to `torch.export.export` and include `strict`, `dynamic_shapes`, `prefer_deferred_runtime_asserts_over_guards`, and `preserve_module_call_signature`.

**Note on LiteRT (TFLite) Export with PyTorch Backend:** With the PyTorch backend, LiteRT export (`format="litert"`) does not support dynamic input shapes. If no static signature is provided, any dynamic dimensions (represented as `None`) are automatically replaced with `1` during export. This can lead to runtime failures for other shapes. You must explicitly specify a fixed static `input_signature` (matching your maximum runtime dimensions) and pad your inputs to this static shape at runtime.

**Note:** This feature is currently supported only with TensorFlow, JAX and Torch backends.

**Note:** Be aware that the exported artifact may contain information from the local file system when using `format="onnx"`, `verbose=True` and Torch backend.

**Examples**

Here's how to export a TensorFlow SavedModel for inference.

Copied!

`# Export the model as a TensorFlow SavedModel artifact model.export("path/to/location", format="tf_saved_model")  # Load the artifact in a different process/environment reloaded_artifact = tf.saved_model.load("path/to/location") predictions = reloaded_artifact.serve(input_data)`

Here's how to export an ONNX for inference.

Copied!

`# Export the model as a ONNX artifact model.export("path/to/location", format="onnx")  # Load the artifact in a different process/environment ort_session = onnxruntime.InferenceSession("path/to/location") ort_inputs = {     k.name: v for k, v in zip(ort_session.get_inputs(), input_data) } predictions = ort_session.run(None, ort_inputs)`

Here's how to export a LiteRT (TFLite) for inference.

Copied!

`# Export the model as a LiteRT artifact model.export("path/to/location", format="litert")  # Load the artifact in a different process/environment interpreter = tf.lite.Interpreter(model_path="path/to/location") interpreter.allocate_tensors() interpreter.set_tensor(     interpreter.get_input_details()[0]['index'], input_data ) interpreter.invoke() output_data = interpreter.get_tensor(     interpreter.get_output_details()[0]['index'] )`

Here's how to export a PyTorch ExportedProgram for inference.

Copied!

`# Export the model as a PyTorch ExportedProgram artifact model.export("path/to/model.pt2", format="torch")  # Load the artifact in a different process/environment import torch loaded_program = torch.export.load("path/to/model.pt2") predictions = loaded_program.module()(input_tensor)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L112)

### `ExportArchive` class

Copied!

`keras.export.ExportArchive()`

ExportArchive is used to write SavedModel artifacts for inference.

If you have a Keras model or layer that you want to export as SavedModel for serving (e.g. via TensorFlow-Serving), you can use `ExportArchive` to configure the different serving endpoints you need to make available, as well as their signatures. Simply instantiate an `ExportArchive`, use `track()` to register the layer(s) or model(s) to be used, then use the `add_endpoint()` method to register a new serving endpoint. When done, use the `write_out()` method to save the artifact.

The resulting artifact is a SavedModel and can be reloaded via [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
.

**Examples**

Here's how to export a model for inference.

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")], ) export_archive.write_out("path/to/location")  # Elsewhere, we can reload the artifact and serve it. # The endpoint we added is available as a method: serving_model = tf.saved_model.load("path/to/location") outputs = serving_model.serve(inputs)`

Here's how to export a model with one endpoint for inference and one endpoint for a training-mode forward pass (e.g. with dropout on).

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="call_inference",     fn=lambda x: model.call(x, training=False),     input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")], ) export_archive.add_endpoint(     name="call_training",     fn=lambda x: model.call(x, training=True),     input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")], ) export_archive.write_out("path/to/location")`

**Note on resource tracking:**

`ExportArchive` is able to automatically track all `keras.Variables` used by its endpoints, so most of the time calling `.track(model)` is not strictly required. However, if your model uses lookup layers such as `IntegerLookup`, `StringLookup`, or `TextVectorization`, it will need to be tracked explicitly via `.track(model)`.

Explicit tracking is also required if you need to be able to access the properties `variables`, `trainable_variables`, or `non_trainable_variables` on the revived archive.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L204)

### `add_endpoint` method

Copied!

`ExportArchive.add_endpoint(name, fn, input_signature=None, **kwargs)`

Register a new serving endpoint.

**Arguments**

*   **name**: `str`. The name of the endpoint.
*   **fn**: A callable. It should only leverage resources (e.g. [`keras.Variable`](https://keras.io/api/layers/base_layer#variable-class)
     objects or [`tf.lookup.StaticHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticHashTable)
     objects) that are available on the models/layers tracked by the `ExportArchive` (you can call `.track(model)` to track a new model). The shape and dtype of the inputs to the function must be known. For that purpose, you can either 1) make sure that `fn` is a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     that has been called at least once, or 2) provide an `input_signature` argument that specifies the shape and dtype of the inputs (see below).
*   **input\_signature**: Optional. Specifies the shape and dtype of `fn`. Can be a structure of [`keras.InputSpec`](https://keras.io/api/layers/core_layers/input_spec#inputspec-class)
    , [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
    , `backend.KerasTensor`, or backend tensor (see below for an example showing a `Functional` model with 2 input arguments). If not provided, `fn` must be a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     that has been called at least once. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments:
    *   Specific to the JAX backend: - `is_static`: Optional `bool`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds). - `jax2tf_kwargs`: Optional `dict`. Arguments for `jax2tf.convert`. See [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)
        . If `native_serialization` and `polymorphic_shapes` are not provided, they are automatically computed.

**Returns**

The [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 wrapping `fn` that was added to the archive.

**Example**

Adding an endpoint using the `input_signature` argument when the model has a single input argument:

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")], )`

Adding an endpoint using the `input_signature` argument when the model has two positional input arguments:

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[         keras.InputSpec(shape=(None, 3), dtype="float32"),         keras.InputSpec(shape=(None, 4), dtype="float32"),     ], )`

Adding an endpoint using the `input_signature` argument when the model has one input argument that is a list of 2 tensors (e.g. a Functional model with 2 inputs):

Copied!

`model = keras.Model(inputs=[x1, x2], outputs=outputs)  export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[         [             keras.InputSpec(shape=(None, 3), dtype="float32"),             keras.InputSpec(shape=(None, 4), dtype="float32"),         ],     ], )`

This also works with dictionary inputs:

Copied!

`model = keras.Model(inputs={"x1": x1, "x2": x2}, outputs=outputs)  export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[         {             "x1": keras.InputSpec(shape=(None, 3), dtype="float32"),             "x2": keras.InputSpec(shape=(None, 4), dtype="float32"),         },     ], )`

Adding an endpoint that is a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
:

Copied!

`@tf.function() def serving_fn(x):     return model(x)  # The function must be traced, i.e. it must be called at least once. serving_fn(tf.random.normal(shape=(2, 3)))  export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(name="serve", fn=serving_fn)`

Combining a model with some TensorFlow preprocessing, which can use TensorFlow resources:

Copied!

`lookup_table = tf.lookup.StaticHashTable(initializer, default_value=0.0)  export_archive = ExportArchive() model_fn = export_archive.track_and_add_endpoint(     "model_fn",     model,     input_signature=[tf.TensorSpec(shape=(None, 5), dtype=tf.float32)], ) export_archive.track(lookup_table)  @tf.function() def serving_fn(x):     x = lookup_table.lookup(x)     return model_fn(x)  export_archive.add_endpoint(name="serve", fn=serving_fn)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L383)

### `add_variable_collection` method

Copied!

`ExportArchive.add_variable_collection(name, variables)`

Register a set of variables to be retrieved after reloading.

**Arguments**

*   **name**: The string name for the collection.
*   **variables**: A tuple/list/set of [`keras.Variable`](https://keras.io/api/layers/base_layer#variable-class)
     instances.

**Example**

Copied!

`export_archive = ExportArchive() export_archive.track(model) # Register an endpoint export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")], ) # Save a variable collection export_archive.add_variable_collection(     name="optimizer_variables", variables=model.optimizer.variables) export_archive.write_out("path/to/location")  # Reload the object revived_object = tf.saved_model.load("path/to/location") # Retrieve the variables optimizer_variables = revived_object.optimizer_variables`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L187)

### `track` method

Copied!

`ExportArchive.track(resource)`

Track the variables (of a layer or model) and other assets.

By default, all variables used by an endpoint function are automatically tracked when you call `add_endpoint()`. However, non-variables assets such as lookup tables need to be tracked manually. Note that lookup tables used by built-in Keras layers (`TextVectorization`, `IntegerLookup`, `StringLookup`) are automatically tracked by `add_endpoint()`.

**Arguments**

*   **resource**: A layer, model or a TensorFlow trackable resource.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L416)

### `write_out` method

Copied!

`ExportArchive.write_out(filepath, options=None, verbose=True)`

Write the corresponding SavedModel to disk.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. Path where to save the artifact.
*   **options**: [`tf.saved_model.SaveOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)
     object that specifies SavedModel saving options.
*   **verbose**: whether to print all the variables of an exported SavedModel.

**Note on TF-Serving**: all endpoints registered via `add_endpoint()` are made visible for TF-Serving in the SavedModel artifact. In addition, the first endpoint registered is made visible under the alias `"serving_default"` (unless an endpoint with the name `"serving_default"` was already registered manually), since TF-Serving requires this endpoint to be set.

* * *

[Model export for inference](https://keras.io/api/models/model_saving_apis/export/#model-export-for-inference)

[`export` method](https://keras.io/api/models/model_saving_apis/export/#export-method)

[`ExportArchive` class](https://keras.io/api/models/model_saving_apis/export/#exportarchive-class)

[`add_endpoint` method](https://keras.io/api/models/model_saving_apis/export/#addendpoint-method)

[`add_variable_collection` method](https://keras.io/api/models/model_saving_apis/export/#addvariablecollection-method)

[`track` method](https://keras.io/api/models/model_saving_apis/export/#track-method)

[`write_out` method](https://keras.io/api/models/model_saving_apis/export/#writeout-method)