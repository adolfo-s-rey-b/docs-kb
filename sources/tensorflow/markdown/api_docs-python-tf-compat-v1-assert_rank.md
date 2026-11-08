[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assert\_rank Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1098-L1159)

Assert `x` has rank equal to `rank`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.assert_rank`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank)

tf.compat.v1.assert_rank(
        x, rank, data=None, summarize=None, message=None, name=None
    )

Example of adding a dependency to an operation:

with tf.control_dependencies([tf.compat.v1.assert_rank(x, 2)]):
      output = tf.reduce_sum(x)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `rank` | Scalar integer `Tensor`. |
| `data` | The tensors to print out if the condition is False. Defaults to error message and the shape of `x`. |
| `summarize` | Print this many entries of each tensor. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_rank". |

|     |
| --- |
| Returns<br>------- |     |
| Op raising `InvalidArgumentError` unless `x` has specified rank. If static checks determine `x` has correct rank, a `no_op` is returned. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If static checks determine `x` has wrong rank. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.