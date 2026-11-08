[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fquantization%2Ffake_quant_with_min_max_vars_per_channel&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.fake\_quant\_with\_min\_max\_vars\_per\_channel Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel#returns)
    

Fake-quantize the 'inputs' tensor of type float via per-channel floats

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.fake_quant_with_min_max_vars_per_channel`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel)
, [`tf.compat.v1.quantization.fake_quant_with_min_max_vars_per_channel`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel)

tf.quantization.fake_quant_with_min_max_vars_per_channel(
        inputs: Annotated[Any, _atypes.Float32],
        min: Annotated[Any, _atypes.Float32],
        max: Annotated[Any, _atypes.Float32],
        num_bits: int = 8,
        narrow_range: bool = False,
        name=None
    ) -> Annotated[Any, _atypes.Float32]

Fake-quantize the `inputs` tensor of type float per-channel and one of the shapes: `[d]`, `[b, d]` `[b, h, w, d]` via per-channel floats `min` and `max` of shape `[d]` to `outputs` tensor of same shape as `inputs`.

Attributes

*   `[min; max]` define the clamping range for the `inputs` data.
*   `inputs` values are quantized into the quantization range ( `[0; 2^num_bits - 1]` when `narrow_range` is false and `[1; 2^num_bits - 1]` when it is true) and then de-quantized and output as floats in `[min; max]` interval.
*   `num_bits` is the bitwidth of the quantization; between 2 and 16, inclusive.

Before quantization, `min` and `max` values are adjusted with the following logic. It is suggested to have `min <= 0 <= max`. If `0` is not in the range of values, the behavior can be unexpected:

*   If `0 < min < max`: `min_adj = 0` and `max_adj = max - min`.
*   If `min < max < 0`: `min_adj = min - max` and `max_adj = 0`.
*   If `min <= 0 <= max`: `scale = (max - min) / (2^num_bits - 1)`, `min_adj = scale * round(min / scale)` and `max_adj = max + min_adj - min`.

This operation has a gradient and thus allows for training `min` and `max` values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A `Tensor` of type `float32`. |
| `min` | A `Tensor` of type `float32`. |
| `max` | A `Tensor` of type `float32`. |
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