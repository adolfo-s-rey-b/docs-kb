[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.graph Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/graph?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L1069-L1135)

Writes a TensorFlow graph summary.

tf.summary.graph(
        graph_data
    )

Write an instance of [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
 or [`tf.compat.v1.GraphDef`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef)
 as summary only in an eager mode. Please prefer to use the trace APIs ([`tf.summary.trace_on`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on)
, [`tf.summary.trace_off`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_off)
, and [`tf.summary.trace_export`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export)
) when using [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 which can automatically collect and record graphs from executions.

#### Usage Example:

writer = tf.summary.create_file_writer("/tmp/mylogs")
    
    @tf.function
    def f():
      x = constant_op.constant(2)
      y = constant_op.constant(3)
      return x**y
    
    with writer.as_default():
      tf.summary.graph(f.get_concrete_function().graph)
    
    # Another example: in a very rare use case, when you are dealing with a TF v1
    # graph.
    graph = tf.Graph()
    with graph.as_default():
      c = tf.constant(30.0)
    with writer.as_default():
      tf.summary.graph(graph)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph_data` | The TensorFlow graph to write, as a [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)<br> or a [`tf.compat.v1.GraphDef`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or False if no summary was written because no default summary writer was available. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | `graph` summary API is invoked in a graph mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.