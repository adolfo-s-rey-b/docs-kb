None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Base Metric class](https://keras.io/api/metrics/base_metric/)
 [Accuracy metrics](https://keras.io/api/metrics/accuracy_metrics/)
 [Probabilistic metrics](https://keras.io/api/metrics/probabilistic_metrics/)
 [Regression metrics](https://keras.io/api/metrics/regression_metrics/)
 [Classification metrics based on True/False positives & negatives](https://keras.io/api/metrics/classification_metrics/)
 [Image segmentation metrics](https://keras.io/api/metrics/segmentation_metrics/)
 [Hinge metrics for "maximum-margin" classification](https://keras.io/api/metrics/hinge_metrics/)
 [Metric wrappers and reduction metrics](https://keras.io/api/metrics/metrics_wrappers/)
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
 / [Metrics](https://keras.io/api/metrics/)
 / Hinge metrics for "maximum-margin" classification

Hinge metrics for "maximum-margin" classification
=================================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/hinge_metrics.py#L8)

### `Hinge` class

Copied!

`keras.metrics.Hinge(name="hinge", dtype=None)`

Computes the hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

Copied!

`>>> m = keras.metrics.Hinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result() 1.3 >>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result() 1.1`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/hinge_metrics.py#L41)

### `SquaredHinge` class

Copied!

`keras.metrics.SquaredHinge(name="squared_hinge", dtype=None)`

Computes the hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = keras.metrics.SquaredHinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result() 1.86 >>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result() 1.46`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/hinge_metrics.py#L74)

### `CategoricalHinge` class

Copied!

`keras.metrics.CategoricalHinge(name="categorical_hinge", dtype=None)`

Computes the categorical hinge metric between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = keras.metrics.CategoricalHinge() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 1.4000001 >>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result() 1.2`

* * *

[Hinge metrics for "maximum-margin" classification](https://keras.io/api/metrics/hinge_metrics/#hinge-metrics-for-maximummargin-classification)

[`Hinge` class](https://keras.io/api/metrics/hinge_metrics/#hinge-class)

[`SquaredHinge` class](https://keras.io/api/metrics/hinge_metrics/#squaredhinge-class)

[`CategoricalHinge` class](https://keras.io/api/metrics/hinge_metrics/#categoricalhinge-class)