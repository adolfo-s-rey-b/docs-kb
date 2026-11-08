[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/name_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/name_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/name_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/name_scope#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/name_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/name_scope#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/name_scope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/name_scope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.name\_scope Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/name_scope#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/name_scope#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/name_scope#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/name_scope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/name_scope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5745-L5837)

A context manager for use when defining a Python op.

tf.name_scope(
        name
    ) -> None

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints) | *   [Displaying text data in TensorBoard](https://www.tensorflow.org/tensorboard/text_summaries)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

This context manager pushes a name scope, which will make the name of all operations added within it have a prefix.

For example, to define a new Python op called `my_op`:

def my_op(a, b, c, name=None):
      with tf.name_scope("MyOp") as scope:
        a = tf.convert_to_tensor(a, name="a")
        b = tf.convert_to_tensor(b, name="b")
        c = tf.convert_to_tensor(c, name="c")
        # Define some computation that uses `a`, `b`, and `c`.
        return foo_op(..., name=scope)

When executed, the Tensors `a`, `b`, `c`, will have names `MyOp/a`, `MyOp/b`, and `MyOp/c`.

Inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, if the scope name already exists, the name will be made unique by appending `_n`. For example, calling `my_op` the second time will generate `MyOp_1/a`, etc.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The prefix to use on all names created within the name scope. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If name is not a string. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` |     |

Methods
-------

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5792-L5824)

__enter__() -> str

Start the scope block.

|     |
| --- |
| Returns |     |
| The scope name. |     |

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5826-L5830)

__exit__(
        type_arg: None, value_arg: None, traceback_arg: None
    ) -> bool

Raise any exception triggered within the runtime context.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.