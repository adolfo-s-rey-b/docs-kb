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
 / Conv2D layer

Conv2D layer
============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/convolutional/conv2d.py#L29)

### `Conv2D` class

Copied!

`tf_keras.layers.Conv2D(     filters,     kernel_size,     strides=(1, 1),     padding="valid",     data_format=None,     dilation_rate=(1, 1),     groups=1,     activation=None,     use_bias=True,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     kernel_regularizer=None,     bias_regularizer=None,     activity_regularizer=None,     kernel_constraint=None,     bias_constraint=None,     **kwargs )`

2D convolution layer (e.g. spatial convolution over images).

This layer creates a convolution kernel that is convolved with the layer input to produce a tensor of outputs. If `use_bias` is True, a bias vector is created and added to the outputs. Finally, if `activation` is not `None`, it is applied to the outputs as well.

When using this layer as the first layer in a model, provide the keyword argument `input_shape` (tuple of integers or `None`, does not include the sample axis), e.g. `input_shape=(128, 128, 3)` for 128x128 RGB pictures in `data_format="channels_last"`. You can use `None` when a dimension has variable size.

**Examples**

Copied!

``>>> # The inputs are 28x28 RGB images with `channels_last` and the batch >>> # size is 4. >>> input_shape = (4, 28, 28, 3) >>> x = tf.random.normal(input_shape) >>> y = tf.keras.layers.Conv2D( ... 2, 3, activation='relu', input_shape=input_shape[1:])(x) >>> print(y.shape) (4, 26, 26, 2)``

Copied!

``>>> # With `dilation_rate` as 2. >>> input_shape = (4, 28, 28, 3) >>> x = tf.random.normal(input_shape) >>> y = tf.keras.layers.Conv2D( ...     2, 3, ...     activation='relu', ...     dilation_rate=2, ...     input_shape=input_shape[1:])(x) >>> print(y.shape) (4, 24, 24, 2)``

Copied!

``>>> # With `padding` as "same". >>> input_shape = (4, 28, 28, 3) >>> x = tf.random.normal(input_shape) >>> y = tf.keras.layers.Conv2D( ... 2, 3, activation='relu', padding="same", input_shape=input_shape[1:])(x) >>> print(y.shape) (4, 28, 28, 2)``

Copied!

`>>> # With extended batch shape [4, 7]: >>> input_shape = (4, 7, 28, 28, 3) >>> x = tf.random.normal(input_shape) >>> y = tf.keras.layers.Conv2D( ... 2, 3, activation='relu', input_shape=input_shape[2:])(x) >>> print(y.shape) (4, 7, 26, 26, 2)`

**Arguments**

*   **filters**: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
*   **kernel\_size**: An integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window. Can be a single integer to specify the same value for all spatial dimensions.
*   **strides**: An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any `dilation_rate` value != 1.
*   **padding**: one of `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding with zeros evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input.
*   **data\_format**: A string, one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs. `channels_last` corresponds to inputs with shape `(batch_size, height, width, channels)` while `channels_first` corresponds to inputs with shape `(batch_size, channels, height, width)`. If left unspecified, it uses the `image_data_format` value found in your TF-Keras config file at `~/.keras/keras.json` (if exists) else 'channels\_last'. Note that the `channels_first` format is currently not supported by TensorFlow on CPU. Defaults to 'channels\_last'.
*   **dilation\_rate**: an integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any `dilation_rate` value != 1 is incompatible with specifying any stride value != 1.
*   **groups**: A positive integer specifying the number of groups in which the input is split along the channel axis. Each group is convolved separately with `filters / groups` filters. The output is the concatenation of all the `groups` results along the channel axis. Input channels and `filters` must both be divisible by `groups`.
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

4+D tensor with shape: `batch_shape + (channels, rows, cols)` if `data_format='channels_first'` or 4+D tensor with shape: `batch_shape + (rows, cols, channels)` if `data_format='channels_last'`.

**Output shape**

4+D tensor with shape: `batch_shape + (filters, new_rows, new_cols)` if `data_format='channels_first'` or 4+D tensor with shape: `batch_shape + (new_rows, new_cols, filters)` if `data_format='channels_last'`. `rows` and `cols` values might have changed due to padding.

**Returns**

A tensor of rank 4+ representing `activation(conv2d(inputs, kernel) + bias)`.

**Raises**

*   **ValueError**: if `padding` is `"causal"`.
*   **ValueError**: when both `strides > 1` and `dilation_rate > 1`.

* * *

[Conv2D layer](https://keras.io/2/api/layers/convolution_layers/convolution2d/#conv2d-layer)

[`Conv2D` class](https://keras.io/2/api/layers/convolution_layers/convolution2d/#conv2d-class)