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
 / [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 / SpatialDropout2D layer

SpatialDropout2D layer
======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/regularization/spatial_dropout2d.py#L28)

### `SpatialDropout2D` class

Copied!

`tf_keras.layers.SpatialDropout2D(rate, data_format=None, **kwargs)`

Spatial 2D version of Dropout.

This version performs the same function as Dropout, however, it drops entire 2D feature maps instead of individual elements. If adjacent pixels within feature maps are strongly correlated (as is normally the case in early convolution layers) then regular dropout will not regularize the activations and will otherwise just result in an effective learning rate decrease. In this case, SpatialDropout2D will help promote independence between feature maps and should be used instead.

**Arguments**

*   **rate**: Float between 0 and 1. Fraction of the input units to drop.
*   **data\_format**: 'channels\_first' or 'channels\_last'. In 'channels\_first' mode, the channels dimension (the depth) is at index 1, in 'channels\_last' mode is it at index 3. When unspecified, uses `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.

**Call arguments**

*   **inputs**: A 4D tensor.
*   **training**: Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing).

**Input shape**

4D tensor with shape: `(samples, channels, rows, cols)` if data\_format='channels\_first' or 4D tensor with shape: `(samples, rows, cols, channels)` if data\_format='channels\_last'.

**Output shape Same as input**

.

References: - [Efficient Object Localization Using Convolutional Networks](https://arxiv.org/abs/1411.4280)

* * *

[SpatialDropout2D layer](https://keras.io/2/api/layers/regularization_layers/spatial_dropout2d/#spatialdropout2d-layer)

[`SpatialDropout2D` class](https://keras.io/2/api/layers/regularization_layers/spatial_dropout2d/#spatialdropout2d-class)