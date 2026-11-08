[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fmetrics%2FBinaryIoU&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.BinaryIoU Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryIoU#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L342-L460)

Computes the Intersection-Over-Union metric for class 0 and/or 1.

Inherits From: [`IoU`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.BinaryIoU(
        target_class_ids=(0, 1), threshold=0.5, name=None, dtype=None
    )

#### Formula:

iou = true_positives / (true_positives + false_positives + false_negatives)

Intersection-Over-Union is a common evaluation metric for semantic image segmentation.

To compute IoUs, the predictions are accumulated in a confusion matrix, weighted by `sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

This class can be used to compute IoUs for a binary classification task where the predictions are provided as logits. First a `threshold` is applied to the predicted values such that those that are below the `threshold` are converted to class 0 and those that are above the `threshold` are converted to class 1.

IoUs for classes 0 and 1 are then computed, the mean of IoUs for the classes that are specified by `target_class_ids` is returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target_class_ids` | A tuple or list of target class ids for which the metric is returned. Options are `[0]`, `[1]`, or `[0, 1]`. With `[0]` (or `[1]`), the IoU metric for class 0 (or class 1, respectively) is returned. With `[0, 1]`, the mean of IoUs for the two classes is returned. |
| `threshold` | A threshold that applies to the prediction logits to convert them to either predicted class 0 if the logit is below `threshold` or predicted class 1 if the logit is above `threshold`. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

    m = keras.metrics.BinaryIoU(target_class_ids=[0, 1], threshold=0.3)

    m.reset_state()

Usage with `compile()` API:

model.compile(
        optimizer='sgd',
        loss='mse',
        metrics=[keras.metrics.BinaryIoU(\
            target_class_ids=[0],\
            threshold=0.5\
        )]
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` |     |
| `variables` |     |

Methods
-------

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L192-L209)

add_variable(
        shape, initializer, dtype=None, aggregation='sum', name=None
    )

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L211-L215)

add_weight(
        shape=(), initializer=None, dtype=None, name=None
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L233-L235)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L454-L460)

get_config()

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L171-L174)

reset_state()

Reset all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L282-L327)

result()

Compute the intersection-over-union via the confusion matrix.

### `stateless_reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L170-L183)

stateless_reset_state()

### `stateless_result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L154-L168)

stateless_result(
        metric_variables
    )

### `stateless_update_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L121-L144)

stateless_update_state(
        metric_variables, *args, **kwargs
    )

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L430-L452)

update_state(
        y_true, y_pred, sample_weight=None
    )

Accumulates the confusion matrix statistics.

Before the confusion matrix is updated, the predicted values are thresholded to be: 0 for values that are smaller than the `threshold` 1 for values that are larger or equal to the `threshold`

|     |     |
| --- | --- |
| Args |     |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Can be a `Tensor` whose rank is either 0, or the same as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |

|     |
| --- |
| Returns |     |
| Update op. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L224-L227)

__call__(
        *args, **kwargs
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.