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
 / Accuracy metrics

Accuracy metrics
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L28)

### `Accuracy` class

Copied!

`tf_keras.metrics.Accuracy(name="accuracy", dtype=None)`

Calculates how often predictions equal labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.Accuracy() >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]]) >>> m.result().numpy() 0.75`

Copied!

`>>> m.reset_state() >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]], ...                sample_weight=[1, 1, 0, 0]) >>> m.result().numpy() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[tf.keras.metrics.Accuracy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L71)

### `BinaryAccuracy` class

Copied!

`tf_keras.metrics.BinaryAccuracy(name="binary_accuracy", dtype=None, threshold=0.5)`

Calculates how often predictions match binary labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **threshold**: (Optional) Float representing the threshold for deciding whether prediction values are 1 or 0.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.BinaryAccuracy() >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]]) >>> m.result().numpy() 0.75`

Copied!

`>>> m.reset_state() >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]], ...                sample_weight=[1, 0, 0, 1]) >>> m.result().numpy() 0.5`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[tf.keras.metrics.BinaryAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L118)

### `CategoricalAccuracy` class

Copied!

`tf_keras.metrics.CategoricalAccuracy(name="categorical_accuracy", dtype=None)`

Calculates how often predictions match one-hot labels.

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

`y_pred` and `y_true` should be passed in as vectors of probabilities, rather than as labels. If necessary, use [`tf.one_hot`](https://www.tensorflow.org/api_docs/python/tf/one_hot)
 to expand `y_true` as a vector.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.CategoricalAccuracy() >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8], ...                 [0.05, 0.95, 0]]) >>> m.result().numpy() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8], ...                 [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result().numpy() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(   optimizer='sgd',   loss='mse',   metrics=[tf.keras.metrics.CategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L177)

### `SparseCategoricalAccuracy` class

Copied!

`tf_keras.metrics.SparseCategoricalAccuracy(     name="sparse_categorical_accuracy", dtype=None )`

Calculates how often predictions match integer labels.

Copied!

`acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))`

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `sparse categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.SparseCategoricalAccuracy() >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]]) >>> m.result().numpy() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result().numpy() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='mse',     metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L258)

### `TopKCategoricalAccuracy` class

Copied!

`tf_keras.metrics.TopKCategoricalAccuracy(     k=5, name="top_k_categorical_accuracy", dtype=None )`

Computes how often targets are in the top `K` predictions.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.TopKCategoricalAccuracy(k=1) >>> m.update_state([[0, 0, 1], [0, 1, 0]], ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]) >>> m.result().numpy() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 0, 1], [0, 1, 0]], ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result().numpy() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='mse',               metrics=[tf.keras.metrics.TopKCategoricalAccuracy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/accuracy_metrics.py#L304)

### `SparseTopKCategoricalAccuracy` class

Copied!

`tf_keras.metrics.SparseTopKCategoricalAccuracy(     k=5, name="sparse_top_k_categorical_accuracy", dtype=None )`

Computes how often integer targets are in the top `K` predictions.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.SparseTopKCategoricalAccuracy(k=1) >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]) >>> m.result().numpy() 0.5`

Copied!

`>>> m.reset_state() >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]], ...                sample_weight=[0.7, 0.3]) >>> m.result().numpy() 0.3`

Usage with `compile()` API:

Copied!

`model.compile(   optimizer='sgd',   loss='mse',   metrics=[tf.keras.metrics.SparseTopKCategoricalAccuracy()])`

* * *

[Accuracy metrics](https://keras.io/2/api/metrics/accuracy_metrics/#accuracy-metrics)

[`Accuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#accuracy-class)

[`BinaryAccuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#binaryaccuracy-class)

[`CategoricalAccuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#categoricalaccuracy-class)

[`SparseCategoricalAccuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#sparsecategoricalaccuracy-class)

[`TopKCategoricalAccuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#topkcategoricalaccuracy-class)

[`SparseTopKCategoricalAccuracy` class](https://keras.io/2/api/metrics/accuracy_metrics/#sparsetopkcategoricalaccuracy-class)