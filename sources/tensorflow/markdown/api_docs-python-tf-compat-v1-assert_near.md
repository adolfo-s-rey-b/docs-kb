[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_near#main-content)

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
    

tf.compat.v1.assert\_near Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L858-L939)

Assert the condition `x` and `y` are close element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.assert_near`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_near)

tf.compat.v1.assert_near(
        x,
        y,
        rtol=None,
        atol=None,
        data=None,
        summarize=None,
        message=None,
        name=None
    )

Example of adding a dependency to an operation:

with tf.control_dependencies([tf.compat.v1.assert_near(x, y)]):
      output = tf.reduce_sum(x)

This condition holds if for every pair of (possibly broadcast) elements `x[i]`, `y[i]`, we have

`tf.abs(x[i] - y[i]) <= atol + rtol * tf.abs(y[i])`.

If both `x` and `y` are empty, this is trivially satisfied.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest representable positive number such that `1 + eps != 1`. This is about `1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`. See `numpy.finfo`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Float or complex `Tensor`. |
| `y` | Float or complex `Tensor`, same `dtype` as, and broadcastable to, `x`. |
| `rtol` | `Tensor`. Same `dtype` as, and broadcastable to, `x`. The relative tolerance. Default is `10 * eps`. |
| `atol` | `Tensor`. Same `dtype` as, and broadcastable to, `x`. The absolute tolerance. Default is `10 * eps`. |
| `data` | The tensors to print out if the condition is False. Defaults to error message and first few entries of `x`, `y`. |
| `summarize` | Print this many entries of each tensor. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_near". |

|     |
| --- |
| Returns<br>------- |     |
| Op that raises `InvalidArgumentError` if `x` and `y` are not close enough. |     |

numpy compatibility
-------------------

Similar to `numpy.testing.assert_allclose`, except tolerance depends on data type. This is due to the fact that `TensorFlow` is often used with `32bit`, `64bit`, and even `16bit` data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.