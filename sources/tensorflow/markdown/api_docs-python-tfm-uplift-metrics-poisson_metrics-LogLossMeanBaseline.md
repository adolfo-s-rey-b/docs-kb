[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#update_state)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.metrics.poisson\_metrics.LogLossMeanBaseline Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#call)
        
    *   [merge\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#merge_state)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#result)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/poisson_metrics/LogLossMeanBaseline#update_state)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/poisson_metrics.py#L133-L201)

Computes the (weighted) poisson log loss for a mean predictor.

tfm.uplift.metrics.poisson_metrics.LogLossMeanBaseline(
        compute_full_loss: bool = False,
        slice_by_treatment: bool = True,
        name: str = 'poisson_log_loss_mean_baseline',
        dtype: tf.DType = tf.float32
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `compute_full_loss` | Specifies whether to compute the full poisson log loss for the mean predictor or not. Defaults to `False`. |
| `slice_by_treatment` | Specifies whether the loss should be sliced by the treatment indicator tensor. If `True`, the metric's result will return the loss values sliced by the treatment group. Note that this can only be set to `True` when `y_pred` is of type `TwoTowerTrainingOutputs`. |
| `name` | Optional name for the instance. |
| `dtype` | Optional data type for the instance. |

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

reset_state()

Resets all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/poisson_metrics.py#L190-L191)

result() -> (tf.Tensor | dict[str, tf.Tensor])

Computes and returns the scalar metric value tensor or a dict of scalars.

Result computation is an idempotent operation that simply calculates the metric value using the state variables.

|     |
| --- |
| Returns |     |
| A scalar tensor, or a dictionary of scalar tensors. |     |

### `update_state`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/metrics/poisson_metrics.py#L171-L188)

update_state(
        y_true: tf.Tensor,
        y_pred: (types.TwoTowerTrainingOutputs | tf.Tensor | None) = None,
        sample_weight: (tf.Tensor | None) = None
    )

Accumulates statistics for the metric.

|     |     |
| --- | --- |
| Args |     |
| `*args` |     |
| `**kwargs` | A mini-batch of inputs to the Metric. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.