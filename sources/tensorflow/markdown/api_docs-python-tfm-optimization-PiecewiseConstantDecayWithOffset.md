[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2FPiecewiseConstantDecayWithOffset&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#returns)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PiecewiseConstantDecayWithOffset Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#returns)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py)

A LearningRateSchedule that uses a piecewise constant decay schedule.

Inherits From: [`base_lr_class`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset/base_lr_class)

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.PiecewiseConstantDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset)

tfm.optimization.PiecewiseConstantDecayWithOffset(
        offset=0, **kwargs
    )

The function returns a 1-arg callable to compute the piecewise constant when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5 for the next 10000 steps, and 0.1 for any additional steps.

step = tf.Variable(0, trainable=False)
    boundaries = [100000, 110000]
    values = [1.0, 0.5, 0.1]
    learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(
        boundaries, values)
    
    # Later, whenever we perform an optimization step, we pass in the step.
    learning_rate = learning_rate_fn(step)

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |
| --- |
| Returns<br>------- |     |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as the boundary tensors.<br><br>The output of the 1-arg function that takes the `step` is `values[0]` when `step <= boundaries[0]`, `values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ..., and values\[-1\] when `step > boundaries[-1]`. |     |

Child Classes
-------------

[`class base_lr_class`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset/base_lr_class)

Methods
-------

### `from_config`

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

get_config()

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L67-L69)

__call__(
        step
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.