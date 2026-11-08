[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.layers.IdentityInitializer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/initializers.py#L25-L55)

Initialize to the identity kernel with the given shape.

#### View aliases

**Main aliases**

[`tfc.IdentityInitializer`](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer)

tfc.layers.IdentityInitializer(
        gain=1
    )

This creates an n-D kernel suitable for `SignalConv*` with the requested support that produces an output identical to its input (except possibly at the signal boundaries).

Methods
-------

### `from_config`

@classmethod

Instantiates an initializer from a configuration dictionary.

#### Example:

initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, the output of `get_config()`. |

|     |
| --- |
| Returns |     |
| An `Initializer` instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/initializers.py#L52-L55)

get_config()

Returns the initializer's configuration as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/layers/initializers.py#L40-L50)

__call__(
        shape, dtype=None, **kwargs
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. |
| `**kwargs` | Additional keyword arguments. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.