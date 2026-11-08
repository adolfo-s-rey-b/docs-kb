[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int4QuantizationConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.Int4QuantizationConfig Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L94-L181)

Int4 quantization config.

Inherits From: [`QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig)

tf.keras.quantizers.Int4QuantizationConfig(
        weight_quantizer=None,
        activation_quantizer='default',
        block_size=128
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weight_quantizer` | Quantizer for weights. |
| `activation_quantizer` | Quantizer for activations. If "default", uses AbsMaxQuantizer with axis=-1. |
| `block_size` | Size of groups along the input dimension for sub-channel quantization. If a positive integer, uses sub-channel quantization with `ceil(input_dim / block_size)` groups. If `None` or `-1`, uses per-channel quantization (one scale per output channel). Default: `128` (sub-channel with 128-element groups). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `mode` |     |

Methods
-------

### `activation_quantizer_or_default`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L58-L62)

@staticmethod

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L166-L181)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L161-L164)

get_config()

### `weight_quantizer_or_default`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L52-L56)

@staticmethod

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.