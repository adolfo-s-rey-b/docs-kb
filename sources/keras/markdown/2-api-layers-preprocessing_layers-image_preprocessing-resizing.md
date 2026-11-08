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
 / [Image preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/)
 / Resizing layer

Resizing layer
==============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/image_preprocessing.py#L44)

### `Resizing` class

Copied!

`tf_keras.layers.Resizing(     height, width, interpolation="bilinear", crop_to_aspect_ratio=False, **kwargs )`

A preprocessing layer which resizes images.

This layer resizes an image input to a target height and width. The input should be a 4D (batched) or 3D (unbatched) tensor in `"channels_last"` format. Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.\
\
This layer can be called on tf.RaggedTensor batches of input images of distinct sizes, and will resize the outputs to dense tensors of uniform size.\
\
For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)\
.\
\
**Arguments**\
\
*   **height**: Integer, the height of the output shape.\
*   **width**: Integer, the width of the output shape.\
*   **interpolation**: String, the interpolation method. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"area"`, `"lanczos3"`, `"lanczos5"`, `"gaussian"`, `"mitchellcubic"`. Defaults to `"bilinear"`.\
*   **crop\_to\_aspect\_ratio**: If True, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved.\
\
* * *\
\
[Resizing layer](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/resizing/#resizing-layer)\
\
[`Resizing` class](https://keras.io/2/api/layers/preprocessing_layers/image_preprocessing/resizing/#resizing-class)