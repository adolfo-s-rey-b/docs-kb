[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random\_normal\_initializer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L371-L434)

Initializer that generates tensors with a normal distribution.

tf.random_normal_initializer(
        mean=0.0, stddev=0.05, seed=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

Initializers allow you to pre-specify an initialization strategy, encoded in the Initializer object, without knowing the shape and dtype of the variable being initialized.

#### Examples:

    def make_variables(k, initializer):

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mean` | a python scalar or a scalar tensor. Mean of the random values to generate. |
| `stddev` | a python scalar or a scalar tensor. Standard deviation of the random values to generate. |
| `seed` | A Python integer. Used to create random seeds. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L76-L96)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L429-L434)

get_config()

Returns the configuration of the initializer as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/init_ops_v2.py#L410-L427)

__call__(
        shape,
        dtype=tf.dtypes.float32,
        **kwargs
    )

Returns a tensor object initialized as specified by the initializer.

|     |     |
| --- | --- |
| Args |     |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. Only floating point types are supported. |
| `**kwargs` | Additional keyword arguments. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the dtype is not floating point |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.