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
 / [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 / ZeroPadding1D layer

ZeroPadding1D layer
===================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/reshaping/zero_padding1d.py#L29)

### `ZeroPadding1D` class

Copied!

`tf_keras.layers.ZeroPadding1D(padding=1, **kwargs)`

Zero-padding layer for 1D input (e.g. temporal sequence).

**Examples**

Copied!

`>>> input_shape = (2, 2, 3) >>> x = np.arange(np.prod(input_shape)).reshape(input_shape) >>> print(x) [[[ 0  1  2]   [ 3  4  5]]  [[ 6  7  8]   [ 9 10 11]]] >>> y = tf.keras.layers.ZeroPadding1D(padding=2)(x) >>> print(y) tf.Tensor(   [[[ 0  0  0]     [ 0  0  0]     [ 0  1  2]     [ 3  4  5]     [ 0  0  0]     [ 0  0  0]]    [[ 0  0  0]     [ 0  0  0]     [ 6  7  8]     [ 9 10 11]     [ 0  0  0]     [ 0  0  0]]], shape=(2, 6, 3), dtype=int64)`

**Arguments**

*   **padding**: Int, or tuple of int (length 2).
    *   If int: How many zeros to add at the beginning and end of the padding dimension (axis 1).
    *   If tuple of int (length 2): How many zeros to add at the beginning and the end of the padding dimension (`(left_pad, right_pad)`).

**Input shape**

3D tensor with shape `(batch_size, axis_to_pad, features)`

**Output shape**

3D tensor with shape `(batch_size, padded_axis, features)`

* * *

[ZeroPadding1D layer](https://keras.io/2/api/layers/reshaping_layers/zero_padding1d/#zeropadding1d-layer)

[`ZeroPadding1D` class](https://keras.io/2/api/layers/reshaping_layers/zero_padding1d/#zeropadding1d-class)