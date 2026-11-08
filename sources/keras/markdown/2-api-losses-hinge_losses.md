None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Probabilistic losses](https://keras.io/2/api/losses/probabilistic_losses/)
 [Regression losses](https://keras.io/2/api/losses/regression_losses/)
 [Hinge losses for "maximum-margin" classification](https://keras.io/2/api/losses/hinge_losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Losses](https://keras.io/2/api/losses/)
 / Hinge losses for "maximum-margin" classification

Hinge losses for "maximum-margin" classification
================================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1239)

### `Hinge` class

Copied!

`tf_keras.losses.Hinge(reduction="auto", name="hinge")`

Computes the hinge loss between `y_true` & `y_pred`.

`loss = maximum(1 - y_true * y_pred, 0)`

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> h = tf.keras.losses.Hinge() >>> h(y_true, y_pred).numpy() 1.3`

Copied!

`>>> # Calling with 'sample_weight'. >>> h(y_true, y_pred, sample_weight=[1, 0]).numpy() 0.55`

Copied!

`>>> # Using 'sum' reduction type. >>> h = tf.keras.losses.Hinge( ...     reduction=tf.keras.losses.Reduction.SUM) >>> h(y_true, y_pred).numpy() 2.6`

Copied!

`>>> # Using 'none' reduction type. >>> h = tf.keras.losses.Hinge( ...     reduction=tf.keras.losses.Reduction.NONE) >>> h(y_true, y_pred).numpy() array([1.1, 1.5], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.Hinge())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1299)

### `SquaredHinge` class

Copied!

`tf_keras.losses.SquaredHinge(reduction="auto", name="squared_hinge")`

Computes the squared hinge loss between `y_true` & `y_pred`.

`loss = square(maximum(1 - y_true * y_pred, 0))`

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> h = tf.keras.losses.SquaredHinge() >>> h(y_true, y_pred).numpy() 1.86`

Copied!

`>>> # Calling with 'sample_weight'. >>> h(y_true, y_pred, sample_weight=[1, 0]).numpy() 0.73`

Copied!

`>>> # Using 'sum' reduction type. >>> h = tf.keras.losses.SquaredHinge( ...     reduction=tf.keras.losses.Reduction.SUM) >>> h(y_true, y_pred).numpy() 3.72`

Copied!

`>>> # Using 'none' reduction type. >>> h = tf.keras.losses.SquaredHinge( ...     reduction=tf.keras.losses.Reduction.NONE) >>> h(y_true, y_pred).numpy() array([1.46, 2.26], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.SquaredHinge())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1361)

### `CategoricalHinge` class

Copied!

`tf_keras.losses.CategoricalHinge(reduction="auto", name="categorical_hinge")`

Computes the categorical hinge loss between `y_true` & `y_pred`.

`loss = maximum(neg - pos + 1, 0)` where `neg=maximum((1-y_true)*y_pred) and pos=sum(y_true*y_pred)`

Standalone usage:

Copied!

`>>> y_true = [[0, 1], [0, 0]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> h = tf.keras.losses.CategoricalHinge() >>> h(y_true, y_pred).numpy() 1.4`

Copied!

`>>> # Calling with 'sample_weight'. >>> h(y_true, y_pred, sample_weight=[1, 0]).numpy() 0.6`

Copied!

`>>> # Using 'sum' reduction type. >>> h = tf.keras.losses.CategoricalHinge( ...     reduction=tf.keras.losses.Reduction.SUM) >>> h(y_true, y_pred).numpy() 2.8`

Copied!

`>>> # Using 'none' reduction type. >>> h = tf.keras.losses.CategoricalHinge( ...     reduction=tf.keras.losses.Reduction.NONE) >>> h(y_true, y_pred).numpy() array([1.2, 1.6], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.CategoricalHinge())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2008)

### `hinge` function

Copied!

`tf_keras.losses.hinge(y_true, y_pred)`

Computes the hinge loss between `y_true` & `y_pred`.

`loss = mean(maximum(1 - y_true * y_pred, 0), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.choice([-1, 1], size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.hinge(y_true, y_pred) >>> assert loss.shape == (2,) >>> assert np.array_equal( ...     loss.numpy(), ...     np.mean(np.maximum(1. - y_true * y_pred, 0.), axis=-1))`

**Arguments**

*   **y\_true**: The ground truth values. `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Hinge loss values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1974)

### `squared_hinge` function

Copied!

`tf_keras.losses.squared_hinge(y_true, y_pred)`

Computes the squared hinge loss between `y_true` & `y_pred`.

`loss = mean(square(maximum(1 - y_true * y_pred, 0)), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.choice([-1, 1], size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.squared_hinge(y_true, y_pred) >>> assert loss.shape == (2,) >>> assert np.array_equal( ...     loss.numpy(), ...     np.mean(np.square(np.maximum(1. - y_true * y_pred, 0.)), axis=-1))`

**Arguments**

*   **y\_true**: The ground truth values. `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Squared hinge loss values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2040)

### `categorical_hinge` function

Copied!

`tf_keras.losses.categorical_hinge(y_true, y_pred)`

Computes the categorical hinge loss between `y_true` & `y_pred`.

`loss = maximum(neg - pos + 1, 0)` where `neg=maximum((1-y_true)*y_pred) and pos=sum(y_true*y_pred)`

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 3, size=(2,)) >>> y_true = tf.keras.utils.to_categorical(y_true, num_classes=3) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.categorical_hinge(y_true, y_pred) >>> assert loss.shape == (2,) >>> pos = np.sum(y_true * y_pred, axis=-1) >>> neg = np.amax((1. - y_true) * y_pred, axis=-1) >>> assert np.array_equal(loss.numpy(), np.maximum(0., neg - pos + 1.))`

**Arguments**

*   **y\_true**: The ground truth values. `y_true` values are expected to be either `{-1, +1}` or `{0, 1}` (i.e. a one-hot-encoded tensor).
*   **y\_pred**: The predicted values.

**Returns**

Categorical hinge loss values.

* * *

[Hinge losses for "maximum-margin" classification](https://keras.io/2/api/losses/hinge_losses/#hinge-losses-for-maximummargin-classification)

[`Hinge` class](https://keras.io/2/api/losses/hinge_losses/#hinge-class)

[`SquaredHinge` class](https://keras.io/2/api/losses/hinge_losses/#squaredhinge-class)

[`CategoricalHinge` class](https://keras.io/2/api/losses/hinge_losses/#categoricalhinge-class)

[`hinge` function](https://keras.io/2/api/losses/hinge_losses/#hinge-function)

[`squared_hinge` function](https://keras.io/2/api/losses/hinge_losses/#squaredhinge-function)

[`categorical_hinge` function](https://keras.io/2/api/losses/hinge_losses/#categoricalhinge-function)