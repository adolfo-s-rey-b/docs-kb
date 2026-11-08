[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FGaussianDropout&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.GaussianDropout Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GaussianDropout#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/regularization/gaussian_dropout.py#L9-L64)

Apply multiplicative 1-centered Gaussian noise.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.GaussianDropout(
        rate, seed=None, **kwargs
    )

As it is a regularization layer, it is only active at training time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `rate` | Float, drop probability (as with `Dropout`). The multiplicative noise will have standard deviation `sqrt(rate / (1 - rate))`. |
| `seed` | Integer, optional random seed to enable deterministic behavior. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | Input tensor (of any rank). |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing). |

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