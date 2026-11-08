[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.avg\_pool3d Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4668-L4706)

Performs the average pooling on the input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.avg_pool3d`](https://www.tensorflow.org/api_docs/python/tf/nn/avg_pool3d)

tf.nn.avg_pool3d(
        input, ksize, strides, padding, data_format='NDHWC', name=None
    )

Each entry in `output` is the mean of the corresponding size `ksize` window in `value`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A 5-D `Tensor` of shape `[batch, depth, height, width, channels]` and type `float32`, `float64`, `qint8`, `quint8`, or `qint32`. |
| `ksize` | An int or list of `ints` that has length `1`, `3` or `5`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `3` or `5`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)<br> for more information. |
| `data_format` | A string. 'NDHWC' and 'NCDHW' are supported. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `value`. The average pooled output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.