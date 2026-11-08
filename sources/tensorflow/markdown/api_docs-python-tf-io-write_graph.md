[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/write_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/write_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/write_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/write_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/write_graph#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.write\_graph Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/write_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/write_graph#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/graph_io.py#L28-L84)

Writes a graph proto to a file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.write_graph`](https://www.tensorflow.org/api_docs/python/tf/io/write_graph)
, [`tf.compat.v1.train.write_graph`](https://www.tensorflow.org/api_docs/python/tf/io/write_graph)

tf.io.write_graph(
        graph_or_graph_def, logdir, name, as_text=True
    )

The graph is written as a text proto unless `as_text` is `False`.

v = tf.Variable(0, name='my_variable')
    sess = tf.compat.v1.Session()
    tf.io.write_graph(sess.graph_def, '/tmp/my-model', 'train.pbtxt')

or

v = tf.Variable(0, name='my_variable')
    sess = tf.compat.v1.Session()
    tf.io.write_graph(sess.graph, '/tmp/my-model', 'train.pbtxt')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph_or_graph_def` | A `Graph` or a `GraphDef` protocol buffer. |
| `logdir` | Directory where to write the graph. This can refer to remote filesystems, such as Google Cloud Storage (GCS). |
| `name` | Filename for the graph. |
| `as_text` | If `True`, writes the graph as an ASCII proto. |

|     |
| --- |
| Returns<br>------- |     |
| The path of the output proto file. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.