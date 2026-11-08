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
 / RandomInvert layer

RandomInvert layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_invert.py#L10)

### `RandomInvert` class

Copied!

`keras.layers.RandomInvert(     factor=1.0, value_range=(0, 255), seed=None, data_format=None, **kwargs )`

Preprocessing layer for random inversion of image colors.

Copied!

``This layer randomly inverts the colors of input images with a specified probability range. When applied, each image has a chance of having its colors inverted, where the pixel values are transformed to their complementary values. Images that are not selected for inversion remain unchanged.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     factor: A single float or a tuple of two floats.         `factor` controls the probability of inverting the image colors.         If a tuple is provided, the value is sampled between the two values         for each image, where `factor[0]` is the minimum and `factor[1]` is         the maximum probability. If a single float is provided, a value         between `0.0` and the provided float is sampled.         Defaults to `(0, 1)`.     value_range: a tuple or a list of two elements. The first value         represents the lower bound for values in passed images, the second         represents the upper bound. Images passed to the layer should have         values within `value_range`. Defaults to `(0, 255)`.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomInvert(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomInvert layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_invert/#randominvert-layer)

[`RandomInvert` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_invert/#randominvert-class)