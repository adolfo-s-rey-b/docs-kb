[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.constraints.MinMaxNorm Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L160-L215)

MinMaxNorm weight constraint.

Inherits From: [`Constraint`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/Constraint)

#### View aliases

**Main aliases**

[`tf.keras.constraints.min_max_norm`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/MinMaxNorm)

tf.keras.constraints.MinMaxNorm(
        min_value=0.0, max_value=1.0, rate=1.0, axis=0
    )

Constrains the weights incident to each hidden unit to have the norm between a lower bound and an upper bound.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `min_value` | the minimum norm for the incoming weights. |
| `max_value` | the maximum norm for the incoming weights. |
| `rate` | rate for enforcing the constraint: weights will be rescaled to yield `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`. Effectively, this means that rate=1.0 stands for strict enforcement of the constraint, while rate<1.0 means that weights will be rescaled at each step to slowly move towards a value inside the desired interval. |
| `axis` | integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L59-L77)

@classmethod

Instantiates a weight constraint from a configuration dictionary.

#### Example:

constraint = UnitNorm()
    config = constraint.get_config()
    constraint = UnitNorm.from_config(config)

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, the output of `get_config()`. |

|     |
| --- |
| Returns |     |
| A [`keras.constraints.Constraint`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/Constraint)<br> instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L209-L215)

get_config()

Returns a Python dict of the object config.

A constraint config is a Python dictionary (JSON-serializable) that can be used to reinstantiate the same object.

|     |
| --- |
| Returns |     |
| Python dict containing the configuration of the constraint object. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L198-L207)

__call__(
        w
    )

Applies the constraint to the input weight variable.

By default, the inputs weight variable is not modified. Users should override this method to implement their own projection function.

|     |     |
| --- | --- |
| Args |     |
| `w` | Input weight variable. |

|     |
| --- |
| Returns |     |
| Projected variable (by default, returns unmodified inputs). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.