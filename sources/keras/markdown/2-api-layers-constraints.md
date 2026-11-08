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
 / Layer weight constraints

Layer weight constraints
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/constraints.py#L106)

### `MaxNorm` class

Copied!

`tf_keras.constraints.MaxNorm(max_value=2, axis=0)`

MaxNorm weight constraint.

Constrains the weights incident to each hidden unit to have a norm less than or equal to a desired value.

Also available via the shortcut function [`tf.keras.constraints.max_norm`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/max_norm)
.

**Arguments**

*   **max\_value**: the maximum norm value for the incoming weights.
*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/constraints.py#L196)

### `MinMaxNorm` class

Copied!

`tf_keras.constraints.MinMaxNorm(min_value=0.0, max_value=1.0, rate=1.0, axis=0)`

MinMaxNorm weight constraint.

Constrains the weights incident to each hidden unit to have the norm between a lower bound and an upper bound.

Also available via the shortcut function [`tf.keras.constraints.min_max_norm`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/min_max_norm)
.

**Arguments**

*   **min\_value**: the minimum norm for the incoming weights.
*   **max\_value**: the maximum norm for the incoming weights.
*   **rate**: rate for enforcing the constraint: weights will be rescaled to yield `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`. Effectively, this means that rate=1.0 stands for strict enforcement of the constraint, while rate<1.0 means that weights will be rescaled at each step to slowly move towards a value inside the desired interval.
*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/constraints.py#L148)

### `NonNeg` class

Copied!

`tf_keras.constraints.NonNeg()`

Constrains the weights to be non-negative.

Also available via the shortcut function [`tf.keras.constraints.non_neg`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/non_neg)
.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/constraints.py#L159)

### `UnitNorm` class

Copied!

`tf_keras.constraints.UnitNorm(axis=0)`

Constrains the weights incident to each hidden unit to have unit norm.

Also available via the shortcut function [`tf.keras.constraints.unit_norm`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/unit_norm)
.

**Arguments**

*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/constraints.py#L256)

### `RadialConstraint` class

Copied!

`tf_keras.constraints.RadialConstraint()`

Constrains `Conv2D` kernel weights to be the same for each radius.

Also available via the shortcut function [`tf.keras.constraints.radial_constraint`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/radial_constraint)
.

For example, the desired output for the following 4-by-4 kernel:

Copied!

    `kernel = [[v_00, v_01, v_02, v_03],               [v_10, v_11, v_12, v_13],               [v_20, v_21, v_22, v_23],               [v_30, v_31, v_32, v_33]]`

is this::

Copied!

    `kernel = [[v_11, v_11, v_11, v_11],               [v_11, v_33, v_33, v_11],               [v_11, v_33, v_33, v_11],               [v_11, v_11, v_11, v_11]]`

This constraint can be applied to any `Conv2D` layer version, including `Conv2DTranspose` and `SeparableConv2D`, and with either `"channels_last"` or `"channels_first"` data format. The method assumes the weight tensor is of shape `(rows, cols, input_depth, output_depth)`.

* * *

[Layer weight constraints](https://keras.io/2/api/layers/constraints/#layer-weight-constraints)

[`MaxNorm` class](https://keras.io/2/api/layers/constraints/#maxnorm-class)

[`MinMaxNorm` class](https://keras.io/2/api/layers/constraints/#minmaxnorm-class)

[`NonNeg` class](https://keras.io/2/api/layers/constraints/#nonneg-class)

[`UnitNorm` class](https://keras.io/2/api/layers/constraints/#unitnorm-class)

[`RadialConstraint` class](https://keras.io/2/api/layers/constraints/#radialconstraint-class)