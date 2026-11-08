[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.MetaGraphDef Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/meta_graph.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `asset_file_def` | `repeated AssetFileDef asset_file_def` |
| `collection_def` | `repeated CollectionDefEntry collection_def` |
| `graph_def` | `GraphDef graph_def` |
| `meta_info_def` | `MetaInfoDef meta_info_def` |
| `object_graph_def` | `SavedObjectGraph object_graph_def` |
| `saver_def` | `SaverDef saver_def` |
| `signature_def` | `repeated SignatureDefEntry signature_def` |

Child Classes
-------------

[`class CollectionDefEntry`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef/CollectionDefEntry)

[`class MetaInfoDef`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef/MetaInfoDef)

[`class SignatureDefEntry`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/MetaGraphDef/SignatureDefEntry)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.