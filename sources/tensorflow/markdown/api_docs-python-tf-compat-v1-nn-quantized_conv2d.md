[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.quantized\_conv2d Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_conv2d#returns)
    

Computes a 2D convolution given quantized 4D input and filter tensors.

tf.compat.v1.nn.quantized_conv2d(
        input: Annotated[Any, TV_QuantizedConv2D_Tinput],
        filter: Annotated[Any, TV_QuantizedConv2D_Tfilter],
        min_input: Annotated[Any, _atypes.Float32],
        max_input: Annotated[Any, _atypes.Float32],
        min_filter: Annotated[Any, _atypes.Float32],
        max_filter: Annotated[Any, _atypes.Float32],
        strides,
        padding: str,
        out_type: TV_QuantizedConv2D_out_type = tf.dtypes.qint32,
        dilations=[1, 1, 1, 1],
        name=None
    )

The inputs are quantized tensors where the lowest value represents the real number of the associated minimum, and the highest represents the maximum. This means that you can only interpret the quantized output in the same way, by taking the returned minimum and maximum values into account.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. |
| `filter` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. filter's input\_depth dimension must match input's depth dimensions. |
| `min_input` | A `Tensor` of type `float32`. The float value that the lowest quantized input value represents. |
| `max_input` | A `Tensor` of type `float32`. The float value that the highest quantized input value represents. |
| `min_filter` | A `Tensor` of type `float32`. The float value that the lowest quantized filter value represents. |
| `max_filter` | A `Tensor` of type `float32`. The float value that the highest quantized filter value represents. |
| `strides` | A list of `ints`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `out_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to [`tf.qint32`](https://www.tensorflow.org/api_docs/python/tf#qint32)<br>. |
| `dilations` | An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D tensor of length 4. The dilation factor for each dimension of `input`. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. Dilations in the batch and depth dimensions must be 1. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (output, min\_output, max\_output). |     |
| `output` | A `Tensor` of type `out_type`. |
| `min_output` | A `Tensor` of type `float32`. |
| `max_output` | A `Tensor` of type `float32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.