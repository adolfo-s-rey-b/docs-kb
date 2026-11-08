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
 / [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 / SeparableConv2D layer

SeparableConv2D layer
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/convolutional/separable_conv2d.py#L31)

### `SeparableConv2D` class

Copied!

`tf_keras.layers.SeparableConv2D(     filters,     kernel_size,     strides=(1, 1),     padding="valid",     data_format=None,     dilation_rate=(1, 1),     depth_multiplier=1,     activation=None,     use_bias=True,     depthwise_initializer="glorot_uniform",     pointwise_initializer="glorot_uniform",     bias_initializer="zeros",     depthwise_regularizer=None,     pointwise_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     depthwise_constraint=None,     pointwise_constraint=None,     bias_constraint=None,     **kwargs )`

Depthwise separable 2D convolution.

Separable convolutions consist of first performing a depthwise spatial convolution (which acts on each input channel separately) followed by a pointwise convolution which mixes the resulting output channels. The `depth_multiplier` argument controls how many output channels are generated per input channel in the depthwise step.

Intuitively, separable convolutions can be understood as a way to factorize a convolution kernel into two smaller kernels, or as an extreme version of an Inception block.

**Arguments**

*   **filters**: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
*   **kernel\_size**: An integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window. Can be a single integer to specify the same value for all spatial dimensions.
*   **strides**: An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Current implementation only supports equal length strides in the row and column dimensions. Specifying any stride value != 1 is incompatible with specifying any `dilation_rate` value != 1.
*   **padding**: one of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding with zeros evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.
*   **dilation\_rate**: An integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution.
*   **depth\_multiplier**: The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `filters_in * depth_multiplier`.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (see `keras.activations`).
*   **use\_bias**: Boolean, whether the layer uses a bias vector.
*   **depthwise\_initializer**: An initializer for the depthwise convolution kernel (see `keras.initializers`). If None, then the default initializer ('glorot\_uniform') will be used.
*   **pointwise\_initializer**: An initializer for the pointwise convolution kernel (see `keras.initializers`). If None, then the default initializer ('glorot\_uniform') will be used.
*   **bias\_initializer**: An initializer for the bias vector. If None, the default initializer ('zeros') will be used (see `keras.initializers`).
*   **depthwise\_regularizer**: Regularizer function applied to the depthwise kernel matrix (see `keras.regularizers`).
*   **pointwise\_regularizer**: Regularizer function applied to the pointwise kernel matrix (see `keras.regularizers`).
*   **bias\_regularizer**: Regularizer function applied to the bias vector (see `keras.regularizers`).
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation") (see `keras.regularizers`).
*   **depthwise\_constraint**: Constraint function applied to the depthwise kernel matrix (see `keras.constraints`).
*   **pointwise\_constraint**: Constraint function applied to the pointwise kernel matrix (see `keras.constraints`).
*   **bias\_constraint**: Constraint function applied to the bias vector (see `keras.constraints`).

**Input shape**

4D tensor with shape: `(batch_size, channels, rows, cols)` if data\_format='channels\_first' or 4D tensor with shape: `(batch_size, rows, cols, channels)` if data\_format='channels\_last'.

**Output shape**

4D tensor with shape: `(batch_size, filters, new_rows, new_cols)` if data\_format='channels\_first' or 4D tensor with shape: `(batch_size, new_rows, new_cols, filters)` if data\_format='channels\_last'. `rows` and `cols` values might have changed due to padding.

**Returns**

A tensor of rank 4 representing `activation(separableconv2d(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: if `padding` is "causal".

* * *

[SeparableConv2D layer](https://keras.io/2/api/layers/convolution_layers/separable_convolution2d/#separableconv2d-layer)

[`SeparableConv2D` class](https://keras.io/2/api/layers/convolution_layers/separable_convolution2d/#separableconv2d-class)