[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.UpSampling3D Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/UpSampling3D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/up_sampling3d.py#L9-L134)

Upsampling layer for 3D inputs.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.UpSampling3D(
        size=(2, 2, 2), data_format=None, **kwargs
    )

Repeats the 1st, 2nd and 3rd dimensions of the data by `size[0]`, `size[1]` and `size[2]` respectively.

#### Example:

    input_shape = (2, 1, 2, 1, 3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `size` | Int, or tuple of 3 integers. The upsampling factors for dim1, dim2 and dim3. |
| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists) else `"channels_last"`. Defaults to `"channels_last"`. |

|     |
| --- |
| Input shape<br>----------- |     |
| 5D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, dim1, dim2, dim3, channels)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, channels, dim1, dim2, dim3)` |     |

|     |
| --- |
| Output shape<br>------------ |     |
| 5D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, upsampled_dim1, upsampled_dim2, upsampled_dim3, channels)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, channels, upsampled_dim1, upsampled_dim2, upsampled_dim3)` |     |

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