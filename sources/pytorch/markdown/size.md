Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/size.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/size.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/size.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/size.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/size.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/size.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/size.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/size.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/size.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/size.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/size.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/size.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/size.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/size.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/size.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/size.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/size.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/size.html)
[v1.13](https://docs.pytorch.org/docs/1.13/size.html)
[v1.12](https://docs.pytorch.org/docs/1.12/size.html)
[v1.11](https://docs.pytorch.org/docs/1.11/size.html)
[v1.10](https://docs.pytorch.org/docs/1.10/size.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/size.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/size.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/size.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/size.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/size.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/size.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/size.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/size.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/size.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/size.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/size.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/size.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/size.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/size.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/size.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/size.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/size.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/size.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/size.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/size.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/size.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/size.html)

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

torch.Size[#](https://docs.pytorch.org/docs/2.15/size.html#torch-size "Link to this heading")

==============================================================================================

Created On: Apr 19, 2024 | Last Updated On: Jun 18, 2025

[`torch.Size`](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
 is the result type of a call to [`torch.Tensor.size()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.size.html#torch.Tensor.size "torch.Tensor.size")
. It describes the size of all dimensions of the original tensor. As a subclass of [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
, it supports common sequence operations like indexing and length.

Example:

    \>>> x \= torch.ones(10, 20, 30)
    \>>> s \= x.size()
    \>>> s
    torch.Size(\[10, 20, 30\])
    \>>> s\[1\]
    20
    \>>> len(s)
    3

Copy to clipboard

_class_ torch.Size(_iterable\=()_, _/_)[#](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "Link to this definition")

count(_value_, _/_)[#](https://docs.pytorch.org/docs/2.15/size.html#torch.Size.count "Link to this definition")

Return number of occurrences of value.

index(_value_, _start\=0_, _stop\=9223372036854775807_, _/_)[#](https://docs.pytorch.org/docs/2.15/size.html#torch.Size.index "Link to this definition")

Return first index of value.

Raises ValueError if the value is not present.

numel() → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/size.html#torch.Size.numel "Link to this definition")

Returns the number of elements a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 with the given size would contain.

More formally, for a tensor `x = tensor.ones(10, 10)` with size `s = torch.Size([10, 10])`, `x.numel() == x.size().numel() == s.numel() == 100` holds true.

Example:

\>>> x\=torch.ones(10, 10)
\>>> s\=x.size()
\>>> s
torch.Size(\[10, 10\])
\>>> s.numel()
100
\>>> x.numel() \== s.numel()
True

Copy to clipboard

Warning

This function does not return the number of dimensions described by [`torch.Size`](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
, but instead the number of elements a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 with that size would contain.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/size.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/size.md.txt)

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