[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLoss#main-content)

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
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.metrics.poisson\_metrics.LogLoss Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/poisson_metrics.py#L28-L124)

Computes the (weighted) poisson log loss sliced by treatment group.

Inherits From: [`LossMetric`](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric)

tfm.uplift.metrics.poisson_metrics.LogLoss(
        from_logits: bool = True,
        compute_full_loss: bool = False,
        slice_by_treatment: bool = True,
        name: str = 'poisson_log_loss',
        dtype: tf.DType = tf.float32
    )

Given labels `y` and the model's predictions `x`, the loss is computed as: `loss = x - y * log(x) + [y * log(y) - y + 0.5 * log(2 * pi * y)]`

Note that from a numerical perspective it is preferred to compute the loss from the model's logits as opposed to directly using its predictions, where `logits = log(x) = log(prediction)`. In this case the loss is computed as: `loss = exp(logits) - y * logits + [y * log(y) - y + 0.5 * log(2 * pi * y)]`

Example standalone usage:

    poisson_loss = poisson_metrics.LogLoss()

Example usage with the `model.compile()` API:

    model.compile(

|     |     |     |
| --- | --- | --- |
| Args<br>---- |     |
| `from_logits` | When `y_pred` is of type [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, specifies whether `y_pred` represents the model's logits or predictions. Otherwise, when `y_pred` is of type `TwoTowerTrainingOutputs`, set this to `True` in order to compute the loss using the true logits. |
| `compute_full_loss` | Specifies whether the full log loss will be computed. If `True`, the expression \`\[y\_true \* log(y\_true) - y\_true + 0.5 \* log(2<br><br>*   pi \* y\_true)\]`will be added to the loss, otherwise the loss will be computed solely by the expression`\[y\_pred - y\_true \* log(y\_pred)\]`. </td> </tr><tr> <td>`slice\_by\_treatment`<a id="slice_by_treatment"></a> </td> <td> Specifies whether the loss should be sliced by the treatment indicator tensor. If`True`, the metric's result will return the loss values sliced by the treatment group. Note that this can only be set to`True`when`y\_pred`is of type`TwoTowerTrainingOutputs`. </td> </tr><tr> <td>`name`<a id="name"></a> </td> <td> Optional name for the instance. </td> </tr><tr> <td>`dtype\` | Optional data type for the instance. |

Methods
-------

### `call`

call(
        inputs, *args, **kwargs
    )

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

### `merge_state`

merge_state(
        metrics
    )

Merges the state from one or more metrics.

This method can be used by distributed systems to merge the state computed by different metric instances. Typically the state will be stored in the form of the metric's weights. For example, a tf.keras.metrics.Mean metric contains a list of two weight values: a total and a count. If there were two instances of a tf.keras.metrics.Accuracy that each independently aggregated partial state for an overall accuracy calculation, these two metric's states could be combined as follows:

    m1 = tf.keras.metrics.Accuracy()

    m2 = tf.keras.metrics.Accuracy()

    m2.merge_state([m1])

|     |     |
| --- | --- |
| Args |     |
| `metrics` | an iterable of metrics. The metrics must have compatible state. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the provided iterable does not contain metrics matching the metric's required specifications. |

### `reset_state`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/loss_metric.py#L186-L187)

reset_state()

Resets all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/loss_metric.py#L183-L184)

result() -> (tf.Tensor | dict[str, tf.Tensor])

Computes and returns the scalar metric value tensor or a dict of scalars.

Result computation is an idempotent operation that simply calculates the metric value using the state variables.

|     |
| --- |
| Returns |     |
| A scalar tensor, or a dictionary of scalar tensors. |     |

### `update_state`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/poisson_metrics.py#L99-L115)

update_state(
        y_true: tf.Tensor,
        y_pred: (types.TwoTowerTrainingOutputs | tf.Tensor),
        sample_weight: (tf.Tensor | None) = None
    )

Updates the overall, control and treatment losses.

|     |     |
| --- | --- |
| Args |     |
| `y_true` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with the targets. |
| `y_pred` | Model outputs. If of type `TwoTowerTrainingOutputs`, the treatment indicator tensor is used to slice the true logits or true predictions into control and treatment losses. |
| `sample_weight` | Optional sample weight to compute weighted losses. If given, the sample weight will also be sliced by the treatment indicator tensor to compute the weighted control and treatment losses. |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if `y_pred` is not of type `TwoTowerTrainingOutputs`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.