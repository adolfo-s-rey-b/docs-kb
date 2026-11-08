[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ConfigProto.Experimental Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConfigProto/Experimental#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/config.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `backend_server_port` | `int32 backend_server_port` |
| `collective_deterministic_sequential_execution` | `bool collective_deterministic_sequential_execution` |
| `collective_group_leader` | `string collective_group_leader` |
| `collective_nccl` | `bool collective_nccl` |
| `coordination_config` | `CoordinationServiceConfig coordination_config` |
| `disable_eager_executor_streaming_enqueue` | `bool disable_eager_executor_streaming_enqueue` |
| `disable_functional_ops_lowering` | `bool disable_functional_ops_lowering` |
| `disable_optimize_for_static_graph` | `bool disable_optimize_for_static_graph` |
| `disable_output_partition_graphs` | `bool disable_output_partition_graphs` |
| `disable_thread_spinning` | `bool disable_thread_spinning` |
| `enable_mlir_bridge` | `bool enable_mlir_bridge` |
| `enable_mlir_graph_optimization` | `bool enable_mlir_graph_optimization` |
| `enable_multi_host` | `bool enable_multi_host` |
| `executor_type` | `string executor_type` |
| `finalize_function_library_runtime` | `bool finalize_function_library_runtime` |
| `finalize_resource_manager` | `bool finalize_resource_manager` |
| `mlir_bridge_rollout` | `MlirBridgeRollout mlir_bridge_rollout` |
| `online_cost_analysis` | `bool online_cost_analysis` |
| `optimize_for_static_graph` | `bool optimize_for_static_graph` |
| `recv_buf_max_chunk` | `int32 recv_buf_max_chunk` |
| `session_metadata` | `SessionMetadata session_metadata` |
| `share_cluster_devices_in_session` | `bool share_cluster_devices_in_session` |
| `share_session_state_in_clusterspec_propagation` | `bool share_session_state_in_clusterspec_propagation` |
| `stream_merge_threshold` | `int32 stream_merge_threshold` |
| `target_gpu` | `bool target_gpu` |
| `target_tpu` | `bool target_tpu` |
| `tf2xla_dump_dir` | `string tf2xla_dump_dir` |
| `tfrt_use_ifrt` | `bool tfrt_use_ifrt` |
| `use_numa_affinity` | `bool use_numa_affinity` |
| `use_tfrt` | `bool use_tfrt` |
| `xla_fusion_autotuner_thresh` | `int64 xla_fusion_autotuner_thresh` |
| `xla_prefer_single_graph_cluster` | `bool xla_prefer_single_graph_cluster` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.