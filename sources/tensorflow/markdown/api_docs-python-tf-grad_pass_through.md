[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.grad\_pass\_through Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/custom_gradient.py#L773-L823)

Creates a grad-pass-through op with the forward behavior provided in f.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.grad_pass_through`](https://www.tensorflow.org/api_docs/python/tf/grad_pass_through)

tf.grad_pass_through(
        f
    )

Use this function to wrap any op, maintaining its behavior in the forward pass, but replacing the original op in the backward graph with an identity. For example:

x = tf.Variable(1.0, name="x")
    z = tf.Variable(3.0, name="z")
    
    with tf.GradientTape() as tape:
      # y will evaluate to 9.0
      y = tf.grad_pass_through(x.assign)(z**2)
    # grads will evaluate to 6.0
    grads = tape.gradient(y, z)

Another example is a 'differentiable' moving average approximation, where gradients are allowed to flow into the last value fed to the moving average, but the moving average is still used for the forward pass:

x = ... # Some scalar value
    # A moving average object, we don't need to know how this is implemented
    moving_average = MovingAverage()
    with backprop.GradientTape() as tape:
      # mavg_x will evaluate to the current running average value
      mavg_x = tf.grad_pass_through(moving_average)(x)
    grads = tape.gradient(mavg_x, x) # grads will evaluate to 1.0

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | function `f(*x)` that returns a `Tensor` or nested structure of `Tensor` outputs. |

|     |
| --- |
| Returns<br>------- |     |
| A function `h(x)` which returns the same values as `f(x)` and whose gradients are the same as those of an identity function. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.