[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.layers.RDFTParameter Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L70-L182)

RDFT reparameterization of a convolution kernel.

Inherits From: [`Parameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)

#### View aliases

**Main aliases**

[`tfc.RDFTParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter)

tfc.layers.RDFTParameter(
        initial_value, name=None, shape=None, dtype=None
    )

This uses the real-input discrete Fourier transform (RDFT) of a kernel as its parameterization. The inverse RDFT is applied to the variable to produce the kernel.

(see [https://en.wikipedia.org/wiki/Discrete\_Fourier\_transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_value` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`. The initial value of the kernel. If not provided, its `shape` must be given, and the initial value of the parameter will be undefined. |
| `name` | String. The name of the kernel. |
| `shape` | [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or compatible. Ignored unless `initial_value is None`. |
| `dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> or compatible. DType of this parameter. If not given, inferred from `initial_value`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shape` | [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>. The shape of the convolution kernel. |
| `real` | [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>. The real part of the RDFT of the kernel. |
| `imag` | [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>. The imaginary part of the RDFT of the kernel. |
| `dtype` |     |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `get_config`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L175-L182)

get_config() -> Dict[str, Any]

Returns the configuration of the `Parameter`.

### `get_weights`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L47-L48)

get_weights()

### `set_weights`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L50-L55)

set_weights(
        weights
    )

### `with_name_scope`

@classmethod

Decorator to automatically enter the module name scope.

    class MyModule(tf.Module):

Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s whose names included the module name:

    mod = MyModule()

|     |     |
| --- | --- |
| Args |     |
| `method` | The method to wrap. |

|     |
| --- |
| Returns |     |
| The original method wrapped such that it enters the module's name scope. |     |

### `__call__`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L144-L173)

__call__(
        compute_dtype=None
    ) -> tf.Tensor

Computes and returns the convolution kernel as a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.