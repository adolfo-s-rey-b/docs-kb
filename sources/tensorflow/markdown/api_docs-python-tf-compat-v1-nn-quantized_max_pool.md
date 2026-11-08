[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Fquantized_max_pool&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.quantized\_max\_pool Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_max_pool#returns)
    

Produces the max pool of the input tensor for quantized types.

tf.compat.v1.nn.quantized_max_pool(
        input: Annotated[Any, TV_QuantizedMaxPool_T],
        min_input: Annotated[Any, _atypes.Float32],
        max_input: Annotated[Any, _atypes.Float32],
        ksize,
        strides,
        padding: str,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. The 4D (batch x rows x cols x depth) Tensor to MaxReduce over. |
| `min_input` | A `Tensor` of type `float32`. The float value that the lowest quantized input value represents. |
| `max_input` | A `Tensor` of type `float32`. The float value that the highest quantized input value represents. |
| `ksize` | A list of `ints`. The size of the window for each dimension of the input tensor. The length must be 4 to match the number of dimensions of the input. |
| `strides` | A list of `ints`. The stride of the sliding window for each dimension of the input tensor. The length must be 4 to match the number of dimensions of the input. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (output, min\_output, max\_output). |     |
| `output` | A `Tensor`. Has the same type as `input`. |
| `min_output` | A `Tensor` of type `float32`. |
| `max_output` | A `Tensor` of type `float32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.