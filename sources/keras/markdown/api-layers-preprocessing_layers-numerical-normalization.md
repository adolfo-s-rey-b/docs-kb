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
 / [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 / [Numerical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/numerical/)
 / Normalization layer

Normalization layer
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/normalization.py#L21)

### `Normalization` class

Copied!

`keras.layers.Normalization(axis=-1, mean=None, variance=None, invert=False, **kwargs)`

A preprocessing layer that normalizes continuous features.

This layer will shift and scale inputs into a distribution centered around 0 with standard deviation 1. It accomplishes this by precomputing the mean and variance of the data, and calling `(input - mean) / sqrt(var)` at runtime.

The mean and variance values for the layer must be either supplied on construction or learned via `adapt()`. `adapt()` will compute the mean and variance of the data and store them as the layer's weights. `adapt()` should be called before `fit()`, `evaluate()`, or `predict()`.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 or `grain` pipeline (independently of which backend you're using).

**Arguments**

*   **axis**: Integer, tuple of integers, or None. The axis or axes that should have a separate mean and variance for each index in the shape. For example, if shape is `(None, 5)` and `axis=1`, the layer will track 5 separate mean and variance values for the last axis. If `axis` is set to `None`, the layer will normalize all elements in the input by a scalar mean and variance. When `-1`, the last axis of the input is assumed to be a feature dimension and is normalized per index. Note that in the specific case of batched scalar inputs where the only axis is the batch axis, the default will normalize each index in the batch separately. In this case, consider passing `axis=None`. Defaults to `-1`.
*   **mean**: The mean value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. `mean` and `variance` must be specified together.
*   **variance**: The variance value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. `mean` and `variance` must be specified together.
*   **invert**: If `True`, this layer will apply the inverse transformation to its inputs: it would turn a normalized input back into its original form.

**Examples**

Calculate a global mean and variance by analyzing the dataset in `adapt()`.

Copied!

`>>> adapt_data = np.array([1., 2., 3., 4., 5.], dtype='float32') >>> input_data = np.array([1., 2., 3.], dtype='float32') >>> layer = keras.layers.Normalization(axis=None) >>> layer.adapt(adapt_data) >>> layer(input_data) array([-1.4142135, -0.70710677, 0.], dtype=float32)`

Calculate a mean and variance for each index on the last axis.

Copied!

`>>> adapt_data = np.array([[0., 7., 4.], ...                        [2., 9., 6.], ...                        [0., 7., 4.], ...                        [2., 9., 6.]], dtype='float32') >>> input_data = np.array([[0., 7., 4.]], dtype='float32') >>> layer = keras.layers.Normalization(axis=-1) >>> layer.adapt(adapt_data) >>> layer(input_data) array([-1., -1., -1.], dtype=float32)`

Pass the mean and variance directly.

Copied!

`>>> input_data = np.array([[1.], [2.], [3.]], dtype='float32') >>> layer = keras.layers.Normalization(mean=3., variance=2.) >>> layer(input_data) array([[-1.4142135 ],        [-0.70710677],        [ 0.        ]], dtype=float32)`

Use the layer to de-normalize inputs (after adapting the layer).

Copied!

`>>> adapt_data = np.array([[0., 7., 4.], ...                        [2., 9., 6.], ...                        [0., 7., 4.], ...                        [2., 9., 6.]], dtype='float32') >>> input_data = np.array([[1., 2., 3.]], dtype='float32') >>> layer = keras.layers.Normalization(axis=-1, invert=True) >>> layer.adapt(adapt_data) >>> layer(input_data) array([2., 10., 8.], dtype=float32)`

* * *

[Normalization layer](https://keras.io/api/layers/preprocessing_layers/numerical/normalization/#normalization-layer)

[`Normalization` class](https://keras.io/api/layers/preprocessing_layers/numerical/normalization/#normalization-class)