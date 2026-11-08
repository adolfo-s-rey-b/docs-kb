[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/exponential_decay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.exponential\_decay Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L28-L101)

Applies exponential decay to the learning rate.

tf.compat.v1.train.exponential_decay(
        learning_rate,
        global_step,
        decay_steps,
        decay_rate,
        staircase=False,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migration examples: Canned Estimators](https://www.tensorflow.org/guide/migrate/canned_estimators) | *   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

When training a model, it is often recommended to lower the learning rate as the training progresses. This function applies an exponential decay function to a provided initial learning rate. It requires a `global_step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The function returns the decayed learning rate. It is computed as:

decayed_learning_rate = learning_rate *
                            decay_rate ^ (global_step / decay_steps)

If the argument `staircase` is `True`, then `global_step / decay_steps` is an integer division and the decayed learning rate follows a staircase function.

Example: decay every 100000 steps with a base of 0.96:

...
    global_step = tf.Variable(0, trainable=False)
    starter_learning_rate = 0.1
    learning_rate = tf.compat.v1.train.exponential_decay(starter_learning_rate,
    global_step,
                                               100000, 0.96, staircase=True)
    # Passing global_step to minimize() will increment it at each step.
    learning_step = (
        tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
        .minimize(...my loss..., global_step=global_step)
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The initial learning rate. |
| `global_step` | A scalar `int32` or `int64` `Tensor` or a Python number. Global step to use for the decay computation. Must not be negative. |
| `decay_steps` | A scalar `int32` or `int64` `Tensor` or a Python number. Must be positive. See the decay computation above. |
| `decay_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The decay rate. |
| `staircase` | Boolean. If `True` decay the learning rate at discrete intervals |
| `name` | String. Optional name of the operation. Defaults to 'ExponentialDecay'. |

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