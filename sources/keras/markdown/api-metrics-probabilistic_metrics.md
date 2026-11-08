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
 / Probabilistic metrics

Probabilistic metrics
=====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L101)

### `BinaryCrossentropy` class

Copied!

`keras.metrics.BinaryCrossentropy(     name="binary_crossentropy", dtype=None, from_logits=False, label_smoothing=0 )`

Computes the crossentropy metric between the labels and predictions.

This is the crossentropy metric class to be used when there are only two label classes (0 and 1).

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **label\_smoothing**: (Optional) Float in `[0, 1]`. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of 0.1 for label "0" and 0.9 for label "1".

**Examples**

Copied!

`>>> m = keras.metrics.BinaryCrossentropy() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result() 0.81492424`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result() 0.9162905`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[keras.metrics.BinaryCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L171)

### `CategoricalCrossentropy` class

Copied!

`keras.metrics.CategoricalCrossentropy(     name="categorical_crossentropy",     dtype=None,     from_logits=False,     label_smoothing=0,     axis=-1, )`

Computes the crossentropy metric between the labels and predictions.

This is the crossentropy metric class to be used when there are multiple label classes (2 or more). It assumes that labels are one-hot encoded, e.g., when labels values are `[2, 0, 1]`, then `y_true` is `[[0, 0, 1], [1, 0, 0], [0, 1, 0]]`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **label\_smoothing**: (Optional) Float in `[0, 1]`. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of 0.1 for label "0" and 0.9 for label "1".
*   **axis**: (Optional) Defaults to `-1`. The dimension along which entropy is computed.

**Examples**

Copied!

``>>> # EPSILON = 1e-7, y = y_true, y` = y_pred >>> # y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON) >>> # y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]] >>> # xent = -sum(y * log(y'), axis = -1) >>> #      = -((log 0.95), (log 0.1)) >>> #      = [0.051, 2.302] >>> # Reduced xent = (0.051 + 2.302) / 2 >>> m = keras.metrics.CategoricalCrossentropy() >>> m.update_state([[0, 1, 0], [0, 0, 1]], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> m.result() 1.1769392``

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1, 0], [0, 0, 1]], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]], ...                sample_weight=np.array([0.3, 0.7])) >>> m.result() 1.6271976`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[keras.metrics.CategoricalCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L258)

### `SparseCategoricalCrossentropy` class

Copied!

`keras.metrics.SparseCategoricalCrossentropy(     name="sparse_categorical_crossentropy",     dtype=None,     from_logits=False,     ignore_class=None,     axis=-1, )`

Computes the crossentropy metric between the labels and predictions.

Use this crossentropy metric when there are two or more label classes. It expects labels to be provided as integers. If you want to provide labels that are one-hot encoded, please use the `CategoricalCrossentropy` metric instead.

There should be `num_classes` floating point values per feature for `y_pred` and a single floating point value per feature for `y_true`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **ignore\_class**: (Optional) Integer. Class to ignore. If `None`, no class is ignored.
*   **axis**: (Optional) Defaults to `-1`. The dimension along which entropy is computed.

**Examples**

Copied!

`>>> # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]] >>> # logits = log(y_pred) >>> # softmax = exp(logits) / sum(exp(logits), axis=-1) >>> # softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]] >>> # xent = -sum(y * log(softmax), 1) >>> # log(softmax) = [[-2.9957, -0.0513, -16.1181], >>> #                [-2.3026, -0.2231, -2.3026]] >>> # y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]] >>> # xent = [0.0513, 2.3026] >>> # Reduced xent = (0.0513 + 2.3026) / 2 >>> m = keras.metrics.SparseCategoricalCrossentropy() >>> m.update_state([1, 2], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> m.result() 1.1769392`

Copied!

`>>> m.reset_state() >>> m.update_state([1, 2], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]], ...                sample_weight=np.array([0.3, 0.7])) >>> m.result() 1.6271976`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[keras.metrics.SparseCategoricalCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L10)

### `KLDivergence` class

Copied!

`keras.metrics.KLDivergence(name="kl_divergence", dtype=None)`

Computes Kullback-Leibler divergence metric between `y_true` and `y_pred`.

Formula:

Copied!

`metric = y_true * log(y_true / y_pred)`

`y_true` and `y_pred` are expected to be probability distributions, with values between 0 and 1. They will get clipped to the `[0, 1]` range.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

Copied!

`>>> m = keras.metrics.KLDivergence() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result() 0.45814306`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result() 0.9162892`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[keras.metrics.KLDivergence()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L58)

### `Poisson` class

Copied!

`keras.metrics.Poisson(name="poisson", dtype=None)`

Computes the Poisson metric between `y_true` and `y_pred`.

Formula:

Copied!

`metric = y_pred - y_true * log(y_pred)`

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

Copied!

`>>> m = keras.metrics.Poisson() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result() 0.49999997`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result() 0.99999994`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[keras.metrics.Poisson()])`

* * *

[Probabilistic metrics](https://keras.io/api/metrics/probabilistic_metrics/#probabilistic-metrics)

[`BinaryCrossentropy` class](https://keras.io/api/metrics/probabilistic_metrics/#binarycrossentropy-class)

[`CategoricalCrossentropy` class](https://keras.io/api/metrics/probabilistic_metrics/#categoricalcrossentropy-class)

[`SparseCategoricalCrossentropy` class](https://keras.io/api/metrics/probabilistic_metrics/#sparsecategoricalcrossentropy-class)

[`KLDivergence` class](https://keras.io/api/metrics/probabilistic_metrics/#kldivergence-class)

[`Poisson` class](https://keras.io/api/metrics/probabilistic_metrics/#poisson-class)