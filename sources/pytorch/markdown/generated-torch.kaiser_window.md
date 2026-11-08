Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.kaiser_window.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.kaiser_window.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.kaiser_window.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.kaiser_window.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.kaiser_window.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.kaiser_window.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.kaiser_window.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.kaiser_window.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.kaiser_window.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.kaiser_window.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.kaiser_window.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.kaiser_window.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.kaiser_window.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.kaiser_window.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.kaiser_window.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.kaiser_window.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.kaiser_window.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.kaiser_window.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.kaiser_window.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.kaiser_window.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.kaiser_window.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.kaiser_window.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.kaiser_window.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.kaiser_window.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.kaiser_window.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.kaiser_window.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.kaiser_window.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.kaiser_window.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.kaiser_window.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.kaiser_window.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.kaiser_window.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.kaiser_window.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.kaiser_window.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.kaiser_window.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.kaiser_window.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.kaiser_window.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.kaiser_window.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.kaiser_window.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.kaiser_window.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.kaiser_window.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.kaiser_window.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.kaiser_window.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.kaiser_window.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.kaiser_window.html)

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

torch.kaiser\_window[#](https://docs.pytorch.org/docs/2.15/generated/torch.kaiser_window.html#torch-kaiser-window "Link to this heading")

==========================================================================================================================================

torch.kaiser\_window(_window\_length_, _periodic\=True_, _beta\=12.0_, _\*_, _dtype\=None_, _layout\=torch.strided_, _device\=None_, _requires\_grad\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.kaiser_window.html#torch.kaiser_window "Link to this definition")

Computes the Kaiser window with window length `window_length` and shape parameter `beta`.

Let I\_0 be the zeroth order modified Bessel function of the first kind (see [`torch.i0()`](https://docs.pytorch.org/docs/2.15/generated/torch.i0.html#torch.i0 "torch.i0")
) and `N = L - 1` if `periodic` is False and `L` if `periodic` is True, where `L` is the `window_length`. This function computes:

outi\=I0(β1−(i−N/2N/2)2)/I0(β)out\_i = I\_0 \\left( \\beta \\sqrt{1 - \\left( {\\frac{i - N/2}{N/2}} \\right) ^2 } \\right) / I\_0( \\beta ) outi​\=I0​​β1−(N/2i−N/2​)2​​/I0​(β)

Calling `torch.kaiser_window(L, B, periodic=True)` is equivalent to calling `torch.kaiser_window(L + 1, B, periodic=False)[:-1])`. The `periodic` argument is intended as a helpful shorthand to produce a periodic window as input to functions like [`torch.stft()`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft")
.

Note

If `window_length` is one, then the returned window is a single element tensor containing a one.

Parameters:

*   **window\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – length of the window.
    
*   **periodic** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, returns a periodic window suitable for use in spectral analysis. If False, returns a symmetric window suitable for use in filter design.
    
*   **beta** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – shape parameter for the window.
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ).
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned window tensor. Only `torch.strided` (dense layout) is supported.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.kaiser_window.rst.txt)

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