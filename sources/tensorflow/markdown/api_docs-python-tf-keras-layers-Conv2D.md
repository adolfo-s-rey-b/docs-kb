[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FConv2D&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#methods)
    *   [convolution\_op](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#convolution_op)
        
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Conv2D Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#methods)
    *   [convolution\_op](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#convolution_op)
        
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/conv2d.py#L5-L137)

2D convolution layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.Convolution2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D)

tf.keras.layers.Conv2D(
        filters,
        kernel_size,
        strides=(1, 1),
        padding='valid',
        data_format=None,
        dilation_rate=(1, 1),
        groups=1,
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

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference) | *   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Image classification](https://www.tensorflow.org/tutorials/images/classification)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

This layer creates a convolution kernel that is convolved with the layer input over a 2D spatial (or temporal) dimension (height and width) to produce a tensor of outputs. If `use_bias` is True, a bias vector is created and added to the outputs. Finally, if `activation` is not `None`, it is applied to the outputs as well.

Note on numerical precision: While in general Keras operation execution results are identical across backends up to 1e-7 precision in float32, `Conv2D` operations may show larger variations. Due to the large number of element-wise multiplications and additions in convolution operations, especially with large inputs or kernel sizes, accumulated floating-point differences can exceed this 1e-7 threshold. These variations are particularly noticeable when using different backends (e.g., TensorFlow vs JAX) or different hardware.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filters` | int, the dimension of the output space (the number of filters in the convolution). |
| `kernel_size` | int or tuple/list of 2 integer, specifying the size of the convolution window. |
| `strides` | int or tuple/list of 2 integer, specifying the stride length of the convolution. `strides > 1` is incompatible with `dilation_rate > 1`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input. When `padding="same"` and `strides=1`, the output has the same size as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `dilation_rate` | int or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. |
| `groups` | A positive int specifying the number of groups in which the input is split along the channel axis. Each group is convolved separately with `filters // groups` filters. The output is the concatenation of all the `groups` results along the channel axis. Input channels and `filters` must both be divisible by `groups`. |
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

*   If `data_format="channels_last"`: A 4D tensor with shape: `(batch_size, height, width, channels)`
*   If `data_format="channels_first"`: A 4D tensor with shape: `(batch_size, channels, height, width)`

#### Output shape:

*   If `data_format="channels_last"`: A 4D tensor with shape: `(batch_size, new_height, new_width, filters)`
*   If `data_format="channels_first"`: A 4D tensor with shape: `(batch_size, filters, new_height, new_width)`

|     |
| --- |
| Returns<br>------- |     |
| A 4D tensor representing `activation(conv2d(inputs, kernel) + bias)`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | when both `strides > 1` and `dilation_rate > 1`. |

#### Example:

    x = np.random.rand(4, 10, 10, 128)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `kernel` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convolution_op`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/base_conv.py#L245-L253)

convolution_op(
        inputs, kernel
    )

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/convolutional/base_conv.py#L280-L325)

enable_lora(
        rank,
        lora_alpha=None,
        a_initializer='he_uniform',
        b_initializer='zeros'
    )

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