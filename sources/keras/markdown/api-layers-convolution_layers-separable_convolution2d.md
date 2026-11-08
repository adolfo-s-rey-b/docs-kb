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
 / [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 / SeparableConv2D layer

SeparableConv2D layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/separable_conv2d.py#L5)

### `SeparableConv2D` class

Copied!

`keras.layers.SeparableConv2D(     filters,     kernel_size,     strides=(1, 1),     padding="valid",     data_format=None,     dilation_rate=(1, 1),     depth_multiplier=1,     activation=None,     use_bias=True,     depthwise_initializer="glorot_uniform",     pointwise_initializer="glorot_uniform",     bias_initializer="zeros",     depthwise_regularizer=None,     pointwise_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     depthwise_constraint=None,     pointwise_constraint=None,     bias_constraint=None,     **kwargs )`

2D separable convolution layer.

This layer performs a depthwise convolution that acts separately on channels, followed by a pointwise convolution that mixes channels. If `use_bias` is True and a bias initializer is provided, it adds a bias vector to the output. It then optionally applies an activation function to produce the final output.

**Arguments**

*   **filters**: int, the dimensionality of the output space (i.e. the number of filters in the pointwise convolution).
*   **kernel\_size**: int or tuple/list of 2 integers, specifying the size of the depthwise convolution window.
*   **strides**: int or tuple/list of 2 integers, specifying the stride length of the depthwise convolution. If only one int is specified, the same stride size will be used for all dimensions. `strides > 1` is incompatible with `dilation_rate > 1`.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dilation\_rate**: int or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. If only one int is specified, the same dilation rate will be used for all dimensions.
*   **depth\_multiplier**: The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `input_channel * depth_multiplier`.
*   **activation**: Activation function. If `None`, no activation is applied.
*   **use\_bias**: bool, if `True`, bias will be added to the output.
*   **depthwise\_initializer**: An initializer for the depthwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used.
*   **pointwise\_initializer**: An initializer for the pointwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used.
*   **bias\_initializer**: An initializer for the bias vector. If None, the default initializer ('"zeros"') will be used.
*   **depthwise\_regularizer**: Optional regularizer for the depthwise convolution kernel.
*   **pointwise\_regularizer**: Optional regularizer for the pointwise convolution kernel.
*   **bias\_regularizer**: Optional regularizer for the bias vector.
*   **activity\_regularizer**: Optional regularizer function for the output.
*   **depthwise\_constraint**: Optional projection function to be applied to the depthwise kernel after being updated by an `Optimizer` (e.g. used for norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape).
*   **pointwise\_constraint**: Optional projection function to be applied to the pointwise kernel after being updated by an `Optimizer`.
*   **bias\_constraint**: Optional projection function to be applied to the bias after being updated by an `Optimizer`.

**Input shape**

*   If `data_format="channels_last"`: A 4D tensor with shape: `(batch_size, height, width, channels)`
*   If `data_format="channels_first"`: A 4D tensor with shape: `(batch_size, channels, height, width)`

**Output shape**

*   If `data_format="channels_last"`: A 4D tensor with shape: `(batch_size, new_height, new_width, filters)`
*   If `data_format="channels_first"`: A 4D tensor with shape: `(batch_size, filters, new_height, new_width)`

**Returns**

A 4D tensor representing `activation(separable_conv2d(inputs, kernel) + bias)`.

**Example**

Copied!

`>>> x = np.random.rand(4, 10, 10, 12) >>> y = keras.layers.SeparableConv2D(3, 4, 3, 2, activation='relu')(x) >>> print(y.shape) (4, 4, 4, 4)`

* * *

[SeparableConv2D layer](https://keras.io/api/layers/convolution_layers/separable_convolution2d/#separableconv2d-layer)

[`SeparableConv2D` class](https://keras.io/api/layers/convolution_layers/separable_convolution2d/#separableconv2d-class)