Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.tensordot.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.tensordot.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.tensordot.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.tensordot.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.tensordot.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.tensordot.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.tensordot.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.tensordot.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.tensordot.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.tensordot.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.tensordot.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.tensordot.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.tensordot.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.tensordot.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.tensordot.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.tensordot.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.tensordot.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.tensordot.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.tensordot.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.tensordot.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.tensordot.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.tensordot.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.tensordot.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.tensordot.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.tensordot.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.tensordot.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.tensordot.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.tensordot.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.tensordot.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.tensordot.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.tensordot.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.tensordot.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.tensordot.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.tensordot.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.tensordot.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.tensordot.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.tensordot.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.tensordot.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.tensordot.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.tensordot.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.tensordot.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.tensordot.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.tensordot.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.tensordot.html)

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

torch.functional.tensordot[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.tensordot.html#torch-functional-tensordot "Link to this heading")

==============================================================================================================================================================

torch.functional.tensordot(_a_, _b_, _dims\=2_, _out\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L1306)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.tensordot.html#torch.functional.tensordot "Link to this definition")

Returns a contraction of a and b over multiple dimensions.

[`tensordot`](https://docs.pytorch.org/docs/2.15/generated/torch.functional.tensordot.html#torch.functional.tensordot "torch.functional.tensordot")
 implements a generalized matrix product.

Parameters:

*   **a** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Left tensor to contract
    
*   **b** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Right tensor to contract
    
*   **dims** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _Tuple__\[__List__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _List__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__\] or_ _List__\[__List__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__\]_ _containing two lists_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – number of dimensions to contract or explicit lists of dimensions for `a` and `b` respectively
    

When called with a non-negative integer argument `dims` = ddd, and the number of dimensions of `a` and `b` is mmm and nnn, respectively, [`tensordot()`](https://docs.pytorch.org/docs/2.15/generated/torch.tensordot.html#torch.tensordot "torch.tensordot")
 computes the tensor rrr of shape `a.shape[:-dims] + b.shape[dims:]` given by:

ri1,...,im−d,j1,...,jn−d\=∑k1,...,kdai1,...,im−d,k1,...,kd×bk1,...,kd,j1,...,jn−d.r\_{i\_1,...,i\_{m-d}, j\_1,...,j\_{n-d}} = \\sum\_{k\_1,...,k\_d} a\_{i\_1,...,i\_{m-d},k\_1,...,k\_d} \\times b\_{k\_1,...,k\_d, j\_1,...,j\_{n-d}}. ri1​,...,im−d​,j1​,...,jn−d​​\=k1​,...,kd​∑​ai1​,...,im−d​,k1​,...,kd​​×bk1​,...,kd​,j1​,...,jn−d​​.

When called with `dims` of the list form, the given dimensions will be contracted in place of the last ddd of `a` and the first ddd of bbb. The sizes in these dimensions must match, but [`tensordot()`](https://docs.pytorch.org/docs/2.15/generated/torch.tensordot.html#torch.tensordot "torch.tensordot")
 will deal with broadcasted dimensions.

Examples:

\>>> a \= torch.arange(60.).reshape(3, 4, 5)
\>>> b \= torch.arange(24.).reshape(4, 3, 2)
\>>> torch.tensordot(a, b, dims\=(\[1, 0\], \[0, 1\]))
tensor(\[\[4400., 4730.\],\
        \[4532., 4874.\],\
        \[4664., 5018.\],\
        \[4796., 5162.\],\
        \[4928., 5306.\]\])

\>>> a \= torch.randn(3, 4, 5, device\='cuda')
\>>> b \= torch.randn(4, 5, 6, device\='cuda')
\>>> c \= torch.tensordot(a, b, dims\=2).cpu()
tensor(\[\[ 8.3504, -2.5436,  6.2922,  2.7556, -1.0732,  3.2741\],\
        \[ 3.3161,  0.0704,  5.0187, -0.4079, -4.3126,  4.8744\],\
        \[ 0.8223,  3.9445,  3.2168, -0.2400,  3.4117,  1.7780\]\])

\>>> a \= torch.randn(3, 5, 4, 6)
\>>> b \= torch.randn(6, 4, 5, 3)
\>>> torch.tensordot(a, b, dims\=(\[2, 1, 3\], \[1, 2, 0\]))
tensor(\[\[  7.7193,  -2.4867, -10.3204\],\
        \[  1.5513, -14.4737,  -6.5113\],\
        \[ -0.2850,   4.2573,  -3.5997\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.tensordot.rst.txt)

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