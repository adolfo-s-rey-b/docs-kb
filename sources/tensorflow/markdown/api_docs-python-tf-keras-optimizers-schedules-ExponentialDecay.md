[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.ExponentialDecay Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/ExponentialDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L79-L184)

A `LearningRateSchedule` that uses an exponential decay schedule.

Inherits From: [`LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps,
        decay_rate,
        staircase=False,
        name='ExponentialDecay'
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Migration examples: Canned Estimators](https://www.tensorflow.org/guide/migrate/canned_estimators) |

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies an exponential decay function to an optimizer step, given a provided initial learning rate.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

def decayed_learning_rate(step):
        return initial_learning_rate * decay_rate ^ (step / decay_steps)

If the argument `staircase` is `True`, then `step / decay_steps` is an integer division and the decayed learning rate follows a staircase function.

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. Example: When fitting a Keras model, decay every 100000 steps with a base of 0.96:

initial_learning_rate = 0.1
    lr_schedule = keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=100000,
        decay_rate=0.96,
        staircase=True)
    
    model.compile(optimizer=keras.optimizers.SGD(learning_rate=lr_schedule),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(data, labels, epochs=5)

The learning rate schedule is also serializable and deserializable using [`keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | A Python float. The initial learning rate. |
| `decay_steps` | A Python integer. Must be positive. See the decay computation above. |
| `decay_rate` | A Python float. The decay rate. |
| `staircase` | Boolean. If `True` decay the learning rate at discrete intervals. |
| `name` | String. Optional name of the operation. Defaults to `"ExponentialDecay`". |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L177-L184)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L162-L175)

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