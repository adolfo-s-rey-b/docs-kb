[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.dequantize Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L5920-L5951)

Dequantize the 'input' tensor into a float or bfloat16 Tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.dequantize`](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize)
, [`tf.compat.v1.quantization.dequantize`](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize)

tf.quantization.dequantize(
        input,
        min_range,
        max_range,
        mode='MIN_COMBINED',
        name=None,
        axis=None,
        narrow_range=False,
        dtype=tf.dtypes.float32
    )

\[min\_range, max\_range\] are scalar floats that specify the range for the output. The 'mode' attribute controls exactly which calculations are used to convert the float values to their quantized equivalents.

In 'MIN\_COMBINED' mode, each value of the tensor will undergo the following:

if T == qint8: in[i] += (range(T) + 1)/ 2.0
    out[i] = min_range + (in[i]* (max_range - min_range) / range(T))

here `range(T) = numeric_limits<T>::max() - numeric_limits<T>::min()`

_MIN\_COMBINED Mode Example_

If the input comes from a QuantizedRelu6, the output type is quint8 (range of 0-255) but the possible range of QuantizedRelu6 is 0-6. The min\_range and max\_range values are therefore 0.0 and 6.0. Dequantize on quint8 will take each value, cast to float, and multiply by 6 / 255. Note that if quantizedtype is qint8, the operation will additionally add each value by 128 prior to casting.

If the mode is 'MIN\_FIRST', then this approach is used:

num_discrete_values = 1 << (# of bits in T)
    range_adjust = num_discrete_values / (num_discrete_values - 1)
    range = (range_max - range_min) * range_adjust
    range_scale = range / num_discrete_values
    const double offset_input = static_cast<double>(input) - lowest_quantized;
    result = range_min + ((input - numeric_limits<T>::min()) * range_scale)

If the mode is `SCALED`, dequantization is performed by multiplying each input value by a scaling\_factor. (Thus an input of 0 always maps to 0.0).

The scaling\_factor is determined from `min_range`, `max_range`, and `narrow_range` in a way that is compatible with `QuantizeAndDequantize{V2|V3}` and `QuantizeV2`, using the following algorithm:

  const int min_expected_T = std::numeric_limits<T>::min() +
        (narrow_range ? 1 : 0);
      const int max_expected_T = std::numeric_limits<T>::max();
      const float max_expected_T = std::numeric_limits<float>::max();
    
      const float scale_factor =
        (std::numeric_limits<T>::min() == 0) ? (max_range / max_expected_T)
                                             : std::max(min_range / min_expected_T,
                                                        max_range / max_expected_T);

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. |
| `min_range` | A `Tensor` of type `float32`. The minimum scalar value possibly produced for the input. |
| `max_range` | A `Tensor` of type `float32`. The maximum scalar value possibly produced for the input. |
| `mode` | An optional `string` from: `"MIN_COMBINED", "MIN_FIRST", "SCALED"`. Defaults to `"MIN_COMBINED"`. |
| `narrow_range` | An optional `bool`. Defaults to `False`. |
| `axis` | An optional `int`. Defaults to `-1`. |
| `dtype` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.bfloat16, tf.float32`. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. Type of the output tensor. Currently Dequantize supports float and bfloat16. If 'dtype' is 'bfloat16', it only supports 'MIN\_COMBINED' mode. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `dtype`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.