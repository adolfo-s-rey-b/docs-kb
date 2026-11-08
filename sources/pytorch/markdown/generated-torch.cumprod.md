Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cumprod.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cumprod.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cumprod.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cumprod.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cumprod.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cumprod.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cumprod.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cumprod.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cumprod.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cumprod.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cumprod.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cumprod.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cumprod.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cumprod.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cumprod.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cumprod.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cumprod.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cumprod.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cumprod.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cumprod.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cumprod.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cumprod.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cumprod.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cumprod.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cumprod.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cumprod.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cumprod.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cumprod.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cumprod.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cumprod.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cumprod.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cumprod.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cumprod.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cumprod.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cumprod.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cumprod.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cumprod.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cumprod.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cumprod.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cumprod.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cumprod.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cumprod.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cumprod.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cumprod.html)

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

torch.cumprod[#](https://docs.pytorch.org/docs/2.15/generated/torch.cumprod.html#torch-cumprod "Link to this heading")

=======================================================================================================================

torch.cumprod(_input_, _dim_, _\*_, _dtype\=None_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cumprod.html#torch.cumprod "Link to this definition")

Returns the cumulative product of elements of `input` in the dimension `dim`.

For example, if `input` is a vector of size N, the result will also be a vector of size N, with elements.

yi\=x1×x2×x3×⋯×xiy\_i = x\_1 \\times x\_2\\times x\_3\\times \\dots \\times x\_i yi​\=x1​×x2​×x3​×⋯×xi​

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the dimension to do the operation over
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. If specified, the input tensor is casted to [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
     before the operation is performed. This is useful for preventing data type overflows. Default: None.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> a \= torch.randn(10)
\>>> a
tensor(\[ 0.6001,  0.2069, -0.1919,  0.9792,  0.6727,  1.0062,  0.4126,\
        -0.2129, -0.4206,  0.1968\])
\>>> torch.cumprod(a, dim\=0)
tensor(\[ 0.6001,  0.1241, -0.0238, -0.0233, -0.0157, -0.0158, -0.0065,\
         0.0014, -0.0006, -0.0001\])

\>>> a\[5\] \= 0.0
\>>> torch.cumprod(a, dim\=0)
tensor(\[ 0.6001,  0.1241, -0.0238, -0.0233, -0.0157, -0.0000, -0.0000,\
         0.0000, -0.0000, -0.0000\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cumprod.rst.txt)

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