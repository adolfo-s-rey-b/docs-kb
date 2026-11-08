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
 / DepthwiseConv1D layer

DepthwiseConv1D layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/depthwise_conv1d.py#L5)

### `DepthwiseConv1D` class

Copied!

`keras.layers.DepthwiseConv1D(     kernel_size,     strides=1,     padding="valid",     depth_multiplier=1,     data_format=None,     dilation_rate=1,     activation=None,     use_bias=True,     depthwise_initializer="glorot_uniform",     bias_initializer="zeros",     depthwise_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     depthwise_constraint=None,     bias_constraint=None,     **kwargs )`

1D depthwise convolution layer.

Depthwise convolution is a type of convolution in which each input channel is convolved with a different kernel (called a depthwise kernel). You can understand depthwise convolution as the first step in a depthwise separable convolution.

It is implemented via the following steps:

*   Split the input into individual channels.
*   Convolve each channel with an individual depthwise kernel with `depth_multiplier` output channels.
*   Concatenate the convolved outputs along the channels axis.

Unlike a regular 1D convolution, depthwise convolution does not mix information across different input channels.

The `depth_multiplier` argument determines how many filters are applied to one input channel. As such, it controls the amount of output channels that are generated per input channel in the depthwise step.

**Arguments**

*   **kernel\_size**: int or tuple/list of 1 integer, specifying the size of the depthwise convolution window.
*   **strides**: int or tuple/list of 1 integer, specifying the stride length of the convolution. `strides > 1` is incompatible with `dilation_rate > 1`.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input.
*   **depth\_multiplier**: The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `input_channel * depth_multiplier`.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dilation\_rate**: int or tuple/list of 1 integers, specifying the dilation rate to use for dilated convolution.
*   **activation**: Activation function. If `None`, no activation is applied.
*   **use\_bias**: bool, if `True`, bias will be added to the output.
*   **depthwise\_initializer**: Initializer for the convolution kernel. If `None`, the default initializer (`"glorot_uniform"`) will be used.
*   **bias\_initializer**: Initializer for the bias vector. If `None`, the default initializer (`"zeros"`) will be used.
*   **depthwise\_regularizer**: Optional regularizer for the convolution kernel.
*   **bias\_regularizer**: Optional regularizer for the bias vector.
*   **activity\_regularizer**: Optional regularizer function for the output.
*   **depthwise\_constraint**: Optional projection function to be applied to the kernel after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training.
*   **bias\_constraint**: Optional projection function to be applied to the bias after being updated by an `Optimizer`.

**Input shape**

*   If `data_format="channels_last"`: A 3D tensor with shape: `(batch_shape, steps, channels)`
*   If `data_format="channels_first"`: A 3D tensor with shape: `(batch_shape, channels, steps)`

**Output shape**

*   If `data_format="channels_last"`: A 3D tensor with shape: `(batch_shape, new_steps, channels * depth_multiplier)`
*   If `data_format="channels_first"`: A 3D tensor with shape: `(batch_shape, channels * depth_multiplier, new_steps)`

**Returns**

A 3D tensor representing `activation(depthwise_conv1d(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: when both `strides > 1` and `dilation_rate > 1`.

**Example**

Copied!

`>>> x = np.random.rand(4, 10, 12) >>> y = keras.layers.DepthwiseConv1D(3, 3, 2, activation='relu')(x) >>> print(y.shape) (4, 4, 36)`

* * *

[DepthwiseConv1D layer](https://keras.io/api/layers/convolution_layers/depthwise_convolution1d/#depthwiseconv1d-layer)

[`DepthwiseConv1D` class](https://keras.io/api/layers/convolution_layers/depthwise_convolution1d/#depthwiseconv1d-class)