[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.RunMetadata Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/config.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `cost_graph` | `CostGraphDef cost_graph` |
| `function_graphs` | `repeated FunctionGraphs function_graphs` |
| `partition_graphs` | `repeated GraphDef partition_graphs` |
| `session_metadata` | `SessionMetadata session_metadata` |
| `step_stats` | `StepStats step_stats` |

Child Classes
-------------

[`class FunctionGraphs`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/RunMetadata/FunctionGraphs)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.