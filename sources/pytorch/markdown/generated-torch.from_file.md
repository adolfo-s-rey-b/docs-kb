Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.from_file.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.from_file.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.from_file.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.from_file.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.from_file.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.from_file.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.from_file.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.from_file.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.from_file.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.from_file.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.from_file.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.from_file.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.from_file.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.from_file.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.from_file.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.from_file.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.from_file.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.from_file.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.from_file.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.from_file.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.from_file.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.from_file.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.from_file.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.from_file.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.from_file.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.from_file.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.from_file.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.from_file.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.from_file.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.from_file.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.from_file.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.from_file.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.from_file.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.from_file.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.from_file.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.from_file.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.from_file.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.from_file.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.from_file.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.from_file.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.from_file.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.from_file.html)

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

torch.from\_file[#](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch-from-file "Link to this heading")

==============================================================================================================================

torch.from\_file(_filename_, _shared\=None_, _size\=0_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _pin\_memory\=False_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch.from_file "Link to this definition")

Creates a CPU tensor with a storage backed by a memory-mapped file.

If `shared` is True, then memory is shared between processes. All changes are written to the file. If `shared` is False, then changes to the tensor do not affect the file.

`size` is the number of elements in the Tensor. If `shared` is `False`, then the file must contain at least `size * sizeof(dtype)` bytes. If `shared` is `True` the file will be created if needed.

Note

Only CPU tensors can be mapped to files.

Note

For now, tensors with storages backed by a memory-mapped file cannot be created in pinned memory.

Parameters:

*   **filename** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – file name to map
    
*   **shared** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html)
    )
    
*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of elements in the tensor
    

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
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    

Example:

\>>> t \= torch.randn(2, 5, dtype\=torch.float64)
\>>> t.numpy().tofile('storage.pt')
\>>> t\_mapped \= torch.from\_file('storage.pt', shared\=False, size\=10, dtype\=torch.float64)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.from_file.rst.txt)

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