[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.Ones Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L78-L106)

Initializer that generates tensors initialized to 1.

Inherits From: [`Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.ones`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Ones)

Also available via the shortcut function `ones`.

#### Examples:

    # Standalone usage:

    # Usage in a Keras layer:

Methods
-------

### `clone`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L96-L97)

clone()

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L76-L94)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L68-L74)

get_config()

Returns the initializer's configuration as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L95-L106)

__call__(
        shape, dtype=None
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. Only numeric or boolean dtypes are supported. If not specified, [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is used, which default to `float32` unless you configured it otherwise (via [`keras.backend.set_floatx(float_dtype)`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.