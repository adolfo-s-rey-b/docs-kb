[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.MomentumOptimizer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/MomentumOptimizer#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/momentum.py#L24-L203)

Optimizer that implements the Momentum algorithm.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)

tf.compat.v1.train.MomentumOptimizer(
        learning_rate,
        momentum,
        use_locking=False,
        name='Momentum',
        use_nesterov=False
    )

Migrate to TF2
--------------

tf.compat.v1.train.MomentumOptimizer is compatible with eager mode and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. When eager execution is enabled, `learning_rate`,`momentum`, can each be a callable that takes no arguments and returns the actual value to use. This can be useful for changing these values across different invocations of optimizer functions.

To switch to native TF2 style, please directly use [`tf.keras.optimizers.SGD`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/SGD)
 with the `momentum` argument.

#### Structural mapping to native TF2

Before:

optimizer = tf.compat.v1.train.MomentumOptimizer(
      learning_rate=learning_rate,
      momentum=momentum,
      use_nesterov=use_nesterov)

After:

optimizer = tf.keras.optimizers.SGD(
      learning_rate=learning_rate,
      momentum=momentum,
      nesterov=use_nesterov)

#### How to map arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `learning_rate` | `learning_rate` | Be careful of setting learning\_rate tensor value computed from the global step. In TF1 this was usually meant to imply a dynamic learning rate and would recompute in each step. In TF2 (eager + function) it will treat it as a scalar value that only gets computed once instead of a symbolic placeholder to be computed each time. |
| `momentum` | `momentum` | \-  |
| `use_locking` | \-  | Not applicable in TF2. |
| `use_nesterov` | `nesterov` | \-  |

#### Before & after usage example

Before:

x = tf.Variable([1,2,3], dtype=tf.float32)
    grad = tf.constant([0.1, 0.2, 0.3])
    optimizer = tf.compat.v1.train.MomentumOptimizer(
      learning_rate=0.001,
      momentum=0.9,
      use_nesterov=False)
    optimizer.apply_gradients(zip([grad], [x]))

After:

x = tf.Variable([1,2,3], dtype=tf.float32)
    grad = tf.constant([0.1, 0.2, 0.3])
    optimizer = tf.keras.optimizers.SGD(
      learning_rate=0.001,
      momentum=0.9,
      nesterov=False)
    optimizer.apply_gradients(zip([grad], [x]))

Description
-----------

Computes (if `use_nesterov = False`):

accumulation = momentum * accumulation + gradient
    variable -= learning_rate * accumulation

Note that in the dense version of this algorithm, `accumulation` is updated and applied regardless of a gradient's value, whereas the sparse version (when the gradient is an `IndexedSlices`, typically because of [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather)
 or an embedding) only updates variable slices and corresponding `accumulation` terms when that part of the variable was used in the forward pass.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A `Tensor` or a floating point value. The learning rate. |
| `momentum` | A `Tensor` or a floating point value. The momentum. |
| `use_locking` | If `True` use locks for update operations. |
| `name` | Optional name prefix for the operations created when applying gradients. Defaults to "Momentum". |
| `use_nesterov` | If `True` use Nesterov Momentum. See (Sutskever et al., 2013). This implementation always computes gradients at the value of the variable(s) passed to the optimizer. Using Nesterov Momentum makes the variable(s) track the values called `theta_t + mu*v_t` in the paper. This implementation is an approximation of the original formula, valid for high values of momentum. It will compute the "adjusted gradient" in NAG by assuming that the new gradient will be estimated by the current average gradient plus the product of momentum and the change in the average gradient. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L656-L783)

apply_gradients(
        grads_and_vars,
        global_step=None,
        name=None,
        skip_gradients_aggregation=False
    )

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that applies gradients.

@compatibility(TF2)

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `grads_and_vars` | `grads_and_vars` | \-  |
| `global_step` | Not supported. | Use `optimizer.iterations` |
| `name` | `name.` | \-  |

|     |     |
| --- | --- |
| Args |     |
| `grads_and_vars` | List of (gradient, variable) pairs as returned by `compute_gradients()`. |
| `global_step` | Optional `Variable` to increment by one after the variables have been updated. |
| `name` | Optional name for the returned operation. Default to the name passed to the `Optimizer` constructor. |
| `skip_gradients_aggregation` | If true, gradients aggregation will not be performed inside optimizer. Usually this arg is set to True when you write custom code aggregating gradients outside the optimizer. |

|     |
| --- |
| Returns |     |
| An `Operation` that applies the specified gradients. If `global_step` was not None, that operation also increments `global_step`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If `grads_and_vars` is malformed. |
| `ValueError` | If none of the variables have gradients. |
| `RuntimeError` | If you should use `_distributed_apply()` instead. |

### `compute_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L523-L644)

compute_gradients(
        loss,
        var_list=None,
        gate_gradients=GATE_OP,
        aggregation_method=None,
        colocate_gradients_with_ops=False,
        grad_loss=None
    )

Compute gradients of `loss` for the variables in `var_list`.

#### Migrate to TF2

[`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 in TF2 does not provide a `compute_gradients` method, and you should use a [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 to obtain the gradients:

@tf.function
    def train step(inputs):
      batch_data, labels = inputs
      with tf.GradientTape() as tape:
        predictions = model(batch_data, training=True)
        loss = tf.keras.losses.CategoricalCrossentropy(
            reduction=tf.keras.losses.Reduction.NONE)(labels, predictions)
      gradients = tape.gradient(loss, model.trainable_variables)
      optimizer.apply_gradients(zip(gradients, model.trainable_variables))

Args: loss: A Tensor containing the value to minimize or a callable taking no arguments which returns the value to minimize. When eager execution is enabled it must be a callable. var\_list: Optional list or tuple of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 to update to minimize `loss`. Defaults to the list of variables collected in the graph under the key `GraphKeys.TRAINABLE_VARIABLES`. gate\_gradients: How to gate the computation of gradients. Can be `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`. aggregation\_method: Specifies the method used to combine gradient terms. Valid values are defined in the class `AggregationMethod`. colocate\_gradients\_with\_ops: If True, try colocating gradients with the corresponding op. grad\_loss: Optional. A `Tensor` holding the gradient computed for `loss`.

Returns: A list of (gradient, variable) pairs. Variable is always present, but gradient can be `None`.

Raises: TypeError: If `var_list` contains anything else than `Variable` objects. ValueError: If some arguments are invalid. RuntimeError: If called with eager execution enabled and `loss` is not callable.

@compatibility(eager) When eager execution is enabled, `gate_gradients`, `aggregation_method`, and `colocate_gradients_with_ops` are ignored.

#### Description

This is the first part of `minimize()`. It returns a list of (gradient, variable) pairs where "gradient" is the gradient for "variable". Note that "gradient" can be a `Tensor`, an `IndexedSlices`, or `None` if there is no gradient for the given variable.

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L918-L944)

variables()

A list of variables which encode the current state of `Optimizer`.

Includes slot variables and additional global variables created by the optimizer in the current default graph.

|     |
| --- |
| Returns |     |
| A list of variables. |     |

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