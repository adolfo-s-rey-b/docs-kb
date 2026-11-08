Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.empty.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.empty.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.empty.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.empty.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.empty.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.empty.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.empty.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.empty.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.empty.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.empty.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.empty.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.empty.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.empty.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.empty.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.empty.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.empty.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.empty.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.empty.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.empty.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.empty.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.empty.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.empty.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.empty.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.empty.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.empty.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.empty.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.empty.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.empty.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.empty.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.empty.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.empty.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.empty.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.empty.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.empty.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.empty.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.empty.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.empty.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.empty.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.empty.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.empty.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.empty.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.empty.html)

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

torch.empty[#](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch-empty "Link to this heading")

=================================================================================================================

torch.empty(_\*size_, _\*_, _out=None_, _dtype=None_, _layout=torch.strided_, _device=None_, _requires\_grad=False_, _pin\_memory=False_, _memory\_format=torch.contiguous\_format_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "Link to this definition")

Returns a tensor filled with uninitialized data. The shape of the tensor is defined by the variable argument `size`.

Note

If [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 and [`torch.utils.deterministic.fill_uninitialized_memory`](https://docs.pytorch.org/docs/2.15/deterministic.html#torch.utils.deterministic.fill_uninitialized_memory "torch.utils.deterministic.fill_uninitialized_memory")
 are both set to `True`, the output tensor is initialized to prevent any possible nondeterministic behavior from using the data as an input to an operation. Floating point and complex tensors are filled with NaN, and integer tensors are filled with the maximum value.

Warning

For `dtype=torch.bool`, the uninitialized bytes may hold values other than `0` (`False`) and `1` (`True`), which are not valid booleans. The behavior of operations that read such values is undefined: they may be preserved as-is or normalized to `1` depending on the operation, device and memory layout. Write to the tensor (e.g. with [`fill_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.fill_.html#torch.Tensor.fill_ "torch.Tensor.fill_")
 or [`copy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.copy_.html#torch.Tensor.copy_ "torch.Tensor.copy_")
) before reading from it, or use [`torch.zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros")
 instead.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_..._) – a sequence of integers defining the shape of the output tensor. Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    
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
    
*   **memory\_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
    , optional) – the desired memory format of returned Tensor. Default: `torch.contiguous_format`.
    

Example:

\>>> torch.empty((2,3), dtype\=torch.int64)
tensor(\[\[ 9.4064e+13,  2.8000e+01,  9.3493e+13\],\
        \[ 7.5751e+18,  7.1428e+18,  7.5955e+18\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.empty.rst.txt)

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