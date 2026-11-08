[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.depthwise\_conv2d Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L801-L896)

Depthwise 2-D convolution.

tf.nn.depthwise_conv2d(
        input,
        filter,
        strides,
        padding,
        data_format=None,
        dilations=None,
        name=None
    )

Given a 4D input tensor ('NHWC' or 'NCHW' data formats) and a filter tensor of shape `[filter_height, filter_width, in_channels, channel_multiplier]` containing `in_channels` convolutional filters of depth 1, `depthwise_conv2d` applies a different filter to each input channel (expanding from 1 channel to `channel_multiplier` channels for each), then concatenates the results together. The output has `in_channels * channel_multiplier` channels.

In detail, with the default NHWC format,

output[b, i, j, k * channel_multiplier + q] =
        sum_{di, dj} filter[di, dj, k, q] *
                     input[b, strides[1] * i + dilations[0] * di,\
                              strides[2] * j + dilations[1] * dj, k]

Must have `strides[0] = strides[3] = 1`. For the most common case of the same horizontal and vertical strides, `strides = [1, stride, stride, 1]`. If any value in `dilations` is greater than 1, we perform atrous depthwise convolution, in which case all values in the `strides` tensor must be equal to 1.

#### Usage Example:

    x = np.array([\
\
    tf.nn.depthwise_conv2d(x, kernel, strides=[1, 1, 1, 1],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | 4-D with shape according to `data_format`. |\
| `filter` | 4-D with shape `[filter_height, filter_width, in_channels, channel_multiplier]`. |\
| `strides` | 1-D of size 4. The stride of the sliding window for each dimension of `input`. |\
| `padding` | Controls how to pad the image before applying the convolution. Can be the string `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. |\
| `data_format` | The data format for input. Either "NHWC" (default) or "NCHW". |\
| `dilations` | 1-D of size 2. The dilation rate in which we sample input values across the `height` and `width` dimensions in atrous convolution. If it is greater than 1, then all values of strides must be 1. |\
| `name` | A name for this operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A 4-D `Tensor` with shape according to `data_format`. E.g., for "NHWC" format, shape is `[batch, out_height, out_width, in_channels * channel_multiplier].` |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-04 UTC.