[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Finitializers%2FRandomUniform&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.RandomUniform Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L145-L198)

Random uniform initializer.

Inherits From: [`Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.random_uniform`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomUniform)

tf.keras.initializers.RandomUniform(
        minval=-0.05, maxval=0.05, seed=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Train a Deep Q Network with TF-Agents](https://www.tensorflow.org/agents/tutorials/1_dqn_tutorial)<br>    <br>*   [Networks](https://www.tensorflow.org/agents/tutorials/8_networks_tutorial) |

Draws samples from a uniform distribution for given parameters.

#### Examples:

    # Standalone usage:

    # Usage in a Keras layer:

|     |     |
| --- | --- |
| Args<br>---- |     |
| `minval` | A python scalar or a scalar keras tensor. Lower bound of the range of random values to generate (inclusive). |
| `maxval` | A python scalar or a scalar keras tensor. Upper bound of the range of random values to generate (exclusive). |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L195-L198)

get_config()

Returns the initializer's configuration as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L186-L193)

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