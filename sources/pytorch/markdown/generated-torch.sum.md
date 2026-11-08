Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.sum.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.sum.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.sum.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.sum.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.sum.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.sum.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.sum.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.sum.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.sum.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.sum.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.sum.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.sum.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.sum.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.sum.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.sum.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.sum.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.sum.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.sum.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.sum.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.sum.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.sum.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.sum.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.sum.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.sum.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.sum.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.sum.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.sum.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.sum.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.sum.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.sum.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.sum.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.sum.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.sum.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.sum.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.sum.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.sum.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.sum.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.sum.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.sum.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.sum.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.sum.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.sum.html)

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

torch.sum[#](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html#torch-sum "Link to this heading")

===========================================================================================================

torch.sum(_input_, _\*_, _dtype\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html#torch.sum "Link to this definition")

Returns the sum of all elements in the `input` tensor.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
, optional) – the desired data type of returned tensor. If specified, the input tensor is casted to [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 before the operation is performed. This is useful for preventing data type overflows. Default: None.

Note

Use the dtype argument if you need the result in a specific tensor type. Otherwise, the result type may be automatically promoted (e.g., from torch.int32 to torch.int64).

Example:

\>>> a \= torch.randn(1, 3)
\>>> a
tensor(\[\[ 0.1133, -0.9567,  0.2958\]\])
\>>> torch.sum(a)
tensor(-0.5475)

Copy to clipboard

torch.sum(_input_, _dim_, _keepdim\=False_, _\*_, _dtype\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Returns the sum of each row of the `input` tensor in the given dimension `dim`. If `dim` is a list of dimensions, reduce over all of them.

If `keepdim` is `True`, the output tensor is of the same size as `input` except in the dimension(s) `dim` where it is of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints__,_ _optional_) – the dimension or dimensions to reduce. If `None`, all dimensions are reduced.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
, optional) – the desired data type of returned tensor. If specified, the input tensor is casted to [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 before the operation is performed. This is useful for preventing data type overflows. Default: None.

Example:

\>>> a \= torch.randn(4, 4)
\>>> a
tensor(\[\[ 0.0569, -0.2475,  0.0737, -0.3429\],\
        \[-0.2993,  0.9138,  0.9337, -1.6864\],\
        \[ 0.1132,  0.7892, -0.1003,  0.5688\],\
        \[ 0.3637, -0.9906, -0.4752, -1.5197\]\])
\>>> torch.sum(a, 1)
tensor(\[-0.4598, -0.1381,  1.3708, -2.6217\])
\>>> b \= torch.arange(4 \* 5 \* 6).view(4, 5, 6)
\>>> torch.sum(b, (2, 1))
tensor(\[  435.,  1335.,  2235.,  3135.\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.sum.rst.txt)

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