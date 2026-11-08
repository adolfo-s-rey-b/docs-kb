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
 / Conv3DTranspose layer

Conv3DTranspose layer
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/convolutional/conv3d_transpose.py#L34)

### `Conv3DTranspose` class

Copied!

`tf_keras.layers.Conv3DTranspose(     filters,     kernel_size,     strides=(1, 1, 1),     padding="valid",     output_padding=None,     data_format=None,     dilation_rate=(1, 1, 1),     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

Transposed convolution layer (sometimes called Deconvolution).

The need for transposed convolutions generally arises from the desire to use a transformation going in the opposite direction of a normal convolution, i.e., from something that has the shape of the output of some convolution to something that has the shape of its input while maintaining a connectivity pattern that is compatible with said convolution.

When using this layer as the first layer in a model, provide the keyword argument `input_shape` (tuple of integers or `None`, does not include the sample axis), e.g. `input_shape=(128, 128, 128, 3)` for a 128x128x128 volume with 3 channels if `data_format="channels_last"`.

**Arguments**

*   **filters**: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
*   **kernel\_size**: An integer or tuple/list of 3 integers, specifying the depth, height and width of the 3D convolution window. Can be a single integer to specify the same value for all spatial dimensions.
*   **strides**: An integer or tuple/list of 3 integers, specifying the strides of the convolution along the depth, height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any `dilation_rate` value != 1.
*   **padding**: one of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding with zeros evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input.
*   **output\_padding**: An integer or tuple/list of 3 integers, specifying the amount of padding along the depth, height, and width. Can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a given dimension must be lower than the stride along that same dimension. If set to `None` (default), the output shape is inferred.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, depth, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, depth, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Defaults to 'channels\_last'.
*   **dilation\_rate**: an integer or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any `dilation_rate` value != 1 is incompatible with specifying any stride value != 1.
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

5D tensor with shape: `(batch_size, channels, depth, rows, cols)` if data\_format='channels\_first' or 5D tensor with shape: `(batch_size, depth, rows, cols, channels)` if data\_format='channels\_last'.

**Output shape**

5D tensor with shape: `(batch_size, filters, new_depth, new_rows, new_cols)` if data\_format='channels\_first' or 5D tensor with shape: `(batch_size, new_depth, new_rows, new_cols, filters)` if data\_format='channels\_last'. `depth` and `rows` and `cols` values might have changed due to padding. If `output_padding` is specified::

Copied!

`new_depth = ((depth - 1) * strides[0] + kernel_size[0] - 2 * padding[0] + output_padding[0]) new_rows = ((rows - 1) * strides[1] + kernel_size[1] - 2 * padding[1] + output_padding[1]) new_cols = ((cols - 1) * strides[2] + kernel_size[2] - 2 * padding[2] + output_padding[2])`

**Returns**

A tensor of rank 5 representing `activation(conv3dtranspose(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: if `padding` is "causal".
*   **ValueError**: when both `strides` > 1 and `dilation_rate` > 1.

**References**

*   [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285v1)
    *   [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
        

* * *

[Conv3DTranspose layer](https://keras.io/2/api/layers/convolution_layers/convolution3d_transpose/#conv3dtranspose-layer)

[`Conv3DTranspose` class](https://keras.io/2/api/layers/convolution_layers/convolution3d_transpose/#conv3dtranspose-class)