[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2Flars%2FLARS&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#apply_gradients)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#set_weights)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#variables)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.lars.LARS Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#methods)
    *   [add\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#add_slot)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#add_weight)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#apply_gradients)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_config)
        
    *   [get\_gradients](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_gradients)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_slot_names)
        
    *   [get\_updates](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_updates)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#get_weights)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#minimize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#set_weights)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars/LARS#variables)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lars.py#L25-L186)

Layer-wise Adaptive Rate Scaling for large batch training.

tfm.optimization.lars.LARS(
        learning_rate: float = 0.01,
        momentum: float = 0.9,
        weight_decay_rate: float = 0.0,
        eeta: float = 0.001,
        nesterov: bool = False,
        classic_momentum: bool = True,
        exclude_from_weight_decay: Optional[List[Text]] = None,
        exclude_from_layer_adaptation: Optional[List[Text]] = None,
        name: Text = 'LARS',
        **kwargs
    )

Introduced by "Large Batch Training of Convolutional Networks" by Y. You, I. Gitman, and B. Ginsburg. ([https://arxiv.org/abs/1708.03888](https://arxiv.org/abs/1708.03888)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | `float` for learning rate. Defaults to 0.01. |
| `momentum` | `float` hyperparameter >= 0 that accelerates gradient descent in the relevant direction and dampens oscillations. Defaults to 0.9. |
| `weight_decay_rate` | `float` for weight decay. |
| `eeta` | `float` LARS coefficient as used in the paper. Default set to LARS coefficient from the paper. (eeta / weight\_decay) determines the highest scaling factor in LARS.. |
| `nesterov` | 'boolean' for whether to use nesterov momentum. |
| `classic_momentum` | `boolean` for whether to use classic (or popular) momentum. The learning rate is applied during momentum update in classic momentum, but after momentum for popular momentum. |
| `exclude_from_weight_decay` | A list of `string` for variable screening, if any of the string appears in a variable's name, the variable will be excluded for computing weight decay. For example, one could specify the list like \['batch\_normalization', 'bias'\] to exclude BN and bias from weight decay. |
| `exclude_from_layer_adaptation` | Similar to exclude\_from\_weight\_decay, but for layer adaptation. If it is None, it will be defaulted the same as exclude\_from\_weight\_decay. |
| `name` | `Text` as optional name for the operations created when applying gradients. Defaults to "LARS". |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lars.py#L184-L186)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lars.py#L171-L182)

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