None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Probabilistic losses](https://keras.io/api/losses/probabilistic_losses/)
 [Regression losses](https://keras.io/api/losses/regression_losses/)
 [Hinge losses for "maximum-margin" classification](https://keras.io/api/losses/hinge_losses/)
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
 / [Losses](https://keras.io/api/losses/)
 / Regression losses

Regression losses
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L52)

### `MeanSquaredError` class

Copied!

`keras.losses.MeanSquaredError(     reduction="sum_over_batch_size", name="mean_squared_error", dtype=None )`

Computes the mean of squares of errors between labels and predictions.

Formula:

Copied!

`loss = mean(square(y_true - y_pred))`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Copied!

`>>> y_true = keras.ops.array([1.0, 0.0, 1.0]) >>> y_pred = keras.ops.array([0.9, 0.1, 0.8]) >>> loss = keras.losses.MeanSquaredError() >>> loss(y_true, y_pred) 0.02`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L101)

### `MeanAbsoluteError` class

Copied!

`keras.losses.MeanAbsoluteError(     reduction="sum_over_batch_size", name="mean_absolute_error", dtype=None )`

Computes the mean of absolute difference between labels and predictions.

Formula:

Copied!

`loss = mean(abs(y_true - y_pred))`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Copied!

`>>> y_true = keras.ops.array([1.0, 0.3, 1.0]) >>> y_pred = keras.ops.array([1.9, 0.3, 1.8]) >>> loss = keras.losses.MeanAbsoluteError() >>> loss(y_true, y_pred) 0.5666667`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L150)

### `MeanAbsolutePercentageError` class

Copied!

`keras.losses.MeanAbsolutePercentageError(     reduction="sum_over_batch_size", name="mean_absolute_percentage_error", dtype=None )`

Computes the mean absolute percentage error between `y_true` & `y_pred`.

Formula:

Copied!

`loss = 100 * mean(abs((y_true - y_pred) / y_true))`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Copied!

`>>> y_true = keras.ops.array([100.0, 200.0, 300.0]) >>> y_pred = keras.ops.array([90.0, 210.0, 310.0]) >>> loss = keras.losses.MeanAbsolutePercentageError() >>> loss(y_true, y_pred) 6.111111`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L202)

### `MeanSquaredLogarithmicError` class

Copied!

`keras.losses.MeanSquaredLogarithmicError(     reduction="sum_over_batch_size", name="mean_squared_logarithmic_error", dtype=None )`

Computes the mean squared logarithmic error between `y_true` & `y_pred`.

Formula:

Copied!

`loss = mean(square(log(y_true + 1) - log(y_pred + 1)))`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L246)

### `CosineSimilarity` class

Copied!

`keras.losses.CosineSimilarity(     axis=-1, reduction="sum_over_batch_size", name="cosine_similarity", dtype=None )`

Computes the cosine similarity between `y_true` & `y_pred`.

Note that it is a number between -1 and 1. When it is a negative number between -1 and 0, 0 indicates orthogonality and values closer to -1 indicate greater similarity. This makes it usable as a loss function in a setting where you try to maximize the proximity between predictions and targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity will be 0 regardless of the proximity between predictions and targets.

Formula:

Copied!

`loss = -sum(l2_norm(y_true) * l2_norm(y_pred))`

**Arguments**

*   **axis**: The axis along which the cosine similarity is computed (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L301)

### `Huber` class

Copied!

`keras.losses.Huber(     delta=1.0, reduction="sum_over_batch_size", name="huber_loss", dtype=None )`

Computes the Huber loss between `y_true` & `y_pred`.

Formula:

Copied!

`for x in error:     if abs(x) <= delta:         loss.append(0.5 * x^2)     elif abs(x) > delta:         loss.append(delta * abs(x) - 0.5 * delta^2)  loss = mean(loss, axis=-1)`

See: [Huber loss](https://en.wikipedia.org/wiki/Huber_loss)
.

**Arguments**

*   **delta**: A float, the point where the Huber loss function changes from a quadratic to linear.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L356)

### `LogCosh` class

Copied!

`keras.losses.LogCosh(reduction="sum_over_batch_size", name="log_cosh", dtype=None)`

Computes the logarithm of the hyperbolic cosine of the prediction error.

Formula:

Copied!

`` error = y_pred - y_true logcosh = mean(log((exp(error) + exp(-error))/2), axis=-1)` ``

where x is the error `y_pred - y_true`.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1376)

### `Tversky` class

Copied!

`keras.losses.Tversky(     alpha=0.5,     beta=0.5,     reduction="sum_over_batch_size",     name="tversky",     axis=None,     dtype=None, )`

Computes the Tversky loss value between `y_true` and `y_pred`.

This loss function is weighted by the alpha and beta coefficients that penalize false positives and false negatives.

With `alpha=0.5` and `beta=0.5`, the loss value becomes equivalent to Dice Loss.

**Arguments**

*   **alpha**: The coefficient controlling incidence of false positives. Defaults to `0.5`.
*   **beta**: The coefficient controlling incidence of false negatives. Defaults to `0.5`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Returns**

Tversky loss value.

**Reference**

*   [Salehi et al., 2017](https://arxiv.org/abs/1706.05721)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1302)

### `Dice` class

Copied!

`keras.losses.Dice(     reduction="sum_over_batch_size", name="dice", axis=None, dtype=None )`

Computes the Dice loss value between `y_true` and `y_pred`.

Formula:

Copied!

`loss = 1 - (2 * sum(y_true * y_pred)) / (sum(y_true) + sum(y_pred))`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **axis**: Tuple for which dimensions the loss is calculated. Defaults to `None`.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Returns**

Dice loss value.

**Example**

Copied!

`>>> y_true = [[[[1.0], [1.0]], [[0.0], [0.0]]], ...           [[[1.0], [1.0]], [[0.0], [0.0]]]] >>> y_pred = [[[[0.0], [1.0]], [[0.0], [1.0]]], ...           [[[0.4], [0.0]], [[0.0], [0.9]]]] >>> axis = (1, 2, 3) >>> loss = keras.losses.Dice(axis=axis, reduction=None)(y_true, y_pred) >>> assert loss.shape == (2,) >>> loss array([0.5, 0.75757575], shape=(2,), dtype=float32)`

Copied!

`>>> loss = keras.losses.Dice()(y_true, y_pred) >>> assert loss.shape == () >>> loss array(0.6164384, shape=(), dtype=float32)`

Copied!

`>>> y_true = np.array(y_true) >>> y_pred = np.array(y_pred) >>> loss = keras.losses.Dice(axis=axis, reduction=None)(y_true, y_pred) >>> assert loss.shape == (2,) >>> loss array([0.5, 0.75757575], shape=(2,), dtype=float32)`

* * *

[Regression losses](https://keras.io/api/losses/regression_losses/#regression-losses)

[`MeanSquaredError` class](https://keras.io/api/losses/regression_losses/#meansquarederror-class)

[`MeanAbsoluteError` class](https://keras.io/api/losses/regression_losses/#meanabsoluteerror-class)

[`MeanAbsolutePercentageError` class](https://keras.io/api/losses/regression_losses/#meanabsolutepercentageerror-class)

[`MeanSquaredLogarithmicError` class](https://keras.io/api/losses/regression_losses/#meansquaredlogarithmicerror-class)

[`CosineSimilarity` class](https://keras.io/api/losses/regression_losses/#cosinesimilarity-class)

[`Huber` class](https://keras.io/api/losses/regression_losses/#huber-class)

[`LogCosh` class](https://keras.io/api/losses/regression_losses/#logcosh-class)

[`Tversky` class](https://keras.io/api/losses/regression_losses/#tversky-class)

[`Dice` class](https://keras.io/api/losses/regression_losses/#dice-class)