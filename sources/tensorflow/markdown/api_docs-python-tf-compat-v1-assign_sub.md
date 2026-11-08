[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fassign_sub&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assign\_sub Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/state_ops.py#L133-L202)

Update `ref` by subtracting `value` from it.

tf.compat.v1.assign_sub(
        ref, value, use_locking=None, name=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.assign_sub`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign_sub)
 is mostly compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

To switch to the native TF2 style, one could use method 'assign\_sub' of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
:

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `ref` | `self` | In `assign_sub()` method |
| `value` | `value` | In `assign_sub()` method |
| `use_locking` | `use_locking` | In `assign_sub()` method |
| `name` | `name` | In `assign_sub()` method |
| \-  | `read_value` | Set to True to replicate behavior (True is default) |

#### Before & After Usage Example

Before:

    with tf.Graph().as_default():

After:

    b = tf.Variable(1, dtype=tf.int64)

Description
-----------

This operation outputs `ref` after the update is done. This makes it easier to chain operations that need to use the reset value. Unlike [`tf.math.subtract`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)
, this op does not broadcast. `ref` and `value` must have the same shape.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ref` | A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be from a `Variable` node. |
| `value` | A `Tensor`. Must have the same shape and dtype as `ref`. The value to be subtracted to the variable. |
| `use_locking` | An optional `bool`. Defaults to `False`. If True, the subtraction will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| Same as `ref`. Returned as a convenience for operations that want to use the new value after the variable has been updated. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.