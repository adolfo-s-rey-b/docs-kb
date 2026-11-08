[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ZeroPadding2D Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding2D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/zero_padding2d.py#L9-L119)

Zero-padding layer for 2D input (e.g. picture).

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ZeroPadding2D(
        padding=(1, 1), data_format=None, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference) | *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

This layer can add rows and columns of zeros at the top, bottom, left and right side of an image tensor.

#### Example:

    input_shape = (1, 1, 2, 2)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `padding` | Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.<br><br>*   If int: the same symmetric padding is applied to height and width.<br>*   If tuple of 2 ints: interpreted as two different symmetric padding values for height and width: `(symmetric_height_pad, symmetric_width_pad)`.<br>*   If tuple of 2 tuples of 2 ints: interpreted as `((top_pad, bottom_pad), (left_pad, right_pad))`. |
| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

|     |
| --- |
| Input shape<br>----------- |     |
| 4D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, height, width, channels)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, channels, height, width)` |     |

|     |
| --- |
| Output shape<br>------------ |     |
| 4D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, padded_height, padded_width, channels)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, channels, padded_height, padded_width)` |     |

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