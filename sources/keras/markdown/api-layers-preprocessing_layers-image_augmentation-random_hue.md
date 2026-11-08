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
 / RandomHue layer

RandomHue layer
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_hue.py#L7)

### `RandomHue` class

Copied!

`keras.layers.RandomHue(     factor, value_range=(0, 255), data_format=None, seed=None, **kwargs )`

Randomly adjusts the hue on given images.

This layer will randomly increase/reduce the hue for the input RGB images.

The image hue is adjusted by converting the image(s) to HSV and rotating the hue channel (H) by delta. The image is then converted back to RGB.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **factor**: A single float or a tuple of two floats. `factor` controls the extent to which the image hue is impacted. `factor=0.0` makes this layer perform a no-op operation, while a value of `1.0` performs the most aggressive contrast adjustment available. If a tuple is used, a `factor` is sampled between the two values for every image augmented. If a single float is used, a value between `0.0` and the passed float is sampled. In order to ensure the value is always the same, please pass a tuple with two identical floats: `(0.5, 0.5)`.
*   **value\_range**: the range of values the incoming images will have. Represented as a two-number tuple written `[low, high]`. This is typically either `[0, 1]` or `[0, 255]` depending on how your preprocessing pipeline is set up.
*   **seed**: Integer. Used to create a random seed.

**Example**

Copied!

`(images, labels), _ = keras.datasets.cifar10.load_data() random_hue = keras.layers.RandomHue(factor=0.5, value_range=[0, 1]) images = keras.ops.cast(images, "float32") augmented_images_batch = random_hue(images[:8])`

* * *

[RandomHue layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_hue/#randomhue-layer)

[`RandomHue` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_hue/#randomhue-class)