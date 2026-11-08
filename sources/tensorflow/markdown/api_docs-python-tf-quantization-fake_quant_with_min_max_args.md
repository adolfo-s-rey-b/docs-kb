[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fquantization%2Ffake_quant_with_min_max_args&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.fake\_quant\_with\_min\_max\_args Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args#returns)
    

Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same shape and type.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.fake_quant_with_min_max_args`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args)
, [`tf.compat.v1.quantization.fake_quant_with_min_max_args`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args)

tf.quantization.fake_quant_with_min_max_args(
        inputs: Annotated[Any, _atypes.Float32],
        min: float = -6,
        max: float = 6,
        num_bits: int = 8,
        narrow_range: bool = False,
        name=None
    ) -> Annotated[Any, _atypes.Float32]

Quantization is called fake since the output is still in floating point. The API converts inputs into values within the range \[min and max\] and returns as output.

Attributes

*   `[min; max]` define the clamping range for the `inputs` data.
*   `inputs` values are quantized into the quantization range ( `[0; 2^num_bits - 1]` when `narrow_range` is false and `[1; 2^num_bits - 1]` when it is true) and then de-quantized and output as floats in `[min; max]` interval.
*   `num_bits` is the bitwidth of the quantization; between 2 and 16, inclusive.

Before quantization, `min` and `max` values are adjusted with the following logic. It is suggested to have `min <= 0 <= max`. If `0` is not in the range of values, the behavior can be unexpected:

*   If `0 < min < max`: `min_adj = 0` and `max_adj = max - min`.
*   If `min < max < 0`: `min_adj = min - max` and `max_adj = 0`.
*   If `min <= 0 <= max`: `scale = (max - min) / (2^num_bits - 1)`, `min_adj = scale * round(min / scale)` and `max_adj = max + min_adj - min`.

Examples

inp = tf.constant ([10.03, -10.23, 3])
    out = tf.quantization.fake_quant_with_min_max_args(inp, min=-5, max=5,
                                                       num_bits=16)
    print(out)
    
    #  Output:
    #  tf.Tensor([ 4.9999237 -5.0000763  3.0000763], shape=(3,), dtype=float32)

|     |
| --- |
| Raises<br>------ |     |
| *   InvalidArgumentError:<br>    *   If num\_bits are outside of range \[2, 16\].<br>    *   If min >= max.<br>*   ValueError: If `inputs` are of any other type than float32. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A `Tensor` of type `float32`. |
| `min` | An optional `float`. Defaults to `-6`. |
| `max` | An optional `float`. Defaults to `6`. |
| `num_bits` | An optional `int`. Defaults to `8`. |
| `narrow_range` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.