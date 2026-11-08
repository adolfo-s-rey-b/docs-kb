[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.MixedPrecisionLossScaleOptimizer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale_optimizer.py#L27-L251)

An optimizer that applies loss scaling.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.MixedPrecisionLossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/MixedPrecisionLossScaleOptimizer)

tf.compat.v1.mixed_precision.MixedPrecisionLossScaleOptimizer(
        opt, loss_scale
    )

Loss scaling is a process that multiplies the loss by a multiplier called the loss scale, and divides each gradient by the same multiplier. The pseudocode for this process is:

loss = ...
    loss *= loss_scale
    grads = gradients(loss, vars)
    grads /= loss_scale

Mathematically, loss scaling has no effect, but can help avoid numerical underflow in intermediate gradients when float16 tensors are used for mixed precision training. By multiplying the loss, each intermediate gradient will have the same multiplier applied.

The loss scale can either be a fixed constant, chosen by the user, or be dynamically determined. Dynamically determining the loss scale is convenient as a loss scale does not have to be explicitly chosen. However it reduces performance.

This optimizer wraps another optimizer and applies loss scaling to it via a `LossScale`. Loss scaling is applied whenever gradients are computed, such as through `minimize()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `use_locking` | Bool. If True apply use locks to prevent concurrent updates to variables. |
| `name` | A non-empty string. The name to use for accumulators created for the optimizer. |
| `use_own_namescope_for_non_slot_vars` | If True, use a root namescope under self.\_name for non-slot variables. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If name is malformed. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale_optimizer.py#L153-L186)

apply_gradients(
        grads_and_vars, global_step=None, name=None
    )

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that conditionally applies gradients if all gradient values are finite. Otherwise no update is performed (nor is `global_step` incremented).

|     |     |
| --- | --- |
| Args |     |
| `grads_and_vars` | List of (gradient, variable) pairs as returned by `compute_gradients()`. |
| `global_step` | Optional `Variable` to increment by one after the variables have been updated. |
| `name` | Optional name for the returned operation. Default to the name passed to the `Optimizer` constructor. |

|     |
| --- |
| Returns |     |
| An `Operation` that conditionally applies the specified gradients. If `global_step` was not None, that operation also increments `global_step`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If you should use `_distributed_apply()` instead. |

### `compute_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale_optimizer.py#L80-L126)

compute_gradients(
        loss,
        var_list=None,
        gate_gradients=optimizer.Optimizer.GATE_OP,
        aggregation_method=None,
        colocate_gradients_with_ops=False,
        grad_loss=None
    )

Compute gradients of `loss` for the variables in `var_list`.

This adjusts the dynamic range of the gradient evaluation by scaling up the `loss` value. The gradient values are then scaled back down by the reciprocal of the loss scale. This is useful in reduced precision training where small gradient values would otherwise underflow the representable range.

|     |     |
| --- | --- |
| Args |     |
| `loss` | A Tensor containing the value to minimize or a callable taking no arguments which returns the value to minimize. When eager execution is enabled it must be a callable. |
| `var_list` | Optional list or tuple of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> to update to minimize `loss`. Defaults to the list of variables collected in the graph under the key `GraphKeys.TRAINABLE_VARIABLES`. |
| `gate_gradients` | How to gate the computation of gradients. Can be `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`. |
| `aggregation_method` | Specifies the method used to combine gradient terms. Valid values are defined in the class `AggregationMethod`. |
| `colocate_gradients_with_ops` | If True, try colocating gradients with the corresponding op. |
| `grad_loss` | Optional. A `Tensor` holding the gradient computed for `loss`. |

|     |
| --- |
| Returns |     |
| A list of (gradient, variable) pairs. Variable is always present, but gradient can be `None`. |     |

### `get_name`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L460-L461)

get_name()

### `get_slot`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L880-L906)

get_slot(
        var, name
    )

Return a slot named `name` created for `var` by the Optimizer.

Some `Optimizer` subclasses use additional variables. For example `Momentum` and `Adagrad` use variables to accumulate updates. This method gives access to these `Variable` objects if for some reason you need them.

Use `get_slot_names()` to get the list of slot names created by the `Optimizer`.

|     |     |
| --- | --- |
| Args |     |
| `var` | A variable passed to `minimize()` or `apply_gradients()`. |
| `name` | A string. |

|     |
| --- |
| Returns |     |
| The `Variable` for the slot if it was created, `None` otherwise. |     |

### `get_slot_names`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L908-L916)

get_slot_names()

Return a list of the names of slots created by the `Optimizer`.

See `get_slot()`.

|     |
| --- |
| Returns |     |
| A list of strings. |     |

### `minimize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L463-L521)

minimize(
        loss,
        global_step=None,
        var_list=None,
        gate_gradients=GATE_OP,
        aggregation_method=None,
        colocate_gradients_with_ops=False,
        name=None,
        grad_loss=None
    )

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and `apply_gradients()`. If you want to process the gradient before applying them call `compute_gradients()` and `apply_gradients()` explicitly instead of using this function.

|     |     |
| --- | --- |
| Args |     |
| `loss` | A `Tensor` containing the value to minimize. |
| `global_step` | Optional `Variable` to increment by one after the variables have been updated. |
| `var_list` | Optional list or tuple of `Variable` objects to update to minimize `loss`. Defaults to the list of variables collected in the graph under the key `GraphKeys.TRAINABLE_VARIABLES`. |
| `gate_gradients` | How to gate the computation of gradients. Can be `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`. |
| `aggregation_method` | Specifies the method used to combine gradient terms. Valid values are defined in the class `AggregationMethod`. |
| `colocate_gradients_with_ops` | If True, try colocating gradients with the corresponding op. |
| `name` | Optional name for the returned operation. |
| `grad_loss` | Optional. A `Tensor` holding the gradient computed for `loss`. |

|     |
| --- |
| Returns |     |
| An Operation that updates the variables in `var_list`. If `global_step` was not `None`, that operation also increments `global_step`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If some of the variables are not `Variable` objects. |

#### eager compatibility

When eager execution is enabled, `loss` should be a Python function that takes no arguments and computes the value to be minimized. Minimization (and gradient computation) is done with respect to the elements of `var_list` if not None, else with respect to any trainable variables created during the execution of the `loss` function. `gate_gradients`, `aggregation_method`, `colocate_gradients_with_ops` and `grad_loss` are ignored when eager execution is enabled.

### `variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale_optimizer.py#L248-L251)

variables()

Returns the variables of the Optimizer.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| GATE\_GRAPH | `2` |
| GATE\_NONE | `0` |
| GATE\_OP | `1` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.