[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.PiecewiseConstantDecay Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/PiecewiseConstantDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L187-L301)

A `LearningRateSchedule` that uses a piecewise constant decay schedule.

Inherits From: [`LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

tf.keras.optimizers.schedules.PiecewiseConstantDecay(
        boundaries, values, name='PiecewiseConstant'
    )

The function returns a 1-arg callable to compute the piecewise constant when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5 for the next 10000 steps, and 0.1 for any additional steps.

step = ops.array(0)
    boundaries = [100000, 110000]
    values = [1.0, 0.5, 0.1]
    learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(
        boundaries, values)
    
    # Later, whenever we perform an optimization step, we pass in the step.
    learning_rate = learning_rate_fn(step)

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boundaries` | A list of Python numbers with strictly increasing entries, and with all elements having the same type as the optimizer step. |
| `values` | A list of Python numbers that specifies the values for the intervals defined by `boundaries`. It should have one more element than `boundaries`, and all elements should have the same type. |
| `name` | A string. Optional name of the operation. Defaults to `"PiecewiseConstant"`. |

|     |
| --- |
| Returns<br>------- |     |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as the boundary tensors.<br><br>The output of the 1-arg function that takes the `step` is `values[0]` when `step <= boundaries[0]`, `values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ..., and `values[-1]` when `step > boundaries[-1]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the number of elements in the `boundaries` and `values` lists do not match. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L66-L76)

@classmethod

Instantiates a `LearningRateSchedule` from its config.

|     |     |
| --- | --- |
| Args |     |
| `config` | Output of `get_config()`. |

|     |
| --- |
| Returns |     |
| A `LearningRateSchedule` instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L296-L301)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L256-L294)

__call__(
        step
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.