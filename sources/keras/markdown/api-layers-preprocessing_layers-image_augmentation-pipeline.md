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
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Image augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/)
 / Pipeline layer

Pipeline layer
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/pipeline.py#L7)

### `Pipeline` class

Copied!

`keras.layers.Pipeline(layers, name=None)`

Applies a series of layers to an input.

This class is useful to build a preprocessing pipeline, in particular an image data augmentation pipeline. Compared to a `Sequential` model, `Pipeline` features a few important differences:

*   It's not a `Model`, just a plain layer.
*   When the layers in the pipeline are compatible with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
    , the pipeline will also remain [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
     compatible. That is to say, the pipeline will not attempt to convert its inputs to backend-native tensors when in a tf.data context (unlike a `Sequential` model).

**Example**

Copied!

``from keras import layers preprocessing_pipeline = layers.Pipeline([     layers.AutoContrast(),     layers.RandomZoom(0.2),     layers.RandomRotation(0.2), ])  # `ds` is a tf.data.Dataset preprocessed_ds = ds.map(     preprocessing_pipeline,     num_parallel_calls=4, )``

* * *

[Pipeline layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/pipeline/#pipeline-layer)

[`Pipeline` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/pipeline/#pipeline-class)