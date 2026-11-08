Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.narrow.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.narrow.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.narrow.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.narrow.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.narrow.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.narrow.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.narrow.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.narrow.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.narrow.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.narrow.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.narrow.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.narrow.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.narrow.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.narrow.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.narrow.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.narrow.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.narrow.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.narrow.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.narrow.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.narrow.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.narrow.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.narrow.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.narrow.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.narrow.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.narrow.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.narrow.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.narrow.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.narrow.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.narrow.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.narrow.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.narrow.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.narrow.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.narrow.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.narrow.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.narrow.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.narrow.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.narrow.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.narrow.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.narrow.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.narrow.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.narrow.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.narrow.html)

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

torch.narrow[#](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html#torch-narrow "Link to this heading")

====================================================================================================================

torch.narrow(_input_, _dim_, _start_, _length_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html#torch.narrow "Link to this definition")

Returns a new tensor that is a narrowed version of `input` tensor. The dimension `dim` is input from `start` to `start + length`. The returned tensor and `input` tensor share the same underlying storage.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to narrow
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the dimension along which to narrow
    
*   **start** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – index of the element to start the narrowed dimension from. Can be negative, which means indexing from the end of dim. If Tensor, it must be an 0-dim integral Tensor (bools not allowed)
    
*   **length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – length of the narrowed dimension, must be weakly positive
    

Example:

\>>> x \= torch.tensor(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\])
\>>> torch.narrow(x, 0, 0, 2)
tensor(\[\[ 1,  2,  3\],\
        \[ 4,  5,  6\]\])
\>>> torch.narrow(x, 1, 1, 2)
tensor(\[\[ 2,  3\],\
        \[ 5,  6\],\
        \[ 8,  9\]\])
\>>> torch.narrow(x, \-1, torch.tensor(\-1), 1)
tensor(\[\[3\],\
        \[6\],\
        \[9\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.narrow.rst.txt)

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