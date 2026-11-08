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
 / RandomGrayscale layer

RandomGrayscale layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_grayscale.py#L11)

### `RandomGrayscale` class

Copied!

`keras.layers.RandomGrayscale(factor=0.5, data_format=None, seed=None, **kwargs)`

Preprocessing layer for random conversion of RGB images to grayscale.

Copied!

``This layer randomly converts input images to grayscale with a specified factor. When applied, it maintains the original number of channels but sets all channels to the same grayscale value. This can be useful for data augmentation and training models to be robust to color variations.  The conversion preserves the perceived luminance of the original color image using standard RGB to grayscale conversion coefficients. Images that are not selected for conversion remain unchanged.  **Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) or `grain` pipeline (independently of which backend you're using).  # Arguments     factor: Float between 0 and 1, specifying the factor of         converting each image to grayscale. Defaults to 0.5. A value of         1.0 means all images will be converted, while 0.0 means no images         will be converted.     data_format: String, one of `"channels_last"` (default) or         `"channels_first"`. The ordering of the dimensions in the inputs.         `"channels_last"` corresponds to inputs with shape         `(batch, height, width, channels)` while `"channels_first"`         corresponds to inputs with shape         `(batch, channels, height, width)`.  # Input shape     3D (unbatched) or 4D (batched) tensor with shape:     `(..., height, width, channels)`, in `"channels_last"` format,     or `(..., channels, height, width)`, in `"channels_first"` format.  # Output shape     Same as input shape. The output maintains the same number of channels     as the input, even for grayscale-converted images where all channels     will have the same value.  # Example``

Copied!

`layer = keras.layers.RandomGrayscale(value_range=(0, 255)) images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")  labels = keras.ops.one_hot(     np.array([0, 1, 2, 0, 1, 2, 0, 1]),     num_classes=3 )  segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")  output = layer(     {         "images": images,         "labels": labels,         "segmentation_masks": segmentation_masks     },     training=True )`

* * *

[RandomGrayscale layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_grayscale/#randomgrayscale-layer)

[`RandomGrayscale` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_grayscale/#randomgrayscale-class)