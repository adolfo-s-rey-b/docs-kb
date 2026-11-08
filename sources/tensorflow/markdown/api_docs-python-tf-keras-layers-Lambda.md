[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Lambda Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/lambda_layer.py#L12-L241)

Wraps arbitrary expressions as a `Layer` object.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Lambda(
        function, output_shape=None, mask=None, arguments=None, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [TensorFlow basics](https://www.tensorflow.org/guide/basics) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation)<br>    <br>*   [Graph regularization for document classification using natural graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_mlp_cora)<br>    <br>*   [Using TensorFlow Recommenders with TFX](https://www.tensorflow.org/recommenders/examples/ranking_tfx)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning) |

The `Lambda` layer exists so that arbitrary expressions can be used as a `Layer` when constructing Sequential and Functional API models. `Lambda` layers are best suited for simple operations or quick experimentation. For more advanced use cases, prefer writing new subclasses of `Layer`.

The main reason to subclass `Layer` instead of using a `Lambda` layer is saving and inspecting a model. `Lambda` layers are saved by serializing the Python bytecode, which is fundamentally non-portable and potentially unsafe. They should only be loaded in the same environment where they were saved. Subclassed layers can be saved in a more portable way by overriding their `get_config()` method. Models that rely on subclassed Layers are also often easier to visualize and reason about.

#### Example:

# add a x -> x^2 layer
    model.add(Lambda(lambda x: x ** 2))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `function` | The function to be evaluated. Takes input tensor as first argument. |
| `output_shape` | Expected output shape from function. This argument can usually be inferred if not explicitly provided. Can be a tuple or function. If a tuple, it only specifies the first dimension onward; sample dimension is assumed either the same as the input: `output_shape = (input_shape[0], ) + output_shape` or, the input is `None` and the sample dimension is also `None`: `output_shape = (None, ) + output_shape`. If a function, it specifies the entire shape as a function of the input shape: `output_shape = f(input_shape)`. |
| `mask` | Either None (indicating no masking) or a callable with the same signature as the `compute_mask` layer method, or a tensor that will be returned as output mask regardless of what the input is. |
| `arguments` | Optional dictionary of keyword arguments to be passed to the function. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/lambda_layer.py#L182-L241)

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