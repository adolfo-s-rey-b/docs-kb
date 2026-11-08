Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.empty_permuted.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.empty_permuted.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.empty_permuted.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.empty_permuted.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.empty_permuted.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.empty_permuted.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.empty_permuted.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.empty_permuted.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.empty_permuted.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.empty_permuted.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.empty_permuted.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.empty_permuted.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.empty_permuted.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.empty_permuted.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.empty_permuted.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.empty_permuted.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.empty_permuted.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.empty_permuted.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.empty_permuted.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.empty_permuted.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.empty_permuted.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.empty_permuted.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.empty_permuted.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.empty_permuted.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.empty_permuted.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.empty_permuted.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.empty_permuted.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.empty_permuted.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.empty_permuted.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.empty_permuted.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.empty_permuted.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.empty_permuted.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.empty_permuted.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.empty_permuted.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.empty_permuted.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.empty_permuted.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.empty_permuted.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.empty_permuted.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.empty_permuted.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.empty_permuted.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.empty_permuted.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.empty_permuted.html)

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

torch.empty\_permuted[#](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html#torch-empty-permuted "Link to this heading")

=============================================================================================================================================

torch.empty\_permuted(_size_, _physical\_layout_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _requires\_grad\=False_, _pin\_memory\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html#torch.empty_permuted "Link to this definition")

Creates an uninitialized, non-overlapping and dense tensor with the specified `size`, with `physical_layout` specifying how the dimensions are physically laid out in memory (each logical dimension is listed from outermost to innermost). `physical_layout` is a generalization of NCHW/NHWC notation: if each dimension is assigned a number according to what order they occur in size (N=0, C=1, H=2, W=3), then NCHW is `(0, 1, 2, 3)` while NHWC is `(0, 2, 3, 1)`. Equivalently, the strides of the output tensor `t` are such that `t.stride(physical_layout[i]) == contiguous_strides[i]` (notably, this function is _not_ equivalent to `torch.empty(size).permute(physical_layout)`).

Unlike [`torch.empty_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_strided.html#torch.empty_strided "torch.empty_strided")
, this is guaranteed to produce a dense tensor with no overlaps. If possible, prefer using this function over [`torch.empty_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_strided.html#torch.empty_strided "torch.empty_strided")
 or manual use of [`torch.as_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided.html#torch.as_strided "torch.as_strided")
.

Note

If [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 and [`torch.utils.deterministic.fill_uninitialized_memory`](https://docs.pytorch.org/docs/2.15/deterministic.html#torch.utils.deterministic.fill_uninitialized_memory "torch.utils.deterministic.fill_uninitialized_memory")
 are both set to `True`, the output tensor is initialized to prevent any possible nondeterministic behavior from using the data as an input to an operation. Floating point and complex tensors are filled with NaN, and integer tensors are filled with the maximum value.

Parameters:

*   **size** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the shape of the output tensor
    
*   **physical\_layout** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the ordering of dimensions physically in memory
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ).
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned Tensor. Default: `torch.strided`.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    

Examples

\>>> torch.empty((2, 3, 5, 7)).stride()
(105, 35, 7, 1)
\>>> torch.empty\_permuted((2, 3, 5, 7), (0, 1, 2, 3)).stride()
(105, 35, 7, 1)
\>>> torch.empty((2, 3, 5, 7), memory\_format\=torch.channels\_last).stride()
(105, 1, 21, 3)
\>>> torch.empty\_permuted((2, 3, 5, 7), (0, 2, 3, 1)).stride()
(105, 1, 21, 3)
\>>> torch.empty\_permuted((2, 3, 5, 7), (0, 2, 3, 1)).dim\_order()
(0, 2, 3, 1)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.empty_permuted.rst.txt)

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