Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator.html)

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

torch.accelerator[#](https://docs.pytorch.org/docs/2.15/accelerator.html#torch-accelerator "Link to this heading")

===================================================================================================================

Created On: Oct 27, 2024 | Last Updated On: Jun 19, 2026

Lazy Initialization and Fork Safety[#](https://docs.pytorch.org/docs/2.15/accelerator.html#lazy-initialization-and-fork-safety "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Accelerator runtimes (CUDA, XPU, MPS, etc.) are initialized lazily — only when the first operation that touches the device runs. This ensures that `import torch` and capability queries do not poison subsequent `fork()` calls. See [Poison fork in multiprocessing](https://docs.pytorch.org/docs/2.15/notes/multiprocessing.html#multiprocessing-poison-fork-note)
 for background.

Certain APIs need to be callable before forking (e.g., `device_count()`, `is_available()`), and some backends provide opt-in mechanisms to make these fork-safe (e.g., CUDA via NVML, XPU via Level Zero Sysman). To keep behavior and runtime state consistent between `torch.accelerator` and per-backend modules, the following APIs are delegated to each backend:

*   **`is_available()` / `device_count()`** should ideally answer without bringing up the runtime, since `DataLoader` and similar tools rely on calling them before forking. Whether this is achievable depends on the backend, so `torch.accelerator` forwards to the corresponding backend implementation.
    
*   **`_lazy_call()`** is used for deferred RNG management. Calling `manual_seed()` before forking should not force runtime initialization. `torch.accelerator` wraps the seeding callback via `_lazy_call()`, which forwards to the backend’s own callback queue (CUDA, XPU, MTIA, …). Each backend owns its init flag and callback queue. If a backend does not provide `_lazy_call` (e.g., MPS), the callback executes immediately.
    

This package introduces support for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
 in python.

|     |     |
| --- | --- |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.device_count.html#torch.accelerator.device_count "torch.accelerator.device_count") | Return the number of current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> available. |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.is_available.html#torch.accelerator.is_available "torch.accelerator.is_available") | Check if the current accelerator is available at runtime: it was built, all the required drivers are available and at least one device is visible. |
| [`current_accelerator`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator "torch.accelerator.current_accelerator") | Return the device of the accelerator available at compilation time. |
| [`set_device_index`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.set_device_index.html#torch.accelerator.set_device_index "torch.accelerator.set_device_index") | Set the current device index to a given device. |
| [`set_device_idx`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.set_device_idx.html#torch.accelerator.set_device_idx "torch.accelerator.set_device_idx") | (Deprecated) Set the current device index to a given device. |
| [`current_device_index`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_device_index.html#torch.accelerator.current_device_index "torch.accelerator.current_device_index") | Return the index of a currently selected device for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br>. |
| [`current_device_idx`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_device_idx.html#torch.accelerator.current_device_idx "torch.accelerator.current_device_idx") | (Deprecated) Return the index of a currently selected device for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br>. |
| [`get_device_capability`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.get_device_capability.html#torch.accelerator.get_device_capability "torch.accelerator.get_device_capability") | Return the capability of the currently selected device. |
| [`set_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.set_stream.html#torch.accelerator.set_stream "torch.accelerator.set_stream") | Set the current stream to a given stream. |
| [`current_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_stream.html#torch.accelerator.current_stream "torch.accelerator.current_stream") | Return the currently selected stream for a given device. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.synchronize.html#torch.accelerator.synchronize "torch.accelerator.synchronize") | Wait for all kernels in all streams on the given device to complete. |
| [`device_index`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.device_index.html#torch.accelerator.device_index "torch.accelerator.device_index") | Context manager to set the current device index for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br>. |

Graphs[#](https://docs.pytorch.org/docs/2.15/accelerator.html#graphs "Link to this heading")

---------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Graph`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph "torch.accelerator.Graph") | Wrapper around an [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> graph that supports capture and replay. |

Memory management[#](https://docs.pytorch.org/docs/2.15/accelerator.html#memory-management "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`empty_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.empty_cache.html#torch.accelerator.memory.empty_cache "torch.accelerator.memory.empty_cache") | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other applications. |
| [`empty_host_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.empty_host_cache.html#torch.accelerator.memory.empty_host_cache "torch.accelerator.memory.empty_host_cache") | Release all unoccupied cached host (pinned) memory currently held by the host caching allocator so that it can be used by other applications. |
| [`get_memory_info`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.get_memory_info.html#torch.accelerator.memory.get_memory_info "torch.accelerator.memory.get_memory_info") | Return the current device memory information for a given device index. |
| [`max_memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.max_memory_allocated.html#torch.accelerator.memory.max_memory_allocated "torch.accelerator.memory.max_memory_allocated") | Return the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> maximum device memory occupied by tensors in bytes for a given device index. |
| [`max_memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.max_memory_reserved.html#torch.accelerator.memory.max_memory_reserved "torch.accelerator.memory.max_memory_reserved") | Return the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> maximum device memory managed by the caching allocator in bytes for a given device index. |
| [`memory_allocated`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.memory_allocated.html#torch.accelerator.memory.memory_allocated "torch.accelerator.memory.memory_allocated") | Return the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> device memory occupied by tensors in bytes for a given device index. |
| [`memory_reserved`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.memory_reserved.html#torch.accelerator.memory.memory_reserved "torch.accelerator.memory.memory_reserved") | Return the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> device memory managed by the caching allocator in bytes for a given device index. |
| [`memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.memory_stats.html#torch.accelerator.memory.memory_stats "torch.accelerator.memory.memory_stats") | Return a dictionary of accelerator device memory allocator statistics for a given device index. |
| [`reset_accumulated_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.reset_accumulated_memory_stats.html#torch.accelerator.memory.reset_accumulated_memory_stats "torch.accelerator.memory.reset_accumulated_memory_stats") | Reset the "accumulated" (historical) stats tracked by the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> memory allocator for a given device index. |
| [`reset_peak_memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.memory.reset_peak_memory_stats.html#torch.accelerator.memory.reset_peak_memory_stats "torch.accelerator.memory.reset_peak_memory_stats") | Reset the "peak" stats tracked by the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> memory allocator for a given device index. |

Random Number Generator[#](https://docs.pytorch.org/docs/2.15/accelerator.html#random-number-generator "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.random.get_rng_state.html#torch.accelerator.random.get_rng_state "torch.accelerator.random.get_rng_state") | Return the RNG state of the default [`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")<br> for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> as a torch.Tensor of dtype torch.uint8 for the specified accelerator device. |
| [`get_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.random.get_rng_state_all.html#torch.accelerator.random.get_rng_state_all "torch.accelerator.random.get_rng_state_all") | Return a list of torch.Tensor of dtype torch.uint8 representing the RNG states of all devices for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br>. |
| [`initial_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.random.initial_seed.html#torch.accelerator.random.initial_seed "torch.accelerator.random.initial_seed") | Return the initial seed of the default [`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")<br> for the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)<br> on the specified device. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator.md.txt)

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