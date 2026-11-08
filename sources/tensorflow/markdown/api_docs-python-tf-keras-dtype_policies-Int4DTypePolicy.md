[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.dtype\_policies.Int4DTypePolicy Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/Int4DTypePolicy#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L291-L361)

Quantized dtype policy for int4 quantization.

Inherits From: [`QuantizedDTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/QuantizedDTypePolicy)
, [`DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)

tf.keras.dtype_policies.Int4DTypePolicy(
        mode, source_name=None
    )

This policy helps propagate quantization settings for int4 sub-channel quantization when loading a quantized model in Keras format.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | The quantization mode. This should be a string in the format `"int4/<block_size>"`.<br><br>*   `"int4"`: The identifier for the quantization algorithm.<br>*   `<block_size>`: The block size for sub-channel quantization. Use -1 for per-channel (legacy) quantization. Any positive integer enables sub-channel quantization with that block size. Example: `"int4/128"` for sub-channel with 128-element groups. |
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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L356-L361)

get_config()

### `__eq__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L351-L354)

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