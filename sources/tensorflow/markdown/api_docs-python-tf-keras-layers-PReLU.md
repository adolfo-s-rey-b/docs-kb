[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FPReLU&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.PReLU Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/PReLU#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/prelu.py#L10-L98)

Parametric Rectified Linear Unit activation layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.PReLU(
        alpha_initializer='Zeros',
        alpha_regularizer=None,
        alpha_constraint=None,
        shared_axes=None,
        **kwargs
    )

#### Formula:

f(x) = alpha * x for x < 0
    f(x) = x for x >= 0

where `alpha` is a learned array with the same shape as x.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `alpha_initializer` | Initializer function for the weights. |
| `alpha_regularizer` | Regularizer for the weights. |
| `alpha_constraint` | Constraint for the weights. |
| `shared_axes` | The axes along which to share learnable parameters for the activation function. For example, if the incoming feature maps are from a 2D convolution with output shape `(batch, height, width, channels)`, and you wish to share parameters across space so that each filter only has one set of parameters, set `shared_axes=[1, 2]`. |
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