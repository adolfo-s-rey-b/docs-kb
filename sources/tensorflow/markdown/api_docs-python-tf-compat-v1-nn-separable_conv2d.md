[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Fseparable_conv2d&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.separable\_conv2d Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/separable_conv2d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L902-L1007)

2-D convolution with separable filters.

tf.compat.v1.nn.separable_conv2d(
        input,
        depthwise_filter,
        pointwise_filter,
        strides,
        padding,
        rate=None,
        name=None,
        data_format=None,
        dilations=None
    )

Performs a depthwise convolution that acts separately on channels followed by a pointwise convolution that mixes channels. Note that this is separability between dimensions `[1, 2]` and `3`, not spatial separability between dimensions `1` and `2`.

In detail, with the default NHWC format,

output[b, i, j, k] = sum_{di, dj, q, r}
        input[b, strides[1] * i + di, strides[2] * j + dj, q] *
        depthwise_filter[di, dj, q, r] *
        pointwise_filter[0, 0, q * channel_multiplier + r, k]

`strides` controls the strides for the depthwise convolution only, since the pointwise convolution has implicit strides of `[1, 1, 1, 1]`. Must have `strides[0] = strides[3] = 1`. For the most common case of the same horizontal and vertical strides, `strides = [1, stride, stride, 1]`. If any value in `rate` is greater than 1, we perform atrous depthwise convolution, in which case all values in the `strides` tensor must be equal to 1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | 4-D `Tensor` with shape according to `data_format`. |
| `depthwise_filter` | 4-D `Tensor` with shape `[filter_height, filter_width, in_channels, channel_multiplier]`. Contains `in_channels` convolutional filters of depth 1. |
| `pointwise_filter` | 4-D `Tensor` with shape `[1, 1, channel_multiplier * in_channels, out_channels]`. Pointwise filter to mix channels after `depthwise_filter` has convolved spatially. |
| `strides` | 1-D of size 4. The strides for the depthwise convolution for each dimension of `input`. |
| `padding` | Controls how to pad the image before applying the depthwise convolution. Can be the string `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a Python list indicating the explicit paddings at the start and end of each dimension. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. |
| `rate` | 1-D of size 2. The dilation rate in which we sample input values across the `height` and `width` dimensions in atrous convolution. If it is greater than 1, then all values of strides must be 1. |
| `name` | A name for this operation (optional). |
| `data_format` | The data format for input. Either "NHWC" (default) or "NCHW". |
| `dilations` | Alias of rate. |

|     |
| --- |
| Returns<br>------- |     |
| A 4-D `Tensor` with shape according to 'data\_format'. For example, with data\_format="NHWC", shape is \[batch, out\_height, out\_width, out\_channels\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.