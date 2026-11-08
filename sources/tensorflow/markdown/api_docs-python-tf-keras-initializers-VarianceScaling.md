[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Finitializers%2FVarianceScaling&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.VarianceScaling Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#methods)
    *   [clone](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#clone)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L201-L329)

Initializer that adapts its scale to the shape of its input tensors.

Inherits From: [`Initializer`](https://www.tensorflow.org/api_docs/python/tf/keras/Initializer)

#### View aliases

**Main aliases**

[`tf.keras.initializers.variance_scaling`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/VarianceScaling)

tf.keras.initializers.VarianceScaling(
        scale=1.0,
        mode='fan_in',
        distribution='truncated_normal',
        seed=None,
        input_axes=None,
        output_axes=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Train a Deep Q Network with TF-Agents](https://www.tensorflow.org/agents/tutorials/1_dqn_tutorial)<br>    <br>*   [Networks](https://www.tensorflow.org/agents/tutorials/8_networks_tutorial) |

With `distribution="truncated_normal" or "untruncated_normal"`, samples are drawn from a truncated/untruncated normal distribution with a mean of zero and a standard deviation (after truncation, if used) `stddev = sqrt(scale / n)`, where `n` is:

*   number of input units in the weight tensor, if `mode="fan_in"`
*   number of output units, if `mode="fan_out"`
*   average of the numbers of input and output units, if `mode="fan_avg"`

With `distribution="uniform"`, samples are drawn from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(3 * scale / n)`.

#### Examples:

    # Standalone usage:

    # Usage in a Keras layer:

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scale` | Scaling factor (positive float). |
| `mode` | One of `"fan_in"`, `"fan_out"`, `"fan_avg"`. |
| `distribution` | Random distribution to use. One of `"truncated_normal"`, `"untruncated_normal"`, or `"uniform"`. |
| `seed` | A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`. |
| `input_axes` | Optional list of integers. The axes of the input tensor that should be considered for computing the fan-in. |
| `output_axes` | Optional list of integers. The axes of the output tensor that should be considered for computing the fan-out. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L320-L329)

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