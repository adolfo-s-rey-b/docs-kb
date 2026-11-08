[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fconstraints%2FNonNeg&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.constraints.NonNeg Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L121-L127)

Constrains the weights to be non-negative.

Inherits From: [`Constraint`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/Constraint)

#### View aliases

**Main aliases**

[`tf.keras.constraints.non_neg`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints/NonNeg)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L48-L57)

get_config()

Returns a Python dict of the object config.

A constraint config is a Python dictionary (JSON-serializable) that can be used to reinstantiate the same object.

|     |
| --- |
| Returns |     |
| Python dict containing the configuration of the constraint object. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/constraints/constraints.py#L125-L127)

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