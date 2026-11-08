[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.conv1d\_transpose Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L2169-L2257)

The transpose of `conv1d`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.conv1d_transpose`](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose)

tf.nn.conv1d_transpose(
        input,
        filters,
        output_shape,
        strides,
        padding='SAME',
        data_format='NWC',
        dilations=None,
        name=None
    )

This operation is sometimes called "deconvolution" after (Zeiler et al., 2010), but is actually the transpose (gradient) of `conv1d` rather than an actual deconvolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A 3-D `Tensor` of type `float` and shape `[batch, in_width, in_channels]` for `NWC` data format or `[batch, in_channels, in_width]` for `NCW` data format. |
| `filters` | A 3-D `Tensor` with the same type as `input` and shape `[filter_width, output_channels, in_channels]`. `filter`'s `in_channels` dimension must match that of `input`. |
| `output_shape` | A 1-D `Tensor`, containing three elements, representing the output shape of the deconvolution op. |
| `strides` | An int or list of `ints` that has length `1` or `3`. The number of entries by which the filter is moved right at each step. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A string. `'NWC'` and `'NCW'` are supported. |
| `dilations` | An int or list of `ints` that has length `1` or `3` which defaults to 1. The dilation factor for each dimension of input. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. Dilations in the batch and depth dimensions must be 1. |
| `name` | Optional name for the returned tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `input`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If input/output depth does not match `filter`'s shape, if `output_shape` is not at 3-element vector, if `padding` is other than `'VALID'` or `'SAME'`, or if `data_format` is invalid. |

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