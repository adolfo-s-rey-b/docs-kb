[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fassert_integer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_integer Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1434-L1452)

Assert that `x` is of integer dtype.

tf.debugging.assert_integer(
        x, message=None, name=None
    )

If `x` has a non-integer type, `message`, as well as the dtype of `x` are printed, and `InvalidArgumentError` is raised.

This can always be checked statically, so this method returns nothing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_integer". |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `x.dtype` is not a non-quantized integer type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.