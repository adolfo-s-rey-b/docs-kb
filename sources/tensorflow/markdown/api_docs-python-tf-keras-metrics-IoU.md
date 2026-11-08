[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.IoU Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/IoU#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L177-L339)

Computes the Intersection-Over-Union metric for specific target classes.

Inherits From: [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.IoU(
        num_classes,
        target_class_ids,
        name=None,
        dtype=None,
        ignore_class=None,
        sparse_y_true=True,
        sparse_y_pred=True,
        axis=-1
    )

#### Formula:

iou = true_positives / (true_positives + false_positives + false_negatives)

Intersection-Over-Union is a common evaluation metric for semantic image segmentation.

To compute IoUs, the predictions are accumulated in a confusion matrix, weighted by `sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

Note, this class first computes IoUs for all individual classes, then returns the mean of IoUs for the classes that are specified by `target_class_ids`. If `target_class_ids` has only one id value, the IoU of that specific class is returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_classes` | The possible number of labels the prediction task can have. |
| `target_class_ids` | A tuple or list of target class ids for which the metric is returned. To compute IoU for a specific class, a list (or tuple) of a single id value should be provided. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during metric computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered. |
| `sparse_y_true` | Whether labels are encoded using integers or dense floating point vectors. If `False`, the `argmax` function is used to determine each sample's most likely associated label. |
| `sparse_y_pred` | Whether predictions are encoded using integers or dense floating point vectors. If `False`, the `argmax` function is used to determine each sample's most likely associated label. |
| `axis` | (Optional) -1 is the dimension containing the logits. Defaults to `-1`. |

#### Examples:

    # cm = [[1, 1],\
\
    m.reset_state()\
\
Usage with `compile()` API:\
\
model.compile(\
        optimizer='sgd',\
        loss='mse',\
        metrics=[keras.metrics.IoU(num_classes=2, target_class_ids=[0])])\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `dtype` |     |\
| `variables` |     |\
\
Methods\
-------\
\
### `add_variable`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L192-L209)\
\
add_variable(\
        shape, initializer, dtype=None, aggregation='sum', name=None\
    )\
\
### `add_weight`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L211-L215)\
\
add_weight(\
        shape=(), initializer=None, dtype=None, name=None\
    )\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L233-L235)\
\
@classmethod\
\
### `get_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L329-L339)\
\
get_config()\
\
Return the serializable config of the metric.\
\
### `reset_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L171-L174)\
\
reset_state()\
\
Reset all of the metric state variables.\
\
This function is called between epochs/steps, when a metric is evaluated during training.\
\
### `result`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L282-L327)\
\
result()\
\
Compute the intersection-over-union via the confusion matrix.\
\
### `stateless_reset_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L170-L183)\
\
stateless_reset_state()\
\
### `stateless_result`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L154-L168)\
\
stateless_result(\
        metric_variables\
    )\
\
### `stateless_update_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L121-L144)\
\
stateless_update_state(\
        metric_variables, *args, **kwargs\
    )\
\
### `update_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/iou_metrics.py#L77-L169)\
\
update_state(\
        y_true, y_pred, sample_weight=None\
    )\
\
Accumulates the confusion matrix statistics.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `y_true` | The ground truth values. |\
| `y_pred` | The predicted values. |\
| `sample_weight` | Optional weighting of each example. Can be a `Tensor` whose rank is either 0, or the same as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |\
\
|     |\
| --- |\
| Returns |     |\
| Update op. |     |\
\
### `__call__`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L224-L227)\
\
__call__(\
        *args, **kwargs\
    )\
\
Call self as a function.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.