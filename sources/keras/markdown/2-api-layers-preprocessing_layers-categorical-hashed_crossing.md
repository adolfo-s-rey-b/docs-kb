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
 / [Categorical features preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/categorical/)
 / HashedCrossing layer

HashedCrossing layer
====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/preprocessing/hashed_crossing.py#L32)

### `HashedCrossing` class

Copied!

`tf_keras.layers.HashedCrossing(num_bins, output_mode="int", sparse=False, **kwargs)`

A preprocessing layer which crosses features using the "hashing trick".

This layer performs crosses of categorical features using the "hashing trick". Conceptually, the transformation can be thought of as: `hash(concatenate(features)) % num_bins`.

This layer currently only performs crosses of scalar inputs and batches of scalar inputs. Valid input shapes are `(batch_size, 1)`, `(batch_size,)` and `()`.

For an overview and full list of preprocessing layers, see the preprocessing [guide](https://keras.io/guides/preprocessing_layers)
.

**Arguments**

*   **num\_bins**: Number of hash bins.
*   **output\_mode**: Specification for the output of the layer. Values can be `"int"`, or `"one_hot"` configuring the layer as follows:
    *   `"int"`: Return the integer bin indices directly.
    *   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. Defaults to `"int"`.
*   **sparse**: Boolean. Only applicable to `"one_hot"` mode. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`.
*   **\*\*kwargs**: Keyword arguments to construct a layer.

**Examples**

**Crossing two scalar features.**

Copied!

`>>> layer = tf.keras.layers.HashedCrossing( ...     num_bins=5) >>> feat1 = tf.constant(['A', 'B', 'A', 'B', 'A']) >>> feat2 = tf.constant([101, 101, 101, 102, 102]) >>> layer((feat1, feat2)) <tf.Tensor: shape=(5,), dtype=int64, numpy=array([1, 4, 1, 1, 3])>`

**Crossing and one-hotting two scalar features.**

Copied!

`>>> layer = tf.keras.layers.HashedCrossing( ...     num_bins=5, output_mode='one_hot') >>> feat1 = tf.constant(['A', 'B', 'A', 'B', 'A']) >>> feat2 = tf.constant([101, 101, 101, 102, 102]) >>> layer((feat1, feat2)) <tf.Tensor: shape=(5, 5), dtype=float32, numpy=   array([[0., 1., 0., 0., 0.],          [0., 0., 0., 0., 1.],          [0., 1., 0., 0., 0.],          [0., 1., 0., 0., 0.],          [0., 0., 0., 1., 0.]], dtype=float32)>`

* * *

[HashedCrossing layer](https://keras.io/2/api/layers/preprocessing_layers/categorical/hashed_crossing/#hashedcrossing-layer)

[`HashedCrossing` class](https://keras.io/2/api/layers/preprocessing_layers/categorical/hashed_crossing/#hashedcrossing-class)