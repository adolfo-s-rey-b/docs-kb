Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.linalg.norm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.norm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.linalg.norm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.linalg.norm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.linalg.norm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.linalg.norm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.linalg.norm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.linalg.norm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.linalg.norm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.linalg.norm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.linalg.norm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.linalg.norm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.linalg.norm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.linalg.norm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.linalg.norm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.linalg.norm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.linalg.norm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.linalg.norm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.linalg.norm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.linalg.norm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.linalg.norm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.linalg.norm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.linalg.norm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.linalg.norm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.linalg.norm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.linalg.norm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.linalg.norm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.linalg.norm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.linalg.norm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.linalg.norm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.linalg.norm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.linalg.norm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.linalg.norm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.linalg.norm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.linalg.norm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.linalg.norm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.linalg.norm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.linalg.norm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.linalg.norm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.linalg.norm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.linalg.norm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.linalg.norm.html)

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

torch.linalg.norm[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch-linalg-norm "Link to this heading")

===================================================================================================================================

torch.linalg.norm(_input_, _ord\=None_, _dim\=None_, _keepdim\=False_, _\*_, _out\=None_, _dtype\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/linalg/__init__.py#L1353)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch.linalg.norm "Link to this definition")

Computes a vector or matrix norm.

Supports input of float, double, cfloat and cdouble dtypes.

Whether this function computes a vector or matrix norm is determined as follows:

*   If `dim` is an int, the vector norm will be computed.
    
*   If `dim` is a 2\-tuple, the matrix norm will be computed.
    
*   If `dim`\= None and `ord`\= None, `input` will be flattened to 1D and the 2\-norm of the resulting vector will be computed.
    
*   If `dim`\= None and `ord` != None, `input` must be 1D or 2D.
    

`ord` defines the norm that is computed. The following norms are supported:

| `ord` | norm for matrices | norm for vectors |
| --- | --- | --- |
| None (default) | Frobenius norm | 2\-norm (see below) |
| ‘fro’ | Frobenius norm | – not supported – |
| ‘nuc’ | nuclear norm | – not supported – |
| inf | max(sum(abs(x), dim=1)) | max(abs(x)) |
| \-inf | min(sum(abs(x), dim=1)) | min(abs(x)) |
| 0   | – not supported – | sum(x != 0) |
| 1   | max(sum(abs(x), dim=0)) | as below |
| \-1 | min(sum(abs(x), dim=0)) | as below |
| 2   | largest [singular value](https://en.wikipedia.org/wiki/Singular_value_decomposition#Singular_values,_singular_vectors,_and_their_relation_to_the_SVD) | as below |
| \-2 | smallest [singular value](https://en.wikipedia.org/wiki/Singular_value_decomposition#Singular_values,_singular_vectors,_and_their_relation_to_the_SVD) | as below |
| other int or float | – not supported – | sum(abs(x)^{ord})^{(1 / ord)} |

where inf refers to float(‘inf’), NumPy’s inf object, or any equivalent object.

See also

[`torch.linalg.vector_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.vector_norm.html#torch.linalg.vector_norm "torch.linalg.vector_norm")
 computes a vector norm.

[`torch.linalg.matrix_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_norm.html#torch.linalg.matrix_norm "torch.linalg.matrix_norm")
 computes a matrix norm.

The above functions are often clearer and more flexible than using [`torch.linalg.norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch.linalg.norm "torch.linalg.norm")
. For example, torch.linalg.norm(input, ord=1, dim=(0, 1)) always computes a matrix norm, but with torch.linalg.vector\_norm(input, ord=1, dim=(0, 1)) it is possible to compute a vector norm over the two dimensions.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor of shape (\*, n) or (\*, m, n) where \* is zero or more batch dimensions
    
*   **ord** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _inf__,_ _\-inf__,_ _'fro'__,_ _'nuc'__,_ _optional_) – order of norm. Default: None
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _optional_) – dimensions over which to compute the vector or matrix norm. See above for the behavior when `dim`\= None. Default: None
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set to True, the reduced dimensions are retained in the result as dimensions with size one. Default: False
    

Keyword Arguments:

*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – output tensor. Ignored if None. Default: None.
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – If specified `x` is cast to `dtype` prior to doing the accumulation. Default: None
    

Returns:

A real-valued tensor, even when `input` is complex.

Examples:

\>>> from torch import linalg as LA
\>>> a \= torch.arange(9, dtype\=torch.float) \- 4
\>>> a
tensor(\[-4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.\])
\>>> B \= a.reshape((3, 3))
\>>> B
tensor(\[\[-4., -3., -2.\],\
        \[-1.,  0.,  1.\],\
        \[ 2.,  3.,  4.\]\])

\>>> LA.norm(a)
tensor(7.7460)
\>>> LA.norm(B)
tensor(7.7460)
\>>> LA.norm(B, 'fro')
tensor(7.7460)
\>>> LA.norm(a, float('inf'))
tensor(4.)
\>>> LA.norm(B, float('inf'))
tensor(9.)
\>>> LA.norm(a, \-float('inf'))
tensor(0.)
\>>> LA.norm(B, \-float('inf'))
tensor(2.)

\>>> LA.norm(a, 1)
tensor(20.)
\>>> LA.norm(B, 1)
tensor(7.)
\>>> LA.norm(a, \-1)
tensor(0.)
\>>> LA.norm(B, \-1)
tensor(6.)
\>>> LA.norm(a, 2)
tensor(7.7460)
\>>> LA.norm(B, 2)
tensor(7.3485)

\>>> LA.norm(a, \-2)
tensor(0.)
\>>> LA.norm(B.double(), \-2)
tensor(1.8570e-16, dtype=torch.float64)
\>>> LA.norm(a, 3)
tensor(5.8480)
\>>> LA.norm(a, \-3)
tensor(0.)

Copy to clipboard

Using the `dim` argument to compute vector norms:

\>>> c \= torch.tensor(\[\[1., 2., 3.\],\
...                   \[\-1, 1, 4\]\])
\>>> LA.norm(c, dim\=0)
tensor(\[1.4142, 2.2361, 5.0000\])
\>>> LA.norm(c, dim\=1)
tensor(\[3.7417, 4.2426\])
\>>> LA.norm(c, ord\=1, dim\=1)
tensor(\[6., 6.\])

Copy to clipboard

Using the `dim` argument to compute matrix norms:

\>>> A \= torch.arange(8, dtype\=torch.float).reshape(2, 2, 2)
\>>> LA.norm(A, dim\=(1,2))
tensor(\[ 3.7417, 11.2250\])
\>>> LA.norm(A\[0, :, :\]), LA.norm(A\[1, :, :\])
(tensor(3.7417), tensor(11.2250))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.linalg.norm.rst.txt)

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