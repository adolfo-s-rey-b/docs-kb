Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.inner.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.inner.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.inner.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.inner.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.inner.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.inner.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.inner.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.inner.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.inner.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.inner.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.inner.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.inner.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.inner.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.inner.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.inner.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.inner.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.inner.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.inner.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.inner.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.inner.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.inner.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.inner.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.inner.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.inner.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.inner.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.inner.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.inner.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.inner.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.inner.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.inner.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.inner.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.inner.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.inner.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.inner.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.inner.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.inner.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.inner.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.inner.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.inner.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.inner.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.inner.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.inner.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.inner.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.inner.html)

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

torch.inner[#](https://docs.pytorch.org/docs/2.15/generated/torch.inner.html#torch-inner "Link to this heading")

=================================================================================================================

torch.inner(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.inner.html#torch.inner "Link to this definition")

Computes the dot product for 1D tensors. For higher dimensions, sums the product of elements from `input` and `other` along their last dimension.

Note

If either `input` or `other` is a scalar, the result is equivalent to torch.mul(input, other).

If both `input` and `other` are non-scalars, the size of their last dimension must match and the result is equivalent to torch.tensordot(input, other, dims=(\[-1\], \[-1\]))

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – First input tensor
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Second input tensor
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – Optional output tensor to write result into. The output shape is input.shape\[:-1\] + other.shape\[:-1\].

Example:

\# Dot product
\>>> torch.inner(torch.tensor(\[1, 2, 3\]), torch.tensor(\[0, 2, 1\]))
tensor(7)

\# Multidimensional input tensors
\>>> a \= torch.randn(2, 3)
\>>> a
tensor(\[\[0.8173, 1.0874, 1.1784\],\
        \[0.3279, 0.1234, 2.7894\]\])
\>>> b \= torch.randn(2, 4, 3)
\>>> b
tensor(\[\[\[\-0.4682, \-0.7159,  0.1506\],\
        \[ 0.4034, \-0.3657,  1.0387\],\
        \[ 0.9892, \-0.6684,  0.1774\],\
        \[ 0.9482,  1.3261,  0.3917\]\],\
\
        \[\[ 0.4537,  0.7493,  1.1724\],\
        \[ 0.2291,  0.5749, \-0.2267\],\
        \[\-0.7920,  0.3607, \-0.3701\],\
        \[ 1.3666, \-0.5850, \-1.7242\]\]\])
\>>> torch.inner(a, b)
tensor(\[\[\[\-0.9837,  1.1560,  0.2907,  2.6785\],\
        \[ 2.5671,  0.5452, \-0.6912, \-1.5509\]\],\
\
        \[\[ 0.1782,  2.9843,  0.7366,  1.5672\],\
        \[ 3.5115, \-0.4864, \-1.2476, \-4.4337\]\]\])

\# Scalar input
\>>> torch.inner(a, torch.tensor(2))
tensor(\[\[1.6347, 2.1748, 2.3567\],\
        \[0.6558, 0.2469, 5.5787\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.inner.rst.txt)

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