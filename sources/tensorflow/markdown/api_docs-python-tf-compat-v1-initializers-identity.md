[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.initializers.identity Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L1555-L1592)

Initializer that generates the identity matrix.

tf.compat.v1.initializers.identity(
        gain=1.0,
        dtype=tf.dtypes.float32
    )

Only use for 2D matrices.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `gain` | Multiplicative factor to apply to the identity matrix. |
| `dtype` | Default data type, used if no `dtype` argument is provided when calling the initializer. Only floating point types are supported. |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L75-L94)

@classmethod

Instantiates an initializer from a configuration dictionary.

#### Example:

initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary. It will typically be the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An Initializer instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L1591-L1592)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops.py#L1575-L1589)

__call__(
        shape, dtype=None, partition_info=None
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. If not provided use the initializer dtype. |
| `partition_info` | Optional information about the possible partitioning of a tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.