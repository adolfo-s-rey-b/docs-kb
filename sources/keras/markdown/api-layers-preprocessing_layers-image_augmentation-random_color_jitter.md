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
 / RandomColorJitter layer

RandomColorJitter layer
=======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter.py#L16)

### `RandomColorJitter` class

Copied!

`keras.layers.RandomColorJitter(     value_range=(0, 255),     brightness_factor=None,     contrast_factor=None,     saturation_factor=None,     hue_factor=None,     seed=None,     data_format=None,     **kwargs )`

RandomColorJitter class randomly apply brightness, contrast, saturation and hue image processing operation sequentially and randomly on the input.

Copied!

``**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     value_range: the range of values the incoming images will have.         Represented as a two number tuple written [low, high].         This is typically either `[0, 1]` or `[0, 255]` depending         on how your preprocessing pipeline is set up.     brightness_factor: Float or a list/tuple of 2 floats between -1.0         and 1.0. The factor is used to determine the lower bound and         upper bound of the brightness adjustment. A float value will         be chosen randomly between the limits. When -1.0 is chosen,         the output image will be black, and when 1.0 is chosen, the         image will be fully white. When only one float is provided,         eg, 0.2, then -0.2 will be used for lower bound and 0.2 will         be used for upper bound.     contrast_factor: a positive float represented as fraction of value,         or a tuple of size 2 representing lower and upper bound. When         represented as a single float, lower = upper. The contrast         factor will be randomly picked between `[1.0 - lower, 1.0 +         upper]`. For any pixel x in the channel, the output will be         `(x - mean) * factor + mean` where `mean` is the mean value         of the channel.     saturation_factor: A tuple of two floats or a single float. `factor`         controls the extent to which the image saturation is impacted.         `factor=0.5` makes this layer perform a no-op operation.         `factor=0.0` makes the image fully grayscale. `factor=1.0`         makes the image fully saturated. Values should be between         `0.0` and `1.0`. If a tuple is used, a `factor` is sampled         between the two values for every image augmented. If a single         float is used, a value between `0.0` and the passed float is         sampled. To ensure the value is always the same, pass a tuple         with two identical floats: `(0.5, 0.5)`.     hue_factor: A single float or a tuple of two floats. `factor`         controls the extent to which the image hue is impacted.         `factor=0.0` makes this layer perform a no-op operation,         while a value of `1.0` performs the most aggressive contrast         adjustment available. If a tuple is used, a `factor` is         sampled between the two values for every image augmented.         If a single float is used, a value between `0.0` and the         passed float is sampled. In order to ensure the value is         always the same, please pass a tuple with two identical         floats: `(0.5, 0.5)`.     seed: Integer. Used to create a random seed.  # Example``

Copied!

`layer = keras.layers.RandomColorJitter(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomColorJitter layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_jitter/#randomcolorjitter-layer)

[`RandomColorJitter` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_jitter/#randomcolorjitter-class)