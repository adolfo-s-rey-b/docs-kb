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
 / Model export for inference

Model export for inference
==========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/export/export_lib.py#L26)

### `ExportArchive` class

Copied!

`tf_keras.export.ExportArchive()`

ExportArchive is used to write SavedModel artifacts (e.g. for inference).

If you have a TF-Keras model or layer that you want to export as SavedModel for serving (e.g. via TensorFlow-Serving), you can use `ExportArchive` to configure the different serving endpoints you need to make available, as well as their signatures. Simply instantiate an `ExportArchive`, use `track()` to register the layer(s) or model(s) to be used, then use the `add_endpoint()` method to register a new serving endpoint. When done, use the `write_out()` method to save the artifact.

The resulting artifact is a SavedModel and can be reloaded via [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
.

**Examples**

Here's how to export a model for inference.

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="serve",     fn=model.call,     input_signature=[tf.TensorSpec(shape=(None, 3), dtype=tf.float32)], ) export_archive.write_out("path/to/location")  # Elsewhere, we can reload the artifact and serve it. # The endpoint we added is available as a method: serving_model = tf.saved_model.load("path/to/location") outputs = serving_model.serve(inputs)`

Here's how to export a model with one endpoint for inference and one endpoint for a training-mode forward pass (e.g. with dropout on).

Copied!

`export_archive = ExportArchive() export_archive.track(model) export_archive.add_endpoint(     name="call_inference",     fn=lambda x: model.call(x, training=False),     input_signature=[tf.TensorSpec(shape=(None, 3), dtype=tf.float32)], ) export_archive.add_endpoint(     name="call_training",     fn=lambda x: model.call(x, training=True),     input_signature=[tf.TensorSpec(shape=(None, 3), dtype=tf.float32)], ) export_archive.write_out("path/to/location")`

**Note on resource tracking:**

`ExportArchive` is able to automatically track all [`tf.Variables`](https://www.tensorflow.org/api_docs/python/tf/Variables)
 used by its endpoints, so most of the time calling `.track(model)` is not strictly required. However, if your model uses lookup layers such as `IntegerLookup`, `StringLookup`, or `TextVectorization`, it will need to be tracked explicitly via `.track(model)`.

Explicit tracking is also required if you need to be able to access the properties `variables`, `trainable_variables`, or `non_trainable_variables` on the revived archive.

* * *

[Model export for inference](https://keras.io/2/api/models/model_saving_apis/export/#model-export-for-inference)

[`ExportArchive` class](https://keras.io/2/api/models/model_saving_apis/export/#exportarchive-class)