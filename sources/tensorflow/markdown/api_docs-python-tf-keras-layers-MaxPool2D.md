[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FMaxPool2D&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.MaxPool2D Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/max_pooling2d.py#L5-L109)

Max pooling operation for 2D spatial data.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.MaxPooling2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D)

tf.keras.layers.MaxPool2D(
        pool_size=(2, 2),
        strides=None,
        padding='valid',
        data_format=None,
        name=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Sparse weights using structural pruning](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | *   [Image classification](https://www.tensorflow.org/tutorials/images/classification)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation)<br>    <br>*   [Load and preprocess images](https://www.tensorflow.org/tutorials/load_data/images)<br>    <br>*   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Convolutional Neural Network (CNN)](https://www.tensorflow.org/tutorials/images/cnn) |

Downsamples the input along its spatial dimensions (height and width) by taking the maximum value over an input window (of size defined by `pool_size`) for each channel of the input. The window is shifted by `strides` along each dimension.

The resulting output when using the `"valid"` padding option has a spatial shape (number of rows or columns) of: `output_shape = math.floor((input_shape - pool_size) / strides) + 1` (when `input_shape >= pool_size`)

The resulting output shape when using the `"same"` padding option is: `output_shape = math.floor((input_shape - 1) / strides) + 1`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pool_size` | int or tuple of 2 integers, factors by which to downscale (dim1, dim2). If only one integer is specified, the same window length will be used for all dimensions. |
| `strides` | int or tuple of 2 integers, or None. Strides values. If None, it will default to `pool_size`. If only one int is specified, the same stride size will be used for all dimensions. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

#### Input shape:

*   If `data_format="channels_last"`: 4D tensor with shape `(batch_size, height, width, channels)`.
*   If `data_format="channels_first"`: 4D tensor with shape `(batch_size, channels, height, width)`.

#### Output shape:

*   If `data_format="channels_last"`: 4D tensor with shape `(batch_size, pooled_height, pooled_width, channels)`.
*   If `data_format="channels_first"`: 4D tensor with shape `(batch_size, channels, pooled_height, pooled_width)`.

#### Examples:

`strides=(1, 1)` and `padding="valid"`:

    x = np.array([[1., 2., 3.],\
\
`strides=(2, 2)` and `padding="valid"`:\
\
    x = np.array([[1., 2., 3., 4.],\
\
`stride=(1, 1)` and `padding="same"`:\
\
    x = np.array([[1., 2., 3.],\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
\
Methods\
-------\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)\
\
@classmethod\
\
Creates an operation from its config.\
\
This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.\
\
if "dtype" in config and isinstance(config["dtype"], dict):\
        policy = dtype_policies.deserialize(config["dtype"])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `config` | A Python dictionary, typically the output of `get_config`. |\
\
|     |\
| --- |\
| Returns |     |\
| An operation instance. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.