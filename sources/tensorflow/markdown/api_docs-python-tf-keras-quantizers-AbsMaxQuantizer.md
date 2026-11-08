[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.AbsMaxQuantizer Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/AbsMaxQuantizer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L307-L373)

Inherits From: [`Quantizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Quantizer)

tf.keras.quantizers.AbsMaxQuantizer(
        axis=None,
        value_range=(-127, 127),
        epsilon=backend.epsilon(),
        output_dtype='int8'
    )

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L28-L46)

@classmethod

Creates a quantizer from its config.

This method is the reverse of `get_config`, capable of instantiating the same quantizer from the config dictionary.

This method is used by Keras `model_to_estimator`, saving and loading models to HDF5 formats, Keras model cloning, some visualization utilities, and exporting models to and from JSON.

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of get\_config. |

|     |
| --- |
| Returns |     |
| A quantizer instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L365-L373)

get_config()

Returns the config of the quantizer.

A quantizer config is a Python dictionary (serializable) containing all configuration parameters of the quantizer. The same quantizer can be reinstantiated later (without any saved state) from this configuration.

This method is optional if you are just training and executing models, exporting to and from SavedModels, or using weight checkpoints.

This method is required for Keras `model_to_estimator`, saving and loading models to HDF5 formats, Keras model cloning, some visualization utilities, and exporting models to and from JSON.

|     |
| --- |
| Returns |     |
| Python dictionary. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L333-L363)

__call__(
        x, axis=None, to_numpy=False
    )

Quantizes the input tensor.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input tensor to quantize. |
| `axis` | Axis along which to compute the quantization range. If None, uses the axis specified in the constructor. If None and no axis was specified in the constructor, defaults to -1. |
| `to_numpy` | Whether to perform the quantization in numpy. This performs the computation on the host CPU and can be useful for saving memory on the device. If False, the computation is performed on the device. |

|     |
| --- |
| Returns |     |
| A tuple of the quantized tensor and the scale. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.