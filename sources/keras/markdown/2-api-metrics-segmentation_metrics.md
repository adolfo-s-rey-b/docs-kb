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
 / Image segmentation metrics

Image segmentation metrics
==========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/metrics/iou_metrics.py#L429)

### `MeanIoU` class

Copied!

`tf_keras.metrics.MeanIoU(     num_classes: int,     name: Optional[str] = None,     dtype: Union[str, tensorflow.python.framework.dtypes.DType, NoneType] = None,     ignore_class: Optional[int] = None,     sparse_y_true: bool = True,     sparse_y_pred: bool = True,     axis: int = -1, )`

Computes the mean Intersection-Over-Union metric.

General definition and computation:

Intersection-Over-Union is a common evaluation metric for semantic image segmentation.

For an individual class, the IoU metric is defined as follows:

Copied!

`iou = true_positives / (true_positives + false_positives + false_negatives)`

To compute IoUs, the predictions are accumulated in a confusion matrix, weighted by `sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

Note that this class first computes IoUs for all individual classes, then returns the mean of these values.

**Arguments**

*   **num\_classes**: The possible number of labels the prediction task can have. This value must be provided, since a confusion matrix of dimension = \[num\_classes, num\_classes\] will be allocated.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **ignore\_class**: Optional integer. The ID of a class to be ignored during metric computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered.
*   **sparse\_y\_true**: Whether labels are encoded using integers or dense floating point vectors. If `False`, the [`tf.argmax`](https://www.tensorflow.org/api_docs/python/tf/argmax)
     function will be used to determine each sample's most likely associated label.
*   **sparse\_y\_pred**: Whether predictions are encoded using integers or dense floating point vectors. If `False`, the [`tf.argmax`](https://www.tensorflow.org/api_docs/python/tf/argmax)
     function will be used to determine each sample's most likely associated label.
*   **axis**: (Optional) The dimension containing the logits. Defaults to `-1`.

Standalone usage:

Copied!

`>>> # cm = [[1, 1], >>> #        [1, 1]] >>> # sum_row = [2, 2], sum_col = [2, 2], true_positives = [1, 1] >>> # iou = true_positives / (sum_row + sum_col - true_positives)) >>> # result = (1 / (2 + 2 - 1) + 1 / (2 + 2 - 1)) / 2 = 0.33 >>> m = tf.keras.metrics.MeanIoU(num_classes=2) >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1]) >>> m.result().numpy() 0.33333334`

Copied!

`>>> m.reset_state() >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1], ...                sample_weight=[0.3, 0.3, 0.3, 0.1]) >>> m.result().numpy() 0.23809525`

Usage with `compile()` API:

Copied!

`model.compile(   optimizer='sgd',   loss='mse',   metrics=[tf.keras.metrics.MeanIoU(num_classes=2)])`

* * *

[Image segmentation metrics](https://keras.io/2/api/metrics/segmentation_metrics/#image-segmentation-metrics)

[`MeanIoU` class](https://keras.io/2/api/metrics/segmentation_metrics/#meaniou-class)