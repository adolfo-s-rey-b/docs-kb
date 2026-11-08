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
 / [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 / Cropping2D layer

Cropping2D layer
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/cropping2d.py#L8)

### `Cropping2D` class

Copied!

`keras.layers.Cropping2D(cropping=((0, 0), (0, 0)), data_format=None, **kwargs)`

Cropping layer for 2D input (e.g. picture).

It crops along spatial dimensions, i.e. height and width.

**Example**

Copied!

`>>> input_shape = (2, 28, 28, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> y = keras.layers.Cropping2D(cropping=((2, 2), (4, 4)))(x) >>> y.shape (2, 24, 20, 3)`

**Arguments**

*   **cropping**: Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
    *   If int: the same symmetric cropping is applied to height and width.
    *   If tuple of 2 ints: interpreted as two different symmetric cropping values for height and width: `(symmetric_height_crop, symmetric_width_crop)`.
    *   If tuple of 2 tuples of 2 ints: interpreted as `((top_crop, bottom_crop), (left_crop, right_crop))`.
*   **data\_format**: A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`.

**Input shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, height, width, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, height, width)`

**Output shape**

4D tensor with shape: - If `data_format` is `"channels_last"`: `(batch_size, cropped_height, cropped_width, channels)` - If `data_format` is `"channels_first"`: `(batch_size, channels, cropped_height, cropped_width)`

* * *

[Cropping2D layer](https://keras.io/api/layers/reshaping_layers/cropping2d/#cropping2d-layer)

[`Cropping2D` class](https://keras.io/api/layers/reshaping_layers/cropping2d/#cropping2d-class)