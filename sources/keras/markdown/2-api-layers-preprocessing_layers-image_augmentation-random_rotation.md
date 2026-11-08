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
 / RandomRotation layer

RandomRotation layer
====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/image_preprocessing.py#L855)

### `RandomRotation` class

Copied!

`tf_keras.layers.RandomRotation(     factor,     fill_mode="reflect",     interpolation="bilinear",     seed=None,     fill_value=0.0,     **kwargs )`

A preprocessing layer which randomly rotates images during training.

This layer will apply random rotations to each image, filling empty space according to `fill_mode`.

By default, random rotations are only applied during training. At inference time, the layer does nothing. If you need to apply random rotations at inference time, set `training` to True when calling the layer.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.\
\
For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)\
.\
\
**Input shape**\
\
3D (unbatched) or 4D (batched) tensor with shape: `(..., height, width, channels)`, in `"channels_last"` format\
\
**Output shape**\
\
3D (unbatched) or 4D (batched) tensor with shape: `(..., height, width, channels)`, in `"channels_last"` format\
\
**Arguments**\
\
*   **factor**: a float represented as fraction of 2 Pi, or a tuple of size 2 representing lower and upper bound for rotating clockwise and counter-clockwise. A positive values means rotating counter clock-wise, while a negative value means clock-wise. When represented as a single float, this value is used for both the upper and lower bound. For instance, `factor=(-0.2, 0.3)` results in an output rotation by a random amount in the range `[-20% * 2pi, 30% * 2pi]`. `factor=0.2` results in an output rotating by a random amount in the range `[-20% * 2pi, 20% * 2pi]`.\
*   **fill\_mode**: Points outside the boundaries of the input are filled according to the given mode (one of `{"constant", "reflect", "wrap", "nearest"}`).\
    *   _reflect_: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.\
    *   _constant_: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k = 0.\
    *   _wrap_: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.\
    *   _nearest_: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel.\
*   **interpolation**: Interpolation mode. Supported values: `"nearest"`, `"bilinear"`.\
*   **seed**: Integer. Used to create a random seed.\
*   **fill\_value**: a float represents the value to be filled outside the boundaries when `fill_mode="constant"`.\
\
* * *\
\
[RandomRotation layer](https://keras.io/2/api/layers/preprocessing_layers/image_augmentation/random_rotation/#randomrotation-layer)\
\
[`RandomRotation` class](https://keras.io/2/api/layers/preprocessing_layers/image_augmentation/random_rotation/#randomrotation-class)