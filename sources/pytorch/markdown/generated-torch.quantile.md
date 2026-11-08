Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.quantile.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.quantile.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.quantile.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.quantile.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.quantile.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.quantile.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.quantile.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.quantile.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.quantile.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.quantile.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.quantile.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.quantile.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.quantile.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.quantile.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.quantile.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.quantile.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.quantile.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.quantile.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.quantile.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.quantile.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.quantile.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.quantile.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.quantile.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.quantile.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.quantile.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.quantile.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.quantile.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.quantile.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.quantile.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.quantile.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.quantile.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.quantile.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.quantile.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.quantile.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.quantile.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.quantile.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.quantile.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.quantile.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.quantile.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.quantile.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.quantile.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.quantile.html)

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

torch.quantile[#](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch-quantile "Link to this heading")

==========================================================================================================================

torch.quantile(_input_, _q_, _dim\=None_, _keepdim\=False_, _\*_, _interpolation\='linear'_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch.quantile "Link to this definition")

Computes the q-th quantiles of each row of the `input` tensor along the dimension `dim`.

To compute the quantile, we map q in \[0, 1\] to the range of indices \[0, n\] to find the location of the quantile in the sorted input. If the quantile lies between two data points `a < b` with indices `i` and `j` in the sorted order, result is computed according to the given `interpolation` method as follows:

*   `linear`: `a + (b - a) * fraction`, where `fraction` is the fractional part of the computed quantile index.
    
*   `lower`: `a`.
    
*   `higher`: `b`.
    
*   `nearest`: `a` or `b`, whichever’s index is closer to the computed quantile index (follows [`torch.round()`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round")
    ).
    
*   `midpoint`: `(a + b) / 2`.
    

If `q` is a 1D tensor, the first dimension of the output represents the quantiles and has size equal to the size of `q`, the remaining dimensions are what remains from the reduction.

Note

By default `dim` is `None` resulting in the `input` tensor being flattened before computation.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **q** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – a scalar or 1D tensor of values in the range \[0, 1\].
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to reduce.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

*   **interpolation** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – interpolation method to use when the desired quantile lies between two data points. Can be `linear`, `lower`, `higher`, `midpoint` and `nearest`. Default is `linear`.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> a \= torch.randn(2, 3)
\>>> a
tensor(\[\[ 0.0795, -1.2117,  0.9765\],\
        \[ 1.1707,  0.6706,  0.4884\]\])
\>>> q \= torch.tensor(\[0.25, 0.5, 0.75\])
\>>> torch.quantile(a, q, dim\=1, keepdim\=True)
tensor(\[\[\[-0.5661\],\
        \[ 0.5795\]\],\
\
        \[\[ 0.0795\],\
        \[ 0.6706\]\],\
\
        \[\[ 0.5280\],\
        \[ 0.9206\]\]\])
\>>> torch.quantile(a, q, dim\=1, keepdim\=True).shape
torch.Size(\[3, 2, 1\])
\>>> a \= torch.arange(4.)
\>>> a
tensor(\[0., 1., 2., 3.\])
\>>> torch.quantile(a, 0.6, interpolation\='linear')
tensor(1.8000)
\>>> torch.quantile(a, 0.6, interpolation\='lower')
tensor(1.)
\>>> torch.quantile(a, 0.6, interpolation\='higher')
tensor(2.)
\>>> torch.quantile(a, 0.6, interpolation\='midpoint')
tensor(1.5000)
\>>> torch.quantile(a, 0.6, interpolation\='nearest')
tensor(2.)
\>>> torch.quantile(a, 0.4, interpolation\='nearest')
tensor(1.)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.quantile.rst.txt)

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