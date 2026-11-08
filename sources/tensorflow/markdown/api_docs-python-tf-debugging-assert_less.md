[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_less Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L942-L947)

Assert the condition `x < y` holds element-wise.

#### View aliases

**Main aliases**

[`tf.assert_less`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less)

tf.debugging.assert_less(
        x, y, message=None, summarize=None, name=None
    )

This Op checks that `x[i] < y[i]` holds for every pair of (possibly broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is trivially satisfied.

If `x` < `y` does not hold, `message`, as well as the first `summarize` entries of `x` and `y` are printed, and `InvalidArgumentError` is raised.

When using inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, this API takes effects during execution. It's recommended to use this API with [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
 to ensure the correct execution order.

In the following example, without [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
, errors may not be raised at all. Check [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
 for more details.

    def check_size(x):

    check_size(tf.ones([2, 3], tf.float32))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `y` | Numeric `Tensor`, same dtype as and broadcastable to `x`. |
| `message` | A string to prefix to the default message. (optional) |
| `summarize` | Print this many entries of each tensor. (optional) |
| `name` | A name for this operation (optional). Defaults to "assert\_less". |

|     |
| --- |
| Returns<br>------- |     |
| Op that raises `InvalidArgumentError` if `x < y` is False. This can be used with [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)<br> inside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s to block followup computation until the check has executed. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if the check can be performed immediately and `x == y` is False. The check can be performed immediately during eager execution or if `x` and `y` are statically known. |

eager compatibility
-------------------

returns None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.