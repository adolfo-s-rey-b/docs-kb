[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/GlorotUniform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.GlorotUniform Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L332-L385)

The Glorot uniform initializer, also called Xavier uniform initializer.

Inherits From: [`VarianceScaling`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling)
, [`Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.glorot_uniform`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/GlorotUniform)

tf.keras.initializers.GlorotUniform(
        seed=None, input_axes=None, output_axes=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(6 / (fan_in + fan_out))` (`fan_in` is the number of input units in the weight tensor and `fan_out` is the number of output units).

#### Examples:

    # Standalone usage:

    # Usage in a Keras layer:

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |

#### Reference:

*   [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L380-L385)

get_config()

Returns the initializer's configuration as a JSON-serializable dict.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L293-L318)

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