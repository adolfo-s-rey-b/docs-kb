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
 / Conv1DTranspose layer

Conv1DTranspose layer
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/convolutional/conv1d_transpose.py#L34)

### `Conv1DTranspose` class

Copied!

`tf_keras.layers.Conv1DTranspose(     filters,     kernel_size,     strides=1,     padding="valid",     output_padding=None,     data_format=None,     dilation_rate=1,     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

Transposed convolution layer (sometimes called Deconvolution).

The need for transposed convolutions generally arises from the desire to use a transformation going in the opposite direction of a normal convolution, i.e., from something that has the shape of the output of some convolution to something that has the shape of its input while maintaining a connectivity pattern that is compatible with said convolution.

When using this layer as the first layer in a model, provide the keyword argument `input_shape` (tuple of integers or `None`, does not include the sample axis), e.g. `input_shape=(128, 3)` for data with 128 time steps and 3 channels.

**Arguments**

*   **filters**: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
*   **kernel\_size**: An integer length of the 1D convolution window.
*   **strides**: An integer specifying the stride of the convolution along the time dimension. Specifying a stride value != 1 is incompatible with specifying a `dilation_rate` value != 1. Defaults to `1`.
*   **padding**: one of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding with zeros evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **output\_padding**: An integer specifying the amount of padding along the time dimension of the output tensor. The amount of output padding must be lower than the stride. If set to `None` (default), the output shape is inferred.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, length, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, length)`.
*   **dilation\_rate**: an integer, specifying the dilation rate to use for dilated convolution. Currently, specifying a `dilation_rate` value != 1 is incompatible with specifying a stride value != 1. Also dilation rate larger than 1 is not currently supported.
*   **activation**: Activation function to use. If you don't specify anything, no activation is applied (see `keras.activations`).
*   **use\_bias**: Boolean, whether the layer uses a bias vector.
*   **kernel\_initializer**: Initializer for the `kernel` weights matrix (see `keras.initializers`). Defaults to 'glorot\_uniform'.
*   **bias\_initializer**: Initializer for the bias vector (see `keras.initializers`). Defaults to 'zeros'.
*   **kernel\_regularizer**: Regularizer function applied to the `kernel` weights matrix (see `keras.regularizers`).
*   **bias\_regularizer**: Regularizer function applied to the bias vector (see `keras.regularizers`).
*   **activity\_regularizer**: Regularizer function applied to the output of the layer (its "activation") (see `keras.regularizers`).
*   **kernel\_constraint**: Constraint function applied to the kernel matrix (see `keras.constraints`).
*   **bias\_constraint**: Constraint function applied to the bias vector (see `keras.constraints`).

**Input shape**

3D tensor with shape: `(batch_size, steps, channels)`

**Output shape**

3D tensor with shape: `(batch_size, new_steps, filters)` If `output_padding` is specified:

Copied!

`new_timesteps = ((timesteps - 1) * strides + kernel_size - 2 * padding + output_padding)`

**Returns**

A tensor of rank 3 representing `activation(conv1dtranspose(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: if `padding` is "causal".
*   **ValueError**: when both `strides` > 1 and `dilation_rate` > 1.

**References**

*   [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285v1)
    *   [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
        

* * *

[Conv1DTranspose layer](https://keras.io/2/api/layers/convolution_layers/convolution1d_transpose/#conv1dtranspose-layer)

[`Conv1DTranspose` class](https://keras.io/2/api/layers/convolution_layers/convolution1d_transpose/#conv1dtranspose-class)