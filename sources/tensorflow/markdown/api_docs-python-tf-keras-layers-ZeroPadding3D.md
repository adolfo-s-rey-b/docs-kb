[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ZeroPadding3D Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ZeroPadding3D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/zero_padding3d.py#L9-L118)

Zero-padding layer for 3D data (spatial or spatio-temporal).

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ZeroPadding3D(
        padding=((1, 1), (1, 1), (1, 1)), data_format=None, **kwargs
    )

#### Example:

    input_shape = (1, 1, 2, 2, 3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `padding` | Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.<br><br>*   If int: the same symmetric padding is applied to depth, height, and width.<br>*   If tuple of 3 ints: interpreted as three different symmetric padding values for depth, height, and width: `(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad)`.<br>*   If tuple of 3 tuples of 2 ints: interpreted as `((left_dim1_pad, right_dim1_pad), (left_dim2_pad, right_dim2_pad), (left_dim3_pad, right_dim3_pad))`. |
| `data_format` | A string, one of `"channels_last"` (default) or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. When unspecified, uses `image_data_format` value found in your Keras config file at `~/.keras/keras.json` (if exists). Defaults to `"channels_last"`. |

|     |
| --- |
| Input shape<br>----------- |     |
| 5D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad, depth)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, depth, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad)` |     |

|     |
| --- |
| Output shape<br>------------ |     |
| 5D tensor with shape:<br><br>*   If `data_format` is `"channels_last"`: `(batch_size, first_padded_axis, second_padded_axis, third_axis_to_pad, depth)`<br>*   If `data_format` is `"channels_first"`: `(batch_size, depth, first_padded_axis, second_padded_axis, third_axis_to_pad)` |     |

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