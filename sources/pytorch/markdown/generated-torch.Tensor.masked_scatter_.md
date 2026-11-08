Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.masked_scatter_.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.masked_scatter_.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.masked_scatter_.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.masked_scatter_.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.masked_scatter_.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.masked_scatter_.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.masked_scatter_.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.masked_scatter_.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.masked_scatter_.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.masked_scatter_.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.masked_scatter_.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.masked_scatter_.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.masked_scatter_.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.masked_scatter_.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.masked_scatter_.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.masked_scatter_.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.masked_scatter_.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.masked_scatter_.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.masked_scatter_.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.masked_scatter_.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.masked_scatter_.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.masked_scatter_.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.masked_scatter_.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.masked_scatter_.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.masked_scatter_.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.masked_scatter_.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.masked_scatter_.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.masked_scatter_.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.masked_scatter_.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.masked_scatter_.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.masked_scatter_.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.masked_scatter_.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.masked_scatter_.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.masked_scatter_.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.masked_scatter_.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.masked_scatter_.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.masked_scatter_.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.masked_scatter_.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.masked_scatter_.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.masked_scatter_.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.masked_scatter_.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.masked_scatter_.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.masked_scatter_.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.masked_scatter_.html)

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

torch.Tensor.masked\_scatter\_[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.masked_scatter_.html#torch-tensor-masked-scatter "Link to this heading")

=====================================================================================================================================================================

Tensor.masked\_scatter\_(_mask_, _source_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.masked_scatter_.html#torch.Tensor.masked_scatter_ "Link to this definition")

Copies elements from `source` into `self` tensor at positions where the `mask` is True. Elements from `source` are copied into `self` starting at position 0 of `source` and continuing in order one-by-one for each occurrence of `mask` being True. The shape of `mask` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with the shape of the underlying tensor. The `source` should have at least as many elements as the number of ones in `mask`.

Parameters:

*   **mask** (_BoolTensor_) – the boolean mask
    
*   **source** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to copy from
    

Note

The `mask` operates on the `self` tensor, not on the given `source` tensor.

Example

\>>> self \= torch.tensor(\[\[0, 0, 0, 0, 0\], \[0, 0, 0, 0, 0\]\])
\>>> mask \= torch.tensor(
...     \[\[0, 0, 0, 1, 1\], \[1, 1, 0, 1, 1\]\],
...     dtype\=torch.bool,
... )
\>>> source \= torch.tensor(\[\[0, 1, 2, 3, 4\], \[5, 6, 7, 8, 9\]\])
\>>> self.masked\_scatter\_(mask, source)
tensor(\[\[0, 0, 0, 0, 1\],\
        \[2, 3, 0, 4, 5\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.masked_scatter_.rst.txt)

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