[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fdepthwise_conv&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.depthwise\_conv Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L1585-L1648)

General N-D depthwise convolution.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.depthwise_conv`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/depthwise_conv)

tf.keras.ops.depthwise_conv(
        inputs,
        kernel,
        strides=1,
        padding='valid',
        data_format=None,
        dilation_rate=1
    )

This ops supports 1D and 2D depthwise convolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Tensor of rank N+2. `inputs` has shape `(batch_size,) + inputs_spatial_shape + (num_channels,)` if `data_format="channels_last"`, or `(batch_size, num_channels) + inputs_spatial_shape` if `data_format="channels_first"`. |
| `kernel` | Tensor of rank N+2. `kernel` has shape \[kernel\_spatial\_shape, num\_input\_channels, num\_channels\_multiplier\], `num_input_channels` should match the number of channels in `inputs`. |
| `strides` | int or int tuple/list of `len(inputs_spatial_shape)`, specifying the strides of the convolution along each spatial dimension. If `strides` is int, then every spatial dimension shares the same `strides`. |
| `padding` | string, either `"valid"` or `"same"`. `"valid"` means no padding is applied, and `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input when `strides=1`. |
| `data_format` | A string, either `"channels_last"` or `"channels_first"`. `data_format` determines the ordering of the dimensions in the inputs. If `data_format="channels_last"`, `inputs` is of shape `(batch_size, ..., channels)` while if `data_format="channels_first"`, `inputs` is of shape `(batch_size, channels, ...)`. |
| `dilation_rate` | int or int tuple/list of `len(inputs_spatial_shape)`, specifying the dilation rate to use for dilated convolution. If `dilation_rate` is int, then every spatial dimension shares the same `dilation_rate`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of rank N+2, the result of the depthwise conv operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.