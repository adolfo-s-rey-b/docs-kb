[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/MultiGraphNodeProto#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/MultiGraphNodeProto)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/MultiGraphNodeProto?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/MultiGraphNodeProto#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.profiler.MultiGraphNodeProto Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/MultiGraphNodeProto#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/profiler/tfprof_output.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `accelerator_exec_micros` | `int64 accelerator_exec_micros` |
| `children` | `repeated MultiGraphNodeProto children` |
| `cpu_exec_micros` | `int64 cpu_exec_micros` |
| `exec_micros` | `int64 exec_micros` |
| `float_ops` | `int64 float_ops` |
| `graph_nodes` | `repeated GraphNodeProto graph_nodes` |
| `name` | `string name` |
| `output_bytes` | `int64 output_bytes` |
| `parameters` | `int64 parameters` |
| `peak_bytes` | `int64 peak_bytes` |
| `requested_bytes` | `int64 requested_bytes` |
| `residual_bytes` | `int64 residual_bytes` |
| `total_accelerator_exec_micros` | `int64 total_accelerator_exec_micros` |
| `total_cpu_exec_micros` | `int64 total_cpu_exec_micros` |
| `total_exec_micros` | `int64 total_exec_micros` |
| `total_float_ops` | `int64 total_float_ops` |
| `total_output_bytes` | `int64 total_output_bytes` |
| `total_parameters` | `int64 total_parameters` |
| `total_peak_bytes` | `int64 total_peak_bytes` |
| `total_requested_bytes` | `int64 total_requested_bytes` |
| `total_residual_bytes` | `int64 total_residual_bytes` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.