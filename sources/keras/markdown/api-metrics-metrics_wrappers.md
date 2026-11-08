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
 / Metric wrappers and reduction metrics

Metric wrappers and reduction metrics
=====================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L161)

### `MeanMetricWrapper` class

Copied!

`keras.metrics.MeanMetricWrapper(fn, name=None, dtype=None, **kwargs)`

Wrap a stateless metric function with the `Mean` metric.

You could use this class to quickly build a mean metric from a function. The function needs to have the signature `fn(y_true, y_pred)` and return a per-sample loss array. `MeanMetricWrapper.result()` will return the average metric value across all samples seen so far.

For example:

Copied!

`def mse(y_true, y_pred):     return (y_true - y_pred) ** 2  mse_metric = MeanMetricWrapper(fn=mse)`

**Arguments**

*   **fn**: The metric function to wrap, with signature `fn(y_true, y_pred, **kwargs)`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **\*\*kwargs**: Keyword arguments to pass on to `fn`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L96)

### `Mean` class

Copied!

`keras.metrics.Mean(name="mean", dtype=None)`

Compute the (weighted) mean of the given values.

For example, if values is `[1, 3, 5, 7]` then the mean is 4. If `sample_weight` was specified as `[1, 1, 0, 0]` then the mean would be 2.

This metric creates two variables, `total` and `count`. The mean value returned is simply `total` divided by `count`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = Mean() >>> m.update_state([1, 3, 5, 7]) >>> m.result() 4.0`

Copied!

`>>> m.reset_state() >>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0]) >>> m.result() 2.0`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L47)

### `Sum` class

Copied!

`keras.metrics.Sum(name="sum", dtype=None)`

Compute the (weighted) sum of the given values.

For example, if `values` is `[1, 3, 5, 7]` then their sum is 16. If `sample_weight` was specified as `[1, 1, 0, 0]` then the sum would be 4.

This metric creates one variable, `total`. This is ultimately returned as the sum value.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = metrics.Sum() >>> m.update_state([1, 3, 5, 7]) >>> m.result() 16.0`

Copied!

`>>> m = metrics.Sum() >>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0]) >>> m.result() 4.0`

* * *

[Metric wrappers and reduction metrics](https://keras.io/api/metrics/metrics_wrappers/#metric-wrappers-and-reduction-metrics)

[`MeanMetricWrapper` class](https://keras.io/api/metrics/metrics_wrappers/#meanmetricwrapper-class)

[`Mean` class](https://keras.io/api/metrics/metrics_wrappers/#mean-class)

[`Sum` class](https://keras.io/api/metrics/metrics_wrappers/#sum-class)