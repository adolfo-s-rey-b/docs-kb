Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.norm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.norm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.norm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.norm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.norm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.norm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.norm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.norm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.norm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.norm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.norm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.norm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.norm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.norm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.norm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.norm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.norm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.norm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.norm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.norm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.norm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.norm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.norm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.norm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.norm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.norm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.norm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.norm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.norm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.norm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.norm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.norm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.norm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.norm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.norm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.norm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.norm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.norm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.norm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.norm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.norm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.norm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.norm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.norm.html)

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

torch.functional.norm[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.norm.html#torch-functional-norm "Link to this heading")

===============================================================================================================================================

torch.functional.norm(_input_, _p\='fro'_, _dim\=None_, _keepdim\=False_, _out\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L1734)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.norm.html#torch.functional.norm "Link to this definition")

Returns the matrix norm or vector norm of a given tensor.

Warning

torch.norm is deprecated and may be removed in a future PyTorch release. Its documentation and behavior may be incorrect, and it is no longer actively maintained.

Use [`torch.linalg.vector_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.vector_norm.html#torch.linalg.vector_norm "torch.linalg.vector_norm")
 when computing vector norms and [`torch.linalg.matrix_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_norm.html#torch.linalg.matrix_norm "torch.linalg.matrix_norm")
 when computing matrix norms. For a function with a similar behavior as this one see [`torch.linalg.norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch.linalg.norm "torch.linalg.norm")
. Note, however, the signature for these functions is slightly different than the signature for `torch.norm`.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The input tensor. Its data type must be either a floating point or complex type. For complex inputs, the norm is calculated using the absolute value of each element. If the input is complex and neither `dtype` nor `out` is specified, the result’s data type will be the corresponding floating point type (e.g. float if `input` is complexfloat).
    
*   **p** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _inf__,_ _\-inf__,_ _'fro'__,_ _'nuc'__,_ _optional_) –
    
    the order of norm. Default: `'fro'` The following norms can be calculated:
    
    | ord | matrix norm | vector norm |
    | --- | --- | --- |
    | ’fro’ | Frobenius norm | –   |
    | ‘nuc’ | nuclear norm | –   |
    | Number | –   | sum(abs(x)\*\*ord)\*\*(1./ord) |
    
    The vector norm can be calculated across any number of dimensions. The corresponding dimensions of `input` are flattened into one dimension, and the norm is calculated on the flattened dimension.
    
    Frobenius norm produces the same result as `p=2` in all cases except when `dim` is a list of three or more dims, in which case Frobenius norm throws an error.
    
    Nuclear norm can only be calculated across exactly two dimensions.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints__,_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _of_ _ints__,_ _optional_) – Specifies which dimension or dimensions of `input` to calculate the norm across. If `dim` is `None`, the norm will be calculated across all dimensions of `input`. If the norm type indicated by `p` does not support the specified number of dimensions, an error will occur.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensors have `dim` retained or not. Ignored if `dim` = `None` and `out` = `None`. Default: `False`
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor. Ignored if `dim` = `None` and `out` = `None`.
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. If specified, the input tensor is casted to `dtype` while performing the operation. Default: None.
    

Note

Even though `p='fro'` supports any number of dimensions, the true mathematical definition of Frobenius norm only applies to tensors with exactly two dimensions. [`torch.linalg.matrix_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_norm.html#torch.linalg.matrix_norm "torch.linalg.matrix_norm")
 with `ord='fro'` aligns with the mathematical definition, since it can only be applied across exactly two dimensions.

Example:

\>>> import torch
\>>> a \= torch.arange(9, dtype\= torch.float) \- 4
\>>> b \= a.reshape((3, 3))
\>>> torch.norm(a)
tensor(7.7460)
\>>> torch.norm(b)
tensor(7.7460)
\>>> torch.norm(a, float('inf'))
tensor(4.)
\>>> torch.norm(b, float('inf'))
tensor(4.)
\>>> c \= torch.tensor(\[\[ 1, 2, 3\], \[\-1, 1, 4\]\] , dtype\=torch.float)
\>>> torch.norm(c, dim\=0)
tensor(\[1.4142, 2.2361, 5.0000\])
\>>> torch.norm(c, dim\=1)
tensor(\[3.7417, 4.2426\])
\>>> torch.norm(c, p\=1, dim\=1)
tensor(\[6., 6.\])
\>>> d \= torch.arange(8, dtype\=torch.float).reshape(2, 2, 2)
\>>> torch.norm(d, dim\=(1, 2))
tensor(\[ 3.7417, 11.2250\])
\>>> torch.norm(d\[0, :, :\]), torch.norm(d\[1, :, :\])
(tensor(3.7417), tensor(11.2250))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.norm.rst.txt)

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