[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fmetrics%2FSensitivityAtSpecificity&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.SensitivityAtSpecificity Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SensitivityAtSpecificity#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L675-L776)

Computes best sensitivity where specificity is >= specified value.

Inherits From: [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.SensitivityAtSpecificity(
        specificity, num_thresholds=200, class_id=None, name=None, dtype=None
    )

`Sensitivity` measures the proportion of actual positives that are correctly identified as such `(tp / (tp + fn))`. `Specificity` measures the proportion of actual negatives that are correctly identified as such `(tn / (tn + fp))`.

This metric creates four local variables, `true_positives`, `true_negatives`, `false_positives` and `false_negatives` that are used to compute the sensitivity at the given specificity. The threshold for the given specificity value is computed and used to evaluate the corresponding sensitivity.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

If `class_id` is specified, we calculate precision by considering only the entries in the batch for which `class_id` is above the threshold predictions, and computing the fraction of them for which `class_id` is indeed a correct label.

For additional information about specificity and sensitivity, see [the following](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `specificity` | A scalar value in range `[0, 1]`. |
| `num_thresholds` | (Optional) Defaults to 200. The number of thresholds to use for matching the given specificity. |
| `class_id` | (Optional) Integer class ID for which we want binary metrics. This must be in the half-open interval `[0, num_classes)`, where `num_classes` is the last dimension of predictions. |\
| `name` | (Optional) string name of the metric instance. |\
| `dtype` | (Optional) data type of the metric result. |\
\
#### Example:\
\
    m = keras.metrics.SensitivityAtSpecificity(0.5)\
\
    m.reset_state()\
\
Usage with `compile()` API:\
\
model.compile(\
        optimizer='sgd',\
        loss='binary_crossentropy',\
        metrics=[keras.metrics.SensitivityAtSpecificity(specificity=0.5)])\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L770-L776)\
\
get_config()\
\
Return the serializable config of the metric.\
\
### `reset_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L638-L643)\
\
reset_state()\
\
Reset all of the metric state variables.\
\
This function is called between epochs/steps, when a metric is evaluated during training.\
\
### `result`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L757-L768)\
\
result()\
\
Compute the current metric value.\
\
|     |\
| --- |\
| Returns |     |\
| A scalar tensor, or a dictionary of scalar tensors. |     |\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L613-L636)\
\
update_state(\
        y_true, y_pred, sample_weight=None\
    )\
\
Accumulates confusion matrix statistics.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `y_true` | The ground truth values. |\
| `y_pred` | The predicted values. |\
| `sample_weight` | Optional weighting of each example. Defaults to `1`. Can be a tensor whose rank is either 0, or the same rank as `y_true`, and must be broadcastable to `y_true`. |\
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