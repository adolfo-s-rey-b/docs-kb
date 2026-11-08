None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Layers API](https://keras.io/2/api/layers/)
 / [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 / [Image augmentation layers](https://keras.io/2/api/layers/preprocessing_layers/image_augmentation/)
 / RandomBrightness layer

RandomBrightness layer
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/image_preprocessing.py#L1331)

### `RandomBrightness` class

Copied!

`tf_keras.layers.RandomBrightness(factor, value_range=(0, 255), seed=None, **kwargs)`

A preprocessing layer which randomly adjusts brightness during training.

This layer will randomly increase/reduce the brightness for the input RGB images. At inference time, the output will be identical to the input. Call the layer with `training=True` to adjust the brightness of the input.

Note that different brightness adjustment factors will be apply to each the images in the batch.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Arguments**

*   **factor**: Float or a list/tuple of 2 floats between -1.0 and 1.0. The factor is used to determine the lower bound and upper bound of the brightness adjustment. A float value will be chosen randomly between the limits. When -1.0 is chosen, the output image will be black, and when 1.0 is chosen, the image will be fully white. When only one float is provided, eg, 0.2, then -0.2 will be used for lower bound and 0.2 will be used for upper bound.
*   **value\_range**: Optional list/tuple of 2 floats for the lower and upper limit of the values of the input data. To make no change, use \[0.0, 1.0\], e.g., if the image input has been scaled before this layer. Defaults to \[0.0, 255.0\]. The brightness adjustment will be scaled to this range, and the output values will be clipped to this range.
*   **seed**: optional integer, for fixed RNG behavior.

Inputs: 3D (HWC) or 4D (NHWC) tensor, with float or int dtype. Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`)\
\
Output: 3D (HWC) or 4D (NHWC) tensor with brightness adjusted based on the `factor`. By default, the layer will output floats. The output value will be clipped to the range `[0, 255]`, the valid range of RGB colors, and rescaled based on the `value_range` if needed.\
\
Sample usage:\
\
Copied!\
\
`random_bright = tf.keras.layers.RandomBrightness(factor=0.2)  # An image with shape [2, 2, 3] image = [[[1, 2, 3], [4 ,5 ,6]], [[7, 8, 9], [10, 11, 12]]]  # Assume we randomly select the factor to be 0.1, then it will apply # 0.1 * 255 to all the channel output = random_bright(image, training=True)  # output will be int64 with 25.5 added to each channel and round down. tf.Tensor([[[26.5, 27.5, 28.5]             [29.5, 30.5, 31.5]]            [[32.5, 33.5, 34.5]             [35.5, 36.5, 37.5]]],           shape=(2, 2, 3), dtype=int64)`\
\
* * *\
\
[RandomBrightness layer](https://keras.io/2/api/layers/preprocessing_layers/image_augmentation/random_brightness/#randombrightness-layer)\
\
[`RandomBrightness` class](https://keras.io/2/api/layers/preprocessing_layers/image_augmentation/random_brightness/#randombrightness-class)