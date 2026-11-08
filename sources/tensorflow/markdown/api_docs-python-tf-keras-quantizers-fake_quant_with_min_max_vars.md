[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.fake\_quant\_with\_min\_max\_vars Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/fake_quant_with_min_max_vars#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L430-L578)

Perform per-tensor or per-channel fake quantization.

tf.keras.quantizers.fake_quant_with_min_max_vars(
        inputs, min_vals, max_vals, num_bits=8, narrow_range=False, axis=None
    )

`[min_vals, max_vals]` define the clamping range for the `inputs`.

The `inputs` are quantized into the quantization range:

*   `[0, 2^num_bits - 1]` when `narrow_range=False`
*   `[1, 2^num_bits - 1]` when `narrow_range=True`

After quantization, the values are dequantized and output as floats within the `[min_vals, max_vals]` interval.

This operation supports gradient computation, allowing `min_vals` and `max_vals` to be trained.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Input Keras tensor of float dtype. |
| `min_vals` | A global minimum scalar or a per-channel minimum tensor. |
| `max_vals` | A global maximum scalar or a per-channel maximum tensor. |
| `num_bits` | Quantization bit width (e.g., `8` for int8). Defaults to `8`. |
| `narrow_range` | Whether to use narrow quantization range. Defaults to `False`. |
| `axis` | Axis along which to perform per-channel quantization. If `None`, per-tensor quantization is performed. Defaults to `None`. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Tensor` | A Keras tensor with fake quantization applied. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.