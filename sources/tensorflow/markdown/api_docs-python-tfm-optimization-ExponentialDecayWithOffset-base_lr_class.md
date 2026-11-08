[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.ExponentialDecayWithOffset.base\_lr\_class Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class#__call__)
        

A LearningRateSchedule that uses an exponential decay schedule.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.ExponentialDecayWithOffset.base_lr_class`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset/base_lr_class)

tfm.optimization.ExponentialDecayWithOffset.base_lr_class(
        initial_learning_rate, decay_steps, decay_rate, staircase=False, name=None
    )

When training a model, it is often useful to lower the learning rate as the training progresses. This schedule applies an exponential decay function to an optimizer step, given a provided initial learning rate.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

def decayed_learning_rate(step):
      return initial_learning_rate * decay_rate ^ (step / decay_steps)

If the argument `staircase` is `True`, then `step / decay_steps` is an integer division and the decayed learning rate follows a staircase function.

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. Example: When fitting a TF-Keras model, decay every 100000 steps with a base of 0.96:

initial_learning_rate = 0.1
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=100000,
        decay_rate=0.96,
        staircase=True)
    
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=lr_schedule),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(data, labels, epochs=5)

The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |
| --- |
| Returns<br>------- |     |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as `initial_learning_rate`. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The initial learning rate. |
| `decay_steps` | A scalar `int32` or `int64` `Tensor` or a Python number. Must be positive. See the decay computation above. |
| `decay_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The decay rate. |
| `staircase` | Boolean. If `True` decay the learning rate at discrete intervals |
| `name` | String. Optional name of the operation. Defaults to 'ExponentialDecay'. |

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

__call__(
        step
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.