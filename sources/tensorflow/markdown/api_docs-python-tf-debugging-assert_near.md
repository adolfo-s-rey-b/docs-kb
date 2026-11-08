[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fassert_near&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#eager-compatibility)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_near Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#eager-compatibility)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L803-L855)

Assert the condition `x` and `y` are close element-wise.

tf.debugging.assert_near(
        x, y, rtol=None, atol=None, message=None, summarize=None, name=None
    )

This Op checks that `x[i] - y[i] < atol + rtol * tf.abs(y[i])` holds for every pair of (possibly broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is trivially satisfied.

If any elements of `x` and `y` are not close, `message`, as well as the first `summarize` entries of `x` and `y` are printed, and `InvalidArgumentError` is raised.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest representable positive number such that `1 + eps != 1`. This is about `1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`. See `numpy.finfo`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Float or complex `Tensor`. |
| `y` | Float or complex `Tensor`, same dtype as and broadcastable to `x`. |
| `rtol` | `Tensor`. Same `dtype` as, and broadcastable to, `x`. The relative tolerance. Default is `10 * eps`. |
| `atol` | `Tensor`. Same `dtype` as, and broadcastable to, `x`. The absolute tolerance. Default is `10 * eps`. |
| `message` | A string to prefix to the default message. |
| `summarize` | Print this many entries of each tensor. |
| `name` | A name for this operation (optional). Defaults to "assert\_near". |

|     |
| --- |
| Returns<br>------- |     |
| Op that raises `InvalidArgumentError` if `x` and `y` are not close enough. This can be used with [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)<br> inside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s to block followup computation until the check has executed. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if the check can be performed immediately and `x != y` is False for any pair of elements in `x` and `y`. The check can be performed immediately during eager execution or if `x` and `y` are statically known. |

eager compatibility
-------------------

returns None

numpy compatibility
-------------------

Similar to `numpy.testing.assert_allclose`, except tolerance depends on data type. This is due to the fact that `TensorFlow` is often used with `32bit`, `64bit`, and even `16bit` data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.