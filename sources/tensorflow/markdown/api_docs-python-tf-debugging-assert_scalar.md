[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_scalar Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L2161-L2181)

Asserts that the given `tensor` is a scalar.

tf.debugging.assert_scalar(
        tensor, message=None, name=None
    )

This function raises `ValueError` unless it can be certain that the given `tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is unknown.

This is always checked statically, so this method returns nothing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation. Defaults to "assert\_scalar" |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the tensor is not scalar (rank 0), or if its shape is unknown. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.