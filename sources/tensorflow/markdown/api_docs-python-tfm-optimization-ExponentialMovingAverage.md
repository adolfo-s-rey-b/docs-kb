[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#apply_gradients)
        
    *   [assign\_average\_vars](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#assign_average_vars)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#set_weights)
        
    *   [shadow\_copy](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#shadow_copy)
        
    *   [swap\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#swap_weights)
        
    *   [update\_average](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#update_average)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#variables)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.ExponentialMovingAverage Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#apply_gradients)
        
    *   [assign\_average\_vars](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#assign_average_vars)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#set_weights)
        
    *   [shadow\_copy](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#shadow_copy)
        
    *   [swap\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#swap_weights)
        
    *   [update\_average](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#update_average)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage#variables)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L51-L296)

Optimizer that computes an exponential moving average of the variables.

#### View aliases

**Main aliases**

[`tfm.optimization.ema_optimizer.ExponentialMovingAverage`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage)

tfm.optimization.ExponentialMovingAverage(
        optimizer: tf_keras.optimizers.Optimizer,
        trainable_weights_only: bool = True,
        average_decay: float = 0.99,
        start_step: int = 0,
        dynamic_decay: bool = True,
        name: str = 'ExponentialMovingAverage',
        **kwargs
    )

Empirically it has been found that using the moving average of the trained parameters of a deep network is better than using its trained parameters directly. This optimizer allows you to compute this moving average and swap the variables at save time so that any code outside of the training loop will use by default the average values instead of the original ones.

Example of usage for training:

opt = tf_keras.optimizers.SGD(learning_rate)
    opt = ExponentialMovingAverage(opt)
    
    opt.shadow_copy(model)

At test time, swap the shadow variables to evaluate on the averaged weights:

opt.swap_weights()
    # Test eval the model here
    opt.swap_weights()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `optimizer` | `tf_keras.optimizers.Optimizer` that will be used to compute and apply gradients. |
| `trainable_weights_only` | 'bool', if True, only model trainable weights will be updated. Otherwise, all model weights will be updated. This mainly affects batch normalization parameters. |
| `average_decay` | float. Decay to use to maintain the moving averages of trained variables. |
| `start_step` | int. What step to start the moving average. |
| `dynamic_decay` | bool. Whether to change the decay based on the number of optimizer updates. Decay will start at 0.1 and gradually increase up to `average_decay` after each optimizer update. This behavior is similar to [`tf.train.ExponentialMovingAverage`](https://www.tensorflow.org/api_docs/python/tf/train/ExponentialMovingAverage)<br> in TF 1.x. |
| `name` | Optional name for the operations created when applying gradients. Defaults to "moving\_average". |
| `**kwargs` | keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`, `decay`}. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `clipnorm` | `float` or `None`. If set, clips gradients to a maximum norm. |
| `clipvalue` | `float` or `None`. If set, clips gradients to a maximum value. |
| `global_clipnorm` | `float` or `None`.<br><br>If set, clips gradients to a maximum norm.<br><br>Check [`tf.clip_by_global_norm`](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm)<br> for more details. |
| `has_shadow_copy` | Whether this optimizer has created shadow variables. |
| `iterations` | Variable. The number of training steps this Optimizer has run. |
| `learning_rate` |     |
| `lr` |     |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L136-L139)

apply_gradients(
        grads_and_vars, name: Optional[str] = None
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

### `assign_average_vars`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L217-L230)

assign_average_vars(
        var_list: List[tf.Variable]
    )

Assign variables in var\_list with their respective averages.

|     |     |
| --- | --- |
| Args |     |
| `var_list` | List of model variables to be assigned to their average. |

|     |     |
| --- | --- |
| Returns |     |
| `assign_op` | The op corresponding to the assignment operation of variables to their average. |

### `from_config`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L290-L296)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L280-L288)

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

### `shadow_copy`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L114-L126)

shadow_copy(
        model: tf_keras.Model
    )

Creates shadow variables for the given model weights.

### `swap_weights`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L164-L178)

swap_weights()

Swap the average and moving weights.

This is a convenience method to allow one to evaluate the averaged weights at test time. Loads the weights stored in `self._average` into the model, keeping a copy of the original model weights. Swapping twice will return the original weights.

### `update_average`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L141-L162)

@tf.function

### `variables`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/ema_optimizer.py#L251-L252)

variables()

Returns variables of this Optimizer based on the order created.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.