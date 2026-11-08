None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
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
 / [Layers API](https://keras.io/api/layers/)
 / [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 / Tensorflow SavedModel layer

Tensorflow SavedModel layer
===========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/tfsm_layer.py#L9)

### `TFSMLayer` class

Copied!

`keras.layers.TFSMLayer(     filepath,     call_endpoint="serve",     call_training_endpoint=None,     trainable=True,     name=None,     dtype=None, )`

Reload a Keras model/layer that was saved via SavedModel / ExportArchive.

**Arguments**

*   **filepath**: `str` or `pathlib.Path` object. The path to the SavedModel.
*   **call\_endpoint**: Name of the endpoint to use as the `call()` method of the reloaded layer. If the SavedModel was created via `model.export()`, then the default endpoint name is `'serve'`. In other cases it may be named `'serving_default'`.

**Example**

Copied!

`model.export("path/to/artifact") reloaded_layer = TFSMLayer("path/to/artifact") outputs = reloaded_layer(inputs)`

The reloaded object can be used like a regular Keras layer, and supports training/fine-tuning of its trainable weights. Note that the reloaded object retains none of the internal structure or custom methods of the original object – it's a brand new layer created around the saved function.

**Limitations:**

*   Only call endpoints with a single `inputs` tensor argument (which may optionally be a dict/tuple/list of tensors) are supported. For endpoints with multiple separate input tensor arguments, consider subclassing `TFSMLayer` and implementing a `call()` method with a custom signature.
*   If you need training-time behavior to differ from inference-time behavior (i.e. if you need the reloaded object to support a `training=True` argument in `__call__()`), make sure that the training-time call function is saved as a standalone endpoint in the artifact, and provide its name to the `TFSMLayer` via the `call_training_endpoint` argument.

* * *

[Tensorflow SavedModel layer](https://keras.io/api/layers/backend_specific_layers/tfsm_layer/#tensorflow-savedmodel-layer)

[`TFSMLayer` class](https://keras.io/api/layers/backend_specific_layers/tfsm_layer/#tfsmlayer-class)