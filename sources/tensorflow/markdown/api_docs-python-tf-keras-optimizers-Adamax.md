[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#update_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.Adamax Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#methods)
    *   [add\_optimizer\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_optimizer_variables)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_variable)
        
    *   [add\_variable\_from\_reference](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#add_variable_from_reference)
        
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#apply)
        
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#apply_gradients)
        
    *   [assign](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign)
        
    *   [assign\_add](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign_add)
        
    *   [assign\_sub](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#assign_sub)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#build)
        
    *   [exclude\_from\_weight\_decay](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#exclude_from_weight_decay)
        
    *   [finalize\_variable\_values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#finalize_variable_values)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#get_config)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#save_own_variables)
        
    *   [scale\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#scale_loss)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#set_weights)
        
    *   [stateless\_apply](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#stateless_apply)
        
    *   [update\_step](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adamax#update_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/adamax.py#L6-L141)

Optimizer that implements the Adamax algorithm.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)

tf.keras.optimizers.Adamax(
        learning_rate=0.001,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-07,
        weight_decay=None,
        clipnorm=None,
        clipvalue=None,
        global_clipnorm=None,
        use_ema=False,
        ema_momentum=0.99,
        ema_overwrite_frequency=None,
        loss_scale_factor=None,
        gradient_accumulation_steps=None,
        name=None,
        **kwargs
    )

Adamax, a variant of Adam based on the infinity norm, is a first-order gradient-based optimization method. Due to its capability of adjusting the learning rate based on data characteristics, it is suited to learn time-variant process, e.g., speech data with dynamically changed noise conditions. Default parameters follow those provided in the paper (see references below).

#### Initialization:

m = 0  # Initialize initial 1st moment vector
    u = 0  # Initialize the exponentially weighted infinity norm
    t = 0  # Initialize timestep

The update rule for parameter `w` with gradient `g` is described at the end of section 7.1 of the paper (see the reference section):

t += 1
    m = beta1 * m + (1 - beta) * g
    u = max(beta2 * u, abs(g))
    current_lr = learning_rate / (1 - beta1 ** t)
    w = w - current_lr * m / (u + epsilon)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)<br> instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`. |
| `beta_1` | A float value or a constant float tensor. The exponential decay rate for the 1st moment estimates. |
| `beta_2` | A float value or a constant float tensor. The exponential decay rate for the exponentially weighted infinity norm. |
| `epsilon` | A small constant for numerical stability. name: String. The name to use for momentum accumulator weights created by the optimizer. |
| `weight_decay` | Float. If set, weight decay is applied. |
| `clipnorm` | Float. If set, the gradient of each weight is individually clipped so that its norm is no higher than this value. |
| `clipvalue` | Float. If set, the gradient of each weight is clipped to be no higher than this value. |
| `global_clipnorm` | Float. If set, the gradient of all weights is clipped so that their global norm is no higher than this value. |
| `use_ema` | Boolean, defaults to `False`. If `True`, exponential moving average (EMA) is applied. EMA consists of computing an exponential moving average of the weights of the model (as the weight values change after each training batch), and periodically overwriting the weights with their moving average. |
| `ema_momentum` | Float, defaults to 0.99. Only used if `use_ema=True`. This is the momentum to use when computing the EMA of the model's weights: `new_average = ema_momentum * old_average + (1 - ema_momentum) * current_variable_value`. |
| `ema_overwrite_frequency` | Int or None, defaults to None. Only used if `use_ema=True`. Every `ema_overwrite_frequency` steps of iterations, we overwrite the model variable by its moving average. If None, the optimizer does not overwrite model variables in the middle of training, and you need to explicitly overwrite the variables at the end of training by calling `optimizer.finalize_variable_values()` (which updates the model variables in-place). When using the built-in `fit()` training loop, this happens automatically after the last epoch, and you don't need to do anything. |
| `loss_scale_factor` | Float or `None`. If a float, the scale factor will be multiplied the loss before computing gradients, and the inverse of the scale factor will be multiplied by the gradients before updating variables. Useful for preventing underflow during mixed precision training. Alternately, [`keras.optimizers.LossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer)<br> will automatically set a loss scale factor. |
| `gradient_accumulation_steps` | Int or `None`. If an int, model & optimizer variables will not be updated at every step; instead they will be updated every `gradient_accumulation_steps` steps, using the average value of the gradients since the last update. This is known as "gradient accumulation". This can be useful when your batch size is very small, in order to reduce gradient noise at each update step. EMA frequency will look at "accumulated" iterations value (optimizer steps // gradient\_accumulation\_steps). Learning rate schedules will look at "real" iterations value (optimizer steps). |

#### Reference:

*   [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
    

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/adamax.py#L89-L103)

build(
        var_list
    )

Initialize optimizer variables.

Adamax optimizer has 2 types of variables: momentums (denoted as m), exponentially weighted infinity norm (denoted as u).

|     |     |
| --- | --- |
| Args |     |
| `var_list` | list of model variables to build Adamax variables on. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/adamax.py#L131-L141)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/adamax.py#L105-L129)

update_step(
        gradient, variable, learning_rate
    )

Update step given gradient and the associated model variable.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.