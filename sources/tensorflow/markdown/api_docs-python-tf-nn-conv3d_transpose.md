[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.conv3d\_transpose Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#returns)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3347-L3418)

The transpose of `conv3d`.

tf.nn.conv3d_transpose(
        input,
        filters,
        output_shape,
        strides,
        padding='SAME',
        data_format='NDHWC',
        dilations=None,
        name=None
    )

This operation is sometimes called "deconvolution" after (Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d` rather than an actual deconvolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A 5-D `Tensor` of type `float` and shape `[batch, depth, height, width, in_channels]` for `NDHWC` data format or `[batch, in_channels, depth, height, width]` for `NCDHW` data format. |
| `filters` | A 5-D `Tensor` with the same type as `input` and shape `[depth, height, width, output_channels, in_channels]`. `filter`'s `in_channels` dimension must match that of `input`. |
| `output_shape` | A 1-D `Tensor` representing the output shape of the deconvolution op. |
| `strides` | An int or list of `ints` that has length `1`, `3` or `5`. The stride of the sliding window for each dimension of `input`. If a single value is given it is replicated in the `D`, `H` and `W` dimension. By default the `N` and `C` dimensions are set to 0. The dimension order is determined by the value of `data_format`, see below for details. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A string. 'NDHWC' and 'NCDHW' are supported. |
| `dilations` | An int or list of `ints` that has length `1`, `3` or `5`, defaults to 1. The dilation factor for each dimension of`input`. If a single value is given it is replicated in the `D`, `H` and `W` dimension. By default the `N` and `C` dimensions are set to 1. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions if a 5-d tensor must be 1. |
| `name` | Optional name for the returned tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `input`. |     |

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