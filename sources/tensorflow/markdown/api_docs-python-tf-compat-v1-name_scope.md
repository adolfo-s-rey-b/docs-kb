[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.name\_scope Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/name_scope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5659-L5707)

A context manager for use when defining a Python op.

tf.compat.v1.name_scope(
        name, default_name=None, values=None
    ) -> None

This context manager validates that the given `values` are from the same graph, makes that graph the default graph, and pushes a name scope in that graph (see [`tf.Graph.name_scope`](https://www.tensorflow.org/api_docs/python/tf/Graph#name_scope)
 for more details on that).

For example, to define a new Python op called `my_op`:

def my_op(a, b, c, name=None):
      with tf.name_scope(name, "MyOp", [a, b, c]) as scope:
        a = tf.convert_to_tensor(a, name="a")
        b = tf.convert_to_tensor(b, name="b")
        c = tf.convert_to_tensor(c, name="c")
        # Define some computation that uses `a`, `b`, and `c`.
        return foo_op(..., name=scope)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The name argument that is passed to the op function. |
| `default_name` | The default name to use if the `name` argument is `None`. |
| `values` | The list of `Tensor` arguments that are passed to the op function. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `default_name` is passed in but not a string. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` |     |

Methods
-------

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5703-L5704)

__enter__() -> Optional[str]

Return `self` upon entering the runtime context.

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5706-L5707)

__exit__(
        *exc_info
    ) -> Optional[bool]

Raise any exception triggered within the runtime context.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.