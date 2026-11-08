[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2FGPUOptions%2FExperimental&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.GPUOptions.Experimental Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/config.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `collective_ring_order` | `string collective_ring_order` |
| `disallow_retry_on_allocation_failure` | `bool disallow_retry_on_allocation_failure` |
| `gpu_host_mem_disallow_growth` | `bool gpu_host_mem_disallow_growth` |
| `gpu_host_mem_limit_in_mb` | `float gpu_host_mem_limit_in_mb` |
| `gpu_system_memory_size_in_mb` | `int32 gpu_system_memory_size_in_mb` |
| `internal_fragmentation_fraction` | `double internal_fragmentation_fraction` |
| `kernel_tracker_max_bytes` | `int32 kernel_tracker_max_bytes` |
| `kernel_tracker_max_interval` | `int32 kernel_tracker_max_interval` |
| `kernel_tracker_max_pending` | `int32 kernel_tracker_max_pending` |
| `node_id` | `int32 node_id` |
| `num_dev_to_dev_copy_streams` | `int32 num_dev_to_dev_copy_streams` |
| `num_virtual_devices_per_gpu` | `int32 num_virtual_devices_per_gpu` |
| `populate_pjrt_gpu_client_creation_info` | `bool populate_pjrt_gpu_client_creation_info` |
| `stream_merge_options` | `StreamMergeOptions stream_merge_options` |
| `timestamped_allocator` | `bool timestamped_allocator` |
| `use_cuda_malloc_async` | `bool use_cuda_malloc_async` |
| `use_unified_memory` | `bool use_unified_memory` |
| `virtual_devices` | `repeated VirtualDevices virtual_devices` |

Child Classes
-------------

[`class StreamMergeOptions`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental/StreamMergeOptions)

[`class VirtualDevices`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GPUOptions/Experimental/VirtualDevices)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.