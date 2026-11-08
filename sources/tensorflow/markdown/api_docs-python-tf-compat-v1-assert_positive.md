[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assert\_positive Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L630-L647)

Assert the condition `x > 0` holds element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.assert_positive`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_positive)

tf.compat.v1.assert_positive(
        x, data=None, summarize=None, message=None, name=None
    )

When running in graph mode, you should add a dependency on this operation to ensure that it runs. Example of adding a dependency to an operation:

with tf.control_dependencies([tf.debugging.assert_positive(x, y)]):
      output = tf.reduce_sum(x)

Positive means, for every element `x[i]` of `x`, we have `x[i] > 0`. If `x` is empty this is trivially satisfied.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `data` | The tensors to print out if the condition is False. Defaults to error message and first few entries of `x`. |
| `summarize` | Print this many entries of each tensor. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_positive". |

|     |
| --- |
| Returns<br>------- |     |
| Op that raises `InvalidArgumentError` if `x > 0` is False. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if the check can be performed immediately and `x > 0` is False. The check can be performed immediately during eager execution or if `x` is statically known. |

eager compatibility
-------------------

returns None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.