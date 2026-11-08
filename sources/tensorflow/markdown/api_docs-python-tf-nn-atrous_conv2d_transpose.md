[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fatrous_conv2d_transpose&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.atrous\_conv2d\_transpose Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L2814-L2976)

The transpose of `atrous_conv2d`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.atrous_conv2d_transpose`](https://www.tensorflow.org/api_docs/python/tf/nn/atrous_conv2d_transpose)

tf.nn.atrous_conv2d_transpose(
        value, filters, output_shape, rate, padding, name=None
    )

This operation is sometimes called "deconvolution" after (Zeiler et al., 2010), but is really the transpose (gradient) of `atrous_conv2d` rather than an actual deconvolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A 4-D `Tensor` of type `float`. It needs to be in the default `NHWC` format. Its shape is `[batch, in_height, in_width, in_channels]`. |
| `filters` | A 4-D `Tensor` with the same type as `value` and shape `[filter_height, filter_width, out_channels, in_channels]`. `filters`' `in_channels` dimension must match that of `value`. Atrous convolution is equivalent to standard convolution with upsampled filters with effective height `filter_height + (filter_height - 1) * (rate - 1)` and effective width `filter_width + (filter_width - 1) * (rate - 1)`, produced by inserting `rate - 1` zeros along consecutive elements across the `filters`' spatial dimensions. |
| `output_shape` | A 1-D `Tensor` of shape representing the output shape of the deconvolution op, of form `[batch, out_height, out_width, out_channels]`. |
| `rate` | A positive int32. The stride with which we sample input values across the `height` and `width` dimensions. Equivalently, the rate by which we upsample the filter values by inserting zeros across the `height` and `width` dimensions. In the literature, the same parameter is sometimes called `input stride` or `dilation`. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `name` | Optional name for the returned tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If input/output depth does not match `filters`' shape, or if padding is other than `'VALID'` or `'SAME'`, or if the `rate` is less than one, or if the output\_shape is not a tensor with 4 elements. |

|     |
| --- |
| References<br>---------- |     |
| Deconvolutional Networks: [Zeiler et al., 2010](https://ieeexplore.ieee.org/abstract/document/5539957)<br> ([pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.