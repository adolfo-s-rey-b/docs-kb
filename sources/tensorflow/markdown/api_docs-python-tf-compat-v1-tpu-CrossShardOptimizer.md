[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.CrossShardOptimizer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/CrossShardOptimizer#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L28-L222)

An optimizer that averages gradients across TPU shards.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)

tf.compat.v1.tpu.CrossShardOptimizer(
        opt,
        reduction=losses.Reduction.MEAN,
        name='CrossShardOptimizer',
        group_assignment=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `opt` | An existing `Optimizer` to encapsulate. |
| `reduction` | The reduction to apply to the shard losses. |
| `name` | Optional name prefix for the operations created when applying gradients. Defaults to "CrossShardOptimizer". |
| `group_assignment` | Optional 2d int32 lists with shape \[num\_groups, num\_replicas\_per\_group\] which describles how to apply optimizer to subgroups. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If reduction is not a valid cross-shard reduction. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L161-L190)

apply_gradients(
        grads_and_vars, global_step=None, name=None
    )

Apply gradients to variables.

Calls tpu\_ops.cross\_replica\_sum() to sum gradient contributions across replicas, and then applies the real optimizer.

|     |     |
| --- | --- |
| Args |     |
| `grads_and_vars` | List of (gradient, variable) pairs as returned by compute\_gradients(). |
| `global_step` | Optional Variable to increment by one after the variables have been updated. |
| `name` | Optional name for the returned operation. Default to the name passed to the Optimizer constructor. |

|     |
| --- |
| Returns |     |
| An `Operation` that applies the gradients. If `global_step` was not None, that operation also increments `global_step`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the grads\_and\_vars is malformed. |

### `compute_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L109-L159)

compute_gradients(
        loss, var_list=None, **kwargs
    )

Compute gradients of "loss" for the variables in "var\_list".

This simply wraps `compute_gradients()` from the real optimizer. The gradients will be aggregated in `apply_gradients()` so that user can modify the gradients like clipping with per replica global norm if needed. The global norm with aggregated gradients can be bad as one replica's huge gradients can hurt the gradients from other replicas.

When the CrossShardOptimizer is constructed with `reduction == losses.Reduction.MEAN` (default), this function scales the loss by `1.0 / num_shards` before computing the gradients. Assuming the optimizer uses the default implementation of `compute_gradients()`, the gradients of the scaled loss are scaled by `1.0 / num_shards` compared to the gradients of the original loss. This scaling factor is important because `apply_gradients()` sums gradients across shards, rather than averaging them. However, the scaling factor must be taken into account when clipping the norm of the gradients or performing other postprocessing.

|     |     |
| --- | --- |
| Args |     |
| `loss` | A Tensor containing the value to minimize. |
| `var_list` | Optional list or tuple of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> to update to minimize `loss`. Defaults to the list of variables collected in the graph under the key `GraphKey.TRAINABLE_VARIABLES`. |
| `**kwargs` | Keyword arguments for compute\_gradients(). |

|     |
| --- |
| Returns |     |
| A list of (gradient, variable) pairs. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If not within a tpu\_shard\_context or group\_assignment is invalid. |

### `get_name`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L460-L461)

get_name()

### `get_slot`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L192-L204)

get_slot(
        *args, **kwargs
    )

Return a slot named "name" created for "var" by the Optimizer.

This simply wraps the get\_slot() from the actual optimizer.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Arguments for get\_slot(). |
| `**kwargs` | Keyword arguments for get\_slot(). |

|     |
| --- |
| Returns |     |
| The `Variable` for the slot if it was created, `None` otherwise. |     |

### `get_slot_names`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L206-L218)

get_slot_names(
        *args, **kwargs
    )

Return a list of the names of slots created by the `Optimizer`.

This simply wraps the get\_slot\_names() from the actual optimizer.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Arguments for get\_slot(). |
| `**kwargs` | Keyword arguments for get\_slot(). |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_optimizer.py#L220-L222)

variables()

Forwarding the variables from the underlying optimizer.

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