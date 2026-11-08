Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nn.attention.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nn.attention.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nn.attention.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nn.attention.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nn.attention.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nn.attention.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nn.attention.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nn.attention.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nn.attention.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nn.attention.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nn.attention.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nn.attention.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nn.attention.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nn.attention.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nn.attention.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nn.attention.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nn.attention.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nn.attention.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nn.attention.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nn.attention.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nn.attention.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nn.attention.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nn.attention.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nn.attention.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nn.attention.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nn.attention.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nn.attention.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nn.attention.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nn.attention.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nn.attention.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nn.attention.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nn.attention.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nn.attention.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nn.attention.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nn.attention.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nn.attention.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nn.attention.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nn.attention.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nn.attention.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nn.attention.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nn.attention.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nn.attention.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nn.attention.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nn.attention.html)

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

torch.nn.attention[#](https://docs.pytorch.org/docs/2.15/nn.attention.html#module-torch.nn.attention "Link to this heading")

=============================================================================================================================

Created On: Jan 24, 2024 | Last Updated On: May 07, 2026

This module contains functions and classes that alter the behavior of torch.nn.functional.scaled\_dot\_product\_attention

Utils[#](https://docs.pytorch.org/docs/2.15/nn.attention.html#utils "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`sdpa_kernel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel "torch.nn.attention.sdpa_kernel") | Context manager to select which backend to use for scaled dot product attention. |
| [`SDPBackend`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.SDPBackend.html#torch.nn.attention.SDPBackend "torch.nn.attention.SDPBackend") | An enum-like class that contains the different backends for scaled dot product attention. |
| [`register_flash_attention_impl`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.register_flash_attention_impl.html#torch.nn.attention.register_flash_attention_impl "torch.nn.attention.register_flash_attention_impl") | Register the callable that activates a flash attention impl. |
| [`activate_flash_attention_impl`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.activate_flash_attention_impl.html#torch.nn.attention.activate_flash_attention_impl "torch.nn.attention.activate_flash_attention_impl") | Activate into the dispatcher a previously registered flash attention impl. |
| [`list_flash_attention_impls`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.list_flash_attention_impls.html#torch.nn.attention.list_flash_attention_impls "torch.nn.attention.list_flash_attention_impls") | Return the names of all available flash attention implementations. |
| [`current_flash_attention_impl`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.current_flash_attention_impl.html#torch.nn.attention.current_flash_attention_impl "torch.nn.attention.current_flash_attention_impl") | Return the currently activated flash attention impl name, if any. |
| [`restore_flash_attention_impl`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.restore_flash_attention_impl.html#torch.nn.attention.restore_flash_attention_impl "torch.nn.attention.restore_flash_attention_impl") | Restore the default FA2 implementation |

Submodules[#](https://docs.pytorch.org/docs/2.15/nn.attention.html#submodules "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`flex_attention`](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#module-torch.nn.attention.flex_attention "torch.nn.attention.flex_attention") | This module implements the user facing API for flex\_attention in PyTorch. |
| [`bias`](https://docs.pytorch.org/docs/2.15/nn.attention.bias.html#module-torch.nn.attention.bias "torch.nn.attention.bias") | Defines bias subclasses that work with scaled\_dot\_product\_attention |
| [`experimental`](https://docs.pytorch.org/docs/2.15/nn.attention.experimental.html#module-torch.nn.attention.experimental "torch.nn.attention.experimental") |     |
| [`varlen`](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#module-torch.nn.attention.varlen "torch.nn.attention.varlen") | Variable-length attention implementation using Flash Attention. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nn.attention.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nn.attention.md.txt)

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