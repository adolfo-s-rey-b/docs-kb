[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#description)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_default\_graph Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#description)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5142-L5167)

Returns the default graph for the current thread.

tf.compat.v1.get_default_graph() -> tf.Graph

Migrate to TF2
--------------

`get_default_graph` does not work with either eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, and you should not invoke it directly. To migrate code that uses Graph-related functions to TF2, rewrite the code without them. See the [migration guide](https://www.tensorflow.org/guide/migrate)
 for more description about the behavior and semantic changes between Tensorflow 1 and Tensorflow 2.

Description
-----------

The returned graph will be the innermost graph on which a [`Graph.as_default()`](https://www.tensorflow.org/api_docs/python/tf/Graph#as_default)
 context has been entered, or a global default graph if none has been explicitly created.

|     |
| --- |
| Returns<br>------- |     |
| The default `Graph` being used in the current thread. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.