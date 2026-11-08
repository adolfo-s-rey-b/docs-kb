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
 / [Categorical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/categorical/)
 / HashedCrossing layer

HashedCrossing layer
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/hashed_crossing.py#L11)

### `HashedCrossing` class

Copied!

`keras.layers.HashedCrossing(     num_bins, output_mode="int", sparse=False, name=None, dtype=None, **kwargs )`

A preprocessing layer which crosses features using the "hashing trick".

This layer performs crosses of categorical features using the "hashing trick". Conceptually, the transformation can be thought of as: `hash(concatenate(features)) % num_bins`.

This layer currently only performs crosses of scalar inputs and batches of scalar inputs. Valid input shapes are `(batch_size, 1)`, `(batch_size,)` and `()`.

**Note:** This layer wraps [`tf.keras.layers.HashedCrossing`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing)
. It cannot be used as part of the compiled computation graph of a model with any backend other than TensorFlow. It can however be used with any backend when running eagerly. It can also always be used as part of an input preprocessing pipeline with any backend (outside the model itself), which is how we recommend to use this layer.

**Note:** This layer is safe to use inside a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipeline (independently of which backend you're using).

**Arguments**

*   **num\_bins**: Number of hash bins.
*   **output\_mode**: Specification for the output of the layer. Values can be `"int"`, or `"one_hot"` configuring the layer as follows:
    *   `"int"`: Return the integer bin indices directly.
    *   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. Defaults to `"int"`.
*   **sparse**: Boolean. Only applicable to `"one_hot"` mode and only valid when using the TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.
*   **\*\*kwargs**: Keyword arguments to construct a layer.

**Examples**

**Crossing two scalar features.**

Copied!

`>>> layer = keras.layers.HashedCrossing( ...     num_bins=5) >>> feat1 = np.array(['A', 'B', 'A', 'B', 'A']) >>> feat2 = np.array([101, 101, 101, 102, 102]) >>> layer((feat1, feat2)) array([1, 4, 1, 1, 3])`

**Crossing and one-hotting two scalar features.**

Copied!

`>>> layer = keras.layers.HashedCrossing( ...     num_bins=5, output_mode='one_hot') >>> feat1 = np.array(['A', 'B', 'A', 'B', 'A']) >>> feat2 = np.array([101, 101, 101, 102, 102]) >>> layer((feat1, feat2)) array([[0., 1., 0., 0., 0.],         [0., 0., 0., 0., 1.],         [0., 1., 0., 0., 0.],         [0., 1., 0., 0., 0.],         [0., 0., 0., 1., 0.]], dtype=float32)`

* * *

[HashedCrossing layer](https://keras.io/api/layers/preprocessing_layers/categorical/hashed_crossing/#hashedcrossing-layer)

[`HashedCrossing` class](https://keras.io/api/layers/preprocessing_layers/categorical/hashed_crossing/#hashedcrossing-class)