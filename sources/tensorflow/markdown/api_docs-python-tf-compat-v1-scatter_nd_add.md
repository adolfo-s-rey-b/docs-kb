[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fscatter_nd_add&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.scatter\_nd\_add Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_nd_add#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/state_ops.py#L551-L611)

Applies sparse addition to individual values or slices in a Variable.

tf.compat.v1.scatter_nd_add(
        ref, indices, updates, use_locking=False, name=None
    )

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`. It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]]

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8 elements. In Python, that addition would look like this:

ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1], [7]])
    updates = tf.constant([9, 10, 11, 12])
    add = tf.compat.v1.scatter_nd_add(ref, indices, updates)
    with tf.compat.v1.Session() as sess:
      print sess.run(add)

The resulting update to ref would look like this:

[1, 13, 3, 14, 14, 6, 7, 20]

See [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd)
 for more details about how to make updates to slices.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ref` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. A mutable Tensor. Should be from a Variable node. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A tensor of indices into ref. |
| `updates` | A `Tensor`. Must have the same type as `ref`. A tensor of updated values to add to ref. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, the assignment will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A mutable `Tensor`. Has the same type as `ref`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.