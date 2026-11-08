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
 / Hinge metrics for "maximum-margin" classification

Hinge metrics for "maximum-margin" classification
=================================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/hinge_metrics.py#L27)

### `Hinge` class

Copied!

`tf_keras.metrics.Hinge(name="hinge", dtype=None)`

Computes the hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.Hinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 1.3`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 1.1`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd', loss='mse', metrics=[tf.keras.metrics.Hinge()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/hinge_metrics.py#L64)

### `SquaredHinge` class

Copied!

`tf_keras.metrics.SquaredHinge(name="squared_hinge", dtype=None)`

Computes the squared hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.SquaredHinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 1.86`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 1.46`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.SquaredHinge()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/hinge_metrics.py#L103)

### `CategoricalHinge` class

Copied!

`tf_keras.metrics.CategoricalHinge(name="categorical_hinge", dtype=None)`

Computes the categorical hinge metric between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.CategoricalHinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 1.4000001`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 1.2`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.CategoricalHinge()])`

* * *

[Hinge metrics for "maximum-margin" classification](https://keras.io/2/api/metrics/hinge_metrics/#hinge-metrics-for-maximummargin-classification)

[`Hinge` class](https://keras.io/2/api/metrics/hinge_metrics/#hinge-class)

[`SquaredHinge` class](https://keras.io/2/api/metrics/hinge_metrics/#squaredhinge-class)

[`CategoricalHinge` class](https://keras.io/2/api/metrics/hinge_metrics/#categoricalhinge-class)