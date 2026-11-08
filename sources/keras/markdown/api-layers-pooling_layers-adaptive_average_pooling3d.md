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
 / AdaptiveAveragePooling3D layer

AdaptiveAveragePooling3D layer
==============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/adaptive_average_pooling3d.py#L9)

### `AdaptiveAveragePooling3D` class

Copied!

`keras.layers.AdaptiveAveragePooling3D(output_size, data_format=None, **kwargs)`

Adaptive average pooling operation for 3D volumetric data.

This layer applies an adaptive average pooling operation, which pools the input such that the output has a target spatial size specified by `output_size`, regardless of the input spatial size. The kernel size and stride are automatically computed to achieve the target output size.

**Arguments**

*   **output\_size**: Integer or tuple of 3 integers specifying the target output size. If an integer, the same value is used for depth, height, and width.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, depth, height, width, channels)`. `"channels_first"` corresponds to inputs with shape `(batch, channels, depth, height, width)`. Defaults to the value found in your Keras config file at `~/.keras/keras.json`. If never set, `"channels_last"` is used.

**Input shape**

*   If `data_format="channels_last"`: 5D tensor `(batch_size, depth, height, width, channels)`
*   If `data_format="channels_first"`: 5D tensor `(batch_size, channels, depth, height, width)`

**Output shape**

*   If `data_format="channels_last"`: `(batch_size, output_depth, output_height, output_width, channels)`
*   If `data_format="channels_first"`: `(batch_size, channels, output_depth, output_height, output_width)`

**Examples**

> > > import numpy as np input\_vol = np.random.rand(1, 32, 32, 32, 3) layer = AdaptiveAveragePooling3D(output\_size=16) output\_vol = layer(input\_vol) output\_vol.shape (1, 16, 16, 16, 3)

* * *

[AdaptiveAveragePooling3D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling3d/#adaptiveaveragepooling3d-layer)

[`AdaptiveAveragePooling3D` class](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling3d/#adaptiveaveragepooling3d-class)