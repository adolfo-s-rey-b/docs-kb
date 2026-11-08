[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Dot Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dot#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/dot.py#L198-L357)

Computes element-wise dot product of two tensors.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Dot(
        axes, normalize=False, **kwargs
    )

It takes a list of inputs of size 2, and the axes corresponding to each input along with the dot product is to be performed.

Let's say `x` and `y` are the two input tensors with shapes `(2, 3, 5)` and `(2, 10, 3)`. The batch dimension should be of same size for both the inputs, and `axes` should correspond to the dimensions that have the same size in the corresponding inputs. e.g. with `axes=(1, 2)`, the dot product of `x`, and `y` will result in a tensor with shape `(2, 5, 10)`

#### Example:

    x = np.arange(10).reshape(1, 5, 2)

Usage in a Keras model:

    x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axes` | Integer or tuple of integers, axis or axes along which to take the dot product. If a tuple, should be two integers corresponding to the desired axis from the first input and the desired axis from the second input, respectively. Note that the size of the two selected axes must match, and that axis `0` (the batch axis) cannot be included. |
| `normalize` | Whether to L2-normalize samples along the dot product axis before taking the dot product. If set to `True`, then the output of the dot product is the cosine proximity between the two samples. |
| `**kwargs` | Standard layer keyword arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, the dot product of the samples from the inputs. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
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