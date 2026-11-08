[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.layers.Parameter Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L30-L55)

Reparameterized `Layer` variable.

#### View aliases

**Main aliases**

[`tfc.Parameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)

tfc.layers.Parameter(
        name=None
    )

This object represents a parameter of a `tf.keras.layer.Layer` object which isn't directly stored in a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
, but can be represented as a function (of any number of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 attributes).

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `get_config`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L42-L45)

@abc.abstractmethod

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

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/parameters.py#L38-L40)

@abc.abstractmethod

Computes and returns the parameter value as a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.