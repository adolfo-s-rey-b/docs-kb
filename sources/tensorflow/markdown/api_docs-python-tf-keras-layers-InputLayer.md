[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.InputLayer Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/input_layer.py#L9-L142)

This is the class from which all layers inherit.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.InputLayer(
        shape=None,
        batch_size=None,
        dtype=None,
        sparse=None,
        ragged=None,
        batch_shape=None,
        input_tensor=None,
        optional=False,
        name=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference) | *   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Post-training dynamic range quantization](https://www.tensorflow.org/lite/performance/post_training_quant)<br>    <br>*   [Retraining an Image Classifier](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining)<br>    <br>*   [Federated Learning for Image Classification](https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification) |

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
| `batch_shape` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

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

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.