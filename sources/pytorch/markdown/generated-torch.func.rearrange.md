Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.rearrange.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.rearrange.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.rearrange.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.rearrange.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.rearrange.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.rearrange.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.rearrange.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.rearrange.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.rearrange.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.rearrange.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.rearrange.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.rearrange.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.rearrange.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.rearrange.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.rearrange.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.rearrange.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.rearrange.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.rearrange.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.rearrange.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.rearrange.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.rearrange.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.rearrange.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.rearrange.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.rearrange.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.rearrange.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.rearrange.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.rearrange.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.rearrange.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.rearrange.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.rearrange.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.rearrange.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.rearrange.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.rearrange.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.rearrange.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.rearrange.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.rearrange.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.rearrange.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.rearrange.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.rearrange.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.rearrange.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.rearrange.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.rearrange.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.rearrange.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.rearrange.html)

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

torch.func.rearrange[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.rearrange.html#torch-func-rearrange "Link to this heading")

============================================================================================================================================

torch.func.rearrange(_tensor_, _pattern_, _\*\*axes\_lengths_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/einops.py#L10)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.rearrange.html#torch.func.rearrange "Link to this definition")

A native implementation of einops.rearrange, a reader-friendly smart element reordering for multidimensional tensors. This operation includes functionality of transpose (axes permutation), reshape (view), squeeze, unsqueeze, stack, concatenate and other operations.

See: [https://einops.rocks/api/rearrange/](https://einops.rocks/api/rearrange/)

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _sequence_ _of_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor(s) to rearrange
    
*   **pattern** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – the rearrangement pattern
    
*   **axes\_lengths** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – any additional length specifications for dimensions
    

Returns:

the rearranged tensor

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> from torch.func import rearrange
\>>> \# suppose we have a set of 32 images in "h w c" format (height-width-channel)
\>>> images \= torch.randn((32, 30, 40, 3))

Copy to clipboard

\>>> \# stack along first (batch) axis, output is a single array
\>>> rearrange(images, "b h w c -> b h w c").shape
torch.Size(\[32, 30, 40, 3\])

Copy to clipboard

\>>> \# concatenate images along height (vertical axis), 960 = 32 \* 30
\>>> rearrange(images, "b h w c -> (b h) w c").shape
torch.Size(\[960, 40, 3\])

Copy to clipboard

\>>> \# concatenated images along horizontal axis, 1280 = 32 \* 40
\>>> rearrange(images, "b h w c -> h (b w) c").shape
torch.Size(\[30, 1280, 3\])

Copy to clipboard

\>>> \# reordered axes to "b c h w" format for deep learning
\>>> rearrange(images, "b h w c -> b c h w").shape
torch.Size(\[32, 3, 30, 40\])

Copy to clipboard

\>>> \# flattened each image into a vector, 3600 = 30 \* 40 \* 3
\>>> rearrange(images, "b h w c -> b (c h w)").shape
torch.Size(\[32, 3600\])

Copy to clipboard

\>>> \# split each image into 4 smaller (top-left, top-right, bottom-left, bottom-right), 128 = 32 \* 2 \* 2
\>>> rearrange(images, "b (h1 h) (w1 w) c -> (b h1 w1) h w c", h1\=2, w1\=2).shape
torch.Size(\[128, 15, 20, 3\])

Copy to clipboard

\>>> \# space-to-depth operation
\>>> rearrange(images, "b (h h1) (w w1) c -> b h w (c h1 w1)", h1\=2, w1\=2).shape
torch.Size(\[32, 15, 20, 12\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.rearrange.rst.txt)

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