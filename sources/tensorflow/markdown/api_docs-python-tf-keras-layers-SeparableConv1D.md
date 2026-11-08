[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.SeparableConv1D Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/separable_conv1d.py#L5-L143)

1D separable convolution layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.SeparableConvolution1D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SeparableConv1D)

tf.keras.layers.SeparableConv1D(
        filters,
        kernel_size,
        strides=1,
        padding='valid',
        data_format=None,
        dilation_rate=1,
        depth_multiplier=1,
        activation=None,
        use_bias=True,
        depthwise_initializer='glorot_uniform',
        pointwise_initializer='glorot_uniform',
        bias_initializer='zeros',
        depthwise_regularizer=None,
        pointwise_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        depthwise_constraint=None,
        pointwise_constraint=None,
        bias_constraint=None,
        **kwargs
    )

This layer performs a depthwise convolution that acts separately on channels, followed by a pointwise convolution that mixes channels. If `use_bias` is True and a bias initializer is provided, it adds a bias vector to the output. It then optionally applies an activation function to produce the final output.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filters` | int, the dimensionality of the output space (i.e. the number of filters in the pointwise convolution). |
| `kernel_size` | int or tuple/list of 1 integers, specifying the size of the depthwise convolution window. |
| `strides` | int or tuple/list of 1 integers, specifying the stride length of the depthwise convolution. If only one int is specified, the same stride size will be used for all dimensions. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 1 integers, specifying the dilation rate to use for dilated convolution. If only one int is specified, the same dilation rate will be used for all dimensions. |
| `depth_multiplier` | The number of depthwise convolution output channels for each input channel. The total number of depthwise convolution output channels will be equal to `input_channel * depth_multiplier`. |
| `activation` | Activation function. If `None`, no activation is applied. |
| `use_bias` | bool, if `True`, bias will be added to the output. |
| `depthwise_initializer` | An initializer for the depthwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used. |
| `pointwise_initializer` | An initializer for the pointwise convolution kernel. If None, then the default initializer (`"glorot_uniform"`) will be used. |
| `bias_initializer` | An initializer for the bias vector. If None, the default initializer ('"zeros"') will be used. |
| `depthwise_regularizer` | Optional regularizer for the depthwise convolution kernel. |
| `pointwise_regularizer` | Optional regularizer for the pointwise convolution kernel. |
| `bias_regularizer` | Optional regularizer for the bias vector. |
| `activity_regularizer` | Optional regularizer function for the output. |
| `depthwise_constraint` | Optional projection function to be applied to the depthwise kernel after being updated by an `Optimizer` (e.g. used for norm constraints or value constraints for layer weights). The function must take as input the unprojected variable and must return the projected variable (which must have the same shape). |
| `pointwise_constraint` | Optional projection function to be applied to the pointwise kernel after being updated by an `Optimizer`. |
| `bias_constraint` | Optional projection function to be applied to the bias after being updated by an `Optimizer`. |

#### Input shape:

*   If `data_format="channels_last"`: A 3D tensor with shape: `(batch_shape, steps, channels)`
*   If `data_format="channels_first"`: A 3D tensor with shape: `(batch_shape, channels, steps)`

#### Output shape:

*   If `data_format="channels_last"`: A 3D tensor with shape: `(batch_shape, new_steps, filters)`
*   If `data_format="channels_first"`: A 3D tensor with shape: `(batch_shape, filters, new_steps)`

|     |
| --- |
| Returns<br>------- |     |
| A 3D tensor representing `activation(separable_conv1d(inputs, kernel) + bias)`. |     |

#### Example:

    x = np.random.rand(4, 10, 12)

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