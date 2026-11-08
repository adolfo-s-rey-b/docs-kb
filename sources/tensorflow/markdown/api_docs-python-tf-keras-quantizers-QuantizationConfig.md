[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fquantizers%2FQuantizationConfig&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#methods)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#activation_quantizer_or_default)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#weight_quantizer_or_default)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.QuantizationConfig Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#methods)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#activation_quantizer_or_default)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig#weight_quantizer_or_default)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L6-L62)

Base class for quantization configs.

tf.keras.quantizers.QuantizationConfig(
        weight_quantizer=None, activation_quantizer=None
    )

Subclasses must implement the `mode` property and the `get_config` and `from_config` class methods.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weight_quantizer` | Quantizer for weights. |
| `activation_quantizer` | Quantizer for activations. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L39-L50)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L29-L37)

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