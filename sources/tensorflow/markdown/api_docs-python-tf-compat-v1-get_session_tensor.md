[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_session_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_session\_tensor Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/session_ops.py#L179-L217)

Get the tensor of type `dtype` by feeding a tensor handle.

tf.compat.v1.get_session_tensor(
        handle, dtype, name=None
    )

This is EXPERIMENTAL and subject to change.

Get the value of the tensor from a tensor handle. The tensor is produced in a previous run() and stored in the state of the session.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `handle` | The string representation of a persistent tensor handle. |
| `dtype` | The type of the output tensor. |
| `name` | Optional name prefix for the return tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A pair of tensors. The first is a placeholder for feeding a tensor handle and the second is the tensor in the session state keyed by the tensor handle. |     |

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