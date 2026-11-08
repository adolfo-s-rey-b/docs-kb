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
 / SeparableConv1D layer

SeparableConv1D layer
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/convolutional/separable_conv1d.py#L31)

### `SeparableConv1D` class

Copied!

`tf_keras.layers.SeparableConv1D(     filters,     kernel_size,     strides=1,     padding="valid",     data_format=None,     dilation_rate=1,     depth_multiplier=1,     activation=None,     use_bias=True,     depthwise_initializer="glorot_uniform",     pointwise_initializer="glorot_uniform",     bias_initializer="zeros",     depthwise_regularizer=None,     pointwise_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     depthwise_constraint=None,     pointwise_constraint=None,     bias_constraint=None,     **kwargs )`

Depthwise separable 1D convolution.

This layer performs a depthwise convolution that acts separately on channels, followed by a pointwise convolution that mixes channels. If `use_bias` is True and a bias initializer is provided, it adds a bias vector to the output. It then optionally applies an activation function to produce the final output.

**Arguments**

*   **filters**: Integer, the dimensionality of the output space (i.e. the number of filters in the convolution).
*   **kernel\_size**: A single integer specifying the spatial dimensions of the filters.
*   **strides**: A single integer specifying the strides of the convolution. Specifying any `stride` value != 1 is incompatible with specifying any `dilation_rate` value != 1.
*   **padding**: One of `"valid"`, `"same"`, or `"causal"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding with zeros evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. `"causal"` results in causal (dilated) convolutions, e.g. `output[t]` does not depend on `input[t+1:]`.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, length, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, length)`.
*   **dilation\_rate**: A single integer, specifying the dilation rate to use for dilated convolution.
*   **depth\_multiplier**: The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `num_filters_in * depth_multiplier`.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (see `keras.activations`).
*   **use\_bias**: Boolean, whether the layer uses a bias.
*   **depthwise\_initializer**: An initializer for the depthwise convolution kernel (see `keras.initializers`). If None, then the default initializer ('glorot\_uniform') will be used.
*   **pointwise\_initializer**: An initializer for the pointwise convolution kernel (see `keras.initializers`). If None, then the default initializer ('glorot\_uniform') will be used.
*   **bias\_initializer**: An initializer for the bias vector. If None, the default initializer ('zeros') will be used (see `keras.initializers`).
*   **depthwise\_regularizer**: Optional regularizer for the depthwise convolution kernel (see `keras.regularizers`).
*   **pointwise\_regularizer**: Optional regularizer for the pointwise convolution kernel (see `keras.regularizers`).
*   **bias\_regularizer**: Optional regularizer for the bias vector (see `keras.regularizers`).
*   **activity\_regularizer**: Optional regularizer function for the output (see `keras.regularizers`).
*   **depthwise\_constraint**: Optional projection function to be applied to the depthwise kernel after being updated by an `Optimizer` (e.g. used for norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training (see `keras.constraints`).
*   **pointwise\_constraint**: Optional projection function to be applied to the pointwise kernel after being updated by an `Optimizer` (see `keras.constraints`).
*   **bias\_constraint**: Optional projection function to be applied to the bias after being updated by an `Optimizer` (see `keras.constraints`).
*   **trainable**: Boolean, if `True` the weights of this layer will be marked as trainable (and listed in `layer.trainable_weights`).

**Input shape**

3D tensor with shape: `(batch_size, channels, steps)` if data\_format='channels\_first' or 3D tensor with shape: `(batch_size, steps, channels)` if data\_format='channels\_last'.

**Output shape**

3D tensor with shape: `(batch_size, filters, new_steps)` if data\_format='channels\_first' or 3D tensor with shape: `(batch_size, new_steps, filters)` if data\_format='channels\_last'. `new_steps` value might have changed due to padding or strides.

**Returns**

A tensor of rank 3 representing `activation(separableconv1d(inputs, kernel) + bias)`.

* * *

[SeparableConv1D layer](https://keras.io/2/api/layers/convolution_layers/separable_convolution1d/#separableconv1d-layer)

[`SeparableConv1D` class](https://keras.io/2/api/layers/convolution_layers/separable_convolution1d/#separableconv1d-class)