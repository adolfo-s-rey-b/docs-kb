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
 / [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 / [Numerical features preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/numerical/)
 / Normalization layer

Normalization layer
===================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/normalization.py#L29)

### `Normalization` class

Copied!

`tf_keras.layers.Normalization(     axis=-1, mean=None, variance=None, invert=False, **kwargs )`

A preprocessing layer which normalizes continuous features.

This layer will shift and scale inputs into a distribution centered around 0 with standard deviation 1. It accomplishes this by precomputing the mean and variance of the data, and calling `(input - mean) / sqrt(var)` at runtime.

The mean and variance values for the layer must be either supplied on construction or learned via `adapt()`. `adapt()` will compute the mean and variance of the data and store them as the layer's weights. `adapt()` should be called before `fit()`, `evaluate()`, or `predict()`.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Arguments**

*   **axis**: Integer, tuple of integers, or None. The axis or axes that should have a separate mean and variance for each index in the shape. For example, if shape is `(None, 5)` and `axis=1`, the layer will track 5 separate mean and variance values for the last axis. If `axis` is set to `None`, the layer will normalize all elements in the input by a scalar mean and variance. When `-1` the last axis of the input is assumed to be a feature dimension and is normalized per index. Note that in the specific case of batched scalar inputs where the only axis is the batch axis, the default will normalize each index in the batch separately. In this case, consider passing `axis=None`. Defaults to `-1`.
*   **mean**: The mean value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called.
*   **variance**: The variance value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called.
*   **invert**: If True, this layer will apply the inverse transformation to its inputs: it would turn a normalized input back into its original form.

**Examples**

Calculate a global mean and variance by analyzing the dataset in `adapt()`.

Copied!

`>>> adapt_data = np.array([1., 2., 3., 4., 5.], dtype='float32') >>> input_data = np.array([1., 2., 3.], dtype='float32') >>> layer = tf.keras.layers.Normalization(axis=None) >>> layer.adapt(adapt_data) >>> layer(input_data) <tf.Tensor: shape=(3,), dtype=float32, numpy= array([-1.4142135, -0.70710677, 0.], dtype=float32)>`

Calculate a mean and variance for each index on the last axis.

Copied!

`>>> adapt_data = np.array([[0., 7., 4.], ...                        [2., 9., 6.], ...                        [0., 7., 4.], ...                        [2., 9., 6.]], dtype='float32') >>> input_data = np.array([[0., 7., 4.]], dtype='float32') >>> layer = tf.keras.layers.Normalization(axis=-1) >>> layer.adapt(adapt_data) >>> layer(input_data) <tf.Tensor: shape=(1, 3), dtype=float32, numpy= array([-1., -1., -1.], dtype=float32)>`

Pass the mean and variance directly.

Copied!

`>>> input_data = np.array([[1.], [2.], [3.]], dtype='float32') >>> layer = tf.keras.layers.Normalization(mean=3., variance=2.) >>> layer(input_data) <tf.Tensor: shape=(3, 1), dtype=float32, numpy= array([[-1.4142135 ],        [-0.70710677],        [ 0.        ]], dtype=float32)>`

Use the layer to de-normalize inputs (after adapting the layer).

Copied!

`>>> adapt_data = np.array([[0., 7., 4.], ...                        [2., 9., 6.], ...                        [0., 7., 4.], ...                        [2., 9., 6.]], dtype='float32') >>> input_data = np.array([[1., 2., 3.]], dtype='float32') >>> layer = tf.keras.layers.Normalization(axis=-1, invert=True) >>> layer.adapt(adapt_data) >>> layer(input_data) <tf.Tensor: shape=(1, 3), dtype=float32, numpy= array([2., 10., 8.], dtype=float32)>`

* * *

[Normalization layer](https://keras.io/2/api/layers/preprocessing_layers/numerical/normalization/#normalization-layer)

[`Normalization` class](https://keras.io/2/api/layers/preprocessing_layers/numerical/normalization/#normalization-class)