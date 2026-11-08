[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.scatter\_sub Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/scatter_sub#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/state_ops.py#L614-L665)

Subtracts sparse updates to a variable reference.

tf.compat.v1.scatter_sub(
        ref, indices, updates, use_locking=False, name=None
    )

    # Scalar indices
        ref[indices, ...] -= updates[...]
    
        # Vector indices (for each i)
        ref[indices[i], ...] -= updates[i, ...]
    
        # High rank indices (for each i, ..., j)
        ref[indices[i, ..., j], ...] -= updates[i, ..., j, ...]

This operation outputs `ref` after the update is done. This makes it easier to chain operations that need to use the reset value.

Duplicate entries are handled correctly: if multiple `indices` reference the same location, their (negated) contributions add.

Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

![](https://www.tensorflow.org/images/ScatterSub.png)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ref` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. Should be from a `Variable` node. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A tensor of indices into the first dimension of `ref`. |
| `updates` | A `Tensor`. Must have the same type as `ref`. A tensor of updated values to subtract from `ref`. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, the subtraction will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
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