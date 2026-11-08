[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2FLayer%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#methods_2)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_loss)
        
    *   [add\_metric](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_metric)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_weight)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#build)
        
    *   [build\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#build_from_config)
        
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#call)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_output_shape)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_output_spec)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#from_config)
        
    *   [get\_build\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_build_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_weights)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#load_own_variables)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantize)
        
    *   [quantized\_build](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantized_build)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#rematerialized_call)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#save_own_variables)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#set_weights)
        
    *   [stateless\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#stateless_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Layer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#methods_2)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_loss)
        
    *   [add\_metric](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_metric)
        
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#add_weight)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#build)
        
    *   [build\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#build_from_config)
        
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#call)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_output_shape)
        
    *   [compute\_output\_spec](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#compute_output_spec)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#from_config)
        
    *   [get\_build\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_build_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#get_weights)
        
    *   [load\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#load_own_variables)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantize)
        
    *   [quantized\_build](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantized_build)
        
    *   [quantized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#quantized_call)
        
    *   [rematerialized\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#rematerialized_call)
        
    *   [save\_own\_variables](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#save_own_variables)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#set_weights)
        
    *   [stateless\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#stateless_call)
        
    *   [symbolic\_call](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#symbolic_call)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Layer?version=stable#__call__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L70-L1863)

This is the class from which all layers inherit.

Inherits From: [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)

tf.keras.Layer(
        *,
        activity_regularizer=None,
        trainable=True,
        dtype=None,
        autocast=True,
        name=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

A layer is a callable object that takes as input one or more tensors and that outputs one or more tensors. It involves _computation_, defined in the `call()` method, and a _state_ (weight variables). State can be created:

*   in `__init__()`, for instance via `self.add_weight()`;
*   in the optional `build()` method, which is invoked by the first `__call__()` to the layer, and supplies the shape(s) of the input(s), which may not have been known at initialization time.

Layers are recursively composable: If you assign a Layer instance as an attribute of another Layer, the outer layer will start tracking the weights created by the inner layer. Nested layers should be instantiated in the `__init__()` method or `build()` method.

Users will just instantiate a layer and then treat it as a callable.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `trainable` | Boolean, whether the layer's variables should be trainable. |
| `name` | String name of the layer. |
| `dtype` | The dtype of the layer's computations and weights. Can also be a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br>, which allows the computation and weight dtype to differ. Defaults to `None`. `None` means to use [`keras.config.dtype_policy()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>, which is a `float32` policy unless set to different value (via [`keras.config.set_dtype_policy()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_dtype_policy)<br>). |

We recommend that descendants of `Layer` implement the following methods:

*   `__init__()`: Defines custom layer attributes, and creates layer weights that do not depend on input shapes, using `add_weight()`, or other state.
*   `build(self, input_shape)`: This method can be used to create weights that depend on the shape(s) of the input(s), using `add_weight()`, or other state. `__call__()` will automatically build the layer (if it has not been built yet) by calling `build()`.
*   `call(self, *args, **kwargs)`: Called in `__call__` after making sure `build()` has been called. `call()` performs the logic of applying the layer to the input arguments. Two reserved keyword arguments you can optionally use in `call()` are: 1. `training` (boolean, whether the call is in inference mode or training mode). 2. `mask` (boolean tensor encoding masked timesteps in the input, used e.g. in RNN layers). A typical signature for this method is `call(self, inputs)`, and user could optionally add `training` and `mask` if the layer need them.
*   `get_config(self)`: Returns a dictionary containing the configuration used to initialize this layer. If the keys differ from the arguments in `__init__()`, then override `from_config(self)` as well. This method is used when saving the layer or a model that contains this layer.

#### Examples:

Here's a basic example: a layer with two variables, `w` and `b`, that returns `y = w . x + b`. It shows how to implement `build()` and `call()`. Variables set as attributes of a layer are tracked as weights of the layers (in `layer.weights`).

class SimpleDense(Layer):
        def __init__(self, units=32):
            super().__init__()
            self.units = units
    
        # Create the state of the layer (weights)
        def build(self, input_shape):
            self.kernel = self.add_weight(
                shape=(input_shape[-1], self.units),
                initializer="glorot_uniform",
                trainable=True,
                name="kernel",
            )
            self.bias = self.add_weight(
                shape=(self.units,),
                initializer="zeros",
                trainable=True,
                name="bias",
            )
    
        # Defines the computation
        def call(self, inputs):
            return ops.matmul(inputs, self.kernel) + self.bias
    
    # Instantiates the layer.
    linear_layer = SimpleDense(4)
    
    # This will also call `build(input_shape)` and create the weights.
    y = linear_layer(ops.ones((2, 2)))
    assert len(linear_layer.weights) == 2
    
    # These weights are trainable, so they're listed in `trainable_weights`:
    assert len(linear_layer.trainable_weights) == 2

Besides trainable weights, updated via backpropagation during training, layers can also have non-trainable weights. These weights are meant to be updated manually during `call()`. Here's a example layer that computes the running sum of its inputs:

class ComputeSum(Layer):
    
      def __init__(self, input_dim):
          super(ComputeSum, self).__init__()
          # Create a non-trainable weight.
          self.total = self.add_weight(
            shape=(),
            initializer="zeros",
            trainable=False,
            name="total",
          )
    
      def call(self, inputs):
          self.total.assign(self.total + ops.sum(inputs))
          return self.total
    
    my_sum = ComputeSum(2)
    x = ops.ones((2, 2))
    y = my_sum(x)
    
    assert my_sum.weights == [my_sum.total]
    assert my_sum.non_trainable_weights == [my_sum.total]
    assert my_sum.trainable_weights == []

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | The name of the layer (string). |
| `dtype` | Dtype of the layer's weights. Alias of `layer.variable_dtype`. |
| `variable_dtype` | Dtype of the layer's weights. |
| `compute_dtype` | The dtype of the layer's computations. Layers automatically cast inputs to this dtype, which causes the computations and output to also be in this dtype. When mixed precision is used with a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br>, this will be different than `variable_dtype`. |
| `trainable_weights` | List of variables to be included in backprop. |
| `non_trainable_weights` | List of variables that should not be included in backprop. |
| `weights` | The concatenation of the lists trainable\_weights and non\_trainable\_weights (in this order). |
| `trainable` | Whether the layer should be trained (boolean), i.e. whether its potentially-trainable weights should be returned as part of `layer.trainable_weights`. |
| `input_spec` | Optional (list of) `InputSpec` object(s) specifying the constraints on inputs that can be accepted by the layer. |
| `dtype_policy` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `input_dtype` | The dtype layer inputs should be converted to. |
| `losses` | List of scalar losses from `add_loss`, regularizers and sublayers. |
| `metrics` | List of all metrics. |
| `metrics_variables` | List of all metric variables. |
| `non_trainable_variables` | List of all non-trainable layer state.<br><br>This extends `layer.non_trainable_weights` to include all state used by the layer including state for metrics and `SeedGenerator`s. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `path` | The path of the layer.<br><br>If the layer has not been built yet, it will be `None`. |
| `quantization_mode` | The quantization mode of this layer, `None` if not quantized. |
| `supports_masking` | Whether this layer supports computing a mask using `compute_mask`. |
| `trainable_variables` | List of all trainable layer state.<br><br>This is equivalent to `layer.trainable_weights`. |
| `variables` | List of all layer state, including random seeds.<br><br>This extends `layer.weights` to include all state used by the layer including `SeedGenerator`s.<br><br>Note that metrics variables are not included here, use `metrics_variables` to visit all the metric variables. |

Methods
-------

### `add_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1255-L1283)

add_loss(
        loss
    )

Can be called inside of the `call()` method to add a scalar loss.

#### Example:

class MyLayer(Layer):
        ...
        def call(self, x):
            self.add_loss(ops.sum(x))
            return x

### `add_metric`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1513-L1521)

add_metric(
        *args, **kwargs
    )

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L498-L522)

add_variable(
        shape,
        initializer,
        dtype=None,
        trainable=True,
        autocast=True,
        regularizer=None,
        constraint=None,
        name=None
    )

Add a weight variable to the layer.

Alias of `add_weight()`.

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L524-L636)

add_weight(
        *args,
        shape=None,
        initializer=None,
        dtype=None,
        trainable=True,
        autocast=True,
        regularizer=None,
        constraint=None,
        aggregation='none',
        overwrite_with_gradient=False,
        name=None
    )

Add a weight variable to the layer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape tuple for the variable. Must be fully-defined (no `None` entries). Defaults to `()` (scalar) if unspecified. |
| `initializer` | Initializer object to use to populate the initial variable value, or string name of a built-in initializer (e.g. `"random_normal"`). If unspecified, defaults to `"glorot_uniform"` for floating-point variables and to `"zeros"` for all other types (e.g. int, bool). |
| `dtype` | Dtype of the variable to create, e.g. `"float32"`. If unspecified, defaults to the layer's variable dtype (which itself defaults to `"float32"` if unspecified). |
| `trainable` | Boolean, whether the variable should be trainable via backprop or whether its updates are managed manually. Defaults to `True`. |
| `autocast` | Boolean, whether to autocast layers variables when accessing them. Defaults to `True`. |
| `regularizer` | Regularizer object to call to apply penalty on the weight. These penalties are summed into the loss function during optimization. Defaults to `None`. |
| `constraint` | Contrainst object to call on the variable after any optimizer update, or string name of a built-in constraint. Defaults to `None`. |
| `aggregation` | Optional string, one of `None`, `"none"`, `"mean"`, `"sum"` or `"only_first_replica"`. Annotates the variable with the type of multi-replica aggregation to be used for this variable when writing custom data parallel training loops. Defaults to `"none"`. |
| `overwrite_with_gradient` | Boolean, whether to overwrite the variable with the computed gradient. This is useful for float8 training. Defaults to `False`. |
| `name` | String name of the variable. Useful for debugging purposes. |

### `build`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L427-L439)

build(
        input_shape
    )

### `build_from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L478-L493)

build_from_config(
        config
    )

Builds the layer's states with the supplied config dict.

By default, this method calls the `build(config["input_shape"])` method, which creates weights based on the layer's input shape in the supplied config. If your config contains other information needed to load the layer's state, you should override this method.

|     |     |
| --- | --- |
| Args |     |
| `config` | Dict containing the input shape associated with this layer. |

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1062-L1063)

call(
        *args, **kwargs
    )

### `compute_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L864-L866)

compute_mask(
        inputs, previous_mask
    )

### `compute_output_shape`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1248-L1253)

compute_output_shape(
        *args, **kwargs
    )

### `compute_output_spec`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1202-L1246)

compute_output_spec(
        *args, **kwargs
    )

### `count_params`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1523-L1537)

count_params()

Count the total number of scalars composing the weights.

|     |
| --- |
| Returns |     |
| An integer count. |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_build_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L454-L476)

get_build_config()

Returns a dictionary with the layer's input shape.

This method returns a config dict that can be used by `build_from_config(config)` to create all states (e.g. Variables and Lookup tables) needed by the layer.

By default, the config only contains the input shape that the layer was built with. If you're writing a custom layer that creates state in an unusual way, you should override this method to make sure this state is already created when Keras attempts to load its value upon model loading.

|     |
| --- |
| Returns |     |
| A dict containing the input shape associated with the layer. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1743-L1755)

get_config()

Returns the config of the object.

An object config is a Python dictionary (serializable) containing the information needed to re-instantiate it.

### `get_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L770-L772)

get_weights()

Return the values of `layer.weights` as a list of NumPy arrays.

### `load_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1482-L1494)

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

### `quantize`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1343-L1344)

quantize(
        mode=None, type_check=True, config=None
    )

### `quantized_build`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1340-L1341)

quantized_build(
        input_shape, mode
    )

### `quantized_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1373-L1398)

quantized_call(
        *args, **kwargs
    )

### `rematerialized_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1770-L1801)

rematerialized_call(
        layer_call, *args, **kwargs
    )

Enable rematerialization dynamically for layer's call method.

|     |     |
| --- | --- |
| Args |     |
| `layer_call` | The original `call` method of a layer. |

|     |
| --- |
| Returns |     |
| Rematerialized layer's `call` method. |     |

### `save_own_variables`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1435-L1446)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L774-L790)

set_weights(
        weights
    )

Sets the values of `layer.weights` from a list of NumPy arrays.

### `stateless_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L1088-L1200)

stateless_call(
        trainable_variables,
        non_trainable_variables,
        *args,
        return_losses=False,
        **kwargs
    )

Call the layer without any side effects.

|     |     |
| --- | --- |
| Args |     |
| `trainable_variables` | List of trainable variables of the model. |
| `non_trainable_variables` | List of non-trainable variables of the model. |
| `*args` | Positional arguments to be passed to `call()`. |
| `return_losses` | If `True`, `stateless_call()` will return the list of losses created during `call()` as part of its return values. |
| `**kwargs` | Keyword arguments to be passed to `call()`. |

|     |
| --- |
| Returns |     |
| A tuple. By default, returns `(outputs, non_trainable_variables)`. If `return_losses = True`, then returns `(outputs, non_trainable_variables, losses)`. |     |

#### Example:

model = ...
    data = ...
    trainable_variables = model.trainable_variables
    non_trainable_variables = model.non_trainable_variables
    # Call the model with zero side effects
    outputs, non_trainable_variables = model.stateless_call(
        trainable_variables,
        non_trainable_variables,
        data,
    )
    # Attach the updated state to the model
    # (until you do this, the model is still in its pre-call state).
    for ref_var, value in zip(
        model.non_trainable_variables, non_trainable_variables
    ):
        ref_var.assign(value)

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L868-L870)

symbolic_call(
        *args, **kwargs
    )

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/layer.py#L872-L1060)

__call__(
        *args, **kwargs
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.