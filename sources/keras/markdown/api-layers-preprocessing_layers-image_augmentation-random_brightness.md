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
 / RandomBrightness layer

RandomBrightness layer
======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L8)

### `RandomBrightness` class

Copied!

`keras.layers.RandomBrightness(factor, value_range=(0, 255), seed=None, **kwargs)`

A preprocessing layer which randomly adjusts brightness during training.

This layer will randomly increase/reduce the brightness for the input RGB images. At inference time, the output will be identical to the input. Call the layer with `training=True` to adjust the brightness of the input.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **factor**: Float or a list/tuple of 2 floats between -1.0 and 1.0. The factor is used to determine the lower bound and upper bound of the brightness adjustment. A float value will be chosen randomly between the limits. When -1.0 is chosen, the output image will be black, and when 1.0 is chosen, the image will be fully white. When only one float is provided, eg, 0.2, then -0.2 will be used for lower bound and 0.2 will be used for upper bound.
*   **value\_range**: Optional list/tuple of 2 floats for the lower and upper limit of the values of the input data. To make no change, use `[0.0, 1.0]`, e.g., if the image input has been scaled before this layer. Defaults to `[0.0, 255.0]`. The brightness adjustment will be scaled to this range, and the output values will be clipped to this range.
*   **seed**: optional integer, for fixed RNG behavior.

Inputs: 3D (HWC) or 4D (NHWC) tensor, with float or int dtype. Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`)\
\
Output: 3D (HWC) or 4D (NHWC) tensor with brightness adjusted based on the `factor`. By default, the layer will output floats. The output value will be clipped to the range `[0, 255]`, the valid range of RGB colors, and rescaled based on the `value_range` if needed.\
\
**Example**\
\
Copied!\
\
`random_bright = keras.layers.RandomBrightness(factor=0.2)  # An image with shape [2, 2, 3] image = [[[1, 2, 3], [4 ,5 ,6]], [[7, 8, 9], [10, 11, 12]]]  # Assume we randomly select the factor to be 0.1, then it will apply # 0.1 * 255 to all the channel output = random_bright(image, training=True)  # output will be int64 with 25.5 added to each channel and round down. ```python >>> array([[[26.5, 27.5, 28.5]             [29.5, 30.5, 31.5]]            [[32.5, 33.5, 34.5]             [35.5, 36.5, 37.5]]],           shape=(2, 2, 3), dtype=int64)`\
\
\`\`\`\
\
* * *\
\
[RandomBrightness layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_brightness/#randombrightness-layer)\
\
[`RandomBrightness` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_brightness/#randombrightness-class)