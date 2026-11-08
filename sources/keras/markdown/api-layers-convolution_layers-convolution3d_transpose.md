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
 / Conv3DTranspose layer

Conv3DTranspose layer
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/conv3d_transpose.py#L5)

### `Conv3DTranspose` class

Copied!

`keras.layers.Conv3DTranspose(     filters,     kernel_size,     strides=(1, 1, 1),     padding="valid",     data_format=None,     output_padding=None,     dilation_rate=(1, 1, 1),     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

3D transposed convolution layer.

The need for transposed convolutions generally arise from the desire to use a transformation going in the opposite direction of a normal convolution, i.e., from something that has the shape of the output of some convolution to something that has the shape of its input while maintaining a connectivity pattern that is compatible with said convolution.

**Arguments**

*   **filters**: int, the dimension of the output space (the number of filters in the transposed convolution).
*   **kernel\_size**: int or tuple/list of 1 integer, specifying the size of the transposed convolution window.
*   **strides**: int or tuple/list of 1 integer, specifying the stride length of the transposed convolution. `strides > 1` is incompatible with `dilation_rate > 1`.
*   **padding**: string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. output\_padding: An integer or tuple/list of 3 integers, specifying the amount of padding along the depth, height, and width. Can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a given dimension must be lower than the stride along that same dimension. If set to `None` (default), the output shape is inferred.
*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dilation\_rate**: an integer or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any `dilation_rate` value != 1 is incompatible with specifying any stride value != 1.
*   **activation**: Activation function. If `None`, no activation is applied.
*   **use\_bias**: bool, if `True`, bias will be added to the output.
*   **kernel\_initializer**: Initializer for the convolution kernel. If `None`, the default initializer (`"glorot_uniform"`) will be used.
*   **bias\_initializer**: Initializer for the bias vector. If `None`, the default initializer (`"zeros"`) will be used.
*   **kernel\_regularizer**: Optional regularizer for the convolution kernel.
*   **bias\_regularizer**: Optional regularizer for the bias vector.
*   **activity\_regularizer**: Optional regularizer function for the output.
*   **kernel\_constraint**: Optional projection function to be applied to the kernel after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training.
*   **bias\_constraint**: Optional projection function to be applied to the bias after being updated by an `Optimizer`.

**Input shape**

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

**Output shape**

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, new_spatial_dim1, new_spatial_dim2, new_spatial_dim3, filters)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, filters, new_spatial_dim1, new_spatial_dim2, new_spatial_dim3)`

**Returns**

A 5D tensor representing `activation(conv3d(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: when both `strides > 1` and `dilation_rate > 1`.

**References**

*   [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285v1)
    
*   [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
    

**Example**

Copied!

`>>> x = np.random.rand(4, 10, 8, 12, 128) >>> y = keras.layers.Conv3DTranspose(32, 2, 2, activation='relu')(x) >>> print(y.shape) (4, 20, 16, 24, 32)`

* * *

[Conv3DTranspose layer](https://keras.io/api/layers/convolution_layers/convolution3d_transpose/#conv3dtranspose-layer)

[`Conv3DTranspose` class](https://keras.io/api/layers/convolution_layers/convolution3d_transpose/#conv3dtranspose-class)