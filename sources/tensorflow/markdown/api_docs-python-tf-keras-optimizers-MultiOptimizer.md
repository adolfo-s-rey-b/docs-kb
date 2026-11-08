[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#update_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.MultiOptimizer Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/MultiOptimizer#update_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L161-L413)

An optimizer wrapper that delegates variables to different optimizers.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)

tf.keras.optimizers.MultiOptimizer(
        optimizer_map, loss_scale_factor=None, name=None
    )

Initialize the object with an OptimizerMap instance or a callable function that returns an optimizer for a given variable.

|     |
| --- |
| Example<br>------- |     |
| model.compile( optimizer=MultiOptimizer( OptimizerMap(default\_optimizer=optimizers.SGD(), {"encoder/.\*": optimizers.Adam()}) ), loss="binary\_crossentropy", )<br><br>Or using a callable<br>===================<br><br>def optimizer\_selector(variable): if "encoder" in variable.path: return optimizers.Adam() else: return optimizers.SGD()<br><br>model.compile( optimizer=MultiOptimizer(optimizer\_selector), loss="binary\_crossentropy", ) |     |

To access the attributes of the sub-optimizers, iterate over the optimizers using `.optimizers`:

#### For example:

optimizer = MultiOptimizer(OptimizerMap( default\_optimizer=optimizers.Adam() )) optimizer\['.encoder'\] = optimizers.SGD()

for optim in optimizer.optimizers: print(optim.learning\_rate) print(optim.iterations) print(optim.loss\_scale\_factor) ...

The MultiOptimizer class instances will not expose `learning_rate` attribute and will raise an error if accessed. This is because the learning rate might be different for different sub-optimizers.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `optimizer_map` | An OptimizerMap instance or a callable function that returns an optimizer for a given variable. |
| `loss_scale_factor` | It overrides the loss\_scale\_factor passed to the sub-optimizers. |
| `name` | The name of the optimizer. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `iterations` |     |
| `learning_rate` |     |
| `loss_scale_factor` |     |
| `optimizers` |     |
| `variables` |     |

Methods
-------

### `add_optimizer_variables`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L327-L403)

add_optimizer_variables(
        trainable_variables, name, initializer='zeros'
    )

Add optimizer variables from the list of trainable model variables.

Create an optimizer variable based on the information of the supplied model variables. For example, in SGD optimizer momemtum, for each model variable, a corresponding momemtum variable is created of the same shape and dtype.

Note that trainable variables with `v.overwrite_with_gradient == True` will insert `None`, into the output list, since the optimizer variable will not be used anyways, and could be wasteful.

|     |     |
| --- | --- |
| Args |     |
| `trainable_variables` | [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>, the corresponding model variable to the optimizer variable to be created. |
| `name` | The name prefix(es) of the optimizer variable(s) to be created. Can be a single string or list of strings. If a list of strings, will create an optimizer variable for each prefix. The variable name will follow the pattern `{variable_name}_{trainable_variable.name}`, e.g., `momemtum/dense_1`. |
| `initializer` | Initializer object(s) to use to populate the initial variable value(s), or string name of a built-in initializer (e.g. `"random_normal"`). If unspecified, defaults to `"zeros"`. |

|     |
| --- |
| Returns |     |
| A list of optimizer variables, in the format of [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>s. If multiple names are provide, returns a tuple of lists. |     |

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L241-L284)

add_variable(
        shape,
        initializer='zeros',
        dtype=None,
        aggregation='none',
        layout=None,
        name=None
    )

Add a variable to the optimizer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape tuple for the variable. Must be fully-defined (no `None` entries). |
| `initializer` | Initializer object to use to populate the initial variable value, or string name of a built-in initializer (e.g. `"random_normal"`). Defaults to `"zeros"`. |
| `dtype` | Dtype of the variable to create, e.g. `"float32"`. If unspecified, defaults to the [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. |
| `aggregation` | Optional string, one of `None`, `"none"`, `"mean"`, `"sum"` or `"only_first_replica"`. Annotates the variable with the type of multi-replica aggregation to be used for this variable when writing custom data parallel training loops. Defaults to `"none"`. |
| `layout` | Optional tensor layout. Defaults to `None`. |
| `name` | String name of the variable. Useful for debugging purposes. |

|     |
| --- |
| Returns |     |
| An optimizer variable, in the format of [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>. |     |

### `add_variable_from_reference`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/optimizer.py#L24-L37)

add_variable_from_reference(
        reference_variable, name=None, initializer='zeros'
    )

Add an optimizer variable from the model variable.

Create an optimizer variable based on the information of model variable. For example, in SGD optimizer momemtum, for each model variable, a corresponding momemtum variable is created of the same shape and dtype.

|     |     |
| --- | --- |
| Args |     |
| `reference_variable` | [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>. The corresponding model variable to the optimizer variable to be created. |
| `name` | Optional string. The name prefix of the optimizer variable to be created. If not provided, it will be set to `"var"`. The variable name will follow the pattern `{variable_name}_{reference_variable.name}`, e.g., `momemtum/dense_1`. Defaults to `None`. |
| `initializer` | Initializer object to use to populate the initial variable value, or string name of a built-in initializer (e.g. `"random_normal"`). If unspecified, defaults to `"zeros"`. |

|     |
| --- |
| Returns |     |
| An optimizer variable, in the format of [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>. |     |

### `apply`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L328-L365)

apply(
        grads, trainable_variables=None
    )

Update traininable variables according to provided gradient values.

`grads` should be a list of gradient tensors with 1:1 mapping to the list of variables the optimizer was built with.

`trainable_variables` can be provided on the first call to build the optimizer.

### `apply_gradients`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L460-L464)

apply_gradients(
        grads_and_vars
    )

### `assign`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/optimizer.py#L47-L54)

assign(
        variable, value
    )

Assign a value to a variable.

This should be used in optimizers instead of `variable.assign(value)` to support backend specific optimizations. Note that the variable can be a model variable or an optimizer variable; it can be a backend native variable or a Keras variable.

|     |     |
| --- | --- |
| Args |     |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `assign_add`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/optimizer.py#L56-L63)

assign_add(
        variable, value
    )

Add a value to a variable.

This should be used in optimizers instead of `variable.assign_add(value)` to support backend specific optimizations. Note that the variable can be a model variable or an optimizer variable; it can be a backend native variable or a Keras variable.

|     |     |
| --- | --- |
| Args |     |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `assign_sub`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/optimizer.py#L65-L72)

assign_sub(
        variable, value
    )

Subtract a value from a variable.

This should be used in optimizers instead of `variable.assign_sub(value)` to support backend specific optimizations. Note that the variable can be a model variable or an optimizer variable; it can be a backend native variable or a Keras variable.

|     |     |
| --- | --- |
| Args |     |
| `variable` | The variable to update. |
| `value` | The value to add to the variable. |

### `build`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L246-L285)

build(
        var_list
    )

### `exclude_from_weight_decay`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L883-L921)

exclude_from_weight_decay(
        var_list=None, var_names=None
    )

Exclude variables from weight decay.

This method must be called before the optimizer's `build` method is called. You can set specific variables to exclude out, or set a list of strings as the anchor words, if any of which appear in a variable's name, then the variable is excluded.

|     |     |
| --- | --- |
| Args |     |
| `var_list` | A list of `Variable`s to exclude from weight decay. |
| `var_names` | A list of strings. If any string in `var_names` appear in the model variable's name, then this model variable is excluded from weight decay. For example, `var_names=['bias']` excludes all bias variables from weight decay. |

### `finalize_variable_values`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L367-L375)

finalize_variable_values(
        var_list
    )

Set the final value of model's trainable variables.

Sometimes there are some extra steps before ending the variable updates, such as overriding the model variables with its average value.

|     |     |
| --- | --- |
| Args |     |
| `var_list` | list of model variables. |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L407-L413)

@classmethod

Creates an optimizer from its config.

This method is the reverse of `get_config`, capable of instantiating the same optimizer from the config dictionary.

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of get\_config. |
| `custom_objects` | A Python dictionary mapping names to additional user-defined Python objects needed to recreate this optimizer. |

|     |
| --- |
| Returns |     |
| An optimizer instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L398-L405)

get_config()

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable) containing the configuration of an optimizer. The same optimizer can be reinstantiated later (without any saved state) from this configuration.

Subclass optimizer should override this method to include other hyperparameters.

|     |
| --- |
| Returns |     |
| Python dictionary. |     |

### `load_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L759-L775)

load_own_variables(
        store
    )

Set the state of this optimizer object.

### `save_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L754-L757)

save_own_variables(
        store
    )

Get the state of this optimizer object.

### `scale_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L691-L700)

scale_loss(
        loss
    )

Scale the loss before computing gradients.

Scales the loss before gradients are computed in a `train_step`. This is primarily useful during mixed precision training to prevent numeric underflow.

### `set_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L377-L396)

set_weights(
        weights
    )

Set the weights of the optimizer.

### `stateless_apply`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/optimizer.py#L39-L45)

stateless_apply(
        optimizer_variables, grads, trainable_variables
    )

Stateless version of `apply` that returns modified variables.

|     |     |
| --- | --- |
| Args |     |
| `optimizer_variables` | list of tensors containing the current values for the optimizer variables. These are native tensors and not [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>s. |
| `grads` | list of gradients to apply. |
| `trainable_variables` | list of tensors containing the current values for the model variables. These are native tensors and not [`keras.Variable`](https://www.tensorflow.org/api_docs/python/tf/keras/Variable)<br>s. |

Returns: A tuple containing two list of tensors, the updated `trainable_variables` and the updated `optimizer_variables`.

### `update_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L457-L458)

update_step(
        gradient, variable, learning_rate
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.