[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.quantization.fake\_quant\_with\_min\_max\_args\_gradient Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient#returns)
    

Compute gradients for a FakeQuantWithMinMaxArgs operation.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.fake_quant_with_min_max_args_gradient`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)
, [`tf.compat.v1.quantization.fake_quant_with_min_max_args_gradient`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)

tf.quantization.fake_quant_with_min_max_args_gradient(
        gradients: Annotated[Any, _atypes.Float32],
        inputs: Annotated[Any, _atypes.Float32],
        min: float = -6,
        max: float = 6,
        num_bits: int = 8,
        narrow_range: bool = False,
        name=None
    ) -> Annotated[Any, _atypes.Float32]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `gradients` | A `Tensor` of type `float32`. Backpropagated gradients above the FakeQuantWithMinMaxArgs operation. |
| `inputs` | A `Tensor` of type `float32`. Values passed as inputs to the FakeQuantWithMinMaxArgs operation. |
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