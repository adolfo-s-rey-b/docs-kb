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
 / Layer weight regularizers

Layer weight regularizers
=========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/regularizers.py#L259)

### `L1` class

Copied!

`tf_keras.regularizers.L1(l1=0.01, **kwargs)`

A regularizer that applies a L1 regularization penalty.

The L1 regularization penalty is computed as: `loss = l1 * reduce_sum(abs(x))`

L1 may be passed to a layer as a string identifier:

Copied!

`>>> dense = tf.keras.layers.Dense(3, kernel_regularizer='l1')`

In this case, the default value used is `l1=0.01`.

**Arguments**

*   **l1**: Float; L1 regularization factor.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/regularizers.py#L293)

### `L2` class

Copied!

`tf_keras.regularizers.L2(l2=0.01, **kwargs)`

A regularizer that applies a L2 regularization penalty.

The L2 regularization penalty is computed as: `loss = l2 * reduce_sum(square(x))`

L2 may be passed to a layer as a string identifier:

Copied!

`>>> dense = tf.keras.layers.Dense(3, kernel_regularizer='l2')`

In this case, the default value used is `l2=0.01`.

**Arguments**

*   **l2**: Float; L2 regularization factor.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/regularizers.py#L213)

### `L1L2` class

Copied!

`tf_keras.regularizers.L1L2(l1=0.0, l2=0.0)`

A regularizer that applies both L1 and L2 regularization penalties.

The L1 regularization penalty is computed as: `loss = l1 * reduce_sum(abs(x))`

The L2 regularization penalty is computed as `loss = l2 * reduce_sum(square(x))`

L1L2 may be passed to a layer as a string identifier:

Copied!

`>>> dense = tf.keras.layers.Dense(3, kernel_regularizer='l1_l2')`

In this case, the default values used are `l1=0.01` and `l2=0.01`.

**Arguments**

*   **l1**: Float; L1 regularization factor.
*   **l2**: Float; L2 regularization factor.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/regularizers.py#L328)

### `OrthogonalRegularizer` class

Copied!

`tf_keras.regularizers.OrthogonalRegularizer(factor=0.01, mode="rows")`

Regularizer that encourages input vectors to be orthogonal to each other.

It can be applied to either the rows of a matrix (`mode="rows"`) or its columns (`mode="columns"`). When applied to a `Dense` kernel of shape `(input_dim, units)`, rows mode will seek to make the feature vectors (i.e. the basis of the output space) orthogonal to each other.

**Arguments**

*   **factor**: Float. The regularization factor. The regularization penalty will be proportional to `factor` times the mean of the dot products between the L2-normalized rows (if `mode="rows"`, or columns if `mode="columns"`) of the inputs, excluding the product of each row/column with itself. Defaults to 0.01.
*   **mode**: String, one of `{"rows", "columns"}`. Defaults to `"rows"`. In rows mode, the regularization effect seeks to make the rows of the input orthogonal to each other. In columns mode, it seeks to make the columns of the input orthogonal to each other.

**Example**

Copied!

`>>> regularizer = tf.keras.regularizers.OrthogonalRegularizer(factor=0.01) >>> layer = tf.keras.layers.Dense(units=4, kernel_regularizer=regularizer)`

* * *

[Layer weight regularizers](https://keras.io/2/api/layers/regularizers/#layer-weight-regularizers)

[`L1` class](https://keras.io/2/api/layers/regularizers/#l1-class)

[`L2` class](https://keras.io/2/api/layers/regularizers/#l2-class)

[`L1L2` class](https://keras.io/2/api/layers/regularizers/#l1l2-class)

[`OrthogonalRegularizer` class](https://keras.io/2/api/layers/regularizers/#orthogonalregularizer-class)