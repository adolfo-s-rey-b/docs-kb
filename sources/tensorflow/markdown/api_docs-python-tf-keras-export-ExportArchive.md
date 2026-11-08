[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#methods)
    *   [add\_endpoint](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#add_endpoint)
        
    *   [add\_variable\_collection](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#add_variable_collection)
        
    *   [track](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#track)
        
    *   [track\_and\_add\_endpoint](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#track_and_add_endpoint)
        
    *   [write\_out](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#write_out)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.export.ExportArchive Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#methods)
    *   [add\_endpoint](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#add_endpoint)
        
    *   [add\_variable\_collection](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#add_variable_collection)
        
    *   [track](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#track)
        
    *   [track\_and\_add\_endpoint](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#track_and_add_endpoint)
        
    *   [write\_out](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive#write_out)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L112-L436)

ExportArchive is used to write SavedModel artifacts for inference.

tf.keras.export.ExportArchive(
        format='saved_model', **kwargs
    )

If you have a Keras model or layer that you want to export as SavedModel for serving (e.g. via TensorFlow-Serving), you can use `ExportArchive` to configure the different serving endpoints you need to make available, as well as their signatures. Simply instantiate an `ExportArchive`, use `track()` to register the layer(s) or model(s) to be used, then use the `add_endpoint()` method to register a new serving endpoint. When done, use the `write_out()` method to save the artifact.

The resulting artifact is a SavedModel and can be reloaded via [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
.

#### Examples:

Here's how to export a model for inference.

export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
    )
    export_archive.write_out("path/to/location")
    
    # Elsewhere, we can reload the artifact and serve it.
    # The endpoint we added is available as a method:
    serving_model = tf.saved_model.load("path/to/location")
    outputs = serving_model.serve(inputs)

Here's how to export a model with one endpoint for inference and one endpoint for a training-mode forward pass (e.g. with dropout on).

export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="call_inference",
        fn=lambda x: model.call(x, training=False),
        input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
    )
    export_archive.add_endpoint(
        name="call_training",
        fn=lambda x: model.call(x, training=True),
        input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
    )
    export_archive.write_out("path/to/location")

**Note on resource tracking:**

`ExportArchive` is able to automatically track all `keras.Variables` used by its endpoints, so most of the time calling `.track(model)` is not strictly required. However, if your model uses lookup layers such as `IntegerLookup`, `StringLookup`, or `TextVectorization`, it will need to be tracked explicitly via `.track(model)`.

Explicit tracking is also required if you need to be able to access the properties `variables`, `trainable_variables`, or `non_trainable_variables` on the revived archive.

Methods
-------

### `add_endpoint`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L204-L349)

add_endpoint(
        name, fn, input_signature=None, **kwargs
    )

Register a new serving endpoint.

|     |     |
| --- | --- |
| Args |     |
| `name` | `str`. The name of the endpoint. |
| `fn` | A callable. It should only leverage resources (e.g. [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br> objects or [`tf.lookup.StaticHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticHashTable)<br> objects) that are available on the models/layers tracked by the `ExportArchive` (you can call `.track(model)` to track a new model). The shape and dtype of the inputs to the function must be known. For that purpose, you can either 1) make sure that `fn` is a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> that has been called at least once, or 2) provide an `input_signature` argument that specifies the shape and dtype of the inputs (see below). |
| `input_signature` | Optional. Specifies the shape and dtype of `fn`. Can be a structure of [`keras.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>, [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br>, `backend.KerasTensor`, or backend tensor (see below for an example showing a `Functional` model with 2 input arguments). If not provided, `fn` must be a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> that has been called at least once. Defaults to `None`. |
| `**kwargs` | Additional keyword arguments:<br><br>*   Specific to the JAX backend:<br>    *   `is_static`: Optional `bool`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds).<br>    *   `jax2tf_kwargs`: Optional `dict`. Arguments for `jax2tf.convert`. See [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)<br>        . If `native_serialization` and `polymorphic_shapes` are not provided, they are automatically computed. |

|     |
| --- |
| Returns |     |
| The [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> wrapping `fn` that was added to the archive. |     |

#### Example:

Adding an endpoint using the `input_signature` argument when the model has a single input argument:

export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
    )

Adding an endpoint using the `input_signature` argument when the model has two positional input arguments:

export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[\
            keras.InputSpec(shape=(None, 3), dtype="float32"),\
            keras.InputSpec(shape=(None, 4), dtype="float32"),\
        ],
    )

Adding an endpoint using the `input_signature` argument when the model has one input argument that is a list of 2 tensors (e.g. a Functional model with 2 inputs):

model = keras.Model(inputs=[x1, x2], outputs=outputs)
    
    export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[\
            [\
                keras.InputSpec(shape=(None, 3), dtype="float32"),\
                keras.InputSpec(shape=(None, 4), dtype="float32"),\
            ],\
        ],
    )

This also works with dictionary inputs:

model = keras.Model(inputs={"x1": x1, "x2": x2}, outputs=outputs)
    
    export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[\
            {\
                "x1": keras.InputSpec(shape=(None, 3), dtype="float32"),\
                "x2": keras.InputSpec(shape=(None, 4), dtype="float32"),\
            },\
        ],
    )

Adding an endpoint that is a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
:

@tf.function()
    def serving_fn(x):
        return model(x)
    
    # The function must be traced, i.e. it must be called at least once.
    serving_fn(tf.random.normal(shape=(2, 3)))
    
    export_archive = ExportArchive()
    export_archive.track(model)
    export_archive.add_endpoint(name="serve", fn=serving_fn)

Combining a model with some TensorFlow preprocessing, which can use TensorFlow resources:

lookup_table = tf.lookup.StaticHashTable(initializer, default_value=0.0)
    
    export_archive = ExportArchive()
    model_fn = export_archive.track_and_add_endpoint(
        "model_fn",
        model,
        input_signature=[tf.TensorSpec(shape=(None, 5), dtype=tf.float32)],
    )
    export_archive.track(lookup_table)
    
    @tf.function()
    def serving_fn(x):
        x = lookup_table.lookup(x)
        return model_fn(x)
    
    export_archive.add_endpoint(name="serve", fn=serving_fn)

### `add_variable_collection`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L383-L414)

add_variable_collection(
        name, variables
    )

Register a set of variables to be retrieved after reloading.

|     |     |
| --- | --- |
| Arguments |     |
| `name` | The string name for the collection. |
| `variables` | A tuple/list/set of [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br> instances. |

#### Example:

export_archive = ExportArchive()
    export_archive.track(model)
    # Register an endpoint
    export_archive.add_endpoint(
        name="serve",
        fn=model.call,
        input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
    )
    # Save a variable collection
    export_archive.add_variable_collection(
        name="optimizer_variables", variables=model.optimizer.variables)
    export_archive.write_out("path/to/location")
    
    # Reload the object
    revived_object = tf.saved_model.load("path/to/location")
    # Retrieve the variables
    optimizer_variables = revived_object.optimizer_variables

### `track`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L187-L202)

track(
        resource
    )

Track the variables (of a layer or model) and other assets.

By default, all variables used by an endpoint function are automatically tracked when you call `add_endpoint()`. However, non-variables assets such as lookup tables need to be tracked manually. Note that lookup tables used by built-in Keras layers (`TextVectorization`, `IntegerLookup`, `StringLookup`) are automatically tracked by `add_endpoint()`.

|     |     |
| --- | --- |
| Args |     |
| `resource` | A layer, model or a TensorFlow trackable resource. |

### `track_and_add_endpoint`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L351-L381)

track_and_add_endpoint(
        name, resource, input_signature, **kwargs
    )

Track the variables and register a new serving endpoint.

This function combines the functionality of `track` and `add_endpoint`. It tracks the variables of the `resource` (either a layer or a model) and registers a serving endpoint using `resource.__call__`.

|     |     |
| --- | --- |
| Args |     |
| `name` | `str`. The name of the endpoint. |
| `resource` | A trackable Keras resource, such as a layer or model. |
| `input_signature` | Optional. Specifies the shape and dtype of `fn`. Can be a structure of [`keras.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>, [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br>, `backend.KerasTensor`, or backend tensor (see below for an example showing a `Functional` model with 2 input arguments). If not provided, `fn` must be a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> that has been called at least once. Defaults to `None`. |
| `**kwargs` | Additional keyword arguments:<br><br>*   Specific to the JAX backend:<br>    *   `is_static`: Optional `bool`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds).<br>    *   `jax2tf_kwargs`: Optional `dict`. Arguments for `jax2tf.convert`. See [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)<br>        . If `native_serialization` and `polymorphic_shapes` are not provided, they are automatically computed. |

### `write_out`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/saved_model.py#L416-L436)

write_out(
        filepath, options=None, verbose=True
    )

Write the corresponding SavedModel to disk.

|     |     |
| --- | --- |
| Arguments |     |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the artifact. |
| `options` | [`tf.saved_model.SaveOptions`](https://www.tensorflow.org/api_docs/python/tf/saved_model/SaveOptions)<br> object that specifies SavedModel saving options. |
| `verbose` | whether to print all the variables of an exported SavedModel. |

**Note on TF-Serving**: all endpoints registered via `add_endpoint()` are made visible for TF-Serving in the SavedModel artifact. In addition, the first endpoint registered is made visible under the alias `"serving_default"` (unless an endpoint with the name `"serving_default"` was already registered manually), since TF-Serving requires this endpoint to be set.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.