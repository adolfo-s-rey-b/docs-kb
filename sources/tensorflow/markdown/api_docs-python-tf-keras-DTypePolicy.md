[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.DTypePolicy Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#methods)
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#get_config)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L9-L204)

A dtype policy for a Keras layer.

#### View aliases

**Main aliases**

[`tf.keras.dtype_policies.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)
, [`tf.keras.mixed_precision.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)
, [`tf.keras.mixed_precision.Policy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)

tf.keras.DTypePolicy(
        name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Mixed precision](https://www.tensorflow.org/guide/mixed_precision) |

A dtype policy determines a layer's computation and variable dtypes. Each layer has a policy. Policies can be passed to the `dtype` argument of layer constructors, or a global policy can be set with [`keras.config.set_dtype_policy`](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_dtype_policy)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`. |

Typically you only need to interact with dtype policies when using mixed precision, which is the use of float16 or bfloat16 for computations and float32 for variables. This is why the term `mixed_precision` appears in the API name. Mixed precision can be enabled by passing `"mixed_float16"` or `"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

    keras.config.set_dtype_policy("mixed_float16")

In the example above, passing `dtype="float32"` to the layer is equivalent to passing `dtype=keras.config.DTypePolicy("float32")`. In general, passing a dtype policy name to a layer is equivalent to passing the corresponding policy, so it is never necessary to explicitly construct a `DTypePolicy` object.

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L177-L178)

get_config()

### `__eq__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L190-L197)

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