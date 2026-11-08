Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cuda.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cuda.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cuda.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cuda.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cuda.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cuda.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cuda.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cuda.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cuda.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cuda.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cuda.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cuda.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cuda.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cuda.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cuda.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cuda.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cuda.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cuda.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cuda.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cuda.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cuda.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cuda.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cuda.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cuda.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cuda.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cuda.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cuda.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cuda.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cuda.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cuda.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cuda.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cuda.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cuda.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cuda.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cuda.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cuda.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cuda.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cuda.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cuda.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cuda.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cuda.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cuda.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cuda.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cuda.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.cuda[#](https://docs.pytorch.org/docs/2.15/cuda.html#module-torch.cuda "Link to this heading")

=====================================================================================================

Created On: Dec 23, 2016 | Last Updated On: Sep 23, 2026

This package adds support for CUDA tensor types.

It implements the same function as CPU tensors, but they utilize GPUs for computation.

It is lazily initialized, so you can always import it, and use [`is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_available.html#torch.cuda.is_available "torch.cuda.is_available")
 to determine if your system supports CUDA.

[CUDA semantics](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics)
 has more details about working with CUDA.

|     |     |
| --- | --- |
| [`StreamContext`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.StreamContext.html#torch.cuda.StreamContext "torch.cuda.StreamContext") | Context-manager that selects a given stream. |
| [`can_device_access_peer`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.can_device_access_peer.html#torch.cuda.can_device_access_peer "torch.cuda.can_device_access_peer") | Check if peer access between two devices is possible. |
| [`check_error`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.check_error.html#torch.cuda.check_error "torch.cuda.check_error") | Raise an error if the result of a CUDA runtime API call is not success. |
| [`current_blas_handle`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_blas_handle.html#torch.cuda.current_blas_handle "torch.cuda.current_blas_handle") | Return the `cublasHandle_t` pointer for the current device and stream. |
| [`current_solver_handle`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_solver_handle.html#torch.cuda.current_solver_handle "torch.cuda.current_solver_handle") | Return cusolverDnHandle\_t pointer to current cuSOLVER handle |
| [`current_device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_device.html#torch.cuda.current_device "torch.cuda.current_device") | Return the index of a currently selected device. |
| [`current_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_stream.html#torch.cuda.current_stream "torch.cuda.current_stream") | Return the currently selected [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream")<br> for a given device. |
| [`cudart`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.cudart.html#torch.cuda.cudart "torch.cuda.cudart") | Retrieves the CUDA runtime API module. |
| [`default_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.default_stream.html#torch.cuda.default_stream "torch.cuda.default_stream") | Return the default [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream")<br> for a given device. |
| [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device.html#torch.cuda.device "torch.cuda.device") | Context-manager that changes the selected device. |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device_count.html#torch.cuda.device_count "torch.cuda.device_count") | Return the number of GPUs available. |
| [`device_memory_used`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device_memory_used.html#torch.cuda.device_memory_used "torch.cuda.device_memory_used") | Return used global (device) memory in bytes as given by nvidia-smi or amd-smi. |
| [`device_of`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device_of.html#torch.cuda.device_of "torch.cuda.device_of") | Context-manager that changes the current device to that of given object. |
| [`get_arch_list`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_arch_list.html#torch.cuda.get_arch_list "torch.cuda.get_arch_list") | Return list CUDA architectures this library was compiled for. |
| [`get_device_capability`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_device_capability.html#torch.cuda.get_device_capability "torch.cuda.get_device_capability") | Get the cuda capability of a device. |
| [`get_device_name`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_device_name.html#torch.cuda.get_device_name "torch.cuda.get_device_name") | Get the name of a device. |
| [`get_device_properties`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_device_properties.html#torch.cuda.get_device_properties "torch.cuda.get_device_properties") | Get the properties of a device. |
| [`get_gencode_flags`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_gencode_flags.html#torch.cuda.get_gencode_flags "torch.cuda.get_gencode_flags") | Return NVCC gencode flags this library was compiled with. |
| [`get_stream_from_external`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_stream_from_external.html#torch.cuda.get_stream_from_external "torch.cuda.get_stream_from_external") | Return a [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream")<br> from an externally allocated CUDA stream. |
| [`get_sync_debug_mode`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_sync_debug_mode.html#torch.cuda.get_sync_debug_mode "torch.cuda.get_sync_debug_mode") | Return current value of debug mode for cuda synchronizing operations. |
| [`init`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.init.html#torch.cuda.init "torch.cuda.init") | Initialize PyTorch's CUDA state. |
| [`ipc_collect`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ipc_collect.html#torch.cuda.ipc_collect "torch.cuda.ipc_collect") | Force collects GPU memory after it has been released by CUDA IPC. |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_available.html#torch.cuda.is_available "torch.cuda.is_available") | Return a bool indicating if CUDA is currently available. |
| [`is_bf16_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_bf16_supported.html#torch.cuda.is_bf16_supported "torch.cuda.is_bf16_supported") | Return a bool indicating if the current CUDA/ROCm device supports dtype bfloat16. |
| [`is_initialized`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_initialized.html#torch.cuda.is_initialized "torch.cuda.is_initialized") | Return whether PyTorch's CUDA state has been initialized. |
| [`is_tf32_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_tf32_supported.html#torch.cuda.is_tf32_supported "torch.cuda.is_tf32_supported") | Return a bool indicating if the current CUDA/ROCm device supports dtype tf32. |
| [`memory_usage`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory_usage.html#torch.cuda.memory_usage "torch.cuda.memory_usage") | Return the percent of time over the past sample period during which global (device) memory was being read or written as given by nvidia-smi. |
| [`set_device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_device.html#torch.cuda.set_device "torch.cuda.set_device") | Set the current device. |
| [`set_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_stream.html#torch.cuda.set_stream "torch.cuda.set_stream") | Set the current stream. This is a wrapper API to set the stream. |
| [`set_sync_debug_mode`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_sync_debug_mode.html#torch.cuda.set_sync_debug_mode "torch.cuda.set_sync_debug_mode") | Set the debug mode for cuda synchronizing operations. |
| [`stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.stream_function.html#torch.cuda.stream "torch.cuda.stream") | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.synchronize.html#torch.cuda.synchronize "torch.cuda.synchronize") | Wait for all kernels in all streams on a CUDA device to complete. |
| [`utilization`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.utilization.html#torch.cuda.utilization "torch.cuda.utilization") | Return the percent of time over the past sample period during which one or more kernels was executing on the GPU as given by nvidia-smi. |
| [`temperature`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.temperature.html#torch.cuda.temperature "torch.cuda.temperature") | Return the average temperature of the GPU sensor in Degrees C (Centigrades). |
| [`power_draw`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.power_draw.html#torch.cuda.power_draw "torch.cuda.power_draw") | Return the average power draw of the GPU sensor in mW (MilliWatts) |
| [`clock_rate`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.clock_rate.html#torch.cuda.clock_rate "torch.cuda.clock_rate") | Return the clock speed of the GPU SM in MHz (megahertz) over the past sample period as given by nvidia-smi. |
| [`AcceleratorError`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.AcceleratorError.html#torch.cuda.AcceleratorError "torch.cuda.AcceleratorError") | Exception raised while executing on device |
| [`OutOfMemoryError`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.OutOfMemoryError.html#torch.cuda.OutOfMemoryError "torch.cuda.OutOfMemoryError") | Exception raised when device is out of memory |

Random Number Generator[#](https://docs.pytorch.org/docs/2.15/cuda.html#random-number-generator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_rng_state.html#torch.cuda.get_rng_state "torch.cuda.get_rng_state") | Return the random number generator state of the specified GPU as a ByteTensor. |
| [`get_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.get_rng_state_all.html#torch.cuda.get_rng_state_all "torch.cuda.get_rng_state_all") | Return a list of ByteTensor representing the random number states of all devices. |
| [`set_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_rng_state.html#torch.cuda.set_rng_state "torch.cuda.set_rng_state") | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_rng_state_all.html#torch.cuda.set_rng_state_all "torch.cuda.set_rng_state_all") | Set the random number generator state of all devices. |
| [`manual_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.manual_seed.html#torch.cuda.manual_seed "torch.cuda.manual_seed") | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.manual_seed_all.html#torch.cuda.manual_seed_all "torch.cuda.manual_seed_all") | Set the seed for generating random numbers on all GPUs. |
| [`seed`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.seed.html#torch.cuda.seed "torch.cuda.seed") | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.seed_all.html#torch.cuda.seed_all "torch.cuda.seed_all") | Set the seed for generating random numbers to a random number on all GPUs. |
| [`initial_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.initial_seed.html#torch.cuda.initial_seed "torch.cuda.initial_seed") | Return the current random seed of the current GPU. |

Communication collectives[#](https://docs.pytorch.org/docs/2.15/cuda.html#communication-collectives "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`comm.broadcast`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.broadcast.html#torch.cuda.comm.broadcast "torch.cuda.comm.broadcast") | Broadcasts a tensor to specified GPU devices. |
| [`comm.broadcast_coalesced`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.broadcast_coalesced.html#torch.cuda.comm.broadcast_coalesced "torch.cuda.comm.broadcast_coalesced") | Broadcast a sequence of tensors to the specified GPUs. |
| [`comm.reduce_add`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.reduce_add.html#torch.cuda.comm.reduce_add "torch.cuda.comm.reduce_add") | Sum tensors from multiple GPUs. |
| [`comm.reduce_add_coalesced`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.reduce_add_coalesced.html#torch.cuda.comm.reduce_add_coalesced "torch.cuda.comm.reduce_add_coalesced") | Sum tensors from multiple GPUs. |
| [`comm.scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.scatter.html#torch.cuda.comm.scatter "torch.cuda.comm.scatter") | Scatters tensor across multiple GPUs. |
| [`comm.gather`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.comm.gather.html#torch.cuda.comm.gather "torch.cuda.comm.gather") | Gathers tensors from multiple GPU devices. |

Streams and events[#](https://docs.pytorch.org/docs/2.15/cuda.html#streams-and-events "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream") | Wrapper around a CUDA stream. |
| [`ExternalStream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream "torch.cuda.ExternalStream") | Wrapper around an externally allocated CUDA stream. |
| [`Event`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Event.html#torch.cuda.Event "torch.cuda.Event") | Wrapper around a CUDA event. |

Graphs (beta)[#](https://docs.pytorch.org/docs/2.15/cuda.html#graphs-beta "Link to this heading")

--------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`is_current_stream_capturing`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_current_stream_capturing.html#torch.cuda.is_current_stream_capturing "torch.cuda.is_current_stream_capturing") | Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise. |
| [`graph_pool_handle`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle "torch.cuda.graph_pool_handle") | Return an opaque token representing the id of a graph memory pool. |
| [`CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph") | Wrapper around a CUDA graph. |
| [`graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph") | Context-manager that captures CUDA work into a [`torch.cuda.CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")<br> object for later replay. |
| [`make_graphed_callables`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables") | Accept callables (functions or [`nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")<br>s) and returns graphed versions. |
| [`export_dot`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.export_dot.html#torch.cuda.export_dot "torch.cuda.export_dot") | Return a capture-end hook that dumps the captured graph to `path` in Graphviz DOT format. |
| [`export_graph_data`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.export_graph_data.html#torch.cuda.export_graph_data "torch.cuda.export_graph_data") | Return a post-instantiate hook that pickles [`CUDAGraph.get_graph_data()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.get_graph_data "torch.cuda.CUDAGraph.get_graph_data")<br> to `path`. |

### CUDA graph lifecycle hooks[#](https://docs.pytorch.org/docs/2.15/cuda.html#cuda-graph-lifecycle-hooks "Link to this heading")

Register callbacks that fire at each point in any CUDA graph’s lifecycle – capture start, capture end, instantiate, each replay, and destroy – for example, a profiler observing graph lifecycle without the graph code carrying any consumer knowledge, and including graphs the consumer did not build. Registering a hook is the opt-in and the whole API – the graph fires them; with none registered they are no-ops. Each has a per-graph counterpart on [`torch.cuda.CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
. Live in `torch.cuda.graphs`.

|     |     |
| --- | --- |
| [`register_graph_capture_start_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_capture_start_hook.html#torch.cuda.graphs.register_graph_capture_start_hook "torch.cuda.graphs.register_graph_capture_start_hook") | Register a hook run with each CUDA graph as its capture begins. |
| [`register_graph_capture_end_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_capture_end_hook.html#torch.cuda.graphs.register_graph_capture_end_hook "torch.cuda.graphs.register_graph_capture_end_hook") | Register a hook run with each CUDA graph when its capture ends, while the captured `cudaGraph_t` is still live (see [`CUDAGraph.register_capture_end_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph.register_capture_end_hook "torch.cuda.graphs.CUDAGraph.register_capture_end_hook")<br>). |
| [`register_graph_instantiate_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_instantiate_hook.html#torch.cuda.graphs.register_graph_instantiate_hook "torch.cuda.graphs.register_graph_instantiate_hook") | Register a hook run with each CUDA graph right after it is instantiated. |
| [`register_graph_replay_start_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_replay_start_hook.html#torch.cuda.graphs.register_graph_replay_start_hook "torch.cuda.graphs.register_graph_replay_start_hook") | Register a hook run with each CUDA graph at the start of every replay, just before it is launched. |
| [`register_graph_replay_end_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_replay_end_hook.html#torch.cuda.graphs.register_graph_replay_end_hook "torch.cuda.graphs.register_graph_replay_end_hook") | Register a hook run with each CUDA graph at the end of every replay, once the replay is _enqueued_ (the launch is asynchronous, so the GPU work has not completed). |
| [`register_graph_destroy_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graphs.register_graph_destroy_hook.html#torch.cuda.graphs.register_graph_destroy_hook "torch.cuda.graphs.register_graph_destroy_hook") | Register `fn(graph_ids)` to run when a CUDA graph is destroyed. |

Graph Kernel Annotations (prototype)[#](https://docs.pytorch.org/docs/2.15/cuda.html#graph-kernel-annotations-prototype "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

`torch.cuda.graph_annotations` annotates the kernels captured in a CUDA graph with user metadata, keyed so the annotations can be joined against the `graph node id` field on kernel events in profiler traces. Enable recording per capture with the `enable_annotations` argument of [`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
, then wrap regions of the captured workload in [`mark_kernels()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels "torch.cuda.graph_annotations.mark_kernels")
 scopes.

These APIs require the `cuda-bindings` package and a CUDA driver that supports `cudaGraphNodeGetToolsId` (CUDA 13.1 or newer, or an equivalent cuda-compat package); recording silently degrades to a no-op otherwise, and is not supported on ROCm. Use [`is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.is_available.html#torch.cuda.graph_annotations.is_available "torch.cuda.graph_annotations.is_available")
 to check support.

The end-to-end workflow: annotate during capture, profile the replay, then merge the annotations into the exported trace and view it in [Perfetto](https://ui.perfetto.dev/)
.

Note

Keep the graphs alive until all profiles using their annotations have been exported. For asynchronous Cuspy exports, also call `prof.wait_for_exports()` before resetting or destroying the graphs. Stopping the profiler or synchronizing CUDA alone does not guarantee that buffered profiling records have been processed. Resetting or destroying a graph removes its annotations, so pending profiles can lose that metadata. Save any Python launch stacks before graph cleanup as well.

During capture:

import torch
from torch.cuda.graph\_annotations import mark\_kernels, get\_kernel\_annotations

x \= torch.randn(1024, 1024, device\="cuda")

\# Warmup: run the workload once outside capture so lazy initialization
\# (e.g. cuBLAS handles) does not end up in -- or invalidate -- the capture.
y \= x @ x.t()
z \= torch.relu(y) @ x
torch.cuda.synchronize()

g \= torch.cuda.CUDAGraph()
with torch.cuda.graph(g, enable\_annotations\=True):
    with mark\_kernels("attention"):
        y \= x @ x.t()
    with mark\_kernels({"name": "mlp", "layer": 3}):
        z \= torch.relu(y) @ x

with torch.profiler.profile() as prof:
    g.replay()
    torch.cuda.synchronize()
prof.export\_chrome\_trace("trace.json")

Copy to clipboard

Each kernel event in the exported trace carries a `graph node id` in its `args`; the recorded annotations are keyed by the same ids, so merging them into the trace is a dictionary lookup:

import json

annotations \= get\_kernel\_annotations()
with open("trace.json") as f:
    trace \= json.load(f)
for event in trace\["traceEvents"\]:
    node\_id \= event.get("args", {}).get("graph node id")
    for ann in annotations.get(node\_id, \[\]):
        event\["args"\].update(ann)
with open("trace\_annotated.json", "w") as f:
    json.dump(trace, f)

Copy to clipboard

Opening `trace_annotated.json` in [Perfetto](https://ui.perfetto.dev/)
 (or `chrome://tracing`) and clicking a kernel from the graph replay now shows the annotation fields – `name: attention` or `name: mlp`, `layer: 3` – alongside the kernel’s grid and block sizes, identifying which region of the captured workload each kernel came from.

Because annotations live in a process-global registry keyed by ids that match the profiler’s, the pickle of `dict(get_kernel_annotations())` can equally be saved next to a trace and joined offline.

To capture Python launch stacks as well, set `annotation_config={"record_py_stacks": True}` with `enable_annotations=True`. Recording uses Cuspy’s CUPTI node-creation callbacks, even when no profiler session is running. It requires `cupti-python`, CUPTI >= 13.3, and a CUPTI subscription not already held by Kineto, Nsight Systems, or another profiler. Use Cuspy for subsequent GPU profiling in the same process. Disable autograd multithreading during both warmup and capture.

Stacks contain user Python frames on the launching thread for kernel, memcpy, memset, batch-memory, event, and host nodes. Framework and generated Inductor frames are omitted by default; C++ autograd nodes do not recover their forward Python stacks. Conditional and child-graph body stacks require `key_by="source"` (CUPTI and driver >= 13.4); they are omitted with `key_by="exec"`.

from torch.cuda.graph\_annotations import dump\_kernel\_py\_stacks

g \= torch.cuda.CUDAGraph()
with (
    torch.autograd.grad\_mode.set\_multithreading\_enabled(False),
    torch.cuda.graph(
        g, enable\_annotations\=True, annotation\_config\={"record\_py\_stacks": True}
    ),
):
    y \= x @ x.t()
dump\_kernel\_py\_stacks("graph\_stacks.json.gz")

Copy to clipboard

Use `annotation_config["py_stack_filter_paths"]` to customize filtering: `None` keeps the defaults, a list or tuple of directory paths replaces them, and `[]` disables frame filtering. For example, `{"record_py_stacks": True, "py_stack_filter_paths": ["/my_project/wrappers"]}` excludes only frames in that directory. Paths match on directory boundaries, and relative paths are resolved when capture begins.

Read stacks with [`get_kernel_py_stacks()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.get_kernel_py_stacks.html#torch.cuda.graph_annotations.get_kernel_py_stacks "torch.cuda.graph_annotations.get_kernel_py_stacks")
 or save them beside the trace with [`dump_kernel_py_stacks()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.dump_kernel_py_stacks.html#torch.cuda.graph_annotations.dump_kernel_py_stacks "torch.cuda.graph_annotations.dump_kernel_py_stacks")
. The gzip-compressed JSON maps decimal node-id strings to newline-separated `filename:line:function` frames, innermost first. With the default `key_by="exec"`, look up a Cuspy Chrome trace event using `str((args["graph id"] << 32) | args["graph node id"])`. For consumers reading CUPTI’s `sourceGraphNodeId`, use `key_by="source"` and look up that ID directly. Save after instantiation and before resetting or destroying the graph.

|     |     |
| --- | --- |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.is_available.html#torch.cuda.graph_annotations.is_available "torch.cuda.graph_annotations.is_available") | Return whether CUDA graph annotation recording is supported. |
| [`mark_kernels`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.mark_kernels.html#torch.cuda.graph_annotations.mark_kernels "torch.cuda.graph_annotations.mark_kernels") | Context manager that annotates GPU work captured within its scope. |
| [`get_kernel_annotations`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.get_kernel_annotations.html#torch.cuda.graph_annotations.get_kernel_annotations "torch.cuda.graph_annotations.get_kernel_annotations") | Return the live registry of recorded kernel annotations. |
| [`get_kernel_py_stacks`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.get_kernel_py_stacks.html#torch.cuda.graph_annotations.get_kernel_py_stacks "torch.cuda.graph_annotations.get_kernel_py_stacks") | Return Python launch stacks recorded during CUDA graph capture. |
| [`dump_kernel_py_stacks`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.dump_kernel_py_stacks.html#torch.cuda.graph_annotations.dump_kernel_py_stacks "torch.cuda.graph_annotations.dump_kernel_py_stacks") | Save recorded CUDA graph launch stacks as gzip-compressed JSON. |
| [`clear_kernel_annotations`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.clear_kernel_annotations.html#torch.cuda.graph_annotations.clear_kernel_annotations "torch.cuda.graph_annotations.clear_kernel_annotations") | Clear all recorded kernel annotations. |

This package adds support for device memory management implemented in CUDA.

Memory management[#](https://docs.pytorch.org/docs/2.15/cuda.html#memory-management "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`empty_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.empty_cache.html#torch.cuda.memory.empty_cache "torch.cuda.memory.empty_cache") | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other GPU application and visible in nvidia-smi. |
| [`get_per_process_memory_fraction`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.get_per_process_memory_fraction.html#torch.cuda.memory.get_per_process_memory_fraction "torch.cuda.memory.get_per_process_memory_fraction") | Get memory fraction for a process. |
| [`list_gpu_processes`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.list_gpu_processes.html#torch.cuda.memory.list_gpu_processes "torch.cuda.memory.list_gpu_processes") | Return a human-readable printout of the running processes and their GPU memory use for a given device. |
| [`mem_get_info`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.mem_get_info.html#torch.cuda.memory.mem_get_info "torch.cuda.memory.mem_get_info") | Return the global free and total GPU memory for a given device using cudaMemGetInfo. |
| [`memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_stats.html#torch.cuda.memory.memory_stats "torch.cuda.memory.memory_stats") | Return a dictionary of CUDA memory allocator statistics for a given device. |
| [`memory_stats_as_nested_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_stats_as_nested_dict.html#torch.cuda.memory.memory_stats_as_nested_dict "torch.cuda.memory.memory_stats_as_nested_dict") | Return the result of `memory_stats()` as a nested dictionary. |
| [`reset_accumulated_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_accumulated_memory_stats.html#torch.cuda.memory.reset_accumulated_memory_stats "torch.cuda.memory.reset_accumulated_memory_stats") | Reset the "accumulated" (historical) stats tracked by the CUDA memory allocator. |
| [`host_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.host_memory_stats.html#torch.cuda.memory.host_memory_stats "torch.cuda.memory.host_memory_stats") | Return a dictionary of pinned (host) allocator statistics. |
| [`host_memory_stats_as_nested_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.host_memory_stats_as_nested_dict.html#torch.cuda.memory.host_memory_stats_as_nested_dict "torch.cuda.memory.host_memory_stats_as_nested_dict") | Return the result of `host_memory_stats()` as a nested dictionary. |
| [`reset_accumulated_host_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_accumulated_host_memory_stats.html#torch.cuda.memory.reset_accumulated_host_memory_stats "torch.cuda.memory.reset_accumulated_host_memory_stats") | Reset the "accumulated" (historical) stats tracked by the host memory allocator. |
| [`memory_summary`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_summary.html#torch.cuda.memory.memory_summary "torch.cuda.memory.memory_summary") | Return a human-readable printout of the current memory allocator statistics for a given device. |
| [`memory_snapshot`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_snapshot.html#torch.cuda.memory.memory_snapshot "torch.cuda.memory.memory_snapshot") | Return a snapshot of the CUDA memory allocator state across all devices. |
| [`memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_allocated.html#torch.cuda.memory.memory_allocated "torch.cuda.memory.memory_allocated") | Return the current GPU memory occupied by tensors in bytes for a given device. |
| [`max_memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.max_memory_allocated.html#torch.cuda.memory.max_memory_allocated "torch.cuda.memory.max_memory_allocated") | Return the maximum GPU memory occupied by tensors in bytes for a given device. |
| [`reset_max_memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_max_memory_allocated.html#torch.cuda.memory.reset_max_memory_allocated "torch.cuda.memory.reset_max_memory_allocated") | Reset the starting point in tracking maximum GPU memory occupied by tensors for a given device. |
| [`memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_reserved.html#torch.cuda.memory.memory_reserved "torch.cuda.memory.memory_reserved") | Return the current GPU memory managed by the caching allocator in bytes for a given device. |
| [`max_memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.max_memory_reserved.html#torch.cuda.memory.max_memory_reserved "torch.cuda.memory.max_memory_reserved") | Return the maximum GPU memory managed by the caching allocator in bytes for a given device. |
| [`set_per_process_memory_fraction`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.set_per_process_memory_fraction.html#torch.cuda.memory.set_per_process_memory_fraction "torch.cuda.memory.set_per_process_memory_fraction") | Set memory fraction for a process. |
| [`memory_cached`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.memory_cached.html#torch.cuda.memory.memory_cached "torch.cuda.memory.memory_cached") | Deprecated; see `memory_reserved()`. |
| [`max_memory_cached`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.max_memory_cached.html#torch.cuda.memory.max_memory_cached "torch.cuda.memory.max_memory_cached") | Deprecated; see `max_memory_reserved()`. |
| [`reset_max_memory_cached`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_max_memory_cached.html#torch.cuda.memory.reset_max_memory_cached "torch.cuda.memory.reset_max_memory_cached") | Reset the starting point in tracking maximum GPU memory managed by the caching allocator for a given device. |
| [`reset_peak_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_peak_memory_stats.html#torch.cuda.memory.reset_peak_memory_stats "torch.cuda.memory.reset_peak_memory_stats") | Reset the "peak" stats tracked by the CUDA memory allocator. |
| [`reset_peak_host_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.reset_peak_host_memory_stats.html#torch.cuda.memory.reset_peak_host_memory_stats "torch.cuda.memory.reset_peak_host_memory_stats") | Reset the "peak" stats tracked by the host memory allocator. |
| [`caching_allocator_alloc`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.caching_allocator_alloc.html#torch.cuda.memory.caching_allocator_alloc "torch.cuda.memory.caching_allocator_alloc") | Perform a memory allocation using the CUDA memory allocator. |
| [`caching_allocator_delete`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.caching_allocator_delete.html#torch.cuda.memory.caching_allocator_delete "torch.cuda.memory.caching_allocator_delete") | Delete memory allocated using the CUDA memory allocator. |
| [`get_allocator_backend`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.get_allocator_backend.html#torch.cuda.memory.get_allocator_backend "torch.cuda.memory.get_allocator_backend") | Return a string describing the active allocator backend as set by `PYTORCH_ALLOC_CONF`. |
| [`CUDAPluggableAllocator`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.CUDAPluggableAllocator.html#torch.cuda.memory.CUDAPluggableAllocator "torch.cuda.memory.CUDAPluggableAllocator") | CUDA memory allocator loaded from a so file. |
| [`change_current_allocator`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.change_current_allocator.html#torch.cuda.memory.change_current_allocator "torch.cuda.memory.change_current_allocator") | Change the currently used memory allocator to be the one provided. |
| [`MemPool`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.MemPool.html#torch.cuda.memory.MemPool "torch.cuda.memory.MemPool") | MemPool represents a pool of memory in a caching allocator. |

|     |     |
| --- | --- |
| [`caching_allocator_disabled`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.caching_allocator_disabled.html#torch.cuda.memory.caching_allocator_disabled "torch.cuda.memory.caching_allocator_disabled") | Context manager that temporarily disables the CUDA caching allocator. |
| [`caching_allocator_enable`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.caching_allocator_enable.html#torch.cuda.memory.caching_allocator_enable "torch.cuda.memory.caching_allocator_enable") | Enable or disable the CUDA memory allocator. |

_class_ torch.cuda.use\_mem\_pool(_pool_, _device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/memory.py#L1442)
[#](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.use_mem_pool "Link to this definition")

A context manager that routes allocations to a given pool.

Parameters:

*   **pool** (_torch.cuda.MemPool_) – a MemPool object to be made active so that allocations route to this pool.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – selected device. Uses MemPool on the current device, given by [`current_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_device.html#torch.cuda.current_device "torch.cuda.current_device")
    , if [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device.html#torch.cuda.device "torch.cuda.device")
     is `None` (default).
    

Note

This context manager makes only current thread’s allocations route to the given pool. If a new thread is spawned inside the context manager (e.g. by calling backward) the allocations in that thread will not route to the given pool.

Note

When used during [`CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
 capture, the graph retains the pool until the graph is reset or destroyed.

torch.cuda.nccl.version()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/nccl.py#L35)
[#](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.nccl.version "Link to this definition")

Returns the version of the NCCL.

This function returns a tuple containing the major, minor, and patch version numbers of the NCCL. The suffix is also included in the tuple if a version suffix exists. :returns: The version information of the NCCL. :rtype: tuple

|     |     |
| --- | --- |
| [`profile`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.profiler.profile.html#torch.cuda.profiler.profile "torch.cuda.profiler.profile") | Enable profiling. |
| [`start`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.profiler.start.html#torch.cuda.profiler.start "torch.cuda.profiler.start") | Starts cuda profiler data collection. |
| [`stop`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.profiler.stop.html#torch.cuda.profiler.stop "torch.cuda.profiler.stop") | Stops cuda profiler data collection. |

NVIDIA Tools Extension (NVTX)[#](https://docs.pytorch.org/docs/2.15/cuda.html#nvidia-tools-extension-nvtx "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`nvtx.mark`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.mark.html#torch.cuda.nvtx.mark "torch.cuda.nvtx.mark") | Describe an instantaneous event that occurred at some point. |
| [`nvtx.range_push`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.range_push.html#torch.cuda.nvtx.range_push "torch.cuda.nvtx.range_push") | Push a range onto a stack of nested range span. |
| [`nvtx.range_pop`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.range_pop.html#torch.cuda.nvtx.range_pop "torch.cuda.nvtx.range_pop") | Pop a range off of a stack of nested range spans. |
| [`nvtx.range`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.range.html#torch.cuda.nvtx.range "torch.cuda.nvtx.range") | Context manager / decorator that pushes an NVTX range at the beginning of its scope, and pops it at the end. |
| [`nvtx.range_end`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.range_end.html#torch.cuda.nvtx.range_end "torch.cuda.nvtx.range_end") | Mark the end of a range for a given range\_id. |
| [`nvtx.range_start`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.nvtx.range_start.html#torch.cuda.nvtx.range_start "torch.cuda.nvtx.range_start") | Mark the start of a range with string message. |

Jiterator (beta)[#](https://docs.pytorch.org/docs/2.15/cuda.html#jiterator-beta "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`jiterator._create_jit_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.jiterator._create_jit_fn.html#torch.cuda.jiterator._create_jit_fn "torch.cuda.jiterator._create_jit_fn") | Create a jiterator-generated cuda kernel for an elementwise op. |
| [`jiterator._create_multi_output_jit_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.jiterator._create_multi_output_jit_fn.html#torch.cuda.jiterator._create_multi_output_jit_fn "torch.cuda.jiterator._create_multi_output_jit_fn") | Create a jiterator-generated cuda kernel for an elementwise op that supports returning one or more outputs. |

TunableOp[#](https://docs.pytorch.org/docs/2.15/cuda.html#tunableop "Link to this heading")

--------------------------------------------------------------------------------------------

Some operations could be implemented using more than one library or more than one technique. For example, a GEMM could be implemented for CUDA or ROCm using either the cublas/cublasLt libraries or hipblas/hipblasLt libraries, respectively. How does one know which implementation is the fastest and should be chosen? That’s what TunableOp provides. Certain operators have been implemented using multiple strategies as Tunable Operators. At runtime, all strategies are profiled and the fastest is selected for all subsequent operations.

See the [documentation](https://docs.pytorch.org/docs/2.15/cuda.tunable.html)
 for information on how to use it.

Stream Sanitizer (prototype)[#](https://docs.pytorch.org/docs/2.15/cuda.html#stream-sanitizer-prototype "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

CUDA Sanitizer is a prototype tool for detecting synchronization errors between streams in PyTorch. See the [documentation](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html)
 for information on how to use it.

GPUDirect Storage (prototype)[#](https://docs.pytorch.org/docs/2.15/cuda.html#gpudirect-storage-prototype "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The APIs in `torch.cuda.gds` provide thin wrappers around certain cuFile APIs that allow direct memory access transfers between GPU memory and storage, avoiding a bounce buffer in the CPU. See the [cufile api documentation](https://docs.nvidia.com/gpudirect-storage/api-reference-guide/index.html#cufile-io-api)
 for more details.

These APIs can be used with CUDA 12.6 or newer. In order to use these APIs, one must ensure that their system is appropriately configured to use GPUDirect Storage per the [GPUDirect Storage documentation](https://docs.nvidia.com/gpudirect-storage/troubleshooting-guide/contents.html)
.

On ROCm, the same APIs are backed by [hipFile](https://rocm.docs.amd.com/projects/hipFile/en/latest/)
 rather than cuFile and require ROCm 7.14 or newer. The hipFile entry points and the ROCm system configuration steps, which differ from the CUDA ones, are covered in [hipFile (GPUDirect Storage)](https://docs.pytorch.org/docs/2.15/notes/hip.html#rocm-gds)
.

See the docs for [`GdsFile`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile "torch.cuda.gds.GdsFile")
 for an example of how to use these.

|     |     |
| --- | --- |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.is_available.html#torch.cuda.gds.is_available "torch.cuda.gds.is_available") | Return `True` if GPUDirect Storage (GDS) support is built in. |
| [`gds_register_buffer`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.gds_register_buffer.html#torch.cuda.gds.gds_register_buffer "torch.cuda.gds.gds_register_buffer") | Registers a storage on a CUDA device as a GDS buffer. |
| [`gds_deregister_buffer`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.gds_deregister_buffer.html#torch.cuda.gds.gds_deregister_buffer "torch.cuda.gds.gds_deregister_buffer") | Deregisters a previously registered GDS buffer. |
| [`GdsFile`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile "torch.cuda.gds.GdsFile") | Wrapper around a file registered with the GPUDirect Storage (GDS) driver. |

Green Contexts (experimental)[#](https://docs.pytorch.org/docs/2.15/cuda.html#green-contexts-experimental "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

`torch.cuda.green_contexts` provides thin wrappers around the CUDA Green Context APIs to enable more general carveout of SM resources for CUDA kernels.

These APIs require the `cuda.bindings` package and can be used in PyTorch with CUDA versions greater than or equal to 12.8. Workqueue configuration requires CUDA 13.1 or newer.

Install instructions for `cuda.bindings` can be found here: https://nvidia.github.io/cuda-python/

Create streams from the green context and use them like other custom CUDA streams:

ctx \= GreenContext(...)
stream \= ctx.Stream()
with torch.cuda.stream(stream):
    \# torch operations here are using resources from \`ctx\`
    pass

Copy to clipboard

Synchronization between green-context streams and other streams is the user’s responsibility. Use CUDA events to order work, just as you would for any other custom stream.

The `GreenContext.set_context()` and `GreenContext.pop_context()` methods are deprecated compatibility APIs.

To create contexts with disjoint SM allocations (CUDA driver and bindings 13.1+), specify all groups in one operation:

from torch.cuda.green\_contexts import GreenContext, SMPartition

a, b \= GreenContext.split(
    num\_sms\=(24, 40), coscheduled\_sm\_count\=(8, 4), device\_id\=0
)
print(a.sm\_count, b.sm\_count)

Copy to clipboard

To retain the remainder, use `SMPartition.split`. To subdivide a returned partition or remainder, create a context from it and split the resource queried through its `sm_partition` property. CUDA drivers can reject raw split outputs as already partitioned resources, so the context creation is explicit:

sms \= SMPartition.from\_device(device\_id\=0)
(first,), rest \= sms.split(num\_sms\=4, coscheduled\_sm\_count\=2)
rest\_ctx \= GreenContext(sm\_partition\=rest)
(second,), rest \= rest\_ctx.sm\_partition.split(num\_sms\=4, coscheduled\_sm\_count\=2)
ctx \= GreenContext(sm\_partition\=second, workqueue\_scope\="balanced")

Copy to clipboard

Each split partitions its input resource. Its children and remainder are mutually disjoint, but overlap the parent. Results of separate splits on the same or overlapping input resources may overlap. CUDA evaluates new constraints when subdividing a resource; the remainder does not inherit the earlier split’s alignment. Partitioning does not reserve SMs against other contexts or guarantee concurrent execution. Each split option accepts a scalar or a sequence. All sequences must have the same nonzero length; scalars are broadcast to that length. With scalars only, one group is created. The default `num_sms=0` discovers the largest group satisfying its constraints. Groups are evaluated in order, so an early discovery group can exhaust the SMs needed by later groups. A group with both `num_sms=0` and `backfill=True` consumes all remaining SMs, so it must be the last group. Otherwise, specify a positive SM count. CUDA validates hardware constraints without PyTorch rounding the requested sizes. CUDA permits kernels to use additional SMs in some configurations involving MPS or dynamic parallelism; see the [CUDA green-context documentation](https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__GREEN__CONTEXTS.html)
.

`GreenContext.sm_count` reports the actual allocation, including for contexts created through the existing `num_sms` constructor. Independent constructor calls do not guarantee disjoint SMs. A context’s `sm_partition` property returns a resource that can be subdivided and keeps its originating context alive.

Locality domains describe hardware topology. With CUDA driver and bindings 13.4+, add locality constraints when splitting a resource:

from torch.cuda.green\_contexts import get\_num\_locality\_domains

n \= get\_num\_locality\_domains(device\_id\=0)
contexts \= GreenContext.split(
    coscheduled\_sm\_count\=2,
    locality\_domain\_ids\=tuple(range(n)),
    device\_id\=0,
)

Copy to clipboard

Here, the default zero SM count is broadcast to each locality domain and discovers its available SMs. Some device SMs may be outside all locality domains and remain unassigned. A domain can contain multiple partitions; its ID can also constrain subdivision through an existing context’s queried SM resource, as shown above. Use `None` for a group with no locality constraint. Workqueue settings can be combined with either kind of split.

`backfill=True` permits CUDA to fill a group with SMs outside its co-scheduling or locality constraints. It preserves the separation between sibling partitions. The `locality_domain_id` property on partitions and contexts reads CUDA’s reported metadata and returns `None` if CUDA does not specify a domain.

`get_num_locality_domains` returns `1` when the required software is unavailable. With CUDA driver and bindings 13.4+, it queries CUDA directly; invalid devices and failed queries raise. Supplying an explicit device index initializes only the driver, without initializing PyTorch CUDA state or creating a primary context. Driver initialization can still prevent CUDA use in subsequently forked children.

`is_localization_supported` returns false for unsupported software or devices with at most one domain. Before driver initialization, it attempts a best-effort NVML capability check using `CUDA_VISIBLE_DEVICES`. If NVML cannot determine support, it raises; initialize CUDA explicitly before querying again if needed. After driver initialization, the query always uses CUDA and query errors propagate. The predicate does not initialize the driver or a context, so calling it does not poison subsequent forks. Actual splitting and context creation always use CUDA, independently of this capability check.

|     |     |
| --- | --- |
| [`GreenContext`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext "torch.cuda.green_contexts.GreenContext") | Wrapper around a CUDA green context. |
| [`SMPartition`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.green_contexts.SMPartition.html#torch.cuda.green_contexts.SMPartition "torch.cuda.green_contexts.SMPartition") | An SM resource selected by CUDA, with its device and allocation metadata. |
| [`get_num_locality_domains`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.green_contexts.get_num_locality_domains.html#torch.cuda.green_contexts.get_num_locality_domains "torch.cuda.green_contexts.get_num_locality_domains") | Return the device's locality-domain count reported by CUDA. |
| [`is_localization_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.green_contexts.is_localization_supported.html#torch.cuda.green_contexts.is_localization_supported "torch.cuda.green_contexts.is_localization_supported") | Return whether the software supports localization on a multi-domain GPU. |

torch.cuda.nccl.is\_available(_tensors_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/nccl.py#L14)
[#](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.nccl.is_available "Link to this definition")

This package adds support for NVIDIA Tools Extension (NVTX) used in profiling.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cuda.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cuda.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |