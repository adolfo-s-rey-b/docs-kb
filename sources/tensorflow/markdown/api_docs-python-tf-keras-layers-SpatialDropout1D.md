[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#call-arguments)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#input-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.SpatialDropout1D Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#call-arguments)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#input-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout1D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/regularization/spatial_dropout.py#L31-L68)

Spatial 1D version of Dropout.

Inherits From: [`Dropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.SpatialDropout1D(
        rate, seed=None, name=None, dtype=None
    )

This layer performs the same function as Dropout, however, it drops entire 1D feature maps instead of individual elements. If adjacent frames within feature maps are strongly correlated (as is normally the case in early convolution layers) then regular dropout will not regularize the activations and will otherwise just result in an effective learning rate decrease. In this case, `SpatialDropout1D` will help promote independence between feature maps and should be used instead.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `rate` | Float between 0 and 1. Fraction of the input units to drop. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A 3D tensor. |
| `training` | Python boolean indicating whether the layer should behave in training mode (applying dropout) or in inference mode (pass-through). |

|     |
| --- |
| Input shape<br>----------- |     |
| 3D tensor with shape: `(samples, timesteps, channels)` |     |

Output shape: Same as input.

#### Reference:

*   [Tompson et al., 2014](https://arxiv.org/abs/1411.4280)
    

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