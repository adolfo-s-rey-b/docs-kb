[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.space\_to\_depth Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L3606-L3662)

Rearranges blocks of spatial data into depth.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.space_to_depth`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/space_to_depth)

tf.keras.ops.space_to_depth(
        x, block_size, data_format='channels_last'
    )

This operation is useful for resizing the activations between convolutions (but keeping all data). It is also useful for training purely convolutional models.

This operation rearranges elements in a tensor of shape `(N, H * block_size, W * block_size, C)` to a tensor of shape `(N, H, W, C * block_size ** 2)` (for `data_format="channels_last"`) or `(N, C, H * block_size, W * block_size)` to `(N, C * block_size ** 2, H, W)` (for `data_format="channels_first"`).

This is the reverse transformation of `depth_to_space`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. Must be 4D. |
| `block_size` | An integer specifying the size of the spatial block. The height and width of the input must be divisible by `block_size`. |
| `data_format` | A string specifying the data format of the input tensor. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. Defaults to `"channels_last"`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same dtype as `x`, with shape `(N, H // block_size, W // block_size, C * block_size ** 2)` for `data_format="channels_last"` or `(N, C * block_size ** 2, H // block_size, W // block_size)` for `data_format="channels_first"`. |     |

#### Example:

    x = keras.ops.reshape(keras.ops.arange(1 * 4 * 4 * 3), (1, 4, 4, 3))

    # channels_first example

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.