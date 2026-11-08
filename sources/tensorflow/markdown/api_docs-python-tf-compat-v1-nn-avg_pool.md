[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Favg_pool&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.avg\_pool Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L4535-L4577)

Performs the average pooling on the input.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.avg_pool2d`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/avg_pool)

tf.compat.v1.nn.avg_pool(
        value,
        ksize,
        strides,
        padding,
        data_format='NHWC',
        name=None,
        input=None
    )

Each entry in `output` is the mean of the corresponding size `ksize` window in `value`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A 4-D `Tensor` of shape `[batch, height, width, channels]` and type `float32`, `float64`, `qint8`, `quint8`, or `qint32`. |
| `ksize` | An int or list of `ints` that has length `1`, `2` or `4`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `2` or `4`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See the "returns" section of [`tf.nn.convolution`](https://www.tensorflow.org/api_docs/python/tf/nn/convolution)<br> for details. |
| `data_format` | A string. 'NHWC' and 'NCHW' are supported. |
| `name` | Optional name for the operation. |
| `input` | Alias for value. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `value`. The average pooled output tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.