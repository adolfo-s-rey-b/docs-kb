[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.piecewise\_constant Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L104-L182)

Piecewise constant from boundaries and interval values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.piecewise_constant_decay`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/piecewise_constant)

tf.compat.v1.train.piecewise_constant(
        x, boundaries, values, name=None
    )

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5 for the next 10000 steps, and 0.1 for any additional steps.

global_step = tf.Variable(0, trainable=False)
    boundaries = [100000, 110000]
    values = [1.0, 0.5, 0.1]
    learning_rate = tf.compat.v1.train.piecewise_constant(global_step, boundaries,
    values)
    
    # Later, whenever we perform an optimization step, we increment global_step.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A 0-D scalar `Tensor`. Must be one of the following types: `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`. |
| `boundaries` | A list of `Tensor`s or `int`s or `float`s with strictly increasing entries, and with all elements having the same type as `x`. |
| `values` | A list of `Tensor`s or `float`s or `int`s that specifies the values for the intervals defined by `boundaries`. It should have one more element than `boundaries`, and all elements should have the same type. |
| `name` | A string. Optional name of the operation. Defaults to 'PiecewiseConstant'. |

|     |
| --- |
| Returns<br>------- |     |
| A 0-D Tensor. Its value is `values[0]` when `x <= boundaries[0]`, `values[1]` when `x > boundaries[0]` and `x <= boundaries[1]`, ..., and values\[-1\] when `x > boundaries[-1]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if types of `x` and `boundaries` do not match, or types of all `values` do not match or the number of elements in the lists does not match. |

eager compatibility
-------------------

When eager execution is enabled, this function returns a function which in turn returns the decayed learning rate Tensor. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.