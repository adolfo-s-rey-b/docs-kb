Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.RMSNorm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.RMSNorm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.RMSNorm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.RMSNorm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.RMSNorm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.RMSNorm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.RMSNorm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.RMSNorm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.RMSNorm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.RMSNorm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.RMSNorm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.RMSNorm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.RMSNorm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.RMSNorm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.RMSNorm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.RMSNorm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.RMSNorm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.RMSNorm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.RMSNorm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.RMSNorm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.RMSNorm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.RMSNorm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.RMSNorm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.RMSNorm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.RMSNorm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.RMSNorm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.RMSNorm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.RMSNorm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.RMSNorm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.RMSNorm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.RMSNorm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.RMSNorm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.RMSNorm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.RMSNorm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.RMSNorm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.RMSNorm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.RMSNorm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.RMSNorm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.RMSNorm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.RMSNorm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.RMSNorm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.RMSNorm.html)

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

RMSNorm[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#rmsnorm "Link to this heading")

==============================================================================================================

_class_ torch.nn.RMSNorm(_normalized\_shape_, _eps\=None_, _elementwise\_affine\=True_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/normalization.py#L343)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#torch.nn.RMSNorm "Link to this definition")

Applies Root Mean Square Layer Normalization over a mini-batch of inputs.

This layer implements the operation as described in the paper [Root Mean Square Layer Normalization](https://arxiv.org/pdf/1910.07467.pdf)

yi\=xiRMS(x)∗γi,whereRMS(x)\=ϵ+1n∑i\=1nxi2y\_i = \\frac{x\_i}{\\mathrm{RMS}(x)} \* \\gamma\_i, \\quad \\text{where} \\quad \\text{RMS}(x) = \\sqrt{\\epsilon + \\frac{1}{n} \\sum\_{i=1}^{n} x\_i^2} yi​\=RMS(x)xi​​∗γi​,whereRMS(x)\=ϵ+n1​i\=1∑n​xi2​​

The RMS is taken over the last `D` dimensions, where `D` is the dimension of `normalized_shape`. For example, if `normalized_shape` is `(3, 5)` (a 2-dimensional shape), the RMS is computed over the last 2 dimensions of the input.

Parameters:

*   **normalized\_shape** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _or_ [_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
    ) –
    
    input shape from an expected input of size
    
    \[∗×normalized\_shape\[0\]×normalized\_shape\[1\]×…×normalized\_shape\[−1\]\]\[\* \\times \\text{normalized\\\_shape}\[0\] \\times \\text{normalized\\\_shape}\[1\] \\times \\ldots \\times \\text{normalized\\\_shape}\[-1\]\] \[∗×normalized\_shape\[0\]×normalized\_shape\[1\]×…×normalized\_shape\[−1\]\]
    
    If a single integer is used, it is treated as a singleton list, and this module will normalize over the last dimension which is expected to be of that specific size.
    
*   **eps** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – a value added to the denominator for numerical stability. If not specified, uses the machine epsilon of the computation (opmath) type: fp16/bf16 and fp32 inputs use `torch.finfo(torch.float32).eps`, while fp64 inputs use `torch.finfo(torch.float64).eps`. Default: `None`
    
*   **elementwise\_affine** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – a boolean value that when set to `True`, this module has learnable per-element affine parameters initialized to ones (for weights). Default: `True`.
    

Shape:

*   Input: (N,∗)(N, \*)(N,∗)
    
*   Output: (N,∗)(N, \*)(N,∗) (same shape as input)
    

Examples:

\>>> rms\_norm \= nn.RMSNorm(\[2, 3\])
\>>> input \= torch.randn(2, 2, 3)
\>>> rms\_norm(input)

Copy to clipboard

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/normalization.py#L429)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#torch.nn.RMSNorm.extra_repr "Link to this definition")

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

forward(_x_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/normalization.py#L423)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#torch.nn.RMSNorm.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

reset\_parameters()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/normalization.py#L416)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RMSNorm.html#torch.nn.RMSNorm.reset_parameters "Link to this definition")

Resets parameters based on their initialization used in \_\_init\_\_.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.RMSNorm.rst.txt)

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