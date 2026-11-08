[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/R2Score#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.R2Score Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/regression_metrics.py#L352-L577)

Computes R2 score.

Inherits From: [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.R2Score(
        class_aggregation='uniform_average',
        num_regressors=0,
        name='r2_score',
        dtype=None
    )

#### Formula:

sum_squares_residuals = sum((y_true - y_pred) ** 2)
    sum_squares = sum((y_true - mean(y_true)) ** 2)
    R2 = 1 - sum_squares_residuals / sum_squares

This is also called the [coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
.

It indicates how close the fitted regression line is to ground-truth data.

*   The highest score possible is 1.0. It indicates that the predictors perfectly accounts for variation in the target.
*   A score of 0.0 indicates that the predictors do not account for variation in the target.
*   It can also be negative if the model is worse than random.

This metric can also compute the "Adjusted R2" score.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `class_aggregation` | Specifies how to aggregate scores corresponding to different output classes (or target dimensions), i.e. different dimensions on the last axis of the predictions. Equivalent to `multioutput` argument in Scikit-Learn. Should be one of `None` (no aggregation), `"uniform_average"`, `"variance_weighted_average"`. |
| `num_regressors` | Number of independent regressors used ("Adjusted R2" score). 0 is the standard R2 score. Defaults to `0`. |
| `name` | Optional. string name of the metric instance. |
| `dtype` | Optional. data type of the metric result. |

#### Example:

    y_true = np.array([[1], [4], [3]], dtype=np.float32)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/regression_metrics.py#L569-L577)

get_config()

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/regression_metrics.py#L565-L567)

reset_state()

Reset all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/regression_metrics.py#L527-L563)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/regression_metrics.py#L480-L525)

update_state(
        y_true, y_pred, sample_weight=None
    )

Accumulates root mean squared error statistics.

|     |     |
| --- | --- |
| Args |     |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Can be a `Tensor` whose rank is either 0, or the same rank as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |

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