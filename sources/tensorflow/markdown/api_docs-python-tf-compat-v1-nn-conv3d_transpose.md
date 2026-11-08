[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.conv3d\_transpose Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/conv3d_transpose#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3275-L3344)

The transpose of `conv3d`.

tf.compat.v1.nn.conv3d_transpose(
        value,
        filter=None,
        output_shape=None,
        strides=None,
        padding='SAME',
        data_format='NDHWC',
        name=None,
        input=None,
        filters=None,
        dilations=None
    )

This operation is sometimes called "deconvolution" after (Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d` rather than an actual deconvolution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A 5-D `Tensor` of type `float` and shape `[batch, depth, height, width, in_channels]`. |
| `filter` | A 5-D `Tensor` with the same type as `value` and shape `[depth, height, width, output_channels, in_channels]`. `filter`'s `in_channels` dimension must match that of `value`. |
| `output_shape` | A 1-D `Tensor` representing the output shape of the deconvolution op. |
| `strides` | A list of ints. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See the "returns" section of [`tf.nn.convolution`](https://www.tensorflow.org/api_docs/python/tf/nn/convolution)<br> for details. |
| `data_format` | A string, either `'NDHWC'` or `'NCDHW`' specifying the layout of the input and output tensors. Defaults to `'NDHWC'`. |
| `name` | Optional name for the returned tensor. |
| `input` | Alias of value. |
| `filters` | Alias of filter. |
| `dilations` | An int or list of `ints` that has length `1`, `3` or `5`, defaults to 1. The dilation factor for each dimension of`input`. If a single value is given it is replicated in the `D`, `H` and `W` dimension. By default the `N` and `C` dimensions are set to 1. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions if a 5-d tensor must be 1. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If input/output depth does not match `filter`'s shape, or if padding is other than `'VALID'` or `'SAME'`. |

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