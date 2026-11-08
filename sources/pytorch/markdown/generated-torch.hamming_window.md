Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.hamming_window.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.hamming_window.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.hamming_window.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.hamming_window.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.hamming_window.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.hamming_window.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.hamming_window.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.hamming_window.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.hamming_window.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.hamming_window.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.hamming_window.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.hamming_window.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.hamming_window.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.hamming_window.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.hamming_window.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.hamming_window.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.hamming_window.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.hamming_window.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.hamming_window.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.hamming_window.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.hamming_window.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.hamming_window.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.hamming_window.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.hamming_window.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.hamming_window.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.hamming_window.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.hamming_window.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.hamming_window.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.hamming_window.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.hamming_window.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.hamming_window.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.hamming_window.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.hamming_window.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.hamming_window.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.hamming_window.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.hamming_window.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.hamming_window.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.hamming_window.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.hamming_window.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.hamming_window.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.hamming_window.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.hamming_window.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.hamming_window.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.hamming_window.html)

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

torch.hamming\_window[#](https://docs.pytorch.org/docs/2.15/generated/torch.hamming_window.html#torch-hamming-window "Link to this heading")

=============================================================================================================================================

torch.hamming\_window(_window\_length_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _pin\_memory\=False_, _requires\_grad\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.hamming_window.html#torch.hamming_window "Link to this definition")

Hamming window function.

w\[n\]\=α−β cos⁡(2πnN−1),w\[n\] = \\alpha - \\beta\\ \\cos \\left( \\frac{2 \\pi n}{N - 1} \\right), w\[n\]\=α−β cos(N−12πn​),

where NNN is the full window size.

The input `window_length` is a positive integer controlling the returned window size. `periodic` flag determines whether the returned window trims off the last duplicate value from the symmetric window and is ready to be used as a periodic window with functions like [`torch.stft()`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft")
. Therefore, if `periodic` is true, the NNN in above formula is in fact window\_length+1\\text{window\\\_length} + 1window\_length+1. Also, we always have `torch.hamming_window(L, periodic=True)` equal to `torch.hamming_window(L + 1, periodic=False)[:-1])`.

Note

If `window_length` \=1\=1\=1, the returned window contains a single value 1.

Note

This is a generalized version of [`torch.hann_window()`](https://docs.pytorch.org/docs/2.15/generated/torch.hann_window.html#torch.hann_window "torch.hann_window")
.

Parameters:

**window\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – the size of returned window

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ). Only floating point types are supported.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned window tensor. Only `torch.strided` (dense layout) is supported.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

Returns:

A 1-D tensor of size (window\_length,)(\\text{window\\\_length},)(window\_length,) containing the window.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.hamming\_window(_window\_length_, _periodic_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _pin\_memory\=False_, _requires\_grad\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Hamming window function with periodic specified.

Parameters:

*   **window\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the size of returned window
    
*   **periodic** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, returns a window to be used as periodic function. If False, return a symmetric window.
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ). Only floating point types are supported.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned window tensor. Only `torch.strided` (dense layout) is supported.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

Returns:

A 1-D tensor of size (window\_length,)(\\text{window\\\_length},)(window\_length,) containing the window.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.hamming\_window(_window\_length_, _periodic_, _float alpha_, _\*_, _dtype=None_, _layout=None_, _device=None_, _pin\_memory=False_, _requires\_grad=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Hamming window function with periodic and alpha specified.

Parameters:

*   **window\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the size of returned window
    
*   **periodic** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, returns a window to be used as periodic function. If False, return a symmetric window.
    
*   **alpha** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – The coefficient α\\alphaα in the equation above
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ). Only floating point types are supported.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned window tensor. Only `torch.strided` (dense layout) is supported.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

Returns:

A 1-D tensor of size (window\_length,)(\\text{window\\\_length},)(window\_length,) containing the window.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.hamming\_window(_window\_length_, _periodic_, _float alpha_, _float beta_, _\*_, _dtype=None_, _layout=None_, _device=None_, _pin\_memory=False_, _requires\_grad=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Hamming window function with periodic, alpha and beta specified.

Parameters:

*   **window\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the size of returned window
    
*   **periodic** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, returns a window to be used as periodic function. If False, return a symmetric window.
    
*   **alpha** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – The coefficient α\\alphaα in the equation above
    
*   **beta** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – The coefficient β\\betaβ in the equation above
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ). Only floating point types are supported.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned window tensor. Only `torch.strided` (dense layout) is supported.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

Returns:

A 1-D tensor of size (window\_length,)(\\text{window\\\_length},)(window\_length,) containing the window.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.hamming_window.rst.txt)

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