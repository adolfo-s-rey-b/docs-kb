[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.polynomial\_decay Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/polynomial_decay#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L185-L283)

Applies a polynomial decay to the learning rate.

tf.compat.v1.train.polynomial_decay(
        learning_rate,
        global_step,
        decay_steps,
        end_learning_rate=0.0001,
        power=1.0,
        cycle=False,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD) |

It is commonly observed that a monotonically decreasing learning rate, whose degree of change is carefully chosen, results in a better performing model. This function applies a polynomial decay function to a provided initial `learning_rate` to reach an `end_learning_rate` in the given `decay_steps`.

It requires a `global_step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The function returns the decayed learning rate. It is computed as:

global_step = min(global_step, decay_steps)
    decayed_learning_rate = (learning_rate - end_learning_rate) *
                            (1 - global_step / decay_steps) ^ (power) +
                            end_learning_rate

If `cycle` is True then a multiple of `decay_steps` is used, the first one that is bigger than `global_steps`.

decay_steps = decay_steps * ceil(global_step / decay_steps)
    decayed_learning_rate = (learning_rate - end_learning_rate) *
                            (1 - global_step / decay_steps) ^ (power) +
                            end_learning_rate

Example: decay from 0.1 to 0.01 in 10000 steps using sqrt (i.e. power=0.5):

...
    global_step = tf.Variable(0, trainable=False)
    starter_learning_rate = 0.1
    end_learning_rate = 0.01
    decay_steps = 10000
    learning_rate = tf.compat.v1.train.polynomial_decay(starter_learning_rate,
    global_step,
                                              decay_steps, end_learning_rate,
                                              power=0.5)
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
| `end_learning_rate` | A scalar `float32` or `float64` `Tensor` or a Python number. The minimal end learning rate. |
| `power` | A scalar `float32` or `float64` `Tensor` or a Python number. The power of the polynomial. Defaults to linear, 1.0. |
| `cycle` | A boolean, whether or not it should cycle beyond decay\_steps. |
| `name` | String. Optional name of the operation. Defaults to 'PolynomialDecay'. |

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