[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Initializer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L4-L97)

Initializer base class: all Keras initializers inherit from this class.

#### View aliases

**Main aliases**

[`tf.keras.initializers.Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

Initializers should implement a `__call__()` method with one of two possible signatures. If your initializer does not handle distribution layouts, it should use this signature:

def __call__(self, shape, dtype=None):
        # returns a tensor of shape `shape` and dtype `dtype`
        # containing values drawn using a function of your choice.

If your initializer handles distribution layouts, it should use this signature. `layout` can either be a [`keras.distribution.TensorLayout`](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout)
 or a backend-specific layout. If the given `layout` is not `None`, the returned value must be distributed according to `layout`.

def __call__(self, shape, dtype=None, layout=None):
        # returns a tensor of shape `shape`, dtype `dtype` and distributed
        # across devices according to the layout `layout`.
        # containing values drawn using a function of your choice.

Optionally, you can also implement the method `get_config()` and the class method `from_config` in order to support serialization, just like with any Keras object.

Here's a simple example: a random normal initializer.

class ExampleRandomNormal(Initializer):
        def __init__(self, mean, stddev):
            self.mean = mean
            self.stddev = stddev
    
        def __call__(self, shape, dtype=None):
            return keras.random.normal(
                shape, mean=self.mean, stddev=self.stddev, dtype=dtype
            )
    
        def get_config(self):  # To support serialization
            return {"mean": self.mean, "stddev": self.stddev}

Note that we don't have to implement `from_config()` in the example above since the constructor arguments of the class the keys in the config returned by `get_config()` are the same. In this case, the default `from_config()` works fine.

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L57-L66)

__call__(
        shape, dtype=None
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.