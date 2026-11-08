[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.depthwise\_conv2d\_backprop\_filter Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3126-L3196)

Computes the gradients of depthwise convolution with respect to the filter.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.depthwise_conv2d_backprop_filter`](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter)
, [`tf.compat.v1.nn.depthwise_conv2d_native_backprop_filter`](https://www.tensorflow.org/api_docs/python/tf/nn/depthwise_conv2d_backprop_filter)

tf.nn.depthwise_conv2d_backprop_filter(
        input,
        filter_sizes,
        out_backprop,
        strides,
        padding,
        data_format='NHWC',
        dilations=[1, 1, 1, 1],
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. 4-D with shape based on `data_format`. For example, if `data_format` is 'NHWC' then `input` is a 4-D `[batch, in_height, in_width, in_channels]` tensor. |
| `filter_sizes` | A `Tensor` of type `int32`. An integer vector representing the tensor shape of `filter`, where `filter` is a 4-D `[filter_height, filter_width, in_channels, depthwise_multiplier]` tensor. |
| `out_backprop` | A `Tensor`. Must have the same type as `input`. 4-D with shape based on `data_format`. For example, if `data_format` is 'NHWC' then out\_backprop shape is `[batch, out_height, out_width, out_channels]`. Gradients w.r.t. the output of the convolution. |
| `strides` | A list of `ints`. The stride of the sliding window for each dimension of the input of the convolution. |
| `padding` | Controls how to pad the image before applying the convolution. Can be the string `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. |
| `data_format` | An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`. Specify the data format of the input and output data. With the default format "NHWC", the data is stored in the order of: \[batch, height, width, channels\]. Alternatively, the format could be "NCHW", the data storage order of: \[batch, channels, height, width\]. |
| `dilations` | An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D tensor of length 4. The dilation factor for each dimension of `input`. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions must be 1. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.