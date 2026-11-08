None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Accuracy metrics](https://keras.io/2/api/metrics/accuracy_metrics/)
 [Probabilistic metrics](https://keras.io/2/api/metrics/probabilistic_metrics/)
 [Regression metrics](https://keras.io/2/api/metrics/regression_metrics/)
 [Classification metrics based on True/False positives & negatives](https://keras.io/2/api/metrics/classification_metrics/)
 [Image segmentation metrics](https://keras.io/2/api/metrics/segmentation_metrics/)
 [Hinge metrics for "maximum-margin" classification](https://keras.io/2/api/metrics/hinge_metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Metrics](https://keras.io/2/api/metrics/)
 / Regression metrics

Regression metrics
==================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L250)

### `MeanSquaredError` class

Copied!

`tf_keras.metrics.MeanSquaredError(name="mean_squared_error", dtype=None)`

Computes the mean squared error between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.MeanSquaredError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.25`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.MeanSquaredError()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L323)

### `RootMeanSquaredError` class

Copied!

`tf_keras.metrics.RootMeanSquaredError(name="root_mean_squared_error", dtype=None)`

Computes root mean squared error metric between `y_true` and `y_pred`.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.RootMeanSquaredError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.70710677`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.RootMeanSquaredError()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L177)

### `MeanAbsoluteError` class

Copied!

`tf_keras.metrics.MeanAbsoluteError(name="mean_absolute_error", dtype=None)`

Computes the mean absolute error between the labels and predictions.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.MeanAbsoluteError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.25`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.MeanAbsoluteError()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L213)

### `MeanAbsolutePercentageError` class

Copied!

`tf_keras.metrics.MeanAbsolutePercentageError(     name="mean_absolute_percentage_error", dtype=None )`

Computes the mean absolute percentage error between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.MeanAbsolutePercentageError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 250000000.0`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 500000000.0`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.MeanAbsolutePercentageError()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L286)

### `MeanSquaredLogarithmicError` class

Copied!

`tf_keras.metrics.MeanSquaredLogarithmicError(     name="mean_squared_logarithmic_error", dtype=None )`

Computes the mean squared logarithmic error between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.MeanSquaredLogarithmicError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.12011322`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.24022643`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.MeanSquaredLogarithmicError()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L127)

### `CosineSimilarity` class

Copied!

`tf_keras.metrics.CosineSimilarity(name="cosine_similarity", dtype=None, axis=-1)`

Computes the cosine similarity between the labels and predictions.

`cosine similarity = (a . b) / ||a|| ||b||`

See: [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
.

This metric keeps the average cosine similarity between `predictions` and `labels` over a stream of data.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **axis**: (Optional) The dimension along which the cosine similarity is computed. Defaults to `-1`.

Standalone usage:

Copied!

`>>> # l2_norm(y_true) = [[0., 1.], [1./1.414, 1./1.414]] >>> # l2_norm(y_pred) = [[1., 0.], [1./1.414, 1./1.414]] >>> # l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]] >>> # result = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1)) >>> #        = ((0. + 0.) +  (0.5 + 0.5)) / 2 >>> m = tf.keras.metrics.CosineSimilarity(axis=1) >>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]]) >>> m.result().numpy() 0.49999997`

Copied!

`>>> m.reset_state() >>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]], ...                sample_weight=[0.3, 0.7]) >>> m.result().numpy() 0.6999999`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.CosineSimilarity(axis=1)])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/regression_metrics.py#L379)

### `LogCoshError` class

Copied!

`tf_keras.metrics.LogCoshError(name="logcosh", dtype=None)`

Computes the logarithm of the hyperbolic cosine of the prediction error.

`logcosh = log((exp(x) + exp(-x))/2)`, where x is the error (y\_pred - y\_true)

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.LogCoshError() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.10844523`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.21689045`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[tf.keras.metrics.LogCoshError()])`

* * *

[Regression metrics](https://keras.io/2/api/metrics/regression_metrics/#regression-metrics)

[`MeanSquaredError` class](https://keras.io/2/api/metrics/regression_metrics/#meansquarederror-class)

[`RootMeanSquaredError` class](https://keras.io/2/api/metrics/regression_metrics/#rootmeansquarederror-class)

[`MeanAbsoluteError` class](https://keras.io/2/api/metrics/regression_metrics/#meanabsoluteerror-class)

[`MeanAbsolutePercentageError` class](https://keras.io/2/api/metrics/regression_metrics/#meanabsolutepercentageerror-class)

[`MeanSquaredLogarithmicError` class](https://keras.io/2/api/metrics/regression_metrics/#meansquaredlogarithmicerror-class)

[`CosineSimilarity` class](https://keras.io/2/api/metrics/regression_metrics/#cosinesimilarity-class)

[`LogCoshError` class](https://keras.io/2/api/metrics/regression_metrics/#logcosherror-class)