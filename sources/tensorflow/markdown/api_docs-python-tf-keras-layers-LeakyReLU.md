[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.LeakyReLU Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LeakyReLU#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/leaky_relu.py#L8-L67)

Leaky version of a Rectified Linear Unit activation layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.LeakyReLU(
        negative_slope=0.3, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Customizing what happens in \`fit()\`](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit) | *   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

This layer allows a small gradient when the unit is not active.

#### Formula:

f(x) = alpha * x if x < 0
    f(x) = x if x >= 0

#### Example:

leaky_relu_layer = LeakyReLU(negative_slope=0.5)
    input = np.array([-10, -5, 0.0, 5, 10])
    result = leaky_relu_layer(input)
    # result = [-5. , -2.5,  0. ,  5. , 10.]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `negative_slope` | Float >= 0.0. Negative slope coefficient. Defaults to `0.3`. |
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