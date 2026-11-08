[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.FBetaScore Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/FBetaScore#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/f_score_metrics.py#L8-L247)

Computes F-Beta score.

Inherits From: [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.FBetaScore(
        average=None,
        beta=1.0,
        threshold=None,
        name='fbeta_score',
        dtype=None
    )

#### Formula:

b2 = beta ** 2
    f_beta_score = (1 + b2) * (precision * recall) / (precision * b2 + recall)

This is the weighted harmonic mean of precision and recall. Its output range is `[0, 1]`. It works for both multi-class and multi-label classification.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `average` | Type of averaging to be performed across per-class results in the multi-class case. Acceptable values are `None`, `"micro"`, `"macro"` and `"weighted"`. Defaults to `None`. If `None`, no averaging is performed and `result()` will return the score for each class. If `"micro"`, compute metrics globally by counting the total true positives, false negatives and false positives. If `"macro"`, compute metrics for each label, and return their unweighted mean. This does not take label imbalance into account. If `"weighted"`, compute metrics for each label, and return their average weighted by support (the number of true instances for each label). This alters `"macro"` to account for label imbalance. It can result in an score that is not between precision and recall. |
| `beta` | Determines the weight of given to recall in the harmonic mean between precision and recall (see pseudocode equation above). Defaults to `1`. |
| `threshold` | Elements of `y_pred` greater than `threshold` are converted to be 1, and the rest 0. If `threshold` is `None`, the argmax of `y_pred` is converted to 1, and the rest to 0. |
| `name` | Optional. String name of the metric instance. |
| `dtype` | Optional. Data type of the metric result. |

|     |
| --- |
| Returns<br>------- |     |
| F-Beta Score: float. |     |

#### Example:

    metric = keras.metrics.FBetaScore(beta=2.0, threshold=0.5)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/f_score_metrics.py#L231-L243)

get_config()

Returns the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/f_score_metrics.py#L245-L247)

reset_state()

Reset all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/f_score_metrics.py#L201-L229)

result()

Compute the current metric value.

|     |
| --- |
| Returns |     |
| A scalar tensor, or a dictionary of scalar tensors. |     |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/f_score_metrics.py#L158-L199)

update_state(
        y_true, y_pred, sample_weight=None
    )

Accumulate statistics for the metric.

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