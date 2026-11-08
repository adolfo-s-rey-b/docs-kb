Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cpu.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cpu.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cpu.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cpu.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cpu.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cpu.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cpu.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cpu.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cpu.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cpu.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cpu.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cpu.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cpu.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cpu.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cpu.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cpu.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cpu.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cpu.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cpu.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cpu.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cpu.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cpu.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cpu.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cpu.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cpu.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cpu.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cpu.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cpu.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cpu.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cpu.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cpu.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cpu.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cpu.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cpu.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cpu.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cpu.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cpu.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cpu.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cpu.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cpu.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cpu.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cpu.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cpu.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cpu.html)

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

torch.cpu[#](https://docs.pytorch.org/docs/2.15/cpu.html#module-torch.cpu "Link to this heading")

==================================================================================================

Created On: Jul 11, 2023 | Last Updated On: May 08, 2026

This package implements abstractions found in `torch.cuda` to facilitate writing device-agnostic code.

|     |     |
| --- | --- |
| [`current_device`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.current_device.html#torch.cpu.current_device "torch.cpu.current_device") | Returns current device for cpu. |
| [`current_stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.current_stream.html#torch.cpu.current_stream "torch.cpu.current_stream") | Returns the currently selected [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.Stream_class.html#torch.cpu.Stream "torch.cpu.Stream")<br> for a given device. |
| [`get_capabilities`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.get_capabilities.html#torch.cpu.get_capabilities "torch.cpu.get_capabilities") | Returns an immutable mapping of CPU capabilities detected at runtime. |
| [`is_available`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.is_available.html#torch.cpu.is_available "torch.cpu.is_available") | Returns a bool indicating if CPU is currently available. |
| [`is_initialized`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.is_initialized.html#torch.cpu.is_initialized "torch.cpu.is_initialized") | Returns True if the CPU is initialized. |
| [`synchronize`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.synchronize.html#torch.cpu.synchronize "torch.cpu.synchronize") | Waits for all kernels in all streams on the CPU device to complete. |
| [`stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.stream_function.html#torch.cpu.stream "torch.cpu.stream") | Wrapper around the Context-manager StreamContext that selects a given stream. |
| [`set_device`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.set_device.html#torch.cpu.set_device "torch.cpu.set_device") | Sets the current device, in CPU we do nothing. |
| [`device_count`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.device_count.html#torch.cpu.device_count "torch.cpu.device_count") | Returns number of CPU devices (not cores). |
| [`StreamContext`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.StreamContext.html#torch.cpu.StreamContext "torch.cpu.StreamContext") | Context-manager that selects a given stream. |

Streams and events[#](https://docs.pytorch.org/docs/2.15/cpu.html#streams-and-events "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cpu.Stream_class.html#torch.cpu.Stream "torch.cpu.Stream") | N.B. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cpu.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cpu.md.txt)

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