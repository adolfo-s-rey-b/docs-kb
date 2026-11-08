[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.layers.GDNParameter Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L185-L269)

Nonnegative parameterization as needed for GDN parameters.

Inherits From: [`Parameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)

#### View aliases

**Main aliases**

[`tfc.GDNParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter)

tfc.layers.GDNParameter(
        initial_value,
        name=None,
        minimum=0.0,
        offset=(2 ** -18),
        shape=None,
        dtype=None
    )

The variable is subjected to an invertible transformation that slows down the learning rate for small values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_value` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`. The initial value of the kernel. If not provided, its `shape` must be given, and the initial value of the parameter will be undefined. |
| `name` | String. The name of the parameter. |
| `minimum` | Float. Lower bound for the parameter (defaults to zero). |
| `offset` | Float. Offset added to the reparameterization. The parameterization of beta/gamma as their square roots lets the training slow down when values are close to zero, which is desirable as small values in the denominator can lead to a situation where gradient noise on beta/gamma leads to extreme amounts of noise in the GDN activations. However, without the offset, we would get zero gradients if any elements of beta or gamma were exactly zero, and thus the training could get stuck. To prevent this, we add this small constant. The default value was empirically determined as a good starting point. Making it bigger potentially leads to more gradient noise on the activations, making it too small may lead to numerical precision issues. |
| `shape` | [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or compatible. Ignored unless `initial_value is None`. |
| `dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> or compatible. DType of this parameter. If not given, inferred from `initial_value`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `minimum` | Float. The `minimum` parameter provided on initialization. |
| `offset` | Float. The `offset` parameter provided on initialization. |
| `variable` | [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>. The reparameterized variable. |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `get_config`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L260-L269)

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

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L240-L250)

__call__(
        compute_dtype=None
    ) -> tf.Tensor

Computes and returns the non-negative value as a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.