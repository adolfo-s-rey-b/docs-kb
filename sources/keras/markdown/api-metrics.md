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
 / Metrics

Metrics
=======

A metric is a function that is used to judge the performance of your model.

Metric functions are similar to loss functions, except that the results from evaluating a metric are not used when training the model. Note that you may use any loss function as a metric.

Available metrics
-----------------

### [Base Metric class](https://keras.io/api/metrics/base_metric/)

*   [Metric class](https://keras.io/api/metrics/base_metric/#metric-class)
    

### [Accuracy metrics](https://keras.io/api/metrics/accuracy_metrics/)

*   [Accuracy class](https://keras.io/api/metrics/accuracy_metrics/#accuracy-class)
    
*   [BinaryAccuracy class](https://keras.io/api/metrics/accuracy_metrics/#binaryaccuracy-class)
    
*   [CategoricalAccuracy class](https://keras.io/api/metrics/accuracy_metrics/#categoricalaccuracy-class)
    
*   [SparseCategoricalAccuracy class](https://keras.io/api/metrics/accuracy_metrics/#sparsecategoricalaccuracy-class)
    
*   [TopKCategoricalAccuracy class](https://keras.io/api/metrics/accuracy_metrics/#topkcategoricalaccuracy-class)
    
*   [SparseTopKCategoricalAccuracy class](https://keras.io/api/metrics/accuracy_metrics/#sparsetopkcategoricalaccuracy-class)
    

### [Probabilistic metrics](https://keras.io/api/metrics/probabilistic_metrics/)

*   [BinaryCrossentropy class](https://keras.io/api/metrics/probabilistic_metrics/#binarycrossentropy-class)
    
*   [CategoricalCrossentropy class](https://keras.io/api/metrics/probabilistic_metrics/#categoricalcrossentropy-class)
    
*   [SparseCategoricalCrossentropy class](https://keras.io/api/metrics/probabilistic_metrics/#sparsecategoricalcrossentropy-class)
    
*   [KLDivergence class](https://keras.io/api/metrics/probabilistic_metrics/#kldivergence-class)
    
*   [Poisson class](https://keras.io/api/metrics/probabilistic_metrics/#poisson-class)
    

### [Regression metrics](https://keras.io/api/metrics/regression_metrics/)

*   [MeanSquaredError class](https://keras.io/api/metrics/regression_metrics/#meansquarederror-class)
    
*   [RootMeanSquaredError class](https://keras.io/api/metrics/regression_metrics/#rootmeansquarederror-class)
    
*   [MeanAbsoluteError class](https://keras.io/api/metrics/regression_metrics/#meanabsoluteerror-class)
    
*   [MeanAbsolutePercentageError class](https://keras.io/api/metrics/regression_metrics/#meanabsolutepercentageerror-class)
    
*   [MeanSquaredLogarithmicError class](https://keras.io/api/metrics/regression_metrics/#meansquaredlogarithmicerror-class)
    
*   [CosineSimilarity class](https://keras.io/api/metrics/regression_metrics/#cosinesimilarity-class)
    
*   [LogCoshError class](https://keras.io/api/metrics/regression_metrics/#logcosherror-class)
    
*   [R2Score class](https://keras.io/api/metrics/regression_metrics/#r2score-class)
    

### [Classification metrics based on True/False positives & negatives](https://keras.io/api/metrics/classification_metrics/)

*   [AUC class](https://keras.io/api/metrics/classification_metrics/#auc-class)
    
*   [Precision class](https://keras.io/api/metrics/classification_metrics/#precision-class)
    
*   [Recall class](https://keras.io/api/metrics/classification_metrics/#recall-class)
    
*   [TruePositives class](https://keras.io/api/metrics/classification_metrics/#truepositives-class)
    
*   [TrueNegatives class](https://keras.io/api/metrics/classification_metrics/#truenegatives-class)
    
*   [FalsePositives class](https://keras.io/api/metrics/classification_metrics/#falsepositives-class)
    
*   [FalseNegatives class](https://keras.io/api/metrics/classification_metrics/#falsenegatives-class)
    
*   [PrecisionAtRecall class](https://keras.io/api/metrics/classification_metrics/#precisionatrecall-class)
    
*   [RecallAtPrecision class](https://keras.io/api/metrics/classification_metrics/#recallatprecision-class)
    
*   [SensitivityAtSpecificity class](https://keras.io/api/metrics/classification_metrics/#sensitivityatspecificity-class)
    
*   [SpecificityAtSensitivity class](https://keras.io/api/metrics/classification_metrics/#specificityatsensitivity-class)
    
*   [F1Score class](https://keras.io/api/metrics/classification_metrics/#f1score-class)
    
*   [FBetaScore class](https://keras.io/api/metrics/classification_metrics/#fbetascore-class)
    
*   [PearsonCorrelation class](https://keras.io/api/metrics/classification_metrics/#pearsoncorrelation-class)
    
*   [ConcordanceCorrelation class](https://keras.io/api/metrics/classification_metrics/#concordancecorrelation-class)
    

### [Image segmentation metrics](https://keras.io/api/metrics/segmentation_metrics/)

*   [IoU class](https://keras.io/api/metrics/segmentation_metrics/#iou-class)
    
*   [BinaryIoU class](https://keras.io/api/metrics/segmentation_metrics/#binaryiou-class)
    
*   [OneHotIoU class](https://keras.io/api/metrics/segmentation_metrics/#onehotiou-class)
    
*   [OneHotMeanIoU class](https://keras.io/api/metrics/segmentation_metrics/#onehotmeaniou-class)
    
*   [MeanIoU class](https://keras.io/api/metrics/segmentation_metrics/#meaniou-class)
    

### [Hinge metrics for "maximum-margin" classification](https://keras.io/api/metrics/hinge_metrics/)

*   [Hinge class](https://keras.io/api/metrics/hinge_metrics/#hinge-class)
    
*   [SquaredHinge class](https://keras.io/api/metrics/hinge_metrics/#squaredhinge-class)
    
*   [CategoricalHinge class](https://keras.io/api/metrics/hinge_metrics/#categoricalhinge-class)
    

### [Metric wrappers and reduction metrics](https://keras.io/api/metrics/metrics_wrappers/)

*   [MeanMetricWrapper class](https://keras.io/api/metrics/metrics_wrappers/#meanmetricwrapper-class)
    
*   [Mean class](https://keras.io/api/metrics/metrics_wrappers/#mean-class)
    
*   [Sum class](https://keras.io/api/metrics/metrics_wrappers/#sum-class)
    

* * *

Usage with `compile()` & `fit()`
--------------------------------

The `compile()` method takes a `metrics` argument, which is a list of metrics:

Copied!

`model.compile(     optimizer='adam',     loss='mean_squared_error',     metrics=[         metrics.MeanSquaredError(),         metrics.AUC(),     ] )`

Metric values are displayed during `fit()` and logged to the `History` object returned by `fit()`. They are also returned by `model.evaluate()`.

Note that the best way to monitor your metrics during training is via [TensorBoard](https://keras.io/api/callbacks/tensorboard)
.

To track metrics under a specific name, you can pass the `name` argument to the metric constructor:

Copied!

`model.compile(     optimizer='adam',     loss='mean_squared_error',     metrics=[         metrics.MeanSquaredError(name='my_mse'),         metrics.AUC(name='my_auc'),     ] )`

All built-in metrics may also be passed via their string identifier (in this case, default constructor argument values are used, including a default metric name):

Copied!

`model.compile(     optimizer='adam',     loss='mean_squared_error',     metrics=[         'MeanSquaredError',         'AUC',     ] )`

* * *

Standalone usage
----------------

Unlike losses, metrics are stateful. You update their state using the `update_state()` method, and you query the scalar metric result using the `result()` method:

Copied!

`m = keras.metrics.AUC() m.update_state([0, 1, 1, 1], [0, 1, 0, 0]) print('Intermediate result:', float(m.result()))  m.update_state([1, 1, 1, 1], [0, 1, 1, 0]) print('Final result:', float(m.result()))`

The internal state can be cleared via `metric.reset_states()`.

Here's how you would use a metric as part of a simple custom training loop:

Copied!

``accuracy = keras.metrics.CategoricalAccuracy() loss_fn = keras.losses.CategoricalCrossentropy(from_logits=True) optimizer = keras.optimizers.Adam()  # Iterate over the batches of a dataset. for step, (x, y) in enumerate(dataset):     with tf.GradientTape() as tape:         logits = model(x)         # Compute the loss value for this batch.         loss_value = loss_fn(y, logits)      # Update the state of the `accuracy` metric.     accuracy.update_state(y, logits)      # Update the weights of the model to minimize the loss value.     gradients = tape.gradient(loss_value, model.trainable_weights)     optimizer.apply_gradients(zip(gradients, model.trainable_weights))      # Logging the current accuracy value so far.     if step % 100 == 0:         print('Step:', step)                 print('Total running accuracy so far: %.3f' % accuracy.result())``

* * *

Creating custom metrics
-----------------------

### As simple callables (stateless)

Much like loss functions, any callable with signature `metric_fn(y_true, y_pred)` that returns an array of losses (one of sample in the input batch) can be passed to `compile()` as a metric. Note that sample weighting is automatically supported for any such metric.

Here's a simple example:

Copied!

``from keras import ops  def my_metric_fn(y_true, y_pred):     squared_difference = ops.square(y_true - y_pred)     return ops.mean(squared_difference, axis=-1)  # Note the `axis=-1`  model.compile(optimizer='adam', loss='mean_squared_error', metrics=[my_metric_fn])``

In this case, the scalar metric value you are tracking during training and evaluation is the average of the per-batch metric values for all batches see during a given epoch (or during a given call to `model.evaluate()`).

### As subclasses of `Metric` (stateful)

Not all metrics can be expressed via stateless callables, because metrics are evaluated for each batch during training and evaluation, but in some cases the average of the per-batch values is not what you are interested in.

Let's say that you want to compute AUC over a given evaluation dataset: the average of the per-batch AUC values isn't the same as the AUC over the entire dataset.

For such metrics, you're going to want to subclass the `Metric` class, which can maintain a state across batches. It's easy:

*   Create the state variables in `__init__`
*   Update the variables given `y_true` and `y_pred` in `update_state()`
*   Return the scalar metric result in `result()`
*   Clear the state in `reset_states()`

Here's a simple example computing binary true positives:

Copied!

`class BinaryTruePositives(keras.metrics.Metric):    def __init__(self, name='binary_true_positives', **kwargs):     super().__init__(name=name, **kwargs)     self.true_positives = self.add_weight(name='tp', initializer='zeros')    def update_state(self, y_true, y_pred, sample_weight=None):     y_true = ops.cast(y_true, "bool")     y_pred = ops.cast(y_pred, "bool")      values = ops.logical_and(ops.equal(y_true, True), ops.equal(y_pred, True))     values = ops.cast(values, self.dtype)     if sample_weight is not None:       sample_weight = ops.cast(sample_weight, self.dtype)       values = values * sample_weight     self.true_positives.assign_add(ops.sum(values))    def result(self):     return self.true_positives    def reset_state(self):     self.true_positives.assign(0)  m = BinaryTruePositives() m.update_state([0, 1, 1, 1], [0, 1, 0, 0]) print(f'Intermediate result: {m.result().numpy()}')  m.update_state([1, 1, 1, 1], [0, 1, 1, 0]) print(f'Intermediate result: {m.result().numpy()}')`

[Metrics](https://keras.io/api/metrics/#metrics)

[Available metrics](https://keras.io/api/metrics/#available-metrics)

[Base Metric class](https://keras.io/api/metrics/#base-metric-class)

[Accuracy metrics](https://keras.io/api/metrics/#accuracy-metrics)

[Probabilistic metrics](https://keras.io/api/metrics/#probabilistic-metrics)

[Regression metrics](https://keras.io/api/metrics/#regression-metrics)

[Classification metrics based on True/False positives & negatives](https://keras.io/api/metrics/#classification-metrics-based-on-truefalse-positives-amp-negatives)

[Image segmentation metrics](https://keras.io/api/metrics/#image-segmentation-metrics)

[Hinge metrics for "maximum-margin" classification](https://keras.io/api/metrics/#hinge-metrics-for-maximummargin-classification)

[Metric wrappers and reduction metrics](https://keras.io/api/metrics/#metric-wrappers-and-reduction-metrics)

[Usage with `compile()` & `fit()`](https://keras.io/api/metrics/#usage-with-compile-amp-fit)

[Standalone usage](https://keras.io/api/metrics/#standalone-usage)

[Creating custom metrics](https://keras.io/api/metrics/#creating-custom-metrics)

[As simple callables (stateless)](https://keras.io/api/metrics/#as-simple-callables-stateless)

[As subclasses of `Metric` (stateful)](https://keras.io/api/metrics/#as-subclasses-of-metric-stateful)