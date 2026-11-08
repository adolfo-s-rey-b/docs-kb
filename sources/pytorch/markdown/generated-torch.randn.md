Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.randn.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.randn.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.randn.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.randn.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.randn.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.randn.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.randn.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.randn.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.randn.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.randn.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.randn.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.randn.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.randn.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.randn.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.randn.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.randn.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.randn.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.randn.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.randn.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.randn.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.randn.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.randn.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.randn.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.randn.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.randn.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.randn.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.randn.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.randn.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.randn.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.randn.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.randn.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.randn.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.randn.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.randn.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.randn.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.randn.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.randn.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.randn.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.randn.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.randn.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.randn.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.randn.html)

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

torch.randn[#](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#torch-randn "Link to this heading")

=================================================================================================================

torch.randn(_\*size_, _\*_, _generator=None_, _out=None_, _dtype=None_, _layout=torch.strided_, _device=None_, _requires\_grad=False_, _pin\_memory=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#torch.randn "Link to this definition")

Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution).

outi∼N(0,1)\\text{out}\_{i} \\sim \\mathcal{N}(0, 1) outi​∼N(0,1)

For complex dtypes, the tensor is i.i.d. sampled from a [complex normal distribution](https://en.wikipedia.org/wiki/Complex_normal_distribution)
 with zero mean and unit variance as

outi∼CN(0,1)\\text{out}\_{i} \\sim \\mathcal{CN}(0, 1) outi​∼CN(0,1)

This is equivalent to separately sampling the real (Re⁡)(\\operatorname{Re})(Re) and imaginary (Im⁡)(\\operatorname{Im})(Im) part of outi\\text{out}\_iouti​ as

Re⁡(outi)∼N(0,12),Im⁡(outi)∼N(0,12)\\operatorname{Re}(\\text{out}\_{i}) \\sim \\mathcal{N}(0, \\frac{1}{2}),\\quad \\operatorname{Im}(\\text{out}\_{i}) \\sim \\mathcal{N}(0, \\frac{1}{2}) Re(outi​)∼N(0,21​),Im(outi​)∼N(0,21​)

The shape of the tensor is defined by the variable argument `size`.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_..._) – a sequence of integers defining the shape of the output tensor. Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

*   **generator** ([`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    , optional) – a pseudorandom number generator for sampling
    
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
    

Example:

\>>> torch.randn(4)
tensor(\[-2.1436,  0.9966,  2.3426, -0.6366\])
\>>> torch.randn(2, 3)
tensor(\[\[ 1.5954,  2.8929, -1.0923\],\
        \[ 1.1719, -0.4709, -0.1996\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.randn.rst.txt)

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