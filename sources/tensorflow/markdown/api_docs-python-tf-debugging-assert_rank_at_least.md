[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_rank\_at\_least Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1162-L1193)

Assert that `x` has rank of at least `rank`.

tf.debugging.assert_rank_at_least(
        x, rank, message=None, name=None
    )

This Op checks that the rank of `x` is greater or equal to `rank`.

If `x` has a rank lower than `rank`, `message`, as well as the shape of `x` are printed, and `InvalidArgumentError` is raised.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | `Tensor`. |
| `rank` | Scalar integer `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_rank\_at\_least". |

|     |
| --- |
| Returns<br>------- |     |
| Op raising `InvalidArgumentError` unless `x` has specified rank or higher. If static checks determine `x` has correct rank, a `no_op` is returned. This can be used with [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)<br> inside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>s to block followup computation until the check has executed. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | `x` does not have rank at least `rank`, but the rank cannot be statically determined. |
| `ValueError` | If static checks determine `x` has mismatched rank. |

eager compatibility
-------------------

returns None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.