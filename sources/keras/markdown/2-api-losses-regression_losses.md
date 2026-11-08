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
 / Regression losses

Regression losses
=================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L304)

### `MeanSquaredError` class

Copied!

`tf_keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")`

Computes the mean of squares of errors between labels and predictions.

`loss = mean(square(y_true - y_pred))`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[1., 1.], [1., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> mse = tf.keras.losses.MeanSquaredError() >>> mse(y_true, y_pred).numpy() 0.5`

Copied!

`>>> # Calling with 'sample_weight'. >>> mse(y_true, y_pred, sample_weight=[0.7, 0.3]).numpy() 0.25`

Copied!

`>>> # Using 'sum' reduction type. >>> mse = tf.keras.losses.MeanSquaredError( ...     reduction=tf.keras.losses.Reduction.SUM) >>> mse(y_true, y_pred).numpy() 1.0`

Copied!

`>>> # Using 'none' reduction type. >>> mse = tf.keras.losses.MeanSquaredError( ...     reduction=tf.keras.losses.Reduction.NONE) >>> mse(y_true, y_pred).numpy() array([0.5, 0.5], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.MeanSquaredError())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L364)

### `MeanAbsoluteError` class

Copied!

`tf_keras.losses.MeanAbsoluteError(reduction="auto", name="mean_absolute_error")`

Computes the mean of absolute difference between labels and predictions.

`loss = mean(abs(y_true - y_pred))`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[1., 1.], [1., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> mae = tf.keras.losses.MeanAbsoluteError() >>> mae(y_true, y_pred).numpy() 0.5`

Copied!

`>>> # Calling with 'sample_weight'. >>> mae(y_true, y_pred, sample_weight=[0.7, 0.3]).numpy() 0.25`

Copied!

`>>> # Using 'sum' reduction type. >>> mae = tf.keras.losses.MeanAbsoluteError( ...     reduction=tf.keras.losses.Reduction.SUM) >>> mae(y_true, y_pred).numpy() 1.0`

Copied!

`>>> # Using 'none' reduction type. >>> mae = tf.keras.losses.MeanAbsoluteError( ...     reduction=tf.keras.losses.Reduction.NONE) >>> mae(y_true, y_pred).numpy() array([0.5, 0.5], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.MeanAbsoluteError())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L426)

### `MeanAbsolutePercentageError` class

Copied!

`tf_keras.losses.MeanAbsolutePercentageError(     reduction="auto", name="mean_absolute_percentage_error" )`

Computes the mean absolute percentage error between `y_true` & `y_pred`.

Formula:

`loss = 100 * abs((y_true - y_pred) / y_true)`

Note that to avoid dividing by zero, a small epsilon value is added to the denominator.

Standalone usage:

Copied!

`>>> y_true = [[2., 1.], [2., 3.]] >>> y_pred = [[1., 1.], [1., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> mape = tf.keras.losses.MeanAbsolutePercentageError() >>> mape(y_true, y_pred).numpy() 50.`

Copied!

`>>> # Calling with 'sample_weight'. >>> mape(y_true, y_pred, sample_weight=[0.7, 0.3]).numpy() 20.`

Copied!

`>>> # Using 'sum' reduction type. >>> mape = tf.keras.losses.MeanAbsolutePercentageError( ...     reduction=tf.keras.losses.Reduction.SUM) >>> mape(y_true, y_pred).numpy() 100.`

Copied!

`>>> # Using 'none' reduction type. >>> mape = tf.keras.losses.MeanAbsolutePercentageError( ...     reduction=tf.keras.losses.Reduction.NONE) >>> mape(y_true, y_pred).numpy() array([25., 75.], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=tf.keras.losses.MeanAbsolutePercentageError())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L496)

### `MeanSquaredLogarithmicError` class

Copied!

`tf_keras.losses.MeanSquaredLogarithmicError(     reduction="auto", name="mean_squared_logarithmic_error" )`

Computes the mean squared logarithmic error between `y_true` & `y_pred`.

`loss = square(log(y_true + 1.) - log(y_pred + 1.))`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[1., 1.], [1., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> msle = tf.keras.losses.MeanSquaredLogarithmicError() >>> msle(y_true, y_pred).numpy() 0.240`

Copied!

`>>> # Calling with 'sample_weight'. >>> msle(y_true, y_pred, sample_weight=[0.7, 0.3]).numpy() 0.120`

Copied!

`>>> # Using 'sum' reduction type. >>> msle = tf.keras.losses.MeanSquaredLogarithmicError( ...     reduction=tf.keras.losses.Reduction.SUM) >>> msle(y_true, y_pred).numpy() 0.480`

Copied!

`>>> # Using 'none' reduction type. >>> msle = tf.keras.losses.MeanSquaredLogarithmicError( ...     reduction=tf.keras.losses.Reduction.NONE) >>> msle(y_true, y_pred).numpy() array([0.240, 0.240], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=tf.keras.losses.MeanSquaredLogarithmicError())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1162)

### `CosineSimilarity` class

Copied!

`tf_keras.losses.CosineSimilarity(axis=-1, reduction="auto", name="cosine_similarity")`

Computes the cosine similarity between labels and predictions.

Note that it is a number between -1 and 1. When it is a negative number between -1 and 0, 0 indicates orthogonality and values closer to -1 indicate greater similarity. The values closer to 1 indicate greater dissimilarity. This makes it usable as a loss function in a setting where you try to maximize the proximity between predictions and targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity will be 0 regardless of the proximity between predictions and targets.

`loss = -sum(l2_norm(y_true) * l2_norm(y_pred))`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [1., 1.]] >>> y_pred = [[1., 0.], [1., 1.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> cosine_loss = tf.keras.losses.CosineSimilarity(axis=1) >>> # l2_norm(y_true) = [[0., 1.], [1./1.414, 1./1.414]] >>> # l2_norm(y_pred) = [[1., 0.], [1./1.414, 1./1.414]] >>> # l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]] >>> # loss = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1)) >>> #       = -((0. + 0.) +  (0.5 + 0.5)) / 2 >>> cosine_loss(y_true, y_pred).numpy() -0.5`

Copied!

`>>> # Calling with 'sample_weight'. >>> cosine_loss(y_true, y_pred, sample_weight=[0.8, 0.2]).numpy() -0.0999`

Copied!

`>>> # Using 'sum' reduction type. >>> cosine_loss = tf.keras.losses.CosineSimilarity(axis=1, ...     reduction=tf.keras.losses.Reduction.SUM) >>> cosine_loss(y_true, y_pred).numpy() -0.999`

Copied!

`>>> # Using 'none' reduction type. >>> cosine_loss = tf.keras.losses.CosineSimilarity(axis=1, ...     reduction=tf.keras.losses.Reduction.NONE) >>> cosine_loss(y_true, y_pred).numpy() array([-0., -0.999], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=tf.keras.losses.CosineSimilarity(axis=1))`

**Arguments**

*   **axis**: The axis along which the cosine similarity is computed (the features axis). Defaults to -1.
*   **reduction**: Type of [`tf.keras.losses.Reduction`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction)
     to apply to loss. Default value is `AUTO`. `AUTO` indicates that the reduction option will be determined by the usage context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When used under a [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
    , except via `Model.compile()` and `Model.fit()`, using `AUTO` or `SUM_OVER_BATCH_SIZE` will raise an error. Please see this custom training [tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training)
     for more details.
*   **name**: Optional name for the instance. Defaults to 'cosine\_similarity'.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1671)

### `mean_squared_error` function

Copied!

`tf_keras.losses.mean_squared_error(y_true, y_pred)`

Computes the mean squared error between labels and predictions.

After computing the squared distance between the inputs, the mean value over the last dimension is returned.

`loss = mean(square(y_true - y_pred), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 2, size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.mean_squared_error(y_true, y_pred) >>> assert loss.shape == (2,) >>> assert np.array_equal( ...     loss.numpy(), np.mean(np.square(y_true - y_pred), axis=-1))`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Mean squared error values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1816)

### `mean_absolute_error` function

Copied!

`tf_keras.losses.mean_absolute_error(y_true, y_pred)`

Computes the mean absolute error between labels and predictions.

`loss = mean(abs(y_true - y_pred), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 2, size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.mean_absolute_error(y_true, y_pred) >>> assert loss.shape == (2,) >>> assert np.array_equal( ...     loss.numpy(), np.mean(np.abs(y_true - y_pred), axis=-1))`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Mean absolute error values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1857)

### `mean_absolute_percentage_error` function

Copied!

`tf_keras.losses.mean_absolute_percentage_error(y_true, y_pred)`

Computes the mean absolute percentage error between `y_true` & `y_pred`.

`loss = 100 * mean(abs((y_true - y_pred) / y_true), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.random(size=(2, 3)) >>> y_true = np.maximum(y_true, 1e-7)  # Prevent division by zero >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.mean_absolute_percentage_error(y_true, y_pred) >>> assert loss.shape == (2,) >>> assert np.array_equal( ...     loss.numpy(), ...     100. * np.mean(np.abs((y_true - y_pred) / y_true), axis=-1))`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Mean absolute percentage error values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1906)

### `mean_squared_logarithmic_error` function

Copied!

`tf_keras.losses.mean_squared_logarithmic_error(y_true, y_pred)`

Computes the mean squared logarithmic error between `y_true` & `y_pred`.

`loss = mean(square(log(y_true + 1) - log(y_pred + 1)), axis=-1)`

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 2, size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.mean_squared_logarithmic_error(y_true, y_pred) >>> assert loss.shape == (2,) >>> y_true = np.maximum(y_true, 1e-7) >>> y_pred = np.maximum(y_pred, 1e-7) >>> assert np.allclose( ...     loss.numpy(), ...     np.mean( ...         np.square(np.log(y_true + 1.) - np.log(y_pred + 1.)), axis=-1))`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Mean squared logarithmic error values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2797)

### `cosine_similarity` function

Copied!

`tf_keras.losses.cosine_similarity(y_true, y_pred, axis=-1)`

Computes the cosine similarity between labels and predictions.

Note that it is a number between -1 and 1. When it is a negative number between -1 and 0, 0 indicates orthogonality and values closer to -1 indicate greater similarity. The values closer to 1 indicate greater dissimilarity. This makes it usable as a loss function in a setting where you try to maximize the proximity between predictions and targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity will be 0 regardless of the proximity between predictions and targets.

`loss = -sum(l2_norm(y_true) * l2_norm(y_pred))`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [1., 1.], [1., 1.]] >>> y_pred = [[1., 0.], [1., 1.], [-1., -1.]] >>> loss = tf.keras.losses.cosine_similarity(y_true, y_pred, axis=1) >>> loss.numpy() array([-0., -0.999, 0.999], dtype=float32)`

**Arguments**

*   **y\_true**: Tensor of true targets.
*   **y\_pred**: Tensor of predicted targets.
*   **axis**: Axis along which to determine similarity.

**Returns**

Cosine similarity tensor.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1601)

### `Huber` class

Copied!

`tf_keras.losses.Huber(delta=1.0, reduction="auto", name="huber_loss")`

Computes the Huber loss between `y_true` & `y_pred`.

For each value x in `error = y_true - y_pred`:

Copied!

`loss = 0.5 * x^2                  if |x| <= d loss = 0.5 * d^2 + d * (|x| - d)  if |x| > d`

where d is `delta`. See: https://en.wikipedia.org/wiki/Huber\_loss

Standalone usage:

Copied!

`>>> y_true = [[0, 1], [0, 0]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> h = tf.keras.losses.Huber() >>> h(y_true, y_pred).numpy() 0.155`

Copied!

`>>> # Calling with 'sample_weight'. >>> h(y_true, y_pred, sample_weight=[1, 0]).numpy() 0.09`

Copied!

`>>> # Using 'sum' reduction type. >>> h = tf.keras.losses.Huber( ...     reduction=tf.keras.losses.Reduction.SUM) >>> h(y_true, y_pred).numpy() 0.31`

Copied!

`>>> # Using 'none' reduction type. >>> h = tf.keras.losses.Huber( ...     reduction=tf.keras.losses.Reduction.NONE) >>> h(y_true, y_pred).numpy() array([0.18, 0.13], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.Huber())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2075)

### `huber` function

Copied!

`tf_keras.losses.huber(y_true, y_pred, delta=1.0)`

Computes Huber loss value.

For each value x in `error = y_true - y_pred`:

Copied!

`loss = 0.5 * x^2                  if |x| <= d loss = d * |x| - 0.5 * d^2        if |x| > d`

where d is `delta`. See: https://en.wikipedia.org/wiki/Huber\_loss

**Arguments**

*   **y\_true**: tensor of true targets.
*   **y\_pred**: tensor of predicted targets.
*   **delta**: A float, the point where the Huber loss function changes from a quadratic to linear.

**Returns**

Tensor with one scalar loss entry per sample.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1479)

### `LogCosh` class

Copied!

`tf_keras.losses.LogCosh(reduction="auto", name="log_cosh")`

Computes the logarithm of the hyperbolic cosine of the prediction error.

`logcosh = log((exp(x) + exp(-x))/2)`, where x is the error `y_pred - y_true`.

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[1., 1.], [0., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> l = tf.keras.losses.LogCosh() >>> l(y_true, y_pred).numpy() 0.108`

Copied!

`>>> # Calling with 'sample_weight'. >>> l(y_true, y_pred, sample_weight=[0.8, 0.2]).numpy() 0.087`

Copied!

`>>> # Using 'sum' reduction type. >>> l = tf.keras.losses.LogCosh( ...     reduction=tf.keras.losses.Reduction.SUM) >>> l(y_true, y_pred).numpy() 0.217`

Copied!

`>>> # Using 'none' reduction type. >>> l = tf.keras.losses.LogCosh( ...     reduction=tf.keras.losses.Reduction.NONE) >>> l(y_true, y_pred).numpy() array([0.217, 0.], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.LogCosh())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2113)

### `log_cosh` function

Copied!

`tf_keras.losses.log_cosh(y_true, y_pred)`

Logarithm of the hyperbolic cosine of the prediction error.

`log(cosh(x))` is approximately equal to `(x ** 2) / 2` for small `x` and to `abs(x) - log(2)` for large `x`. This means that 'logcosh' works mostly like the mean squared error, but will not be so strongly affected by the occasional wildly incorrect prediction.

Standalone usage:

Copied!

`>>> y_true = np.random.random(size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.logcosh(y_true, y_pred) >>> assert loss.shape == (2,) >>> x = y_pred - y_true >>> assert np.allclose( ...     loss.numpy(), ...     np.mean(x + np.log(np.exp(-2. * x) + 1.) - tf.math.log(2.), ...             axis=-1), ...     atol=1e-5)`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Logcosh error values. shape = `[batch_size, d0, .. dN-1]`.

* * *

[Regression losses](https://keras.io/2/api/losses/regression_losses/#regression-losses)

[`MeanSquaredError` class](https://keras.io/2/api/losses/regression_losses/#meansquarederror-class)

[`MeanAbsoluteError` class](https://keras.io/2/api/losses/regression_losses/#meanabsoluteerror-class)

[`MeanAbsolutePercentageError` class](https://keras.io/2/api/losses/regression_losses/#meanabsolutepercentageerror-class)

[`MeanSquaredLogarithmicError` class](https://keras.io/2/api/losses/regression_losses/#meansquaredlogarithmicerror-class)

[`CosineSimilarity` class](https://keras.io/2/api/losses/regression_losses/#cosinesimilarity-class)

[`mean_squared_error` function](https://keras.io/2/api/losses/regression_losses/#meansquarederror-function)

[`mean_absolute_error` function](https://keras.io/2/api/losses/regression_losses/#meanabsoluteerror-function)

[`mean_absolute_percentage_error` function](https://keras.io/2/api/losses/regression_losses/#meanabsolutepercentageerror-function)

[`mean_squared_logarithmic_error` function](https://keras.io/2/api/losses/regression_losses/#meansquaredlogarithmicerror-function)

[`cosine_similarity` function](https://keras.io/2/api/losses/regression_losses/#cosinesimilarity-function)

[`Huber` class](https://keras.io/2/api/losses/regression_losses/#huber-class)

[`huber` function](https://keras.io/2/api/losses/regression_losses/#huber-function)

[`LogCosh` class](https://keras.io/2/api/losses/regression_losses/#logcosh-class)

[`log_cosh` function](https://keras.io/2/api/losses/regression_losses/#logcosh-function)