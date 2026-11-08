[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdtype_policies%2FAWQDTypePolicy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.dtype\_policies.AWQDTypePolicy Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/AWQDTypePolicy#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L452-L536)

Quantized dtype policy for AWQ quantization.

Inherits From: [`QuantizedDTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/QuantizedDTypePolicy)
, [`DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)

tf.keras.dtype_policies.AWQDTypePolicy(
        mode, source_name=None
    )

This policy helps propagate quantization settings for AWQ when loading an AWQ quantized model in Keras format.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | The quantization mode. This should be a string in the format `"awq/<weight_bits>/<group_size>"`.<br><br>*   `"awq"`: The identifier for the quantization algorithm.<br>*   `<weight_bits>`: Number of bits to quantize weights to. AWQ presently only supports 4-bit quantization.<br>*   `<group_size>`: The group size for quantization. Supported values are -1 (for per-channel quantization) or any positive integer. Example: `"awq/4/128"`. |
| `source_name` | The source dtype policy name, e.g. "float32". |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `compute_dtype` | The compute dtype of this policy.<br><br>This is the dtype layers will do their computations in. Typically layers output tensors with the compute dtype as well.<br><br>Note that even if the compute dtype is float16 or bfloat16, hardware devices may not do individual adds, multiplies, and other fundamental operations in float16 or bfloat16, but instead may do some of them in float32 for numeric stability. The compute dtype is the dtype of the inputs and outputs of the ops that the layer executes. Internally, many ops will do certain internal calculations in float32 or some other device-internal intermediate format with higher precision than float16/bfloat16, to increase numeric stability. |
| `name` | Returns the name of this policy. |
| `quantization_mode` | The quantization mode of this policy. |
| `variable_dtype` | The variable dtype of this policy.<br><br>This is the dtype layers will create their variables in, unless a layer explicitly chooses a different dtype. If this is different than [`DTypePolicy.compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#compute_dtype)<br>, Layers will cast variables to the compute dtype to avoid type errors.<br><br>Variable regularizers are run in the variable dtype, not the compute dtype. |

Methods
-------

### `convert_input`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L150-L175)

convert_input(
        x, autocast, dtype
    )

Converts the input dtype based on `autocast` and `dtype`.

Note that `x` can be a tensor, symbolic tensor or numpy array, and this method will keep integer inputs untouched and only apply casting to floats.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L180-L182)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L531-L536)

get_config()

### `__eq__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L523-L529)

__eq__(
        other
    )

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.