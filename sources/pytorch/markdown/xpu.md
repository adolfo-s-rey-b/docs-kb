Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/xpu.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/xpu.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/xpu.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/xpu.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/xpu.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/xpu.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/xpu.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/xpu.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/xpu.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/xpu.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/xpu.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/xpu.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/xpu.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/xpu.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/xpu.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/xpu.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/xpu.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/xpu.html)
[v1.13](https://docs.pytorch.org/docs/1.13/xpu.html)
[v1.12](https://docs.pytorch.org/docs/1.12/xpu.html)
[v1.11](https://docs.pytorch.org/docs/1.11/xpu.html)
[v1.10](https://docs.pytorch.org/docs/1.10/xpu.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/xpu.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/xpu.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/xpu.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/xpu.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/xpu.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/xpu.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/xpu.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/xpu.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/xpu.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/xpu.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/xpu.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/xpu.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/xpu.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/xpu.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/xpu.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/xpu.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/xpu.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/xpu.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/xpu.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/xpu.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/xpu.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/xpu.html)

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

torch.xpu[#](https://docs.pytorch.org/docs/2.15/xpu.html#module-torch.xpu "Link to this heading")

==================================================================================================

Created On: Feb 01, 2024 | Last Updated On: Jun 18, 2026

This package introduces support for the XPU backend, specifically tailored for Intel GPU optimization.

This package is lazily initialized, so you can always import it, and use [`is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_available.html#torch.xpu.is_available "torch.xpu.is_available")
 to determine if your system supports XPU.

|     |     |
| --- | --- |
| [`StreamContext`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.StreamContext.html#torch.xpu.StreamContext "torch.xpu.StreamContext") | Context-manager that selects a given stream. |
| [`can_device_access_peer`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.can_device_access_peer.html#torch.xpu.can_device_access_peer "torch.xpu.can_device_access_peer") | Query whether a device can access a peer device's memory. |
| [`clock_rate`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.clock_rate.html#torch.xpu.clock_rate "torch.xpu.clock_rate") | Return the GPU clock rate in MHz. |
| [`current_device`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.current_device.html#torch.xpu.current_device "torch.xpu.current_device") | Return the index of a currently selected device. |
| [`current_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.current_stream.html#torch.xpu.current_stream "torch.xpu.current_stream") | Return the currently selected [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.Stream_class.html#torch.xpu.Stream "torch.xpu.Stream")<br> for a given device. |
| [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.device.html#torch.xpu.device "torch.xpu.device") | Context-manager that changes the selected device. |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.device_count.html#torch.xpu.device_count "torch.xpu.device_count") | Return the number of XPU device available. |
| [`device_of`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.device_of.html#torch.xpu.device_of "torch.xpu.device_of") | Context-manager that changes the current device to that of given object. |
| [`device_memory_used`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.device_memory_used.html#torch.xpu.device_memory_used "torch.xpu.device_memory_used") | Return the current GPU used global (device) memory in bytes. |
| [`get_arch_list`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_arch_list.html#torch.xpu.get_arch_list "torch.xpu.get_arch_list") | Return list XPU architectures this library was compiled for. |
| [`get_device_capability`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_device_capability.html#torch.xpu.get_device_capability "torch.xpu.get_device_capability") | Get the xpu capability of a device. |
| [`get_device_name`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_device_name.html#torch.xpu.get_device_name "torch.xpu.get_device_name") | Get the name of a device. |
| [`get_device_properties`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_device_properties.html#torch.xpu.get_device_properties "torch.xpu.get_device_properties") | Get the properties of a device. |
| [`get_gencode_flags`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_gencode_flags.html#torch.xpu.get_gencode_flags "torch.xpu.get_gencode_flags") | Return XPU AOT(ahead-of-time) build flags this library was compiled with. |
| [`get_stream_from_external`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_stream_from_external.html#torch.xpu.get_stream_from_external "torch.xpu.get_stream_from_external") | Return a [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.Stream_class.html#torch.xpu.Stream "torch.xpu.Stream")<br> from an external SYCL queue. |
| [`init`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.init.html#torch.xpu.init "torch.xpu.init") | Initialize PyTorch's XPU state. |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_available.html#torch.xpu.is_available "torch.xpu.is_available") | Return a bool indicating if XPU is currently available. |
| [`is_bf16_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_bf16_supported.html#torch.xpu.is_bf16_supported "torch.xpu.is_bf16_supported") | Return a bool indicating if the current XPU device supports dtype bfloat16. |
| [`is_initialized`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_initialized.html#torch.xpu.is_initialized "torch.xpu.is_initialized") | Return whether PyTorch's XPU state has been initialized. |
| [`is_tf32_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_tf32_supported.html#torch.xpu.is_tf32_supported "torch.xpu.is_tf32_supported") | Return a bool indicating if the current XPU device supports dtype tf32. |
| [`memory_usage`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory_usage.html#torch.xpu.memory_usage "torch.xpu.memory_usage") | Return the GPU memory bandwidth usage as a percentage. |
| [`power_draw`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.power_draw.html#torch.xpu.power_draw "torch.xpu.power_draw") | Return the GPU card power draw in watts. |
| [`set_device`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.set_device.html#torch.xpu.set_device "torch.xpu.set_device") | Set the current device. |
| [`set_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.set_stream.html#torch.xpu.set_stream "torch.xpu.set_stream") | Set the current stream. This is a wrapper API to set the stream. |
| [`stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.stream_function.html#torch.xpu.stream "torch.xpu.stream") | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.synchronize.html#torch.xpu.synchronize "torch.xpu.synchronize") | Wait for all kernels in all streams on a XPU device to complete. |
| [`temperature`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.temperature.html#torch.xpu.temperature "torch.xpu.temperature") | Return the GPU temperature in degrees Celsius. |
| [`utilization`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.utilization.html#torch.xpu.utilization "torch.xpu.utilization") | Return the GPU engine utilization as a percentage. |

Random Number Generator[#](https://docs.pytorch.org/docs/2.15/xpu.html#random-number-generator "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_rng_state.html#torch.xpu.get_rng_state "torch.xpu.get_rng_state") | Return the random number generator state of the specified GPU as a ByteTensor. |
| [`get_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.get_rng_state_all.html#torch.xpu.get_rng_state_all "torch.xpu.get_rng_state_all") | Return a list of ByteTensor representing the random number states of all devices. |
| [`initial_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.initial_seed.html#torch.xpu.initial_seed "torch.xpu.initial_seed") | Return the current random seed of the current GPU. |
| [`manual_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.manual_seed.html#torch.xpu.manual_seed "torch.xpu.manual_seed") | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.manual_seed_all.html#torch.xpu.manual_seed_all "torch.xpu.manual_seed_all") | Set the seed for generating random numbers on all GPUs. |
| [`seed`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.seed.html#torch.xpu.seed "torch.xpu.seed") | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.seed_all.html#torch.xpu.seed_all "torch.xpu.seed_all") | Set the seed for generating random numbers to a random number on all GPUs. |
| [`set_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.set_rng_state.html#torch.xpu.set_rng_state "torch.xpu.set_rng_state") | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.set_rng_state_all.html#torch.xpu.set_rng_state_all "torch.xpu.set_rng_state_all") | Set the random number generator state of all devices. |

Streams and events[#](https://docs.pytorch.org/docs/2.15/xpu.html#streams-and-events "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Event`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.Event.html#torch.xpu.Event "torch.xpu.Event") | Wrapper around a XPU event. |
| [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.Stream_class.html#torch.xpu.Stream "torch.xpu.Stream") | Wrapper around a XPU stream. |

Graphs[#](https://docs.pytorch.org/docs/2.15/xpu.html#graphs "Link to this heading")

-------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`is_current_stream_capturing`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.is_current_stream_capturing.html#torch.xpu.is_current_stream_capturing "torch.xpu.is_current_stream_capturing") | Return True if XPU graph capture is underway on the current XPU stream, False otherwise. |
| [`graph_pool_handle`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.graph_pool_handle.html#torch.xpu.graph_pool_handle "torch.xpu.graph_pool_handle") | Return an opaque token representing the id of a graph memory pool. |
| [`XPUGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.XPUGraph.html#torch.xpu.XPUGraph "torch.xpu.XPUGraph") | Wrapper around a XPU graph. |
| [`graph`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.graph.html#torch.xpu.graph "torch.xpu.graph") | Context-manager that captures XPU work into a [`torch.xpu.XPUGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.XPUGraph.html#torch.xpu.XPUGraph "torch.xpu.XPUGraph")<br> object for later replay. |
| [`make_graphed_callables`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.make_graphed_callables.html#torch.xpu.make_graphed_callables "torch.xpu.make_graphed_callables") | Accept callables (functions or [`nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")<br>s) and returns graphed versions. |

Memory management[#](https://docs.pytorch.org/docs/2.15/xpu.html#memory-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`XPUPluggableAllocator`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.XPUPluggableAllocator.html#torch.xpu.memory.XPUPluggableAllocator "torch.xpu.memory.XPUPluggableAllocator") | XPU memory allocator loaded dynamically from a shared library. |
| [`change_current_allocator`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.change_current_allocator.html#torch.xpu.memory.change_current_allocator "torch.xpu.memory.change_current_allocator") | Change the currently used memory allocator to be the one provided. |
| [`empty_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.empty_cache.html#torch.xpu.memory.empty_cache "torch.xpu.memory.empty_cache") | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other XPU application. |
| [`get_per_process_memory_fraction`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.get_per_process_memory_fraction.html#torch.xpu.memory.get_per_process_memory_fraction "torch.xpu.memory.get_per_process_memory_fraction") | Retrieve the memory fraction currently set for a process on a given XPU device. |
| [`list_gpu_processes`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.list_gpu_processes.html#torch.xpu.memory.list_gpu_processes "torch.xpu.memory.list_gpu_processes") | Return a printout of running processes and their GPU memory usage on a given device. |
| [`max_memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.max_memory_allocated.html#torch.xpu.memory.max_memory_allocated "torch.xpu.memory.max_memory_allocated") | Return the maximum GPU memory occupied by tensors in bytes for a given device. |
| [`max_memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.max_memory_reserved.html#torch.xpu.memory.max_memory_reserved "torch.xpu.memory.max_memory_reserved") | Return the maximum GPU memory managed by the caching allocator in bytes for a given device. |
| [`mem_get_info`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.mem_get_info.html#torch.xpu.memory.mem_get_info "torch.xpu.memory.mem_get_info") | Return the global free and total GPU memory for a given device. |
| [`memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.memory_allocated.html#torch.xpu.memory.memory_allocated "torch.xpu.memory.memory_allocated") | Return the current GPU memory occupied by tensors in bytes for a given device. |
| [`memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.memory_reserved.html#torch.xpu.memory.memory_reserved "torch.xpu.memory.memory_reserved") | Return the current GPU memory managed by the caching allocator in bytes for a given device. |
| [`memory_snapshot`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.memory_snapshot.html#torch.xpu.memory.memory_snapshot "torch.xpu.memory.memory_snapshot") | Return a snapshot of the XPU memory allocator state across all devices. |
| [`memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.memory_stats.html#torch.xpu.memory.memory_stats "torch.xpu.memory.memory_stats") | Return a dictionary of XPU memory allocator statistics for a given device. |
| [`memory_stats_as_nested_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.memory_stats_as_nested_dict.html#torch.xpu.memory.memory_stats_as_nested_dict "torch.xpu.memory.memory_stats_as_nested_dict") | Return the result of `memory_stats()` as a nested dictionary. |
| [`reset_accumulated_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.reset_accumulated_memory_stats.html#torch.xpu.memory.reset_accumulated_memory_stats "torch.xpu.memory.reset_accumulated_memory_stats") | Reset the "accumulated" (historical) stats tracked by the XPU memory allocator. |
| [`reset_peak_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.reset_peak_memory_stats.html#torch.xpu.memory.reset_peak_memory_stats "torch.xpu.memory.reset_peak_memory_stats") | Reset the "peak" stats tracked by the XPU memory allocator. |
| [`set_per_process_memory_fraction`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.set_per_process_memory_fraction.html#torch.xpu.memory.set_per_process_memory_fraction "torch.xpu.memory.set_per_process_memory_fraction") | Set the memory fraction for a single process on XPU device. |
| [`MemPool`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.memory.MemPool.html#torch.xpu.memory.MemPool "torch.xpu.memory.MemPool") | MemPool represents a pool of memory in a caching allocator. |

_class_ torch.xpu.use\_mem\_pool(_pool_, _device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/xpu/memory.py#L599)
[#](https://docs.pytorch.org/docs/2.15/xpu.html#torch.xpu.use_mem_pool "Link to this definition")

A context manager that routes allocations to a given pool.

Parameters:

*   **pool** (_torch.xpu.MemPool_) – a `MemPool` object to be made active so that allocations route to this pool.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – selected device. Uses `MemPool` on the current device, given by [`current_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.current_device.html#torch.xpu.current_device "torch.xpu.current_device")
    , if [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.xpu.device.html#torch.xpu.device "torch.xpu.device")
     is `None` (default).
    

Note

This context manager makes only current thread’s allocations route to the given pool. If a new thread is spawned inside the context manager (e.g. by calling backward) the allocations in that thread will not route to the given pool.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/xpu.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/xpu.md.txt)

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