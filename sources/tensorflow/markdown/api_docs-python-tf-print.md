[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/print#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/print)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/print?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/print#used-in-the-notebooks)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/print#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/print#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/print#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/print#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.print Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/print#used-in-the-notebooks)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/print#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/print#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/print#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/print#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/logging_ops.py#L147-L395)

Print the specified inputs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.print`](https://www.tensorflow.org/api_docs/python/tf/print)

tf.print(
        *inputs, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input) |

A TensorFlow operator that prints the specified inputs to a desired output stream or logging level. The inputs may be dense or sparse Tensors, primitive python objects, data structures that contain tensors, and printable Python objects. Printed tensors will recursively show the first and last elements of each dimension to summarize.

|     |
| --- |
| Example<br>------- |     |
| Single-input usage:<br><br>tensor = tf.range(10)<br>    tf.print(tensor, output_stream=sys.stderr)<br><br>(This prints "\[0 1 2 ... 7 8 9\]" to sys.stderr)<br><br>Multi-input usage:<br><br>tensor = tf.range(10)<br>    tf.print("tensors:", tensor, {2: tensor * 2}, output_stream=sys.stdout)<br><br>(This prints "tensors: \[0 1 2 ... 7 8 9\] {2: \[0 2 4 ... 14 16 18\]}" to sys.stdout)<br><br>Changing the input separator:<br><br>tensor_a = tf.range(2)<br>    tensor_b = tensor_a * 2<br>    tf.print(tensor_a, tensor_b, output_stream=sys.stderr, sep=',')<br><br>(This prints "\[0 1\],\[0 2\]" to sys.stderr)<br><br>Usage in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>:<br><br>@tf.function<br>    def f():<br>        tensor = tf.range(10)<br>        tf.print(tensor, output_stream=sys.stderr)<br>        return tensor<br>    <br>    range_tensor = f()<br><br>(This prints "\[0 1 2 ... 7 8 9\]" to sys.stderr) |     |

_Compatibility usage in TF 1.x graphs_:

In graphs manually created outside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, this method returns the created TF operator that prints the data. To make sure the operator runs, users need to pass the produced op to [`tf.compat.v1.Session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session)
's run method, or to use the op as a control dependency for executed ops by specifying `with tf.compat.v1.control_dependencies([print_op])`.

  tf.compat.v1.disable_v2_behavior()  # for TF1 compatibility only
    
      sess = tf.compat.v1.Session()
      with sess.as_default():
        tensor = tf.range(10)
        print_op = tf.print("tensors:", tensor, {2: tensor * 2},
                            output_stream=sys.stdout)
        with tf.control_dependencies([print_op]):
          tripled_tensor = tensor * 3
    
        sess.run(tripled_tensor)

(This prints "tensors: \[0 1 2 ... 7 8 9\] {2: \[0 2 4 ... 14 16 18\]}" to sys.stdout)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `*inputs` | Positional arguments that are the inputs to print. Inputs in the printed output will be separated by spaces. Inputs may be python primitives, tensors, data structures such as dicts and lists that may contain tensors (with the data structures possibly nested in arbitrary ways), and printable python objects. |
| `output_stream` | The output stream, logging level, or file to print to. Defaults to sys.stderr, but sys.stdout, tf.compat.v1.logging.info, tf.compat.v1.logging.warning, tf.compat.v1.logging.error, absl.logging.info, absl.logging.warning and absl.logging.error are also supported. To print to a file, pass a string started with "file://" followed by the file path, e.g., "file:///tmp/foo.out". |
| `summarize` | The first and last `summarize` elements within each dimension are recursively printed per Tensor. If None, then the first 3 and last 3 elements of each dimension are printed for each tensor. If set to -1, it will print all elements of every tensor. |
| `sep` | The string to use to separate the inputs. Defaults to " ". |
| `end` | End character that is appended at the end the printed string. Defaults to the newline character. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| None when executing eagerly. During graph tracing this returns a TF operator that prints the specified inputs in the specified output stream or logging level. This operator will be automatically executed except inside of [`tf.compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)<br> graphs and sessions. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If an unsupported output stream is specified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.