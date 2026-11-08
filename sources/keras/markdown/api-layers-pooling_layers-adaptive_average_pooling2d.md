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
 / [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 / AdaptiveAveragePooling2D layer

AdaptiveAveragePooling2D layer
==============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/adaptive_average_pooling2d.py#L9)

### `AdaptiveAveragePooling2D` class

Copied!

`keras.layers.AdaptiveAveragePooling2D(output_size, data_format=None, **kwargs)`

Adaptive average pooling operation for 2D spatial data.

This layer applies an adaptive average pooling operation, which pools the input such that the output has a target spatial size specified by `output_size`, regardless of the input spatial size. The kernel size and stride are automatically computed to achieve the target output size.

**Arguments**

*   **output\_size**: Integer or tuple of 2 integers specifying the target output size. If an integer, the same value is used for both height and width.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`. `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. Defaults to the value found in your Keras config file at `~/.keras/keras.json`. If never set, `"channels_last"` is used.

**Input shape**

*   If `data_format="channels_last"`: 4D tensor `(batch_size, height, width, channels)`
*   If `data_format="channels_first"`: 4D tensor `(batch_size, channels, height, width)`

**Output shape**

*   If `data_format="channels_last"`: `(batch_size, output_height, output_width, channels)`
*   If `data_format="channels_first"`: `(batch_size, channels, output_height, output_width)`

**Examples**

> > > import numpy as np input\_img = np.random.rand(1, 64, 64, 3) layer = AdaptiveAveragePooling2D(output\_size=32) output\_img = layer(input\_img) output\_img.shape (1, 32, 32, 3)

* * *

[AdaptiveAveragePooling2D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling2d/#adaptiveaveragepooling2d-layer)

[`AdaptiveAveragePooling2D` class](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling2d/#adaptiveaveragepooling2d-class)