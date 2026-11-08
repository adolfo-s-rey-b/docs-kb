[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.conv2d Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L2260-L2364)

Computes a 2-D convolution given `input` and 4-D `filters` tensors.

tf.nn.conv2d(
        input,
        filters,
        strides,
        padding,
        data_format='NHWC',
        dilations=None,
        name=None
    )

The `input` tensor may have rank `4` or higher, where shape dimensions `[:-3]` are considered batch dimensions (`batch_shape`).

Given an input tensor of shape `batch_shape + [in_height, in_width, in_channels]` and a filter / kernel tensor of shape `[filter_height, filter_width, in_channels, out_channels]`, this op performs the following:

1.  Flattens the filter to a 2-D matrix with shape `[filter_height * filter_width * in_channels, output_channels]`.
2.  Extracts image patches from the input tensor to form a _virtual_ tensor of shape `[batch, out_height, out_width, filter_height * filter_width * in_channels]`.
3.  For each patch, right-multiplies the filter matrix and the image patch vector.

In detail, with the default NHWC format,

output[b, i, j, k] =
        sum_{di, dj, q} input[b, strides[1] * i + di, strides[2] * j + dj, q] *
                        filter[di, dj, q, k]

Must have `strides[0] = strides[3] = 1`. For the most common case of the same horizontal and vertical strides, `strides = [1, stride, stride, 1]`.

#### Usage Example:

    x_in = np.array([[\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. A Tensor of rank at least 4. The dimension order is interpreted according to the value of `data_format`; with the all-but-inner-3 dimensions acting as batch dimensions. See below for details. |\
| `filters` | A `Tensor`. Must have the same type as `input`. A 4-D tensor of shape `[filter_height, filter_width, in_channels, out_channels]` |\
| `strides` | An int or list of `ints` that has length `1`, `2` or `4`. The stride of the sliding window for each dimension of `input`. If a single value is given it is replicated in the `H` and `W` dimension. By default the `N` and `C` dimensions are set to 1. The dimension order is determined by the value of `data_format`, see below for details. |\
| `padding` | Either the `string` `"SAME"` or `"VALID"` indicating the type of padding algorithm to use, or a list indicating the explicit paddings at the start and end of each dimension. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. When explicit padding is used and data\_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used and data\_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`. |\
| `data_format` | An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`. Specify the data format of the input and output data. With the default format "NHWC", the data is stored in the order of: `batch_shape + [height, width, channels]`. Alternatively, the format could be "NCHW", the data storage order of: `batch_shape + [channels, height, width]`. |\
| `dilations` | An int or list of `ints` that has length `1`, `2` or `4`, defaults to 1. The dilation factor for each dimension of`input`. If a single value is given it is replicated in the `H` and `W` dimension. By default the `N` and `C` dimensions are set to 1. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions if a 4-d tensor must be 1. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `input` and the same outer batch shape. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.