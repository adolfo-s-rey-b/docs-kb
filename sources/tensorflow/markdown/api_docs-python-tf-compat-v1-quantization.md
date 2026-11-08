[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.quantization Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization#functions)
    

Public API for tf.\_api.v2.quantization namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/quantization/experimental)
 module: Public API for tf.\_api.v2.quantization.experimental namespace

Functions
---------

[`dequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/dequantize)
: Dequantize the 'input' tensor into a float or bfloat16 Tensor.

[`fake_quant_with_min_max_args(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args)
: Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same shape and type.

[`fake_quant_with_min_max_args_gradient(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)
: Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars)
: Fake-quantize the 'inputs' tensor of type float via global float scalars

[`fake_quant_with_min_max_vars_gradient(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_gradient)
: Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel)
: Fake-quantize the 'inputs' tensor of type float via per-channel floats

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient)
: Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`quantize(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize)
: Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantize_and_dequantize(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize)
: Quantizes then dequantizes a tensor. (deprecated)

[`quantize_and_dequantize_v2(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantize_and_dequantize_v2)
: Quantizes then dequantizes a tensor.

[`quantized_concat(...)`](https://www.tensorflow.org/api_docs/python/tf/quantization/quantized_concat)
: Concatenates quantized tensors along one dimension.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.