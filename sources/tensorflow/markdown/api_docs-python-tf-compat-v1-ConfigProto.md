[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ConfigProto Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/config.proto)

A ProtocolMessage

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate multi-worker CPU/GPU training](https://www.tensorflow.org/guide/migrate/multi_worker_cpu_gpu_training) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD) |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `allow_soft_placement` | `bool allow_soft_placement` |
| `cluster_def` | `ClusterDef cluster_def` |
| `device_count` | `repeated DeviceCountEntry device_count` |
| `device_filters` | `repeated string device_filters` |
| `experimental` | `Experimental experimental` |
| `gpu_options` | `GPUOptions gpu_options` |
| `graph_options` | `GraphOptions graph_options` |
| `inter_op_parallelism_threads` | `int32 inter_op_parallelism_threads` |
| `intra_op_parallelism_threads` | `int32 intra_op_parallelism_threads` |
| `isolate_session_state` | `bool isolate_session_state` |
| `log_device_placement` | `bool log_device_placement` |
| `operation_timeout_in_ms` | `int64 operation_timeout_in_ms` |
| `placement_period` | `int32 placement_period` |
| `pluggable_device_options` | `GPUOptions pluggable_device_options` |
| `rpc_options` | `RPCOptions rpc_options` |
| `session_inter_op_thread_pool` | `repeated ThreadPoolOptionProto session_inter_op_thread_pool` |
| `share_cluster_devices_in_session` | `bool share_cluster_devices_in_session` |
| `use_per_session_threads` | `bool use_per_session_threads` |

Child Classes
-------------

[`class DeviceCountEntry`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/DeviceCountEntry)

[`class Experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.