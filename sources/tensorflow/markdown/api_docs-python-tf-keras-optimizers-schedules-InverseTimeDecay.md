[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Foptimizers%2Fschedules%2FInverseTimeDecay&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.InverseTimeDecay Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L460-L569)

A `LearningRateSchedule` that uses an inverse time decay schedule.

Inherits From: [`LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

tf.keras.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate,
        decay_steps,
        decay_rate,
        staircase=False,
        name='InverseTimeDecay'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit) |

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies the inverse decay function to an optimizer step, given a provided initial learning rate. It requires a `step` value to compute the decayed learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

def decayed_learning_rate(step):
        return initial_learning_rate / (1 + decay_rate * step / decay_step)

or, if `staircase` is `True`, as:

def decayed_learning_rate(step):
        return initial_learning_rate /
               (1 + decay_rate * floor(step / decay_step))

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. Example: Fit a Keras model when decaying 1/t with a rate of 0.5:

...
    initial_learning_rate = 0.1
    decay_steps = 1.0
    decay_rate = 0.5
    learning_rate_fn = keras.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate, decay_steps, decay_rate)
    
    model.compile(optimizer=keras.optimizers.SGD(
                      learning_rate=learning_rate_fn),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(data, labels, epochs=5)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | A Python float. The initial learning rate. |
| `decay_steps` | How often to apply decay. |
| `decay_rate` | A Python number. The decay rate. |
| `staircase` | Whether to apply decay in a discrete staircase, as o pposed to continuous, fashion. |
| `name` | String. Optional name of the operation. Defaults to `"InverseTimeDecay"`. |

|     |
| --- |
| Returns<br>------- |     |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar tensor of the same type as `initial_learning_rate`. |     |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L562-L569)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L545-L560)

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