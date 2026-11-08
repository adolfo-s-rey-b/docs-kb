[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2FOptimizer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#update_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Optimizer Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#update_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/optimizer.py#L21-L23)

Abstract optimizer base class.

#### View aliases

**Main aliases**

[`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)

tf.keras.Optimizer(
        *args, **kwargs
    )

If you intend to create your own optimization algorithm, please inherit from this class and override the following methods:

*   `build`: Create your optimizer-related variables, such as momentum variables in the SGD optimizer.
*   `update_step`: Implement your optimizer's variable updating logic.
*   `get_config`: serialization of the optimizer.

#### Example:

class SGD(Optimizer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.momentum = 0.9
    
        def build(self, variables):
            super().build(variables)
            self.momentums = []
            for variable in variables:
                self.momentums.append(
                    self.add_variable_from_reference(
                        reference_variable=variable, name="momentum"
                    )
                )
    
        def update_step(self, gradient, variable, learning_rate):
            learning_rate = ops.cast(learning_rate, variable.dtype)
            gradient = ops.cast(gradient, variable.dtype)
            m = self.momentums[self._get_variable_index(variable)]
            self.assign(
                m,
                ops.subtract(
                    ops.multiply(m, ops.cast(self.momentum, variable.dtype)),
                    ops.multiply(gradient, learning_rate),
                ),
            )
            self.assign_add(variable, m)
    
        def get_config(self):
            config = super().get_config()
            config.update(
                {
                    "momentum": self.momentum,
                    "nesterov": self.nesterov,
                }
            )
            return config

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `iterations` |     |
| `learning_rate` |     |
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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L466-L533)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L210-L228)

build(
        variables
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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L1008-L1021)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L1073-L1095)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L1026-L1071)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/base_optimizer.py#L736-L752)

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