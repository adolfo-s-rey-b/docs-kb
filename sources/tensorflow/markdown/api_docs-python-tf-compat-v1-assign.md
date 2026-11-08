[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assign Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/state_ops.py#L277-L356)

Update `ref` by assigning `value` to it.

tf.compat.v1.assign(
        ref, value, validate_shape=None, use_locking=None, name=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.assign`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assign)
 is mostly compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. However, argument 'validate\_shape' will be ignored. To avoid shape validation, set 'shape' to tf.TensorShape(None) when constructing the variable:

    import tensorflow as tf

To switch to the native TF2 style, one could use method 'assign' of [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
:

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `ref` | `self` | In `assign()` method |
| `value` | `value` | In `assign()` method |
| `validate_shape` | Not supported | Specify `shape` in the constructor to replicate behavior |
| `use_locking` | `use_locking` | In `assign()` method |
| `name` | `name` | In `assign()` method |
| \-  | `read_value` | Set to True to replicate behavior (True is default) |

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial) |

This operation outputs a Tensor that holds the new value of `ref` after the value has been assigned. This makes it easier to chain operations that need to use the reset value.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ref` | A mutable `Tensor`. Should be from a `Variable` node. May be uninitialized. |
| `value` | A `Tensor`. Must have the same shape and dtype as `ref`. The value to be assigned to the variable. |
| `validate_shape` | An optional `bool`. Defaults to `True`. If true, the operation will validate that the shape of 'value' matches the shape of the Tensor being assigned to. If false, 'ref' will take on the shape of 'value'. |
| `use_locking` | An optional `bool`. Defaults to `True`. If True, the assignment will be protected by a lock; otherwise the behavior is undefined, but may exhibit less contention. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` that will hold the new value of `ref` after the assignment has completed. |     |

#### Before & After Usage Example

#### Before:

    with tf.Graph().as_default():

#### After:

    b = tf.Variable(0, dtype=tf.int64)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.