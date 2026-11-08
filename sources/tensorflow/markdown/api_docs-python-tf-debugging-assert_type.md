[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fassert_type&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.assert\_type Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1494-L1526)

Asserts that the given `Tensor` is of the specified type.

tf.debugging.assert_type(
        tensor, tf_type, message=None, name=None
    )

This can always be checked statically, so this method returns nothing.

#### Example:

    a = tf.Variable(1.0)

    b = tf.constant(21)

    c = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2],

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`, `SparseTensor` or [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> . |
| `tf_type` | A tensorflow type ([`dtypes.float32`](https://www.tensorflow.org/api_docs/python/tf/dtypes#float32)<br>, [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>, [`dtypes.bool`](https://www.tensorflow.org/api_docs/python/tf/dtypes#bool)<br>, etc). |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation. Defaults to "assert\_type" |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the tensor's data type doesn't match `tf_type`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.