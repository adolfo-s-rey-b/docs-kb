[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fquantizers%2FInt8QuantizationConfig%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#activation_quantizer_or_default)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#weight_quantizer_or_default)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.Int8QuantizationConfig Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#methods_2)
    *   [activation\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#activation_quantizer_or_default)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#get_config)
        
    *   [weight\_quantizer\_or\_default](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/Int8QuantizationConfig?version=stable#weight_quantizer_or_default)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantization_config.py#L65-L91)

Int8 quantization config.

Inherits From: [`QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/QuantizationConfig)

tf.keras.quantizers.Int8QuantizationConfig(
        weight_quantizer=None, activation_quantizer='default'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `weight_quantizer` | Quantizer for weights. |
| `activation_quantizer` | Quantizer for activations. If "default", uses AbsMaxQuantizer with axis=-1. |

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