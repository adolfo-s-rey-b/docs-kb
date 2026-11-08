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
 / Solarization layer

Solarization layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/solarization.py#L10)

### `Solarization` class

Copied!

`keras.layers.Solarization(     addition_factor=0.0, threshold_factor=0.0, value_range=(0, 255), seed=None, **kwargs )`

Applies `(max_value - pixel + min_value)` for each pixel in the image.

When created without `threshold` parameter, the layer performs solarization to all values. When created with specified `threshold` the layer only augments pixels that are above the `threshold` value.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **addition\_factor**: (Optional) A tuple of two floats or a single float, between 0 and 1. For each augmented image a value is sampled from the provided range. If a float is passed, the range is interpreted as `(0, addition_factor)`. If specified, this value (times the value range of input images, e.g. 255), is added to each pixel before solarization and thresholding. Defaults to 0.0.
*   **threshold\_factor**: (Optional) A tuple of two floats or a single float. For each augmented image a value is sampled from the provided range. If a float is passed, the range is interpreted as `(0, threshold_factor)`. If specified, only pixel values above this threshold will be solarized.
*   **value\_range**: a tuple or a list of two elements. The first value represents the lower bound for values in input images, the second represents the upper bound. Images passed to the layer should have values within `value_range`. Typical values to pass are `(0, 255)` (RGB image) or `(0., 1.)` (scaled image).
*   **seed**: Integer. Used to create a random seed.
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.

**Example**

Copied!

`(images, labels), _ = keras.datasets.cifar10.load_data() print(images[0, 0, 0]) # [59 62 63] # Note that images are Tensor with values in the range [0, 255] solarization = Solarization(value_range=(0, 255)) images = solarization(images) print(images[0, 0, 0]) # [196, 193, 192]`

* * *

[Solarization layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/solarization/#solarization-layer)

[`Solarization` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/solarization/#solarization-class)