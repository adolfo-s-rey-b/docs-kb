[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.log\_sigmoid Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4203-L4245)

Computes log sigmoid of `x` element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.log_sigmoid`](https://www.tensorflow.org/api_docs/python/tf/math/log_sigmoid)

tf.math.log_sigmoid(
        x, name=None
    )

Specifically, `y = log(1 / (1 + exp(-x)))`. For numerical stability, we use `y = -tf.nn.softplus(-x)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A Tensor with type `float32` or `float64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor with the same type as `x`. |     |

#### Usage Example:

If a positive number is large, then its log\_sigmoid will approach to 0 since the formula will be `y = log( <large_num> / (1 + <large_num>) )` which approximates to `log (1)` which is 0.

    x = tf.constant([0.0, 1.0, 50.0, 100.0])

If a negative number is large, its log\_sigmoid will approach to the number itself since the formula will be `y = log( 1 / (1 + <large_num>) )` which is `log (1) - log ( (1 + <large_num>) )` which approximates to `- <large_num>` that is the number itself.

    x = tf.constant([-100.0, -50.0, -1.0, 0.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.