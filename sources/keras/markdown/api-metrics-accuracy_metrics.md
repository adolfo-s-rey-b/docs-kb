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
 / Accuracy metrics

Accuracy metrics
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L15)

### `Accuracy` class

Copied!

`keras.metrics.Accuracy(name="accuracy", dtype=None)`

Calculates how often predictions equal labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

Copied!

`>>> m = keras.metrics.Accuracy() >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]]) >>> m.result() 0.75`

Copied!

`>>> m.reset_state() >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]], ...                sample_weight=[1, 1, 0, 0]) >>> m.result() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='binary_crossentropy',               metrics=[keras.metrics.Accuracy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L72)

### `BinaryAccuracy` class

Copied!

`keras.metrics.BinaryAccuracy(name="binary_accuracy", dtype=None, threshold=0.5)`

Calculates how often predictions match binary labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **threshold**: (Optional) Float representing the threshold for deciding whether prediction values are 1 or 0.

**Example**

Copied!

`>>> m = keras.metrics.BinaryAccuracy() >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]]) >>> m.result() 0.75`

Copied!

`>>> m.reset_state() >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]], ...                sample_weight=[1, 0, 0, 1]) >>> m.result() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='binary_crossentropy',               metrics=[keras.metrics.BinaryAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L160)

### `CategoricalAccuracy` class

Copied!

`keras.metrics.CategoricalAccuracy(name="categorical_accuracy", dtype=None)`

Calculates how often predictions match one-hot labels.

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

`y_pred` and `y_true` should be passed in as vectors of probabilities, rather than as labels. If necessary, use `ops.one_hot` to expand `y_true` as a vector.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = keras.metrics.CategoricalAccuracy() >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8], ...                 [0.05, 0.95, 0]]) >>> m.result() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8], ...                 [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='categorical_crossentropy',               metrics=[keras.metrics.CategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L249)

### `SparseCategoricalAccuracy` class

Copied!

`keras.metrics.SparseCategoricalAccuracy(     name="sparse_categorical_accuracy", dtype=None )`

Calculates how often predictions match integer labels.

Copied!

`acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))`

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `sparse categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = keras.metrics.SparseCategoricalAccuracy() >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]]) >>> m.result() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='sparse_categorical_crossentropy',               metrics=[keras.metrics.SparseCategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L333)

### `TopKCategoricalAccuracy` class

Copied!

`keras.metrics.TopKCategoricalAccuracy(     k=5, name="top_k_categorical_accuracy", dtype=None )`

Computes how often targets are in the top `K` predictions.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

Copied!

`>>> m = keras.metrics.TopKCategoricalAccuracy(k=1) >>> m.update_state([[0, 0, 1], [0, 1, 0]], ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]) >>> m.result() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 0, 1], [0, 1, 0]], ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='categorical_crossentropy',               metrics=[keras.metrics.TopKCategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L439)

### `SparseTopKCategoricalAccuracy` class

Copied!

`keras.metrics.SparseTopKCategoricalAccuracy(     k=5, name="sparse_top_k_categorical_accuracy", dtype=None, from_sorted_ids=False )`

Computes how often integer targets are in the top `K` predictions.

By default, the arguments expected by `update_state()` are: - `y_true`: a tensor of shape `(batch_size)` representing indices of true categories. - `y_pred`: a tensor of shape `(batch_size, num_categories)` containing the scores for each sample for all possible categories.

With `from_sorted_ids=True`, the arguments expected by `update_state` are: - `y_true`: a tensor of shape `(batch_size)` representing indices or IDs of true categories. - `y_pred`: a tensor of shape `(batch_size, N)` containing the indices or IDs of the top `N` categories sorted in order from highest score to lowest score. `N` must be greater or equal to `k`.

The `from_sorted_ids=True` option can be more efficient when the set of categories is very large and the model has an optimized way to retrieve the top ones either without scoring or without maintaining the scores for all the possible categories.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_sorted\_ids**: (Optional) When `False`, the default, the tensor passed in `y_pred` contains the unsorted scores of all possible categories. When `True`, `y_pred` contains a the indices or IDs for the top categories.

**Example**

Copied!

`>>> m = keras.metrics.SparseTopKCategoricalAccuracy(k=1) >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]) >>> m.result() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result() 0.3`

Copied!

`>>> m = keras.metrics.SparseTopKCategoricalAccuracy(k=1, ...                                                from_sorted_ids=True) >>> m.update_state([2, 1], [[1, 0, 3], [1, 2, 3]]) >>> m.result() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='sparse_categorical_crossentropy',               metrics=[keras.metrics.SparseTopKCategoricalAccuracy()])`

* * *

[Accuracy metrics](https://keras.io/api/metrics/accuracy_metrics/#accuracy-metrics)

[`Accuracy` class](https://keras.io/api/metrics/accuracy_metrics/#accuracy-class)

[`BinaryAccuracy` class](https://keras.io/api/metrics/accuracy_metrics/#binaryaccuracy-class)

[`CategoricalAccuracy` class](https://keras.io/api/metrics/accuracy_metrics/#categoricalaccuracy-class)

[`SparseCategoricalAccuracy` class](https://keras.io/api/metrics/accuracy_metrics/#sparsecategoricalaccuracy-class)

[`TopKCategoricalAccuracy` class](https://keras.io/api/metrics/accuracy_metrics/#topkcategoricalaccuracy-class)

[`SparseTopKCategoricalAccuracy` class](https://keras.io/api/metrics/accuracy_metrics/#sparsetopkcategoricalaccuracy-class)