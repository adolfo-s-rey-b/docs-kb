[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Finverse_time_decay&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.inverse\_time\_decay Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/inverse_time_decay#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L374-L454)

Applies inverse time decay to the initial learning rate.

tf.compat.v1.train.inverse_time_decay(
        learning_rate,
        global_step,
        decay_steps,
        decay_rate,
        staircase=False,
        name=None
    )

When training a model, it is often recommended to lower the learning rate as the training progresses. This function applies an inverse decay function to a provided initial learning rate. It requires an `global_step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The function returns the decayed learning rate. It is computed as:

decayed_learning_rate = learning_rate / (1 + decay_rate * global_step /
    decay_step)

or, if `staircase` is `True`, as:

decayed_learning_rate = learning_rate / (1 + decay_rate * floor(global_step /
    decay_step))

Example: decay 1/t with a rate of 0.5:

...
    global_step = tf.Variable(0, trainable=False)
    learning_rate = 0.1
    decay_steps = 1.0
    decay_rate = 0.5
    learning_rate = tf.compat.v1.train.inverse_time_decay(learning_rate,
    global_step,
    decay_steps, decay_rate)
    
    # Passing global_step to minimize() will increment it at each step.
    learning_step = (
        tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
        .minimize(...my loss..., global_step=global_step)
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The initial learning rate. |
| `global_step` | A Python number. Global step to use for the decay computation. Must not be negative. |
| `decay_steps` | How often to apply decay. |
| `decay_rate` | A Python number. The decay rate. |
| `staircase` | Whether to apply decay in a discrete staircase, as opposed to continuous, fashion. |
| `name` | String. Optional name of the operation. Defaults to 'InverseTimeDecay'. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of the same type as `learning_rate`. The decayed learning rate. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `global_step` is not supplied. |

eager compatibility
-------------------

When eager execution is enabled, this function returns a function which in turn returns the decayed learning rate Tensor. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.