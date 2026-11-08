[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ReLU Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReLU#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/relu.py#L6-L87)

Rectified Linear Unit activation function layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ReLU(
        max_value=None, negative_slope=0.0, threshold=0.0, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference)<br>    <br>*   [Sparse weights using structural pruning](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

#### Formula:

f(x) = max(x,0)
    f(x) = max_value if x >= max_value
    f(x) = x if threshold <= x < max_value
    f(x) = negative_slope * (x - threshold) otherwise

#### Example:

relu_layer = keras.layers.ReLU(
        max_value=10,
        negative_slope=0.5,
        threshold=0,
    )
    input = np.array([-10, -5, 0.0, 5, 10])
    result = relu_layer(input)
    # result = [-5. , -2.5,  0. ,  5. , 10.]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_value` | Float >= 0. Maximum activation value. `None` means unlimited. Defaults to `None`. |
| `negative_slope` | Float >= 0. Negative slope coefficient. Defaults to `0.0`. |
| `threshold` | Float >= 0. Threshold value for thresholded activation. Defaults to `0.0`. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

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