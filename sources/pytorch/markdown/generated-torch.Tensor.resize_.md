Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.resize_.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.resize_.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.resize_.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.resize_.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.resize_.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.resize_.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.resize_.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.resize_.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.resize_.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.resize_.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.resize_.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.resize_.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.resize_.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.resize_.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.resize_.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.resize_.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.resize_.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.resize_.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.resize_.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.resize_.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.resize_.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.resize_.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.resize_.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.resize_.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.resize_.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.resize_.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.resize_.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.resize_.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.resize_.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.resize_.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.resize_.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.resize_.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.resize_.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.resize_.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.resize_.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.resize_.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.resize_.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.resize_.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.resize_.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.resize_.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.resize_.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.resize_.html)

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

torch.Tensor.resize\_[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#torch-tensor-resize "Link to this heading")

============================================================================================================================================

Tensor.resize\_(_\*sizes_, _memory\_format\=torch.contiguous\_format_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#torch.Tensor.resize_ "Link to this definition")

Resizes `self` tensor to the specified size. If the number of elements is larger than the current storage size, then the underlying storage is resized to fit the new number of elements. If the number of elements is smaller, the underlying storage is not changed. Existing elements are preserved but any new memory is uninitialized.

Warning

This is a low-level method. The storage is reinterpreted as C-contiguous, ignoring the current strides (unless the target size equals the current size, in which case the tensor is left unchanged). For most purposes, you will instead want to use [`view()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view")
, which checks for contiguity, or [`reshape()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape.html#torch.Tensor.reshape "torch.Tensor.reshape")
, which copies data if needed. To change the size in-place with custom strides, see [`set_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.set_.html#torch.Tensor.set_ "torch.Tensor.set_")
.

Note

If [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 and [`torch.utils.deterministic.fill_uninitialized_memory`](https://docs.pytorch.org/docs/2.15/deterministic.html#torch.utils.deterministic.fill_uninitialized_memory "torch.utils.deterministic.fill_uninitialized_memory")
 are both set to `True`, new elements are initialized to prevent nondeterministic behavior from using the result as an input to an operation. Floating point and complex values are set to NaN, and integer values are set to the maximum value.

Parameters:

*   **sizes** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _..._) – the desired size
    
*   **memory\_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
    , optional) – the desired memory format of Tensor. Default: `torch.contiguous_format`. Note that memory format of `self` is going to be unaffected if `self.size()` matches `sizes`.
    

Example:

\>>> x \= torch.tensor(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> x.resize\_(2, 2)
tensor(\[\[ 1,  2\],\
        \[ 3,  4\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.resize_.rst.txt)

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