[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#add_loss)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#build)
        
    *   [build\_from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#build_from_config)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#compute_output_shape)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#from_config)
        
    *   [get\_build\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_build_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_weights)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#save_own_variables)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.layers.SoftRound Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#add_loss)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#build)
        
    *   [build\_from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#build_from_config)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#compute_output_shape)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#from_config)
        
    *   [get\_build\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_build_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#get_weights)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#load_own_variables)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#save_own_variables)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/soft_round.py#L27-L42)

Applies a differentiable approximation of rounding.

#### View aliases

**Main aliases**

[`tfc.SoftRound`](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound)

tfc.layers.SoftRound(
        alpha=5.0, inverse=False, **kwargs
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `activity_regularizer` | Optional regularizer function for the output of this layer. |
| `compute_dtype` | The dtype of the layer's computations.<br><br>This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless mixed precision is used, this is the same as [`Layer.dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#dtype)<br>, the dtype of the weights.<br><br>Layers automatically cast their inputs to the compute dtype, which causes computations and the output to be in the compute dtype as well. This is done by the base Layer class in [`Layer.**call**`](https://www.tensorflow.org/probability/oryx/api_docs/python/oryx/core/state/Module#__call__)<br>, so you do not have to insert these casts if implementing your own layer.<br><br>Layers often perform certain internal computations in higher precision when `compute_dtype` is float16 or bfloat16 for numeric stability. The output will still typically be float16 or bfloat16 in such cases. |
| `dtype` | The dtype of the layer weights.<br><br>This is equivalent to `Layer.dtype_policy.variable_dtype`. Unless mixed precision is used, this is the same as [`Layer.compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#compute_dtype)<br>, the dtype of the layer's computations. |
| `dtype_policy` | The dtype policy associated with this layer.<br><br>This is an instance of a [`tf.keras.mixed_precision.Policy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br>. |
| `dynamic` | Whether the layer is dynamic (eager-only); set in the constructor. |
| `input` | Retrieves the input tensor(s) of a layer.<br><br>Only applicable if the layer has exactly one input, i.e. if it is connected to one incoming layer. |
| `input_spec` | `InputSpec` instance(s) describing the input format for this layer.<br><br>When you create a layer subclass, you can set `self.input_spec` to enable the layer to run input compatibility checks when it is called. Consider a `Conv2D` layer: it can only be called on a single input tensor of rank 4. As such, you can set, in `__init__()`:<br><br>self.input_spec = tf.keras.layers.InputSpec(ndim=4)<br><br>Now, if you try to call the layer on an input that isn't rank 4 (for instance, an input of shape `(2,)`, it will raise a nicely-formatted error:<br><br>ValueError: Input 0 of layer conv2d is incompatible with the layer:<br>    expected ndim=4, found ndim=1. Full shape received: [2]<br><br>Input checks that can be specified via `input_spec` include:<br><br>*   Structure (e.g. a single input, a list of 2 inputs, etc)<br>*   Shape<br>*   Rank (ndim)<br>*   Dtype<br><br>For more information, see [`tf.keras.layers.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>. |
| `losses` | List of losses added using the `add_loss()` API.<br><br>Variable regularization tensors are created when this property is accessed, so it is eager safe: accessing `losses` under a [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)<br> will propagate gradients back to the corresponding variables.<br><br>    class MyLayer(tf.keras.layers.Layer):<br><br>    inputs = tf.keras.Input(shape=(10,))<br><br>    inputs = tf.keras.Input(shape=(10,)) |
| `metrics` | List of metrics attached to the layer. |
| `name` | Name of the layer (string), set in the constructor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_weights` | List of all non-trainable weights tracked by this layer.<br><br>Non-trainable weights are _not_ updated during training. They are expected to be updated manually in `call()`. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only applicable if the layer has exactly one output, i.e. if it is connected to one incoming layer. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `supports_masking` | Whether this layer supports computing a mask using `compute_mask`. |
| `trainable` |     |
| `trainable_weights` | List of all trainable weights tracked by this layer.<br><br>Trainable weights are updated via gradient descent during training. |
| `variable_dtype` | Alias of [`Layer.dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#dtype)<br>, the dtype of the weights. |
| `weights` | Returns the list of all layer variables/weights. |

Methods
-------

### `add_loss`

add_loss(
        losses, **kwargs
    )

Add loss tensor(s), potentially dependent on layer inputs.

Some losses (for instance, activity regularization losses) may be dependent on the inputs passed when calling a layer. Hence, when reusing the same layer on different inputs `a` and `b`, some entries in `layer.losses` may be dependent on `a` and some on `b`. This method automatically keeps track of dependencies.

This method can be used inside a subclassed layer or model's `call` function, in which case `losses` should be a Tensor or list of Tensors.

#### Example:

class MyLayer(tf.keras.layers.Layer):
      def call(self, inputs):
        self.add_loss(tf.abs(tf.reduce_mean(inputs)))
        return inputs

The same code works in distributed training: the input to `add_loss()` is treated like a regularization loss and averaged across replicas by the training loop (both built-in [`Model.fit()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 and compliant custom training loops).

The `add_loss` method can also be called directly on a Functional Model during construction. In this case, any loss Tensors passed to this Model must be symbolic and be able to be traced back to the model's `Input`s. These losses become part of the model's topology and are tracked in `get_config`.

#### Example:

inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Activity regularization.
    model.add_loss(tf.abs(tf.reduce_mean(x)))

If this is not the case for your loss (if, for example, your loss references a `Variable` of one of the model's layers), you can wrap your loss in a zero-argument lambda. These losses are not tracked as part of the model's topology since they can't be serialized.

#### Example:

inputs = tf.keras.Input(shape=(10,))
    d = tf.keras.layers.Dense(10)
    x = d(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Weight regularization.
    model.add_loss(lambda: tf.reduce_mean(d.kernel))

|     |     |
| --- | --- |
| Args |     |
| `losses` | Loss tensor, or list/tuple of tensors. Rather than tensors, losses may also be zero-argument callables which create a loss tensor. |
| `**kwargs` | Used for backwards compatibility only. |

### `build`

build(
        input_shape
    )

Creates the variables of the layer (for subclass implementers).

This is a method that implementers of subclasses of `Layer` or `Model` can override if they need a state-creation step in-between layer instantiation and layer call. It is invoked automatically before the first execution of `call()`.

This is typically used to create the weights of `Layer` subclasses (at the discretion of the subclass implementer).

|     |     |
| --- | --- |
| Args |     |
| `input_shape` | Instance of `TensorShape`, or list of instances of `TensorShape` if the layer expects a list of inputs (one instance per input). |

### `build_from_config`

build_from_config(
        config
    )

Builds the layer's states with the supplied config dict.

By default, this method calls the `build(config["input_shape"])` method, which creates weights based on the layer's input shape in the supplied config. If your config contains other information needed to load the layer's state, you should override this method.

|     |     |
| --- | --- |
| Args |     |
| `config` | Dict containing the input shape associated with this layer. |

### `compute_mask`

compute_mask(
        inputs, mask=None
    )

Computes an output mask tensor.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Tensor or list of tensors. |
| `mask` | Tensor or list of tensors. |

|     |
| --- |
| Returns |     |
| None or a tensor (or list of tensors, one per output tensor of the layer). |     |

### `compute_output_shape`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/soft_round.py#L41-L42)

compute_output_shape(
        input_shape
    )

Computes the output shape of the layer.

This method will cause the layer's state to be built, if that has not happened before. This requires that the layer will later be used with inputs that match the input shape provided here.

|     |     |
| --- | --- |
| Args |     |
| `input_shape` | Shape tuple (tuple of integers) or [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>, or structure of shape tuples / [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> instances (one per output tensor of the layer). Shape tuples can include None for free dimensions, instead of an integer. |

|     |
| --- |
| Returns |     |
| A [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> instance or structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> instances. |     |

### `count_params`

count_params()

Count the total number of scalars composing the weights.

|     |
| --- |
| Returns |     |
| An integer count. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if the layer isn't yet built (in which case its weights aren't yet defined). |

### `from_config`

@classmethod

Creates a layer from its config.

This method is the reverse of `get_config`, capable of instantiating the same layer from the config dictionary. It does not handle layer connectivity (handled by Network), nor weights (handled by `set_weights`).

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of get\_config. |

|     |
| --- |
| Returns |     |
| A layer instance. |     |

### `get_build_config`

get_build_config()

Returns a dictionary with the layer's input shape.

This method returns a config dict that can be used by `build_from_config(config)` to create all states (e.g. Variables and Lookup tables) needed by the layer.

By default, the config only contains the input shape that the layer was built with. If you're writing a custom layer that creates state in an unusual way, you should override this method to make sure this state is already created when Keras attempts to load its value upon model loading.

|     |
| --- |
| Returns |     |
| A dict containing the input shape associated with the layer. |     |

### `get_config`

get_config()

Returns the config of the layer.

A layer config is a Python dictionary (serializable) containing the configuration of a layer. The same layer can be reinstantiated later (without its trained weights) from this configuration.

The config of a layer does not include connectivity information, nor the layer class name. These are handled by `Network` (one layer of abstraction above).

Note that `get_config()` does not guarantee to return a fresh copy of dict every time it is called. The callers should make a copy of the returned dict if they want to modify it.

|     |
| --- |
| Returns |     |
| Python dictionary. |     |

### `get_weights`

get_weights()

Returns the current weights of the layer, as NumPy arrays.

The weights of a layer represent the state of the layer. This function returns both trainable and non-trainable weight values associated with this layer as a list of NumPy arrays, which can in turn be used to load state into similarly parameterized layers.

For example, a `Dense` layer returns a list of two values: the kernel matrix and the bias vector. These can be used to set the weights of another `Dense` layer:

    layer_a = tf.keras.layers.Dense(1,

|     |
| --- |
| Returns |     |
| Weights values as a list of NumPy arrays. |     |

### `load_own_variables`

load_own_variables(
        store
    )

Loads the state of the layer.

You can override this method to take full control of how the state of the layer is loaded upon calling [`keras.models.load_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
.

|     |     |
| --- | --- |
| Args |     |
| `store` | Dict from which the state of the model will be loaded. |

### `save_own_variables`

save_own_variables(
        store
    )

Saves the state of the layer.

You can override this method to take full control of how the state of the layer is saved upon calling `model.save()`.

|     |     |
| --- | --- |
| Args |     |
| `store` | Dict where the state of the model will be saved. |

### `set_weights`

set_weights(
        weights
    )

Sets the weights of the layer, from NumPy arrays.

The weights of a layer represent the state of the layer. This function sets the weight values from numpy arrays. The weight values should be passed in the order they are created by the layer. Note that the layer's weights must be instantiated before calling this function, by calling the layer.

For example, a `Dense` layer returns a list of two values: the kernel matrix and the bias vector. These can be used to set the weights of another `Dense` layer:

    layer_a = tf.keras.layers.Dense(1,

|     |     |
| --- | --- |
| Args |     |
| `weights` | a list of NumPy arrays. The number of arrays and their shape must match number of the dimensions of the weights of the layer (i.e. it should match the output of `get_weights`). |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the provided weights list does not match the layer's specifications. |

### `with_name_scope`

@classmethod

Decorator to automatically enter the module name scope.

    class MyModule(tf.Module):

Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s whose names included the module name:

    mod = MyModule()

|     |     |
| --- | --- |
| Args |     |
| `method` | The method to wrap. |

|     |
| --- |
| Returns |     |
| The original method wrapped such that it enters the module's name scope. |     |

### `__call__`

__call__(
        *args, **kwargs
    )

Wraps `call`, applying pre- and post-processing steps.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Positional arguments to be passed to `self.call`. |
| `**kwargs` | Keyword arguments to be passed to `self.call`. |

|     |
| --- |
| Returns |     |
| Output tensor(s). |     |

|     |
| --- |
| Note |     |
| *   The following optional keyword arguments are reserved for specific uses:<br>    *   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>    *   `mask`: Boolean input mask.<br>*   If the layer's `call` method takes a `mask` argument (as some Keras layers do), its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a Keras layer with masking support.<br>*   If the layer is not built, the method will call `build`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if the layer's `call` method returns None (an invalid value). |
| `RuntimeError` | if `super().__init__()` was not called in the constructor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.