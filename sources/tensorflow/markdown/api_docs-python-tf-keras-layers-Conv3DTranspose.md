[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Conv3DTranspose Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/conv3d_transpose.py#L5-L152)

3D transposed convolution layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Convolution3DTranspose`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3DTranspose)

tf.keras.layers.Conv3DTranspose(
        filters,
        kernel_size,
        strides=(1, 1, 1),
        padding='valid',
        data_format=None,
        output_padding=None,
        dilation_rate=(1, 1, 1),
        activation=None,
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    )

The need for transposed convolutions generally arise from the desire to use a transformation going in the opposite direction of a normal convolution, i.e., from something that has the shape of the output of some convolution to something that has the shape of its input while maintaining a connectivity pattern that is compatible with said convolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filters` | int, the dimension of the output space (the number of filters in the transposed convolution). |
| `kernel_size` | int or tuple/list of 1 integer, specifying the size of the transposed convolution window. |
| `strides` | int or tuple/list of 1 integer, specifying the stride length of the transposed convolution. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. output\_padding: An integer or tuple/list of 3 integers, specifying the amount of padding along the depth, height, and width. Can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a given dimension must be lower than the stride along that same dimension. If set to `None` (default), the output shape is inferred. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | an integer or tuple/list of 3 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any `dilation_rate` value != 1 is incompatible with specifying any stride value != 1. |
| `activation` | Activation function. If `None`, no activation is applied. |
| `use_bias` | bool, if `True`, bias will be added to the output. |
| `kernel_initializer` | Initializer for the convolution kernel. If `None`, the default initializer (`"glorot_uniform"`) will be used. |
| `bias_initializer` | Initializer for the bias vector. If `None`, the default initializer (`"zeros"`) will be used. |
| `kernel_regularizer` | Optional regularizer for the convolution kernel. |
| `bias_regularizer` | Optional regularizer for the bias vector. |
| `activity_regularizer` | Optional regularizer function for the output. |
| `kernel_constraint` | Optional projection function to be applied to the kernel after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `bias_constraint` | Optional projection function to be applied to the bias after being updated by an `Optimizer`. |

#### Input shape:

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

#### Output shape:

*   If `data_format="channels_last"`: 5D tensor with shape: `(batch_size, new_spatial_dim1, new_spatial_dim2, new_spatial_dim3, filters)`
*   If `data_format="channels_first"`: 5D tensor with shape: `(batch_size, filters, new_spatial_dim1, new_spatial_dim2, new_spatial_dim3)`

|     |
| --- |
| Returns<br>------- |     |
| A 5D tensor representing `activation(conv3d(inputs, kernel) + bias)`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | when both `strides > 1` and `dilation_rate > 1`. |

#### References:

*   [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285v1)
    
*   [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
    

#### Example:

    x = np.random.rand(4, 10, 8, 12, 128)

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