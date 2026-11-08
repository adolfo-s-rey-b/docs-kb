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
 / RandomZoom layer

RandomZoom layer
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L16)

### `RandomZoom` class

Copied!

`keras.layers.RandomZoom(     height_factor,     width_factor=None,     fill_mode="reflect",     interpolation="bilinear",     seed=None,     fill_value=0.0,     data_format=None,     **kwargs )`

A preprocessing layer which randomly zooms images during training.

This layer will randomly zoom in or out on each axis of an image independently, filling empty space according to `fill_mode`.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.\
\
**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)\
 or `grain` pipeline (independently of which backend you're using).\
\
**Input shape**\
\
3D (unbatched) or 4D (batched) tensor with shape: `(..., height, width, channels)`, in `"channels_last"` format, or `(..., channels, height, width)`, in `"channels_first"` format.\
\
**Output shape**\
\
3D (unbatched) or 4D (batched) tensor with shape: `(..., target_height, target_width, channels)`, or `(..., channels, target_height, target_width)`, in `"channels_first"` format.\
\
**Arguments**\
\
*   **height\_factor**: a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for zooming vertically. When represented as a single float, this value is used for both the upper and lower bound. A positive value means zooming out, while a negative value means zooming in. For instance, `height_factor=(0.2, 0.3)` result in an output zoomed out by a random amount in the range `[+20%, +30%]`. `height_factor=(-0.3, -0.2)` result in an output zoomed in by a random amount in the range `[+20%, +30%]`.\
*   **width\_factor**: a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for zooming horizontally. When represented as a single float, this value is used for both the upper and lower bound. For instance, `width_factor=(0.2, 0.3)` result in an output zooming out between 20% to 30%. `width_factor=(-0.3, -0.2)` result in an output zooming in between 20% to 30%. `None` means i.e., zooming vertical and horizontal directions by preserving the aspect ratio. Defaults to `None`.\
*   **fill\_mode**: Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"reflect"`.\
    *   `"reflect"`: `(d c b a | a b c d | d c b a)` The input is extended by reflecting about the edge of the last pixel.\
    *   `"constant"`: `(k k k k | a b c d | k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.\
    *   `"wrap"`: `(a b c d | a b c d | a b c d)` The input is extended by wrapping around to the opposite edge.\
    *   `"nearest"`: `(a a a a | a b c d | d d d d)` The input is extended by the nearest pixel. Note that when using torch backend, `"reflect"` is redirected to `"mirror"` `(c d c b | a b c d | c b a b)` because torch does not support `"reflect"`. Note that torch backend does not support `"wrap"`.\
*   **interpolation**: Interpolation mode. Supported values: `"nearest"`, `"bilinear"`.\
*   **seed**: Integer. Used to create a random seed.\
*   **fill\_value**: a float that represents the value to be filled outside the boundaries when `fill_mode="constant"`.\
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.\
*   **\*\*kwargs**: Base layer keyword arguments, such as `name` and `dtype`.\
\
**Example**\
\
Copied!\
\
`>>> input_img = np.random.random((32, 224, 224, 3)) >>> layer = keras.layers.RandomZoom(.5, .2) >>> out_img = layer(input_img)`\
\
* * *\
\
[RandomZoom layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_zoom/#randomzoom-layer)\
\
[`RandomZoom` class](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_zoom/#randomzoom-class)