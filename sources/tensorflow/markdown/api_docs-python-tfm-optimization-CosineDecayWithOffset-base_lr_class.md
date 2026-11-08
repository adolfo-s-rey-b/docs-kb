[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.CosineDecayWithOffset.base\_lr\_class Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class#__call__)
        

A LearningRateSchedule that uses a cosine decay with optional warmup.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.CosineDecayWithOffset.base_lr_class`](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset/base_lr_class)

tfm.optimization.CosineDecayWithOffset.base_lr_class(
        initial_learning_rate,
        decay_steps,
        alpha=0.0,
        name=None,
        warmup_target=None,
        warmup_steps=0
    )

See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983)
, SGDR: Stochastic Gradient Descent with Warm Restarts.

For the idea of a linear warmup of our learning rate, see [Goyal et al.](https://arxiv.org/pdf/1706.02677.pdf)
.

When we begin training a model, we often want an initial increase in our learning rate followed by a decay. If `warmup_target` is an int, this schedule applies a linear increase per optimizer step to our learning rate from `initial_learning_rate` to `warmup_target` for a duration of `warmup_steps`. Afterwards, it applies a cosine decay function taking our learning rate from `warmup_target` to `alpha` for a duration of `decay_steps`. If `warmup_target` is None we skip warmup and our decay will take our learning rate from `initial_learning_rate` to `alpha x initial_learning_rate`. It requires a `step` value to compute the learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The schedule is a 1-arg callable that produces a warmup followed by a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Our warmup is computed as:

def warmup_learning_rate(step):
        completed_fraction = step / warmup_steps
        total_delta = target_warmup - initial_learning_rate
        return completed_fraction * total_delta + initial_learning_rate

And our decay is computed as:

if warmup_target is None:
        initial_decay_lr = initial_learning_rate
    else:
        initial_decay_lr = warmup_target
    
    def decayed_learning_rate(step):
        step = min(step, decay_steps)
        cosine_decay = 0.5 * (1 + cos(pi * step / decay_steps))
        decayed = (1 - alpha) * cosine_decay + alpha
        return initial_decay_lr * decayed

Example usage without warmup:

decay_steps = 1000
    initial_learning_rate = 0.1
    lr_decayed_fn = tf.keras.optimizers.schedules.CosineDecay(
        initial_learning_rate, decay_steps)

Example usage with warmup:

decay_steps = 1000
    initial_learning_rate = 0
    warmup_steps = 1000
    target_learning_rate = 0.1
    lr_warmup_decayed_fn = tf.keras.optimizers.schedules.CosineDecay(
        initial_learning_rate, decay_steps, warmup_target=target_learning_rate,
        warmup_steps=warmup_steps
    )

You can pass this schedule directly into a [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`tf.keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`tf.keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |
| --- |
| Returns<br>------- |     |
| A 1-arg callable learning rate schedule that takes the current optimizer step and outputs the decayed learning rate, a scalar `Tensor` of the same type as `initial_learning_rate`. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python int. The initial learning rate. |
| `decay_steps` | A scalar `int32` or `int64` `Tensor` or a Python int. Number of steps to decay over. |
| `alpha` | A scalar `float32` or `float64` `Tensor` or a Python int. Minimum learning rate value for decay as a fraction of `initial_learning_rate`. |
| `name` | String. Optional name of the operation. Defaults to 'CosineDecay'. |
| `warmup_target` | None or a scalar `float32` or `float64` `Tensor` or a Python int. The target learning rate for our warmup phase. Will cast to the `initial_learning_rate` datatype. Setting to None will skip warmup and begins decay phase from `initial_learning_rate`. Otherwise scheduler will warmup from `initial_learning_rate` to `warmup_target`. |
| `warmup_steps` | A scalar `int32` or `int64` `Tensor` or a Python int. Number of steps to warmup over. |

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