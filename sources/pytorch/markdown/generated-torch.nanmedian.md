Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nanmedian.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nanmedian.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nanmedian.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nanmedian.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nanmedian.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nanmedian.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nanmedian.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nanmedian.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nanmedian.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nanmedian.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nanmedian.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nanmedian.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nanmedian.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nanmedian.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nanmedian.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nanmedian.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nanmedian.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nanmedian.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nanmedian.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nanmedian.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nanmedian.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nanmedian.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nanmedian.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nanmedian.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nanmedian.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nanmedian.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nanmedian.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nanmedian.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nanmedian.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nanmedian.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nanmedian.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nanmedian.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nanmedian.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nanmedian.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nanmedian.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nanmedian.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nanmedian.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nanmedian.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nanmedian.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nanmedian.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nanmedian.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nanmedian.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nanmedian.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nanmedian.html)

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

torch.nanmedian[#](https://docs.pytorch.org/docs/2.15/generated/torch.nanmedian.html#torch-nanmedian "Link to this heading")

=============================================================================================================================

torch.nanmedian(_input_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nanmedian.html#torch.nanmedian "Link to this definition")

Returns the median of the values in `input`, ignoring `NaN` values.

This function is identical to [`torch.median()`](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "torch.median")
 when there are no `NaN` values in `input`. When `input` has one or more `NaN` values, [`torch.median()`](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "torch.median")
 will always return `NaN`, while this function will return the median of the non-`NaN` elements in `input`. If all the elements in `input` are `NaN` it will also return `NaN`.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Example:

\>>> a \= torch.tensor(\[1, float('nan'), 3, 2\])
\>>> a.median()
tensor(nan)
\>>> a.nanmedian()
tensor(2.)

Copy to clipboard

torch.nanmedian(_input_, _dim\=\-1_, _keepdim\=False_, _\*_, _out\=None_)

Returns a namedtuple `(values, indices)` where `values` contains the median of each row of `input` in the dimension `dim`, ignoring `NaN` values, and `indices` contains the index of the median values found in the dimension `dim`.

This function is identical to [`torch.median()`](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "torch.median")
 when there are no `NaN` values in a reduced row. When a reduced row has one or more `NaN` values, [`torch.median()`](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "torch.median")
 will always reduce it to `NaN`, while this function will reduce it to the median of the non-`NaN` elements. If all the elements in a reduced row are `NaN` then it will be reduced to `NaN`, too.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to reduce. If `None`, all dimensions are reduced.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**out** (_(_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_)__,_ _optional_) – The first tensor will be populated with the median values and the second tensor, which must have dtype long, with their indices in the dimension `dim` of `input`.

Example:

\>>> a \= torch.tensor(\[\[2, 3, 1\], \[float('nan'), 1, float('nan')\]\])
\>>> a
tensor(\[\[2., 3., 1.\],\
        \[nan, 1., nan\]\])
\>>> a.median(0)
torch.return\_types.median(values=tensor(\[nan, 1., nan\]), indices=tensor(\[1, 1, 1\]))
\>>> a.nanmedian(0)
torch.return\_types.nanmedian(values=tensor(\[2., 1., 1.\]), indices=tensor(\[0, 1, 0\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nanmedian.rst.txt)

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