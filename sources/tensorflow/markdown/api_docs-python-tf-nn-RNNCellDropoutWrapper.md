[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#add_loss)
        
    *   [add\_metric](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#add_metric)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#build)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#compute_output_shape)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_initial_state)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#set_weights)
        
    *   [zero\_state](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#zero_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.RNNCellDropoutWrapper Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#add_loss)
        
    *   [add\_metric](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#add_metric)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#build)
        
    *   [compute\_mask](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#compute_mask)
        
    *   [compute\_output\_shape](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#compute_output_shape)
        
    *   [count\_params](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#count_params)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_initial_state)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#set_weights)
        
    *   [zero\_state](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#zero_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/nn/RNNCellDropoutWrapper#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L94-L107)

Operator adding dropout to inputs and outputs of the given cell. (deprecated)

Inherits From: [`Module`](https://www.tensorflow.org/api_docs/python/tf/Module)

tf.nn.RNNCellDropoutWrapper(
        *args, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cell` | an RNNCell, a projection to output\_size is added to it. |
| `input_keep_prob` | unit Tensor or float between 0 and 1, input keep probability; if it is constant and 1, no input dropout will be added. |
| `output_keep_prob` | unit Tensor or float between 0 and 1, output keep probability; if it is constant and 1, no output dropout will be added. |
| `state_keep_prob` | unit Tensor or float between 0 and 1, output keep probability; if it is constant and 1, no output dropout will be added. State dropout is performed on the outgoing states of the cell. **Note** the state components to which dropout is applied when `state_keep_prob` is in `(0, 1)` are also determined by the argument `dropout_state_filter_visitor` (e.g. by default dropout is never applied to the `c` component of an `LSTMStateTuple`). |
| `variational_recurrent` | Python bool. If `True`, then the same dropout pattern is applied across all time steps per run call. If this parameter is set, `input_size` **must** be provided. |
| `input_size` | (optional) (possibly nested tuple of) `TensorShape` objects containing the depth(s) of the input tensors expected to be passed in to the `DropoutWrapper`. Required and used **iff** `variational_recurrent = True` and `input_keep_prob < 1`. |
| `dtype` | (optional) The `dtype` of the input, state, and output tensors. Required and used **iff** `variational_recurrent = True`. |
| `seed` | (optional) integer, the randomness seed. |
| `dropout_state_filter_visitor` | (optional), default: (see below). Function that takes any hierarchical level of the state and returns a scalar or depth=1 structure of Python booleans describing which terms in the state should be dropped out. In addition, if the function returns `True`, dropout is applied across this sublevel. If the function returns `False`, dropout is not applied across this entire sublevel. Default behavior: perform dropout on all terms except the memory (`c`) state of `LSTMCellState` objects, and don't try to apply dropout to `TensorArray` objects: `def dropout_state_filter_visitor(s): if isinstance(s, LSTMCellState): # Never perform dropout on the c state. return LSTMCellState(c=False, h=True) elif isinstance(s, TensorArray): return False return True` |
| `**kwargs` | dict of keyword arguments for base layer. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `cell` is not an `RNNCell`, or `keep_state_fn` is provided but not `callable`. |
| `ValueError` | if any of the keep\_probs are not between 0 and 1. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `activity_regularizer` | Optional regularizer function for the output of this layer. |
| `compute_dtype` | The dtype of the layer's computations.<br><br>This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless mixed precision is used, this is the same as [`Layer.dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#dtype)<br>, the dtype of the weights.<br><br>Layers automatically cast their inputs to the compute dtype, which causes computations and the output to be in the compute dtype as well. This is done by the base Layer class in [`Layer.**call**`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#__call__)<br>, so you do not have to insert these casts if implementing your own layer.<br><br>Layers often perform certain internal computations in higher precision when `compute_dtype` is float16 or bfloat16 for numeric stability. The output will still typically be float16 or bfloat16 in such cases. |
| `dtype` | The dtype of the layer weights.<br><br>This is equivalent to `Layer.dtype_policy.variable_dtype`. Unless mixed precision is used, this is the same as [`Layer.compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#compute_dtype)<br>, the dtype of the layer's computations. |
| `dtype_policy` | The dtype policy associated with this layer.<br><br>This is an instance of a [`tf.keras.mixed_precision.Policy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br>. |
| `dynamic` | Whether the layer is dynamic (eager-only); set in the constructor. |
| `input` | Retrieves the input tensor(s) of a layer.<br><br>Only applicable if the layer has exactly one input, i.e. if it is connected to one incoming layer. |
| `input_spec` | `InputSpec` instance(s) describing the input format for this layer.<br><br>When you create a layer subclass, you can set `self.input_spec` to enable the layer to run input compatibility checks when it is called. Consider a `Conv2D` layer: it can only be called on a single input tensor of rank 4. As such, you can set, in `__init__()`:<br><br>self.input_spec = tf.keras.layers.InputSpec(ndim=4)<br><br>Now, if you try to call the layer on an input that isn't rank 4 (for instance, an input of shape `(2,)`, it will raise a nicely-formatted error:<br><br>ValueError: Input 0 of layer conv2d is incompatible with the layer:<br>    expected ndim=4, found ndim=1. Full shape received: [2]<br><br>Input checks that can be specified via `input_spec` include:<br><br>*   Structure (e.g. a single input, a list of 2 inputs, etc)<br>*   Shape<br>*   Rank (ndim)<br>*   Dtype<br><br>For more information, see [`tf.keras.layers.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>. |
| `losses` | List of losses added using the `add_loss()` API.<br><br>Variable regularization tensors are created when this property is accessed, so it is eager safe: accessing `losses` under a [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)<br> will propagate gradients back to the corresponding variables.<br><br>    class MyLayer(tf.keras.layers.Layer):<br><br>    inputs = tf.keras.Input(shape=(10,))<br><br>    inputs = tf.keras.Input(shape=(10,)) |
| `metrics` | List of metrics added using the `add_metric()` API.<br><br>    input = tf.keras.layers.Input(shape=(3,)) |
| `non_trainable_weights` | List of all non-trainable weights tracked by this layer.<br><br>Non-trainable weights are _not_ updated during training. They are expected to be updated manually in `call()`. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only applicable if the layer has exactly one output, i.e. if it is connected to one incoming layer. |
| `output_size` |     |
| `state_size` |     |
| `supports_masking` | Whether this layer supports computing a mask using `compute_mask`. |
| `trainable` |     |
| `trainable_weights` | List of all trainable weights tracked by this layer.<br><br>Trainable weights are updated via gradient descent during training. |
| `variable_dtype` | Alias of [`Layer.dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#dtype)<br>, the dtype of the weights. |
| `weights` | Returns the list of all layer variables/weights. |
| `wrapped_cell` |     |

Methods
-------

### `add_loss`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L1411-L1531)

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

This method can also be called directly on a Functional Model during construction. In this case, any loss Tensors passed to this Model must be symbolic and be able to be traced back to the model's `Input`s. These losses become part of the model's topology and are tracked in `get_config`.

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
| `**kwargs` | Additional keyword arguments for backward compatibility. Accepted values: inputs - Deprecated, will be automatically inferred. |

### `add_metric`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L1566-L1685)

add_metric(
        value, name=None, **kwargs
    )

Adds metric tensor to the layer.

This method can be used inside the `call()` method of a subclassed layer or model.

class MyMetricLayer(tf.keras.layers.Layer):
      def __init__(self):
        super(MyMetricLayer, self).__init__(name='my_metric_layer')
        self.mean = tf.keras.metrics.Mean(name='metric_1')
    
      def call(self, inputs):
        self.add_metric(self.mean(inputs))
        self.add_metric(tf.reduce_sum(inputs), name='metric_2')
        return inputs

This method can also be called directly on a Functional Model during construction. In this case, any tensor passed to this Model must be symbolic and be able to be traced back to the model's `Input`s. These metrics become part of the model's topology and are tracked when you save the model via `save()`.

inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    model.add_metric(math_ops.reduce_sum(x), name='metric_1')

inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    model.add_metric(tf.keras.metrics.Mean()(x), name='metric_1')

|     |     |
| --- | --- |
| Args |     |
| `value` | Metric tensor. |
| `name` | String metric name. |
| `**kwargs` | Additional keyword arguments for backward compatibility. Accepted values: `aggregation` - When the `value` tensor provided is not the result of calling a [`keras.Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)<br> instance, it will be aggregated by default using a `keras.Metric.Mean`. |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L194-L196)

build(
        inputs_shape
    )

### `compute_mask`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L909-L929)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L755-L798)

compute_output_shape(
        input_shape
    )

Computes the output shape of the layer.

If the layer has not been built, this method will call `build` on the layer. This assumes that the layer will later be used with inputs that match the input shape provided here.

|     |     |
| --- | --- |
| Args |     |
| `input_shape` | Shape tuple (tuple of integers) or list of shape tuples (one per output tensor of the layer). Shape tuples can include None for free dimensions, instead of an integer. |

|     |
| --- |
| Returns |     |
| An input shape tuple. |     |

### `count_params`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L2130-L2149)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L307-L317)

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

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L288-L305)

get_config()

Returns the config of the dropout wrapper.

### `get_initial_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/recurrent.py#L1089-L1090)

get_initial_state(
        inputs=None, batch_size=None, dtype=None
    )

### `get_weights`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L1809-L1851)

get_weights()

Returns the current weights of the layer, as NumPy arrays.

The weights of a layer represent the state of the layer. This function returns both trainable and non-trainable weight values associated with this layer as a list of NumPy arrays, which can in turn be used to load state into similarly parameterized layers.

For example, a `Dense` layer returns a list of two values: the kernel matrix and the bias vector. These can be used to set the weights of another `Dense` layer:

    layer_a = tf.keras.layers.Dense(1,

|     |
| --- |
| Returns |     |
| Weights values as a list of NumPy arrays. |     |

### `set_weights`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L1724-L1807)

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

### `zero_state`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py#L198-L200)

zero_state(
        batch_size, dtype
    )

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/engine/base_layer.py#L931-L1052)

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

Last updated 2026-10-31 UTC.