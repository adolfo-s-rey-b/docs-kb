[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assert\_rank\_in Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1362-L1431)

Assert `x` has rank in `ranks`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.assert_rank_in`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_rank_in)

tf.compat.v1.assert_rank_in(
        x, ranks, data=None, summarize=None, message=None, name=None
    )

Example of adding a dependency to an operation:

with tf.control_dependencies([tf.compat.v1.assert_rank_in(x, (2, 4))]):
      output = tf.reduce_sum(x)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `ranks` | Iterable of scalar `Tensor` objects. |
| `data` | The tensors to print out if the condition is False. Defaults to error message and first few entries of `x`. |
| `summarize` | Print this many entries of each tensor. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_rank\_in". |

|     |
| --- |
| Returns<br>------- |     |
| Op raising `InvalidArgumentError` unless rank of `x` is in `ranks`. If static checks determine `x` has matching rank, a `no_op` is returned. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If static checks determine `x` has mismatched rank. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.