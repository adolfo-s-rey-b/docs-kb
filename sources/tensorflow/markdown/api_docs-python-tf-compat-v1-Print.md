[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.Print Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Print#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/logging_ops.py#L67-L121)

Prints a list of tensors. (deprecated)

tf.compat.v1.Print(
        input_, data, message=None, first_n=None, summarize=None, name=None
    )

Migrate to TF2
--------------

This API is deprecated. Use [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
 instead. [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
 does not need the `input_` argument.

[`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
 works in TF2 when executing eagerly and inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

In TF1-styled sessions, an explicit control dependency declaration is needed to execute the [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
 operation. Refer to the documentation of [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
 for more details.

Description
-----------

This is an identity op (behaves like [`tf.identity`](https://www.tensorflow.org/api_docs/python/tf/identity)
) with the side effect of printing `data` when evaluating.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_` | A tensor passed through this op. |
| `data` | A list of tensors to print out when op is evaluated. |
| `message` | A string, prefix of the error message. |
| `first_n` | Only log `first_n` number of times. Negative numbers log always; this is the default. |
| `summarize` | Only print this many entries of each tensor. If None, then a maximum of 3 elements are printed per input tensor. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type and contents as `input_`.<br><br>sess = tf.compat.v1.Session()<br>    with sess.as_default():<br>        tensor = tf.range(10)<br>        print_op = tf.print(tensor)<br>        with tf.control_dependencies([print_op]):<br>          out = tf.add(tensor, tensor)<br>        sess.run(out) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.