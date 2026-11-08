Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nanmean.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nanmean.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nanmean.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nanmean.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nanmean.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nanmean.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nanmean.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nanmean.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nanmean.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nanmean.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nanmean.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nanmean.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nanmean.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nanmean.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nanmean.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nanmean.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nanmean.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nanmean.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nanmean.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nanmean.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nanmean.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nanmean.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nanmean.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nanmean.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nanmean.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nanmean.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nanmean.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nanmean.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nanmean.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nanmean.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nanmean.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nanmean.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nanmean.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nanmean.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nanmean.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nanmean.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nanmean.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nanmean.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nanmean.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nanmean.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nanmean.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nanmean.html)

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

torch.nanmean[#](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html#torch-nanmean "Link to this heading")

=======================================================================================================================

torch.nanmean(_input_, _dim\=None_, _keepdim\=False_, _\*_, _dtype\=None_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html#torch.nanmean "Link to this definition")

Computes the mean of all non-NaN elements along the specified dimensions. Input must be floating point or complex.

This function is identical to [`torch.mean()`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean")
 when there are no NaN values in the `input` tensor. In the presence of NaN, [`torch.mean()`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean")
 will propagate the NaN to the output whereas [`torch.nanmean()`](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html#torch.nanmean "torch.nanmean")
 will ignore the NaN values (torch.nanmean(a) is equivalent to torch.mean(a\[~a.isnan()\])).

If `keepdim` is `True`, the output tensor is of the same size as `input` except in the dimension(s) `dim` where it is of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor, either of floating point or complex dtype
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints__,_ _optional_) – the dimension or dimensions to reduce. If `None`, all dimensions are reduced.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. If specified, the input tensor is casted to [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
     before the operation is performed. This is useful for preventing data type overflows. Default: None.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

See also

[`torch.mean()`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean")
 computes the mean value, propagating NaN.

Example:

\>>> x \= torch.tensor(\[\[torch.nan, 1, 2\], \[1, 2, 3\]\])
\>>> x.mean()
tensor(nan)
\>>> x.nanmean()
tensor(1.8000)
\>>> x.mean(dim\=0)
tensor(\[   nan, 1.5000, 2.5000\])
\>>> x.nanmean(dim\=0)
tensor(\[1.0000, 1.5000, 2.5000\])

\# If all elements in the reduced dimensions are NaN then the result is NaN
\>>> torch.tensor(\[torch.nan\]).nanmean()
tensor(nan)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nanmean.rst.txt)

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