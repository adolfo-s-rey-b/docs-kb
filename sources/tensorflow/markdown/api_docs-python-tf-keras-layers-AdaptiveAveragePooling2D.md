[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#output-shape)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#examples)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.AdaptiveAveragePooling2D Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#output-shape)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#examples)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AdaptiveAveragePooling2D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/adaptive_average_pooling2d.py#L9-L62)

Adaptive average pooling operation for 2D spatial data.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.AdaptiveAveragePooling2D(
        output_size, data_format=None, **kwargs
    )

This layer applies an adaptive average pooling operation, which pools the input such that the output has a target spatial size specified by `output_size`, regardless of the input spatial size. The kernel size and stride are automatically computed to achieve the target output size.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `output_size` | Integer or tuple of 2 integers specifying the target output size. If an integer, the same value is used for both height and width. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`. `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. Defaults to the value found in your Keras config file at `~/.keras/keras.json`. If never set, `"channels_last"` is used. |

|     |
| --- |
| Input shape<br>----------- |     |
| *   If `data_format="channels_last"`: 4D tensor `(batch_size, height, width, channels)`<br>*   If `data_format="channels_first"`: 4D tensor `(batch_size, channels, height, width)` |     |

|     |
| --- |
| Output shape<br>------------ |     |
| *   If `data_format="channels_last"`: `(batch_size, output_height, output_width, channels)`<br>*   If `data_format="channels_first"`: `(batch_size, channels, output_height, output_width)` |     |

|     |
| --- |
| Examples<br>-------- |     |
| >>> import numpy as np<br>    >>> input_img = np.random.rand(1, 64, 64, 3)<br>    >>> layer = AdaptiveAveragePooling2D(output_size=32)<br>    >>> output_img = layer(input_img)<br>    >>> output_img.shape<br>    (1, 32, 32, 3) |     |

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