[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.dilation2d Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/dilation2d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L482-L550)

Computes the grayscale dilation of 4-D `input` and 3-D `filters` tensors.

tf.nn.dilation2d(
        input, filters, strides, padding, data_format, dilations, name=None
    )

The `input` tensor has shape `[batch, in_height, in_width, depth]` and the `filters` tensor has shape `[filter_height, filter_width, depth]`, i.e., each input channel is processed independently of the others with its own structuring function. The `output` tensor has shape `[batch, out_height, out_width, depth]`. The spatial dimensions of the output tensor depend on the `padding` algorithm. We currently only support the default "NHWC" `data_format`.

In detail, the grayscale morphological 2-D dilation is the max-sum correlation (for consistency with `conv2d`, we use unmirrored filters):

output[b, y, x, c] =
       max_{dy, dx} input[b,\
                          strides[1] * y + rates[1] * dy,\
                          strides[2] * x + rates[2] * dx,\
                          c] +
                    filters[dy, dx, c]

Max-pooling is a special case when the filter has size equal to the pooling kernel size and contains all zeros.

Note on duality: The dilation of `input` by the `filters` is equal to the negation of the erosion of `-input` by the reflected `filters`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. 4-D with shape `[batch, in_height, in_width, depth]`. |
| `filters` | A `Tensor`. Must have the same type as `input`. 3-D with shape `[filter_height, filter_width, depth]`. |
| `strides` | A list of `ints` that has length `>= 4`. The stride of the sliding window for each dimension of the input tensor. Must be: `[1, stride_height, stride_width, 1]`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A `string`, only `"NHWC"` is currently supported. |
| `dilations` | A list of `ints` that has length `>= 4`. The input stride for atrous morphological dilation. Must be: `[1, rate_height, rate_width, 1]`. |
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