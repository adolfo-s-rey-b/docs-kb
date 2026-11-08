Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/mtia.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/mtia.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/mtia.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/mtia.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/mtia.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/mtia.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/mtia.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/mtia.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/mtia.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/mtia.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/mtia.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/mtia.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/mtia.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/mtia.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/mtia.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/mtia.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/mtia.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/mtia.html)
[v1.13](https://docs.pytorch.org/docs/1.13/mtia.html)
[v1.12](https://docs.pytorch.org/docs/1.12/mtia.html)
[v1.11](https://docs.pytorch.org/docs/1.11/mtia.html)
[v1.10](https://docs.pytorch.org/docs/1.10/mtia.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/mtia.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/mtia.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/mtia.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/mtia.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/mtia.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/mtia.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/mtia.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/mtia.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/mtia.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/mtia.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/mtia.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/mtia.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/mtia.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/mtia.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/mtia.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/mtia.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/mtia.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/mtia.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/mtia.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/mtia.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/mtia.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/mtia.html)

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

torch.mtia[#](https://docs.pytorch.org/docs/2.15/mtia.html#torch-mtia "Link to this heading")

==============================================================================================

Created On: Jul 11, 2023 | Last Updated On: Apr 24, 2026

The MTIA backend is implemented out of the tree, only interfaces are defined here.

This package enables an interface for accessing MTIA backend in python

|     |     |
| --- | --- |
| [`StreamContext`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.StreamContext.html#torch.mtia.StreamContext "torch.mtia.StreamContext") | Context-manager that selects a given stream. |
| [`current_device`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.current_device.html#torch.mtia.current_device "torch.mtia.current_device") | Return the index of a currently selected device. |
| [`current_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.current_stream.html#torch.mtia.current_stream "torch.mtia.current_stream") | Return the currently selected [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.Stream_class.html#torch.mtia.Stream "torch.mtia.Stream")<br> for a given device. |
| [`default_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.default_stream.html#torch.mtia.default_stream "torch.mtia.default_stream") | Return the default [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.Stream_class.html#torch.mtia.Stream "torch.mtia.Stream")<br> for a given device. |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.device_count.html#torch.mtia.device_count "torch.mtia.device_count") | Return the number of MTIA devices available. |
| [`init`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.init.html#torch.mtia.init "torch.mtia.init") |     |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.is_available.html#torch.mtia.is_available "torch.mtia.is_available") | Return true if MTIA device is available |
| [`is_bf16_supported`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.is_bf16_supported.html#torch.mtia.is_bf16_supported "torch.mtia.is_bf16_supported") | Return a bool indicating if the current MTIA device supports dtype bfloat16. |
| [`is_initialized`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.is_initialized.html#torch.mtia.is_initialized "torch.mtia.is_initialized") | Return whether PyTorch's MTIA state has been initialized. |
| [`memory_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.memory_stats.html#torch.mtia.memory_stats "torch.mtia.memory_stats") | Return a dictionary of MTIA memory allocator statistics for a given device. |
| [`get_device_capability`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.get_device_capability.html#torch.mtia.get_device_capability "torch.mtia.get_device_capability") | Return capability of a given device as a tuple of (major version, minor version). |
| [`get_device_properties`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.get_device_properties.html#torch.mtia.get_device_properties "torch.mtia.get_device_properties") | Return a dictionary of MTIA device properties |
| [`empty_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.empty_cache.html#torch.mtia.empty_cache "torch.mtia.empty_cache") | Empty the MTIA device cache. |
| [`record_memory_history`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.record_memory_history.html#torch.mtia.record_memory_history "torch.mtia.record_memory_history") | Enable/Disable the memory profiler on MTIA allocator |
| [`snapshot`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.snapshot.html#torch.mtia.snapshot "torch.mtia.snapshot") | Return a dictionary of MTIA memory allocator history |
| [`attach_out_of_memory_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.attach_out_of_memory_observer.html#torch.mtia.attach_out_of_memory_observer "torch.mtia.attach_out_of_memory_observer") | Attach an out-of-memory observer to MTIA memory allocator |
| [`set_device`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.set_device.html#torch.mtia.set_device "torch.mtia.set_device") | Set the current device. |
| [`set_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.set_stream.html#torch.mtia.set_stream "torch.mtia.set_stream") | Set the current stream. This is a wrapper API to set the stream. |
| [`stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.stream_function.html#torch.mtia.stream "torch.mtia.stream") | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.synchronize.html#torch.mtia.synchronize "torch.mtia.synchronize") | Waits for all jobs in all streams on a MTIA device to complete. |
| [`device`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.device.html#torch.mtia.device "torch.mtia.device") | Context-manager that changes the selected device. |
| [`set_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.set_rng_state.html#torch.mtia.set_rng_state "torch.mtia.set_rng_state") | Sets the random number generator state of the specified MTIA device. |
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.get_rng_state.html#torch.mtia.get_rng_state "torch.mtia.get_rng_state") | Returns the random number generator state of the specified MTIA device as a ByteTensor. |
| [`set_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.set_rng_state_all.html#torch.mtia.set_rng_state_all "torch.mtia.set_rng_state_all") | Sets the random number generator state of all devices. |
| [`get_rng_state_all`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.get_rng_state_all.html#torch.mtia.get_rng_state_all "torch.mtia.get_rng_state_all") | Returns a list of ByteTensor representing the random number states of all devices. |
| [`manual_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.manual_seed.html#torch.mtia.manual_seed "torch.mtia.manual_seed") | Sets the seed for generating random numbers for the current MTIA device. |
| [`manual_seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.manual_seed_all.html#torch.mtia.manual_seed_all "torch.mtia.manual_seed_all") | Sets the seed for generating random numbers on all MTIA devices. |
| [`seed`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.seed.html#torch.mtia.seed "torch.mtia.seed") | Sets the seed for generating random numbers to a random number for the current MTIA device. |
| [`seed_all`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.seed_all.html#torch.mtia.seed_all "torch.mtia.seed_all") | Sets the seed for generating random numbers to a random number on all MTIA devices. |
| [`initial_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.initial_seed.html#torch.mtia.initial_seed "torch.mtia.initial_seed") | Returns the current random seed of the current MTIA device. |
| [`DeferredMtiaCallError`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.DeferredMtiaCallError.html#torch.mtia.DeferredMtiaCallError "torch.mtia.DeferredMtiaCallError") |     |

Streams and events[#](https://docs.pytorch.org/docs/2.15/mtia.html#streams-and-events "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Event`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.Event.html#torch.mtia.Event "torch.mtia.Event") | Query and record Stream status to identify or control dependencies across Stream and measure timing. |
| [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.mtia.Stream_class.html#torch.mtia.Stream "torch.mtia.Stream") | An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/mtia.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/mtia.md.txt)

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