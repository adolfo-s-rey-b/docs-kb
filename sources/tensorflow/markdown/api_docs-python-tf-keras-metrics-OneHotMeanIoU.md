[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.OneHotMeanIoU Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/OneHotMeanIoU#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L682-L787)

Computes mean Intersection-Over-Union metric for one-hot encoded labels.

Inherits From: [`MeanIoU`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanIoU)
, [`IoU`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.OneHotMeanIoU(
        num_classes,
        name=None,
        dtype=None,
        ignore_class=None,
        sparse_y_pred=False,
        axis=-1
    )

#### Formula:

iou = true_positives / (true_positives + false_positives + false_negatives)

Intersection-Over-Union is a common evaluation metric for semantic image segmentation.

To compute IoUs, the predictions are accumulated in a confusion matrix, weighted by `sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

This class can be used to compute the mean IoU for multi-class classification tasks where the labels are one-hot encoded (the last axis should have one dimension per class). Note that the predictions should also have the same shape. To compute the mean IoU, first the labels and predictions are converted back into integer format by taking the argmax over the class axis. Then the same computation steps as for the base `MeanIoU` class apply.

Note, if there is only one channel in the labels and predictions, this class is the same as class `MeanIoU`. In this case, use `MeanIoU` instead.

Also, make sure that `num_classes` is equal to the number of classes in the data, to avoid a "labels out of bound" error when the confusion matrix is computed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | The possible number of labels the prediction task can have. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during metric computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered. |
| `sparse_y_pred` | Whether predictions are encoded using natural numbers or probability distribution vectors. If `False`, the `argmax` function will be used to determine each sample's most likely associated label. |
| `axis` | (Optional) The dimension containing the logits. Defaults to `-1`. |

#### Example:

    y_true = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 0]])

Usage with `compile()` API:

model.compile(
        optimizer='sgd',
        loss='mse',
        metrics=[keras.metrics.OneHotMeanIoU(num_classes=3)])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L779-L787)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L77-L169)

update_state(
        y_true, y_pred, sample_weight=None
    )

Accumulates the confusion matrix statistics.

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