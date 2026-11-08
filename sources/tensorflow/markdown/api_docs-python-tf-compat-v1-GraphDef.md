[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#used-in-the-notebooks)
        
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.GraphDef Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#used-in-the-notebooks)
        
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/framework/graph.proto)

A protobuf containing the graph of operations.

Migrate to TF2
--------------

This API is not available in TensorFlow 2.x.

You should not need to use `GraphDef`s directly in TF2. To load `GraphDef`s in TF2, use SavedModel. The SavedModel contains the `GraphDef`.

Before:

with tf.io.gfile.GFile('/tmp/graph.pb', 'rb') as f:
      graph_def = tf.compat.v1.GraphDef()
      graph_def.ParseFromString(f.read())

After:

tf.saved_model.load('/tmp/saved_model')

If you would like to create a `GraphDef` in TF2, use [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 and `get_concrete_function`.

    @tf.function

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite) |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `debug_info` | `GraphDebugInfo debug_info` |
| `library` | `FunctionDefLibrary library` |
| `node` | `repeated NodeDef node` |
| `version` | `int32 version` |
| `versions` | `VersionDef versions` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.