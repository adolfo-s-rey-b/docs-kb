Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/mps.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/mps.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/mps.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/mps.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/mps.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/mps.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/mps.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/mps.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/mps.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/mps.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/mps.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/mps.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/mps.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/mps.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/mps.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/mps.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/mps.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/mps.html)
[v1.13](https://docs.pytorch.org/docs/1.13/mps.html)
[v1.12](https://docs.pytorch.org/docs/1.12/mps.html)
[v1.11](https://docs.pytorch.org/docs/1.11/mps.html)
[v1.10](https://docs.pytorch.org/docs/1.10/mps.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/mps.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/mps.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/mps.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/mps.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/mps.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/mps.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/mps.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/mps.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/mps.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/mps.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/mps.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/mps.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/mps.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/mps.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/mps.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/mps.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/mps.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/mps.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/mps.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/mps.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/mps.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/mps.html)

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

torch.mps[#](https://docs.pytorch.org/docs/2.15/mps.html#module-torch.mps "Link to this heading")

==================================================================================================

Created On: Feb 10, 2023 | Last Updated On: Jul 07, 2026

This package enables an interface for accessing MPS (Metal Performance Shaders) backend in Python. Metal is Apple’s API for programming metal GPU (graphics processor unit). Using MPS means that increased performance can be achieved, by running work on the metal GPU(s). See [https://developer.apple.com/documentation/metalperformanceshaders](https://developer.apple.com/documentation/metalperformanceshaders)
 for more details.

|     |     |
| --- | --- |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.is_available.html#torch.mps.is_available "torch.mps.is_available") |     |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.device_count.html#torch.mps.device_count "torch.mps.device_count") | Returns the number of available MPS devices. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.synchronize.html#torch.mps.synchronize "torch.mps.synchronize") | Waits for all kernels in all streams on a MPS device to complete. |
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.get_rng_state.html#torch.mps.get_rng_state "torch.mps.get_rng_state") | Returns the random number generator state as a ByteTensor. |
| [`set_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.set_rng_state.html#torch.mps.set_rng_state "torch.mps.set_rng_state") | Sets the random number generator state. |
| [`manual_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.manual_seed.html#torch.mps.manual_seed "torch.mps.manual_seed") | Sets the seed for generating random numbers. |
| [`seed`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.seed.html#torch.mps.seed "torch.mps.seed") | Sets the seed for generating random numbers to a random number. |
| [`empty_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.empty_cache.html#torch.mps.empty_cache "torch.mps.empty_cache") | Releases all unoccupied cached memory currently held by the caching allocator so that those can be used in other GPU applications. |
| [`set_per_process_memory_fraction`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.set_per_process_memory_fraction.html#torch.mps.set_per_process_memory_fraction "torch.mps.set_per_process_memory_fraction") | Set memory fraction for limiting process's memory allocation on MPS device. |
| [`current_allocated_memory`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.current_allocated_memory.html#torch.mps.current_allocated_memory "torch.mps.current_allocated_memory") | Returns the current GPU memory occupied by tensors in bytes. |
| [`driver_allocated_memory`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.driver_allocated_memory.html#torch.mps.driver_allocated_memory "torch.mps.driver_allocated_memory") | Returns total GPU memory allocated by Metal driver for the process in bytes. |
| [`recommended_max_memory`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.recommended_max_memory.html#torch.mps.recommended_max_memory "torch.mps.recommended_max_memory") | Returns recommended max Working set size for GPU memory in bytes. |
| [`compile_shader`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.compile_shader.html#torch.mps.compile_shader "torch.mps.compile_shader") | Compiles compute shader from source and allows one to invoke kernels defined there from the comfort of Python runtime Example. |
| [`load_metallib`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.load_metallib.html#torch.mps.load_metallib "torch.mps.load_metallib") | Loads a precompiled Metal library (.metallib) and returns a shader library object that allows invoking kernels defined in it. |

MPS Profiler[#](https://docs.pytorch.org/docs/2.15/mps.html#mps-profiler "Link to this heading")

-------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`profiler.start`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.start.html#torch.mps.profiler.start "torch.mps.profiler.start") | Start OS Signpost tracing from MPS backend. |
| [`profiler.stop`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.stop.html#torch.mps.profiler.stop "torch.mps.profiler.stop") | Stops generating OS Signpost tracing from MPS backend. |
| [`profiler.profile`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.profile.html#torch.mps.profiler.profile "torch.mps.profiler.profile") | Context Manager to enabling generating OS Signpost tracing from MPS backend. |
| [`profiler.is_capturing_metal`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.is_capturing_metal.html#torch.mps.profiler.is_capturing_metal "torch.mps.profiler.is_capturing_metal") | Checks if metal capture is in progress |
| [`profiler.is_metal_capture_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.is_metal_capture_enabled.html#torch.mps.profiler.is_metal_capture_enabled "torch.mps.profiler.is_metal_capture_enabled") | Checks if metal\_capture context manager is usable To enable metal capture, set MTL\_CAPTURE\_ENABLED envvar |
| [`profiler.metal_capture`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.profiler.metal_capture.html#torch.mps.profiler.metal_capture "torch.mps.profiler.metal_capture") | Context manager that enables capturing of Metal calls into gputrace |

MPS Event[#](https://docs.pytorch.org/docs/2.15/mps.html#mps-event "Link to this heading")

-------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`event.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.mps.event.Event.html#torch.mps.event.Event "torch.mps.event.Event") | Wrapper around an MPS event. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/mps.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/mps.md.txt)

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