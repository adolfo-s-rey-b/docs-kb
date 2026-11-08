[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fquantization%2Fquantize_and_dequantize&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.quantize\_and\_dequantize Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L5957-L6021)

Quantizes then dequantizes a tensor. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.quantization.quantize_and_dequantize`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize)

tf.quantization.quantize_and_dequantize(
        input,
        input_min,
        input_max,
        signed_input=True,
        num_bits=8,
        range_given=False,
        round_mode='HALF_TO_EVEN',
        name=None,
        narrow_range=False,
        axis=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` to quantize and dequantize. |
| `input_min` | If range\_given=True, the minimum input value, that needs to be represented in the quantized representation. If axis is specified, this should be a vector of minimum values for each slice along axis. |
| `input_max` | If range\_given=True, the maximum input value that needs to be represented in the quantized representation. If axis is specified, this should be a vector of maximum values for each slice along axis. |
| `signed_input` | True if the quantization is signed or unsigned. |
| `num_bits` | The bitwidth of the quantization. |
| `range_given` | If true use `input_min` and `input_max` for the range of the input, otherwise determine min and max from the input `Tensor`. |
| `round_mode` | Rounding mode when rounding from float values to quantized ones. one of \['HALF\_TO\_EVEN', 'HALF\_UP'\] |
| `name` | Optional name for the operation. |
| `narrow_range` | If true, then the absolute value of the quantized minimum value is the same as the quantized maximum value, instead of 1 greater. i.e. for 8 bit quantization, the minimum value is -127 instead of -128. |
| `axis` | Integer. If specified, refers to a dimension of the input tensor, such that quantization will be per slice along that dimension. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Each element is the result of quantizing and dequantizing the corresponding element of `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.