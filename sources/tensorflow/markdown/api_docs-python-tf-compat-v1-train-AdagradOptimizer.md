[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#used-in-the-notebooks)
        
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.AdagradOptimizer Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#used-in-the-notebooks)
        
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#compute_gradients)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#get_slot_names)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/adagrad.py#L27-L195)

Optimizer that implements the Adagrad algorithm.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)

tf.compat.v1.train.AdagradOptimizer(
        learning_rate,
        initial_accumulator_value=0.1,
        use_locking=False,
        name='Adagrad'
    )

Migrate to TF2
--------------

tf.compat.v1.train.AdagradOptimizer is compatible with eager mode and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. When eager execution is enabled, `learning_rate`, `initial_accumulator_value`, and `epsilon` can each be a callable that takes no arguments and returns the actual value to use. This can be useful for changing these values across different invocations of optimizer functions.

To switch to native TF2 style, use [`tf.keras.optimizers.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adagrad)
 instead. Please notice that due to the implementation differences, [`tf.keras.optimizers.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adagrad)
 and [`tf.compat.v1.train.AdagradOptimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdagradOptimizer)
 may have slight differences in floating point numerics even though the formula used for the variable updates still matches.

#### Structural mapping to native TF2

Before:

optimizer = tf.compat.v1.train.AdagradOptimizer(
      learning_rate=learning_rate,
      initial_accumulator_value=initial_accumulator_value)

After:

optimizer = tf.keras.optimizers.Adagrad(
      learning_rate=learning_rate,
      initial_accumulator_value=initial_accumulator_value,
      epsilon=1e-07)

#### How to map arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `learning_rate` | `learning_rate` | Be careful of setting learning\_rate tensor value computed from the global step. In TF1 this was usually meant to imply a dynamic learning rate and would recompute in each step. In TF2 (eager + function) it will treat it as a scalar value that only gets computed once instead of a symbolic placeholder to be computed each time. |
| `initial_accumulator_value` | `initial_accumulator_value` | The argument can be value of zero in TF2, which is not accepted in TF1.\| |
| \-  | `epsilon` | `epsilon` is become configurable in TF2. The defualt value is changed from 1e-8 to 1e-7 |
| `use_locking` | \-  | Not applicable in TF2. |

#### Before & after usage example

Before:

x = tf.Variable([1,2,3], dtype=tf.float32)
    grad = tf.constant([0.1, 0.2, 0.3])
    optimizer = tf.compat.v1.train.AdagradOptimizer(learning_rate=0.001)
    optimizer.apply_gradients(zip([grad], [x]))

After:

x = tf.Variable([1,2,3], dtype=tf.float32)
    grad = tf.constant([0.1, 0.2, 0.3])
    optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.001)
    optimizer.apply_gradients(zip([grad], [x]))

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping)<br>    <br>*   [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/logging_stop_hook)<br>    <br>*   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers)<br>    <br>*   [Migrate from Estimator to Keras APIs](https://www.tensorflow.org/guide/migrate/migrating_estimator)<br>    <br>*   [Migrate single-worker multiple-GPU training](https://www.tensorflow.org/guide/migrate/mirrored_strategy) |

|     |
| --- |
| References<br>---------- |     |
| Adaptive Subgradient Methods for Online Learning and Stochastic Optimization :[Duchi et al., 2011](http://jmlr.org/papers/v12/duchi11a.html)<br> ([pdf](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf)<br>) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A `Tensor` or a floating point value. The learning rate. |
| `initial_accumulator_value` | A floating point value. Starting value for the accumulators, must be positive. |
| `use_locking` | If `True` use locks for update operations. |
| `name` | Optional name prefix for the operations created when applying gradients. Defaults to "Adagrad". |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the `initial_accumulator_value` is invalid. |

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