[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.CosineDecay Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L572-L764)

A `LearningRateSchedule` that uses a cosine decay with optional warmup.

Inherits From: [`LearningRateSchedule`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/LearningRateSchedule)

tf.keras.optimizers.schedules.CosineDecay(
        initial_learning_rate,
        decay_steps,
        alpha=0.0,
        name='CosineDecay',
        warmup_target=None,
        warmup_steps=0
    )

See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983)
, SGDR: Stochastic Gradient Descent with Warm Restarts.

For the idea of a linear warmup of our learning rate, see [Goyal et al.](https://arxiv.org/pdf/1706.02677.pdf)
.

When we begin training a model, we often want an initial increase in our learning rate followed by a decay. If `warmup_target` is an int, this schedule applies a linear increase per optimizer step to our learning rate from `initial_learning_rate` to `warmup_target` for a duration of `warmup_steps`. Afterwards, it applies a cosine decay function taking our learning rate from `warmup_target` to `warmup_target * alpha` for a duration of `decay_steps`. If `warmup_target` is None we skip warmup and our decay will take our learning rate from `initial_learning_rate` to `initial_learning_rate * alpha`. It requires a `step` value to compute the learning rate. You can just pass a backend variable that you increment at each training step.

The schedule is a 1-arg callable that produces a warmup followed by a decayed learning rate when passed the current optimizer step. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Our warmup is computed as:

def warmup_learning_rate(step):
        completed_fraction = step / warmup_steps
        total_delta = target_warmup - initial_learning_rate
        return completed_fraction * total_delta

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
    lr_decayed_fn = keras.optimizers.schedules.CosineDecay(
        initial_learning_rate, decay_steps)

Example usage with warmup:

decay_steps = 1000
    initial_learning_rate = 0
    warmup_steps = 1000
    target_learning_rate = 0.1
    lr_warmup_decayed_fn = keras.optimizers.schedules.CosineDecay(
        initial_learning_rate, decay_steps, warmup_target=target_learning_rate,
        warmup_steps=warmup_steps
    )

You can pass this schedule directly into a [`keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 as the learning rate. The learning rate schedule is also serializable and deserializable using [`keras.optimizers.schedules.serialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
 and [`keras.optimizers.schedules.deserialize`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | A Python float. The initial learning rate. |
| `decay_steps` | A Python int. Number of steps to decay over. |
| `alpha` | A Python float. Minimum learning rate value for decay as a fraction of `warmup_target` or, if `warmup_target` is None, `initial_learning_rate`. |
| `name` | String. Optional name of the operation. Defaults to `"CosineDecay"`. |
| `warmup_target` | A Python float. The target learning rate for our warmup phase. Will cast to the `initial_learning_rate` datatype. Setting to `None` will skip warmup and begins decay phase from `initial_learning_rate`. Otherwise scheduler will warmup from `initial_learning_rate` to `warmup_target`. |
| `warmup_steps` | A Python int. Number of steps to warmup over. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L756-L764)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L713-L754)

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