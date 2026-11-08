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
 / Equalization layer

Equalization layer
==================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L8)

### `Equalization` class

Copied!

`keras.layers.Equalization(value_range=(0, 255), bins=256, data_format=None, **kwargs)`

Preprocessing layer for histogram equalization on image channels.

Histogram equalization is a technique to adjust image intensities to enhance contrast by effectively spreading out the most frequent intensity values. This layer applies equalization on a channel-wise basis, which can improve the visibility of details in images.

This layer works with both grayscale and color images, performing equalization independently on each color channel. At inference time, the equalization is consistently applied.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **value\_range**: Optional list/tuple of 2 floats specifying the lower and upper limits of the input data values. Defaults to `[0, 255]`. If the input image has been scaled, use the appropriate range (e.g., `[0.0, 1.0]`). The equalization will be scaled to this range, and output values will be clipped accordingly.
*   **bins**: Integer specifying the number of histogram bins to use for equalization. Defaults to 256, which is suitable for 8-bit images. Larger values can provide more granular intensity redistribution.

**Input shape**

3D (unbatched) or 4D (batched) tensor with shape: `(..., height, width, channels)`, in `"channels_last"` format, or `(..., channels, height, width)`, in `"channels_first"` format.

**Output shape**

3D (unbatched) or 4D (batched) tensor with shape: `(..., target_height, target_width, channels)`, or `(..., channels, target_height, target_width)`, in `"channels_first"` format.

**Example**

Copied!

`# Create an equalization layer for standard 8-bit images equalizer = keras.layers.Equalization()  # An image with uneven intensity distribution image = [...] # your input image  # Apply histogram equalization equalized_image = equalizer(image)  # For images with custom value range custom_equalizer = keras.layers.Equalization(     value_range=[0.0, 1.0],  # for normalized images     bins=128  # fewer bins for more subtle equalization ) custom_equalized = custom_equalizer(normalized_image)`

* * *

[Equalization layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/equalization/#equalization-layer)

[`Equalization` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/equalization/#equalization-class)