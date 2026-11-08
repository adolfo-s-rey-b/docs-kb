[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.erosion2d Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/erosion2d#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L6464-L6534)

Computes the grayscale erosion of 4-D `value` and 3-D `filters` tensors.

tf.nn.erosion2d(
        value, filters, strides, padding, data_format, dilations, name=None
    )

The `value` tensor has shape `[batch, in_height, in_width, depth]` and the `filters` tensor has shape `[filters_height, filters_width, depth]`, i.e., each input channel is processed independently of the others with its own structuring function. The `output` tensor has shape `[batch, out_height, out_width, depth]`. The spatial dimensions of the output tensor depend on the `padding` algorithm. We currently only support the default "NHWC" `data_format`.

In detail, the grayscale morphological 2-D erosion is given by:

output[b, y, x, c] =
       min_{dy, dx} value[b,\
                          strides[1] * y - dilations[1] * dy,\
                          strides[2] * x - dilations[2] * dx,\
                          c] -
                    filters[dy, dx, c]

Duality: The erosion of `value` by the `filters` is equal to the negation of the dilation of `-value` by the reflected `filters`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A `Tensor`. 4-D with shape `[batch, in_height, in_width, depth]`. |
| `filters` | A `Tensor`. Must have the same type as `value`. 3-D with shape `[filters_height, filters_width, depth]`. |
| `strides` | A list of `ints` that has length `>= 4`. 1-D of length 4. The stride of the sliding window for each dimension of the input tensor. Must be: `[1, stride_height, stride_width, 1]`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A `string`, only `"NHWC"` is currently supported. |
| `dilations` | A list of `ints` that has length `>= 4`. 1-D of length 4. The input stride for atrous morphological dilation. Must be: `[1, rate_height, rate_width, 1]`. |
| `name` | A name for the operation (optional). If not specified "erosion2d" is used. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `value`. 4-D with shape `[batch, out_height, out_width, depth]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the `value` depth does not match `filters`' shape, or if padding is other than `'VALID'` or `'SAME'`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.