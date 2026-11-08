[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#apply_gradients)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#set_weights)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#variables)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.lamb.LAMB Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#apply_gradients)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#set_weights)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb/LAMB#variables)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lamb.py#L29-L252)

Optimizer that implements the Layer-wise Adaptive Moments (LAMB).

tfm.optimization.lamb.LAMB(
        learning_rate: Union[FloatTensorLike, Callable] = 0.001,
        beta_1: tfm.optimization.lamb.FloatTensorLike = 0.9,
        beta_2: tfm.optimization.lamb.FloatTensorLike = 0.999,
        epsilon: tfm.optimization.lamb.FloatTensorLike = 1e-06,
        weight_decay_rate: tfm.optimization.lamb.FloatTensorLike = 0.0,
        exclude_from_weight_decay: Optional[List[str]] = None,
        exclude_from_layer_adaptation: Optional[List[str]] = None,
        name: str = 'LAMB',
        **kwargs
    )

See paper [Large Batch Optimization for Deep Learning: Training BERT in 76 minutes](https://arxiv.org/abs/1904.00962)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A `Tensor` or a floating point value. or a schedule that is a `tf_keras.optimizers.schedules.LearningRateSchedule` The learning rate. |
| `beta_1` | A `float` value or a constant `float` tensor. The exponential decay rate for the 1st moment estimates. |
| `beta_2` | A `float` value or a constant `float` tensor. The exponential decay rate for the 2nd moment estimates. |
| `epsilon` | A small constant for numerical stability. |
| `weight_decay_rate` | weight decay rate. |
| `exclude_from_weight_decay` | List of regex patterns of variables excluded from weight decay. Variables whose name contain a substring matching the pattern will be excluded. |
| `exclude_from_layer_adaptation` | List of regex patterns of variables excluded from layer adaptation. Variables whose name contain a substring matching the pattern will be excluded. |
| `name` | Optional name for the operations created when applying gradients. Defaults to "LAMB". |
| `**kwargs` | keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`, `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip gradients by value, `decay` is included for backward compatibility to allow time inverse decay of learning rate. `lr` is included for backward compatibility, recommended to use `learning_rate` instead. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `clipnorm` | `float` or `None`. If set, clips gradients to a maximum norm. |
| `clipvalue` | `float` or `None`. If set, clips gradients to a maximum value. |
| `global_clipnorm` | `float` or `None`.<br><br>If set, clips gradients to a maximum norm.<br><br>Check [`tf.clip_by_global_norm`](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm)<br> for more details. |
| `iterations` | Variable. The number of training steps this Optimizer has run. |
| `weights` | Returns variables of this Optimizer based on the order created. |

Methods
-------

### `add_slot`

add_slot(
        var, slot_name, initializer='zeros', shape=None
    )

Add a new slot variable for `var`.

A slot variable is an additional variable associated with `var` to train. It is allocated and managed by optimizers, e.g. `Adam`.

|     |     |
| --- | --- |
| Args |     |
| `var` | a `Variable` object. |
| `slot_name` | name of the slot variable. |
| `initializer` | initializer of the slot variable |
| `shape` | (Optional) shape of the slot variable. If not set, it will default to the shape of `var`. |

|     |
| --- |
| Returns |     |
| A slot variable. |     |

### `add_weight`

add_weight(
        name,
        shape,
        dtype=None,
        initializer='zeros',
        trainable=None,
        synchronization=tf.VariableSynchronization.AUTO,
        aggregation=tf.VariableAggregation.NONE
    )

### `apply_gradients`

apply_gradients(
        grads_and_vars, name=None, experimental_aggregate_gradients=True
    )

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that applies gradients.

The method sums gradients from all replicas in the presence of [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 by default. You can aggregate gradients yourself by passing `experimental_aggregate_gradients=False`.

#### Example:

grads = tape.gradient(loss, vars)
    grads = tf.distribute.get_replica_context().all_reduce('sum', grads)
    # Processing aggregated gradients.
    optimizer.apply_gradients(zip(grads, vars),
        experimental_aggregate_gradients=False)

|     |     |
| --- | --- |
| Args |     |
| `grads_and_vars` | List of (gradient, variable) pairs. |
| `name` | Optional name for the returned operation. When `None`, uses the name passed to the `Optimizer` constructor. Defaults to `None`. |
| `experimental_aggregate_gradients` | Whether to sum gradients from different replicas in the presence of [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. If False, it's user responsibility to aggregate the gradients. Default to `True`. |

|     |
| --- |
| Returns |     |
| An `Operation` that applies the specified gradients. The `iterations` will be automatically increased by 1. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If `grads_and_vars` is malformed. |
| `ValueError` | If none of the variables have gradients. |
| `RuntimeError` | If called in a cross-replica context. |

### `from_config`

@classmethod

Creates an optimizer from its config.

This method is the reverse of `get_config`, capable of instantiating the same optimizer from the config dictionary.

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of get\_config. |
| `custom_objects` | A Python dictionary mapping names to additional Python objects used to create this optimizer, such as a function used for a hyperparameter. |

|     |
| --- |
| Returns |     |
| An optimizer instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lamb.py#L217-L229)

get_config()

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable) containing the configuration of an optimizer. The same optimizer can be reinstantiated later (without any saved state) from this configuration.

|     |
| --- |
| Returns |     |
| Python dictionary. |     |

### `get_gradients`

get_gradients(
        loss, params
    )

Returns gradients of `loss` with respect to `params`.

Should be used only in legacy v1 graph mode.

|     |     |
| --- | --- |
| Args |     |
| `loss` | Loss tensor. |
| `params` | List of variables. |

|     |
| --- |
| Returns |     |
| List of gradient tensors. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | In case any gradient cannot be computed (e.g. if gradient function not implemented). |

### `get_slot`

get_slot(
        var, slot_name
    )

### `get_slot_names`

get_slot_names()

A list of names for this optimizer's slots.

### `get_updates`

get_updates(
        loss, params
    )

### `get_weights`

get_weights()

Returns the current weights of the optimizer.

The weights of an optimizer are its state (ie, variables). This function returns the weight values associated with this optimizer as a list of Numpy arrays. The first value is always the iterations count of the optimizer, followed by the optimizer's state variables in the order they were created. The returned list can in turn be used to load state into similarly parameterized optimizers.

For example, the RMSprop optimizer for this simple model returns a list of three values-- the iteration count, followed by the root-mean-square value of the kernel and bias of the single Dense layer:

    opt = tf.keras.optimizers.legacy.RMSprop()

|     |
| --- |
| Returns |     |
| Weights values as a list of numpy arrays. |     |

### `minimize`

minimize(
        loss, var_list, grad_loss=None, name=None, tape=None
    )

Minimize `loss` by updating `var_list`.

This method simply computes gradient using [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 and calls `apply_gradients()`. If you want to process the gradient before applying then call [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 and `apply_gradients()` explicitly instead of using this function.

|     |     |
| --- | --- |
| Args |     |
| `loss` | `Tensor` or callable. If a callable, `loss` should take no arguments and return the value to minimize. If a `Tensor`, the `tape` argument must be passed. |
| `var_list` | list or tuple of `Variable` objects to update to minimize `loss`, or a callable returning the list or tuple of `Variable` objects. Use callable when the variable list would otherwise be incomplete before `minimize` since the variables are created at the first time `loss` is called. |
| `grad_loss` | (Optional). A `Tensor` holding the gradient computed for `loss`. |
| `name` | (Optional) str. Name for the returned operation. |
| `tape` | (Optional) [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)<br>. If `loss` is provided as a `Tensor`, the tape that computed the `loss` must be provided. |

|     |
| --- |
| Returns |     |
| An `Operation` that updates the variables in `var_list`. The `iterations` will be automatically increased by 1. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If some of the variables are not `Variable` objects. |

### `set_weights`

set_weights(
        weights
    )

Set the weights of the optimizer.

The weights of an optimizer are its state (ie, variables). This function takes the weight values associated with this optimizer as a list of Numpy arrays. The first value is always the iterations count of the optimizer, followed by the optimizer's state variables in the order they are created. The passed values are used to set the new state of the optimizer.

For example, the RMSprop optimizer for this simple model takes a list of three values-- the iteration count, followed by the root-mean-square value of the kernel and bias of the single Dense layer:

    opt = tf.keras.optimizers.legacy.RMSprop()

|     |     |
| --- | --- |
| Args |     |
| `weights` | weight values as a list of numpy arrays. |

### `variables`

variables()

Returns variables of this Optimizer based on the order created.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.