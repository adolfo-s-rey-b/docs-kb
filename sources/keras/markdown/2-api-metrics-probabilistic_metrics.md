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
 / Probabilistic metrics

Probabilistic metrics
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/probabilistic_metrics.py#L111)

### `BinaryCrossentropy` class

Copied!

`tf_keras.metrics.BinaryCrossentropy(     name="binary_crossentropy", dtype=None, from_logits=False, label_smoothing=0 )`

Computes the crossentropy metric between the labels and predictions.

This is the crossentropy metric class to be used when there are only two label classes (0 and 1).

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **label\_smoothing**: (Optional) Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of `0.1` for label `0` and `0.9` for label `1`".

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.BinaryCrossentropy() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 0.81492424`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.9162905`

Usage with `compile()` API:

Copied!

`model.compile(     optimizer='sgd',     loss='binary_crossentropy',     metrics=[tf.keras.metrics.BinaryCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/probabilistic_metrics.py#L168)

### `CategoricalCrossentropy` class

Copied!

`tf_keras.metrics.CategoricalCrossentropy(     name="categorical_crossentropy",     dtype=None,     from_logits=False,     label_smoothing=0,     axis=-1, )`

Computes the crossentropy metric between the labels and predictions.

This is the crossentropy metric class to be used when there are multiple label classes (2 or more). Here we assume that labels are given as a `one_hot` representation. eg., When labels values are \[2, 0, 1\], `y_true` = \[\[0, 0, 1\], \[1, 0, 0\], \[0, 1, 0\]\].

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **label\_smoothing**: (Optional) Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of `0.1` for label `0` and `0.9` for label `1`"
*   **axis**: (Optional) -1 is the dimension along which entropy is computed. Defaults to `-1`.

Standalone usage:

Copied!

``>>> # EPSILON = 1e-7, y = y_true, y` = y_pred >>> # y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON) >>> # y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]] >>> # xent = -sum(y * log(y'), axis = -1) >>> #      = -((log 0.95), (log 0.1)) >>> #      = [0.051, 2.302] >>> # Reduced xent = (0.051 + 2.302) / 2 >>> m = tf.keras.metrics.CategoricalCrossentropy() >>> m.update_state([[0, 1, 0], [0, 0, 1]], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> m.result().numpy() 1.1769392``

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1, 0], [0, 0, 1]], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]], ...                sample_weight=tf.constant([0.3, 0.7])) >>> m.result().numpy() 1.6271976`

Usage with `compile()` API:

Copied!

`model.compile(   optimizer='sgd',   loss='categorical_crossentropy',   metrics=[tf.keras.metrics.CategoricalCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/probabilistic_metrics.py#L240)

### `SparseCategoricalCrossentropy` class

Copied!

`tf_keras.metrics.SparseCategoricalCrossentropy(     name: str = "sparse_categorical_crossentropy",     dtype: Union[str, tensorflow.python.framework.dtypes.DType, NoneType] = None,     from_logits: bool = False,     ignore_class: Optional[int] = None,     axis: int = -1, )`

Computes the crossentropy metric between the labels and predictions.

Use this crossentropy metric when there are two or more label classes. We expect labels to be provided as integers. If you want to provide labels using `one-hot` representation, please use `CategoricalCrossentropy` metric. There should be `# classes` floating point values per feature for `y_pred` and a single floating point value per feature for `y_true`.

In the snippet below, there is a single floating point value per example for `y_true` and `# classes` floating pointing values per example for `y_pred`. The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is `[batch_size, num_classes]`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from\_logits**: (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution.
*   **ignore\_class**: Optional integer. The ID of a class to be ignored during metric computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered.
*   **axis**: (Optional) The dimension along which entropy is computed. Defaults to `-1`.

Standalone usage:

Copied!

`>>> # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]] >>> # logits = log(y_pred) >>> # softmax = exp(logits) / sum(exp(logits), axis=-1) >>> # softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]] >>> # xent = -sum(y * log(softmax), 1) >>> # log(softmax) = [[-2.9957, -0.0513, -16.1181], >>> #                [-2.3026, -0.2231, -2.3026]] >>> # y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]] >>> # xent = [0.0513, 2.3026] >>> # Reduced xent = (0.0513 + 2.3026) / 2 >>> m = tf.keras.metrics.SparseCategoricalCrossentropy() >>> m.update_state([1, 2], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> m.result().numpy() 1.1769392`

Copied!

`>>> m.reset_state() >>> m.update_state([1, 2], ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]], ...                sample_weight=tf.constant([0.3, 0.7])) >>> m.result().numpy() 1.6271976`

Usage with `compile()` API:

Copied!

`model.compile(   optimizer='sgd',   loss='sparse_categorical_crossentropy',   metrics=[tf.keras.metrics.SparseCategoricalCrossentropy()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/probabilistic_metrics.py#L73)

### `KLDivergence` class

Copied!

`tf_keras.metrics.KLDivergence(name="kullback_leibler_divergence", dtype=None)`

Computes Kullback-Leibler divergence metric between `y_true` and `y_pred`.

`metric = y_true * log(y_true / y_pred)`

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.KLDivergence() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]]) >>> m.result().numpy() 0.45814306`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.9162892`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='categorical_crossentropy',               metrics=[tf.keras.metrics.KLDivergence()])`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/probabilistic_metrics.py#L34)

### `Poisson` class

Copied!

`tf_keras.metrics.Poisson(name="poisson", dtype=None)`

Computes the Poisson score between `y_true` and `y_pred`.

🐟 🐟 🐟

It is defined as: `poisson_score = y_pred - y_true * log(y_pred)`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

Standalone usage:

Copied!

`>>> m = tf.keras.metrics.Poisson() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]]) >>> m.result().numpy() 0.49999997`

Copied!

`>>> m.reset_state() >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]], ...                sample_weight=[1, 0]) >>> m.result().numpy() 0.99999994`

Usage with `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss='categorical_crossentropy',               metrics=[tf.keras.metrics.Poisson()])`

* * *

[Probabilistic metrics](https://keras.io/2/api/metrics/probabilistic_metrics/#probabilistic-metrics)

[`BinaryCrossentropy` class](https://keras.io/2/api/metrics/probabilistic_metrics/#binarycrossentropy-class)

[`CategoricalCrossentropy` class](https://keras.io/2/api/metrics/probabilistic_metrics/#categoricalcrossentropy-class)

[`SparseCategoricalCrossentropy` class](https://keras.io/2/api/metrics/probabilistic_metrics/#sparsecategoricalcrossentropy-class)

[`KLDivergence` class](https://keras.io/2/api/metrics/probabilistic_metrics/#kldivergence-class)

[`Poisson` class](https://keras.io/2/api/metrics/probabilistic_metrics/#poisson-class)