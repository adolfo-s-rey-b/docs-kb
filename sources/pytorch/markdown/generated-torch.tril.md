Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.tril.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.tril.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.tril.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.tril.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.tril.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.tril.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.tril.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.tril.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.tril.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.tril.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.tril.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.tril.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.tril.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.tril.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.tril.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.tril.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.tril.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.tril.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.tril.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.tril.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.tril.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.tril.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.tril.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.tril.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.tril.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.tril.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.tril.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.tril.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.tril.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.tril.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.tril.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.tril.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.tril.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.tril.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.tril.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.tril.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.tril.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.tril.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.tril.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.tril.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.tril.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.tril.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.tril.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.tril.html)

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

torch.tril[#](https://docs.pytorch.org/docs/2.15/generated/torch.tril.html#torch-tril "Link to this heading")

==============================================================================================================

torch.tril(_input_, _diagonal\=0_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.tril.html#torch.tril "Link to this definition")

Returns the lower triangular part of the matrix (2-D tensor) or batch of matrices `input`, the other elements of the result tensor `out` are set to 0.

The lower triangular part of the matrix is defined as the elements on and below the diagonal.

The argument [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 controls which diagonal to consider. If [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 = 0, all elements on and below the main diagonal are retained. A positive value includes just as many diagonals above the main diagonal, and similarly a negative value excludes just as many diagonals below the main diagonal. The main diagonal are the set of indices {(i,i)}\\lbrace (i, i) \\rbrace{(i,i)} for i∈\[0,min⁡{d1,d2}−1\]i \\in \[0, \\min\\{d\_{1}, d\_{2}\\} - 1\]i∈\[0,min{d1​,d2​}−1\] where d1,d2d\_{1}, d\_{2}d1​,d2​ are the dimensions of the matrix.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **diagonal** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the diagonal to consider
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.randn(3, 3)
\>>> a
tensor(\[\[-1.0813, -0.8619,  0.7105\],\
        \[ 0.0935,  0.1380,  2.2112\],\
        \[-0.3409, -0.9828,  0.0289\]\])
\>>> torch.tril(a)
tensor(\[\[-1.0813,  0.0000,  0.0000\],\
        \[ 0.0935,  0.1380,  0.0000\],\
        \[-0.3409, -0.9828,  0.0289\]\])

\>>> b \= torch.randn(4, 6)
\>>> b
tensor(\[\[ 1.2219,  0.5653, -0.2521, -0.2345,  1.2544,  0.3461\],\
        \[ 0.4785, -0.4477,  0.6049,  0.6368,  0.8775,  0.7145\],\
        \[ 1.1502,  3.2716, -1.1243, -0.5413,  0.3615,  0.6864\],\
        \[-0.0614, -0.7344, -1.3164, -0.7648, -1.4024,  0.0978\]\])
\>>> torch.tril(b, diagonal\=1)
tensor(\[\[ 1.2219,  0.5653,  0.0000,  0.0000,  0.0000,  0.0000\],\
        \[ 0.4785, -0.4477,  0.6049,  0.0000,  0.0000,  0.0000\],\
        \[ 1.1502,  3.2716, -1.1243, -0.5413,  0.0000,  0.0000\],\
        \[-0.0614, -0.7344, -1.3164, -0.7648, -1.4024,  0.0000\]\])
\>>> torch.tril(b, diagonal\=-1)
tensor(\[\[ 0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000\],\
        \[ 0.4785,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000\],\
        \[ 1.1502,  3.2716,  0.0000,  0.0000,  0.0000,  0.0000\],\
        \[-0.0614, -0.7344, -1.3164,  0.0000,  0.0000,  0.0000\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.tril.rst.txt)

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