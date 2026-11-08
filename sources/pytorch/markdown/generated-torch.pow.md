Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.pow.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.pow.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.pow.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.pow.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.pow.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.pow.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.pow.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.pow.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.pow.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.pow.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.pow.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.pow.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.pow.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.pow.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.pow.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.pow.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.pow.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.pow.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.pow.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.pow.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.pow.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.pow.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.pow.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.pow.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.pow.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.pow.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.pow.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.pow.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.pow.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.pow.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.pow.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.pow.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.pow.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.pow.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.pow.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.pow.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.pow.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.pow.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.pow.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.pow.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.pow.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.pow.html)

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

torch.pow[#](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#torch-pow "Link to this heading")

===========================================================================================================

torch.pow(_input_, _exponent_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#torch.pow "Link to this definition")

Takes the power of each element in `input` with `exponent` and returns a tensor with the result.

`exponent` can be either a single `float` number or a Tensor with the same number of elements as `input`.

When `exponent` is a scalar value, the operation applied is:

outi\=xiexponent\\text{out}\_i = x\_i ^ \\text{exponent} outi​\=xiexponent​

When `exponent` is a tensor, the operation applied is:

outi\=xiexponenti\\text{out}\_i = x\_i ^ {\\text{exponent}\_i} outi​\=xiexponenti​​

When `exponent` is a tensor, the shapes of `input` and `exponent` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **exponent** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ _tensor_) – the exponent value
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.randn(4)
\>>> a
tensor(\[ 0.4331,  1.2475,  0.6834, -0.2791\])
\>>> torch.pow(a, 2)
tensor(\[ 0.1875,  1.5561,  0.4670,  0.0779\])
\>>> exp \= torch.arange(1., 5.)

\>>> a \= torch.arange(1., 5.)
\>>> a
tensor(\[ 1.,  2.,  3.,  4.\])
\>>> exp
tensor(\[ 1.,  2.,  3.,  4.\])
\>>> torch.pow(a, exp)
tensor(\[   1.,    4.,   27.,  256.\])

Copy to clipboard

torch.pow(_self_, _exponent_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

`self` is a scalar `float` value, and `exponent` is a tensor. The returned tensor `out` is of the same shape as `exponent`

The operation applied is:

outi\=selfexponenti\\text{out}\_i = \\text{self} ^ {\\text{exponent}\_i} outi​\=selfexponenti​

Parameters:

*   **self** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the scalar base value for the power operation
    
*   **exponent** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the exponent tensor
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> exp \= torch.arange(1., 5.)
\>>> base \= 2
\>>> torch.pow(base, exp)
tensor(\[  2.,   4.,   8.,  16.\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.pow.rst.txt)

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