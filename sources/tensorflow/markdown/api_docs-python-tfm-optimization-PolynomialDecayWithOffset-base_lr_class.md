[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PolynomialDecayWithOffset.base\_lr\_class Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class#__call__)
        

A LearningRateSchedule that uses a polynomial decay schedule.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.PolynomialDecayWithOffset.base_lr_class`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset/base_lr_class)

tfm.optimization.PolynomialDecayWithOffset.base_lr_class(
        initial_learning_rate,
        decay_steps,
        end_learning_rate=0.0001,
        power=1.0,
        cycle=False,
        name=None
    )

It is commonly observed that a monotonically decreasing learning rate, whose degree of change is carefully chosen, results in a better performing model. This schedule applies a polynomial decay function to an optimizer step, given a provided `initial_learning_rate`, to reach an `end_learning_rate` in the given `decay_steps`.

It requires a `step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The schedule is a 1-arg callable that produces a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions. It is computed as:

def decayed_learning_rate(step):
      step = min(step, decay_steps)
      return ((initial_learning_rate - end_learning_rate) *
              (1 - step / decay_steps) ^ (power)
             ) + end_learning_rate

If `cycle` is True then a multiple of `decay_steps` is used, the first one that is bigger than `step`.

def decayed_learning_rate(step):
      decay_steps = decay_steps * ceil(step / decay_steps)
      return ((initial_learning_rate - end_learning_rate) *
              (1 - step / decay_steps) ^ (power)
             ) + end_learning_rate

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. Example: Fit a model while decaying from 0.1 to 0.01 in 10000 steps using sqrt (i.e. power=0.5):

...
    starter_learning_rate = 0.1
    end_learning_rate = 0.01
    decay_steps = 10000
    learning_rate_fn = tf.keras.optimizers.schedules.PolynomialDecay(
        starter_learning_rate,
        decay_steps,
        end_learning_rate,
        power=0.5)
    
    model.compile(optimizer=tf.keras.optimizers.SGD(
                      learning_rate=learning_rate_fn),
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
| `end_learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The minimal end learning rate. |
| `power` | A scalar `float32` or `float64` `Tensor` or a Python number. The power of the polynomial. Defaults to `1.0`. |
| `cycle` | A boolean, whether it should cycle beyond decay\_steps. |
| `name` | String. Optional name of the operation. Defaults to 'PolynomialDecay'. |

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