[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fdelete_session_tensor&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.delete\_session\_tensor Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/delete_session_tensor#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/session_ops.py#L220-L241)

Delete the tensor for the given tensor handle.

tf.compat.v1.delete_session_tensor(
        handle, name=None
    )

This is EXPERIMENTAL and subject to change.

Delete the tensor of a given tensor handle. The tensor is produced in a previous run() and stored in the state of the session.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `handle` | The string representation of a persistent tensor handle. |
| `name` | Optional name prefix for the return tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A pair of graph elements. The first is a placeholder for feeding a tensor handle and the second is a deletion operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.