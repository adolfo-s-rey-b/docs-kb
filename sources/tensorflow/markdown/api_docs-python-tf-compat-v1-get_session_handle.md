[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_session\_handle Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_handle#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/session_ops.py#L136-L176)

Return the handle of `data`.

tf.compat.v1.get_session_handle(
        data, name=None
    )

This is EXPERIMENTAL and subject to change.

Keep `data` "in-place" in the runtime and create a handle that can be used to retrieve `data` in a subsequent run().

Combined with `get_session_tensor`, we can keep a tensor produced in one run call in place, and use it as the input in a future run call.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A tensor to be stored in the session. |
| `name` | Optional name prefix for the return tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar string tensor representing a unique handle for `data`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `data` is not a Tensor. |

#### Example:

c = tf.multiply(a, b)
    h = tf.compat.v1.get_session_handle(c)
    h = sess.run(h)
    
    p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
    b = tf.multiply(a, 10)
    c = sess.run(b, feed_dict={p: h.handle})

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.