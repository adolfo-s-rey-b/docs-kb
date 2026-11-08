[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#update_state)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.metrics.loss\_metric.LossMetric Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/loss_metric/LossMetric#update_state)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/loss_metric.py#L29-L202)

Computes a loss sliced by treatment group.

tfm.uplift.metrics.loss_metric.LossMetric(
        loss_fn: (Callable[[tf.Tensor, tf.Tensor], tf.Tensor] | tf_keras.metrics.Metric),
        from_logits: bool = True,
        slice_by_treatment: bool = True,
        name: str = 'loss',
        dtype: tf.DType = tf.float32,
        **loss_fn_kwargs
    )

Example standalone usage:

    sliced_loss = LossMetric(tf_keras.losses.mean_squared_error)

Example usage with the `model.compile()` API:

    model.compile(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `loss_fn` | The loss function or Keras metric to apply with call signature `__call__(y_true: tf,Tensor, y_pred: tf.Tensor, **loss_fn_kwargs)`. Note that the `loss_fn_kwargs` will not be passed to the `__call__` method if `loss_fn` is a Keras metric. |
| `from_logits` | When `y_pred` is of type `TwoTowerTrainingOutputs`, specifies whether the true logits or true predictions should be used to compute the loss (defaults to using the true logits). Othwerwise, this argument will be ignored if `y_pred` is of type [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `slice_by_treatment` | Specifies whether the loss should be sliced by the treatment indicator tensor. If `True`, `loss_fn` will be wrapped in a `TreatmentSlicedMetric` to report the loss values sliced by the treatment group. |
| `name` | Optional name for the instance. If `loss_fn` is a Keras metric then its name will be used instead. |
| `dtype` | Optional data type for the instance. If `loss_fn` is a Keras metric then its `dtype` will be used instead. |
| `**loss_fn_kwargs` | The keyword arguments that are passed on to `loss_fn`. These arguments will be ignored if `loss_fn` is a Keras metric. |

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/loss_metric.py#L128-L181)

update_state(
        y_true: tf.Tensor,
        y_pred: (types.TwoTowerTrainingOutputs | tf.Tensor | np.ndarray),
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