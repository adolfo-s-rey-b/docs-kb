Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/deterministic.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/deterministic.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/deterministic.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/deterministic.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/deterministic.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/deterministic.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/deterministic.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/deterministic.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/deterministic.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/deterministic.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/deterministic.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/deterministic.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/deterministic.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/deterministic.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/deterministic.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/deterministic.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/deterministic.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/deterministic.html)
[v1.13](https://docs.pytorch.org/docs/1.13/deterministic.html)
[v1.12](https://docs.pytorch.org/docs/1.12/deterministic.html)
[v1.11](https://docs.pytorch.org/docs/1.11/deterministic.html)
[v1.10](https://docs.pytorch.org/docs/1.10/deterministic.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/deterministic.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/deterministic.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/deterministic.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/deterministic.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/deterministic.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/deterministic.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/deterministic.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/deterministic.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/deterministic.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/deterministic.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/deterministic.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/deterministic.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/deterministic.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/deterministic.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/deterministic.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/deterministic.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/deterministic.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/deterministic.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/deterministic.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/deterministic.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/deterministic.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/deterministic.html)

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

torch.utils.deterministic[#](https://docs.pytorch.org/docs/2.15/deterministic.html#module-torch.utils.deterministic "Link to this heading")

============================================================================================================================================

Created On: Oct 26, 2023 | Last Updated On: Jun 06, 2025

torch.utils.deterministic.fill\_uninitialized\_memory[#](https://docs.pytorch.org/docs/2.15/deterministic.html#torch.utils.deterministic.fill_uninitialized_memory "Link to this definition")

A [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 that, if True, causes uninitialized memory to be filled with a known value when [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 is set to `True`. Floating point and complex values are set to NaN, and integer values are set to the maximum value.

Default: `True`

Filling uninitialized memory is detrimental to performance. So if your program is valid and does not use uninitialized memory as the input to an operation, then this setting can be turned off for better performance and still be deterministic.

The following operations will fill uninitialized memory when this setting is turned on:

> *   [`torch.Tensor.resize_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#torch.Tensor.resize_ "torch.Tensor.resize_")
>      when called with a tensor that is not quantized
>     
> *   [`torch.empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty")
>     
> *   [`torch.empty_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_strided.html#torch.empty_strided "torch.empty_strided")
>     
> *   [`torch.empty_permuted()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html#torch.empty_permuted "torch.empty_permuted")
>     
> *   [`torch.empty_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_like.html#torch.empty_like "torch.empty_like")
>     

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/deterministic.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/deterministic.md.txt)

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