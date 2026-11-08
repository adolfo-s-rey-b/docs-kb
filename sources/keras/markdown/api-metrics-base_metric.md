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
 / Base Metric class

Base Metric class
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L11)

### `Metric` class

Copied!

`keras.metrics.Metric(dtype=None, name=None)`

Encapsulates metric logic and state.

**Arguments**

*   **name**: Optional name for the metric instance.
*   **dtype**: The dtype of the metric's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Example**

Copied!

`m = SomeMetric(...) for input in ...:     m.update_state(input) print('Final result: ', m.result())`

Usage with `compile()` API:

Copied!

`model = keras.Sequential() model.add(keras.layers.Dense(64, activation='relu')) model.add(keras.layers.Dense(64, activation='relu')) model.add(keras.layers.Dense(10, activation='softmax'))  model.compile(optimizer=keras.optimizers.RMSprop(0.01),               loss=keras.losses.CategoricalCrossentropy(),               metrics=[keras.metrics.CategoricalAccuracy()])  data = np.random.random((1000, 32)) labels = np.random.random((1000, 10))  model.fit(data, labels, epochs=10)`

To be implemented by subclasses:

*   `__init__()`: All state variables should be created in this method by calling `self.add_variable()` like: `self.var = self.add_variable(...)`
*   `update_state()`: Has all updates to the state variables like: `self.var.assign(...)`.
*   `result()`: Computes and returns a scalar value or a dict of scalar values for the metric from the state variables.

Example subclass implementation:

Copied!

`class BinaryTruePositives(Metric):      def __init__(self, name='binary_true_positives', **kwargs):         super().__init__(name=name, **kwargs)         self.true_positives = self.add_variable(             shape=(),             initializer='zeros',             name='true_positives'         )      def update_state(self, y_true, y_pred, sample_weight=None):         y_true = ops.cast(y_true, "bool")         y_pred = ops.cast(y_pred, "bool")          values = ops.logical_and(             ops.equal(y_true, True), ops.equal(y_pred, True))         values = ops.cast(values, self.dtype)         if sample_weight is not None:             sample_weight = ops.cast(sample_weight, self.dtype)             sample_weight = ops.broadcast_to(                 sample_weight, ops.shape(values)             )             values = ops.multiply(values, sample_weight)         self.true_positives.assign(self.true_positives + ops.sum(values))      def result(self):         return self.true_positives`

**Guides and examples using `Metric`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
    
*   [Denoising Diffusion Implicit Models](https://keras.io/examples/generative/ddim/)
    
*   [Data-efficient GANs with Adaptive Discriminator Augmentation](https://keras.io/examples/generative/gan_ada/)
    

* * *

[Base Metric class](https://keras.io/api/metrics/base_metric/#base-metric-class)

[`Metric` class](https://keras.io/api/metrics/base_metric/#metric-class)