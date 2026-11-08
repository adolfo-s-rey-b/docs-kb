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
 / RandomColorDegeneration layer

RandomColorDegeneration layer
=============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_color_degeneration.py#L11)

### `RandomColorDegeneration` class

Copied!

`keras.layers.RandomColorDegeneration(     factor, value_range=(0, 255), data_format=None, seed=None, **kwargs )`

Randomly performs the color degeneration operation on given images.

Copied!

``The sharpness operation first converts an image to gray scale, then back to color. It then takes a weighted average between original image and the degenerated image. This makes colors appear more dull.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     factor: A tuple of two floats or a single float.         `factor` controls the extent to which the         image sharpness is impacted. `factor=0.0` makes this layer perform a         no-op operation, while a value of 1.0 uses the degenerated result         entirely. Values between 0 and 1 result in linear interpolation         between the original image and the sharpened image.         Values should be between `0.0` and `1.0`. If a tuple is used, a         `factor` is sampled between the two values for every image         augmented. If a single float is used, a value between `0.0` and the         passed float is sampled. In order to ensure the value is always the         same, please pass a tuple with two identical floats: `(0.5, 0.5)`.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomColorDegeneration(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomColorDegeneration layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_degeneration/#randomcolordegeneration-layer)

[`RandomColorDegeneration` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_degeneration/#randomcolordegeneration-class)