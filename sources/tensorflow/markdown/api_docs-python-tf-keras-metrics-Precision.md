[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.Precision Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Precision#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L254-L411)

Computes the precision of the predictions with respect to the labels.

Inherits From: [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.Precision(
        thresholds=None, top_k=None, class_id=None, name=None, dtype=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data) |

The metric creates two local variables, `true_positives` and `false_positives` that are used to compute the precision. This value is ultimately returned as `precision`, an idempotent operation that simply divides `true_positives` by the sum of `true_positives` and `false_positives`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

If `top_k` is set, we'll calculate precision as how often on average a class among the top-k classes with the highest predicted values of a batch entry is correct and can be found in the label for that entry.

If `class_id` is specified, we calculate precision by considering only the entries in the batch for which `class_id` is above the threshold and/or in the top-k highest predictions, and computing the fraction of them for which `class_id` is indeed a correct label.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `thresholds` | (Optional) A float value, or a Python list/tuple of float threshold values in `[0, 1]`. A threshold is compared with prediction values to determine the truth value of predictions (i.e., above the threshold is `True`, below is `False`). If used with a loss function that sets `from_logits=True` (i.e. no sigmoid applied to predictions), `thresholds` should be set to 0. One metric value is generated for each threshold value. If neither `thresholds` nor `top_k` are set, the default is to calculate precision with `thresholds=0.5`. |
| `top_k` | (Optional) Unset by default. An int value specifying the top-k predictions to consider when calculating precision. |
| `class_id` | (Optional) Integer class ID for which we want binary metrics. This must be in the half-open interval `[0, num_classes)`, where `num_classes` is the last dimension of predictions. |\
| `name` | (Optional) string name of the metric instance. |\
| `dtype` | (Optional) data type of the metric result. |\
\
#### Example:\
\
    m = keras.metrics.Precision()\
\
    m.reset_state()\
\
    # With top_k=2, it will calculate precision over y_true[:2]\
\
    # With top_k=4, it will calculate precision over y_true[:4]\
\
Usage with `compile()` API:\
\
model.compile(optimizer='sgd',\
                  loss='binary_crossentropy',\
                  metrics=[keras.metrics.Precision()])\
\
Usage with a loss with `from_logits=True`:\
\
model.compile(optimizer='adam',\
                  loss=keras.losses.BinaryCrossentropy(from_logits=True),\
                  metrics=[keras.metrics.Precision(thresholds=0)])\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L404-L411)\
\
get_config()\
\
Return the serializable config of the metric.\
\
### `reset_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L399-L402)\
\
reset_state()\
\
Reset all of the metric state variables.\
\
This function is called between epochs/steps, when a metric is evaluated during training.\
\
### `result`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L392-L397)\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/confusion_metrics.py#L366-L390)\
\
update_state(\
        y_true, y_pred, sample_weight=None\
    )\
\
Accumulates true positive and false positive statistics.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `y_true` | The ground truth values, with the same dimensions as `y_pred`. Will be cast to `bool`. |\
| `y_pred` | The predicted values. Each element must be in the range `[0, 1]`. |\
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