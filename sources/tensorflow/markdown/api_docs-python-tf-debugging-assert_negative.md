[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fassert_negative&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_negative Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L543-L573)

Assert the condition `x < 0` holds element-wise.

tf.debugging.assert_negative(
        x, message=None, summarize=None, name=None
    )

This Op checks that `x[i] < 0` holds for every element of `x`. If `x` is empty, this is trivially satisfied.

If `x` is not negative everywhere, `message`, as well as the first `summarize` entries of `x` are printed, and `InvalidArgumentError` is raised.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `message` | A string to prefix to the default message. |
| `summarize` | Print this many entries of each tensor. |
| `name` | A name for this operation (optional). Defaults to "assert\_negative". |

|     |
| --- |
| Returns<br>------- |     |
| Op raising `InvalidArgumentError` unless `x` is all negative. This can be used with [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)<br> inside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s to block followup computation until the check has executed. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if the check can be performed immediately and `x[i] < 0` is False. The check can be performed immediately during eager execution or if `x` is statically known. |

eager compatibility
-------------------

returns None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.