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
 / RandomSharpness layer

RandomSharpness layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_sharpness.py#L11)

### `RandomSharpness` class

Copied!

`keras.layers.RandomSharpness(     factor, value_range=(0, 255), data_format=None, seed=None, **kwargs )`

Randomly performs the sharpness operation on given images.

Copied!

``The sharpness operation first performs a blur, then blends between the original image and the processed image. This operation adjusts the clarity of the edges in an image, ranging from blurred to enhanced sharpness.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     factor: A tuple of two floats or a single float.         `factor` controls the extent to which the image sharpness         is impacted. `factor=0.0` results in a fully blurred image,         `factor=0.5` applies no operation (preserving the original image),         and `factor=1.0` enhances the sharpness beyond the original. Values         should be between `0.0` and `1.0`. If a tuple is used, a `factor`         is sampled between the two values for every image augmented.         If a single float is used, a value between `0.0` and the passed         float is sampled. To ensure the value is always the same,         pass a tuple with two identical floats: `(0.5, 0.5)`.     value_range: the range of values the incoming images will have.         Represented as a two-number tuple written `[low, high]`. This is         typically either `[0, 1]` or `[0, 255]` depending on how your         preprocessing pipeline is set up.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomSharpness(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomSharpness layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_sharpness/#randomsharpness-layer)

[`RandomSharpness` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_sharpness/#randomsharpness-class)