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
 / RandomContrast layer

RandomContrast layer
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_contrast.py#L11)

### `RandomContrast` class

Copied!

`keras.layers.RandomContrast(factor, value_range=(0, 255), seed=None, **kwargs)`

A preprocessing layer which randomly adjusts contrast during training.

Copied!

``This layer will randomly adjust the contrast of an image or images by a random factor. Contrast is adjusted independently for each channel of each image during training.  For each channel, this layer computes the mean of the image pixels in the channel and then adjusts each component `x` of each pixel to `(x - mean) * contrast_factor + mean`.  Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and in integer or floating point dtype. By default, the layer will output floats.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Input shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format.  # Output shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format.  # Arguments     factor: a positive float represented as fraction of value, or a tuple of         size 2 representing lower and upper bound.         When represented as a single float, lower = upper.         The contrast factor will be randomly picked between         `[1.0 - lower, 1.0 + upper]`. For any pixel x in the channel,         the output will be `(x - mean) * factor + mean`         where `mean` is the mean value of the channel.     value_range: the range of values the incoming images will have.         Represented as a two-number tuple written `[low, high]`. This is         typically either `[0, 1]` or `[0, 255]` depending on how your         preprocessing pipeline is set up.     seed: Integer. Used to create a random seed.  # Example``\
\
Copied!\
\
`layer = keras.layers.RandomContrast(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`\
\
* * *\
\
[RandomContrast layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_contrast/#randomcontrast-layer)\
\
[`RandomContrast` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_contrast/#randomcontrast-class)