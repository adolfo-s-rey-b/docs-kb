Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.linalg.pinv.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.pinv.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.linalg.pinv.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.linalg.pinv.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.linalg.pinv.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.linalg.pinv.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.linalg.pinv.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.linalg.pinv.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.linalg.pinv.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.linalg.pinv.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.linalg.pinv.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.linalg.pinv.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.linalg.pinv.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.linalg.pinv.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.linalg.pinv.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.linalg.pinv.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.linalg.pinv.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.linalg.pinv.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.linalg.pinv.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.linalg.pinv.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.linalg.pinv.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.linalg.pinv.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.linalg.pinv.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.linalg.pinv.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.linalg.pinv.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.linalg.pinv.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.linalg.pinv.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.linalg.pinv.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.linalg.pinv.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.linalg.pinv.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.linalg.pinv.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.linalg.pinv.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.linalg.pinv.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.linalg.pinv.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.linalg.pinv.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.linalg.pinv.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.linalg.pinv.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.linalg.pinv.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.linalg.pinv.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.linalg.pinv.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.linalg.pinv.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.linalg.pinv.html)

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

torch.linalg.pinv[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html#torch-linalg-pinv "Link to this heading")

===================================================================================================================================

torch.linalg.pinv(_A_, _\*_, _atol\=None_, _rtol\=None_, _hermitian\=False_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/linalg/__init__.py#L2056)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html#torch.linalg.pinv "Link to this definition")

Computes the pseudoinverse (Moore-Penrose inverse) of a matrix.

The pseudoinverse may be [defined algebraically](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse#Existence_and_uniqueness)
 but it is more computationally convenient to understand it [through the SVD](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse#Singular_value_decomposition_(SVD))

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches of matrices, and if `A` is a batch of matrices then the output has the same batch dimensions.

If `hermitian`\= True, `A` is assumed to be Hermitian if complex or symmetric if real, but this is not checked internally. Instead, just the lower triangular part of the matrix is used in the computations.

The singular values (or the norm of the eigenvalues when `hermitian`\= True) that are below max⁡(atol,σ1⋅rtol)\\max(\\text{atol}, \\sigma\_1 \\cdot \\text{rtol})max(atol,σ1​⋅rtol) threshold are treated as zero and discarded in the computation, where σ1\\sigma\_1σ1​ is the largest singular value (or eigenvalue).

If `rtol` is not specified and `A` is a matrix of dimensions (m, n), the relative tolerance is set to be rtol\=max⁡(m,n)ε\\text{rtol} = \\max(m, n) \\varepsilonrtol\=max(m,n)ε and ε\\varepsilonε is the epsilon value for the dtype of `A` (see [`finfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "torch.torch.finfo")
). If `rtol` is not specified and `atol` is specified to be larger than zero then `rtol` is set to zero.

If `atol` or `rtol` is a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, its shape must be broadcastable to that of the singular values of `A` as returned by [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
.

Note

This function uses [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 if `hermitian`\= False and [`torch.linalg.eigh()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigh.html#torch.linalg.eigh "torch.linalg.eigh")
 if `hermitian`\= True. For CUDA inputs, this function synchronizes that device with the CPU.

Note

Consider using [`torch.linalg.lstsq()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lstsq.html#torch.linalg.lstsq "torch.linalg.lstsq")
 if possible for multiplying a matrix on the left by the pseudoinverse, as:

torch.linalg.lstsq(A, B).solution \== A.pinv() @ B

Copy to clipboard

It is always preferred to use [`lstsq()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lstsq.html#torch.linalg.lstsq "torch.linalg.lstsq")
 when possible, as it is faster and more numerically stable than computing the pseudoinverse explicitly.

Note

This function has NumPy compatible variant linalg.pinv(A, rcond, hermitian=False). However, use of the positional argument `rcond` is deprecated in favor of `rtol`.

Warning

This function uses internally [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 (or [`torch.linalg.eigh()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigh.html#torch.linalg.eigh "torch.linalg.eigh")
 when `hermitian`\= True), so its derivative has the same problems as those of these functions. See the warnings in [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 and [`torch.linalg.eigh()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigh.html#torch.linalg.eigh "torch.linalg.eigh")
 for more details.

See also

[`torch.linalg.inv()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv.html#torch.linalg.inv "torch.linalg.inv")
 computes the inverse of a square matrix.

[`torch.linalg.lstsq()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lstsq.html#torch.linalg.lstsq "torch.linalg.lstsq")
 computes `A`.pinv() @ `B` with a numerically stable algorithm.

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor of shape (\*, m, n) where \* is zero or more batch dimensions.
    
*   **rcond** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – \[NumPy Compat\]. Alias for `rtol`. Default: None.
    

Keyword Arguments:

*   **atol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the absolute tolerance value. When None it’s considered to be zero. Default: None.
    
*   **rtol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the relative tolerance value. See above for the value it takes when None. Default: None.
    
*   **hermitian** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – indicates whether `A` is Hermitian if complex or symmetric if real. Default: False.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – output tensor. Ignored if None. Default: None.
    

Examples:

\>>> A \= torch.randn(3, 5)
\>>> A
tensor(\[\[ 0.5495,  0.0979, -1.4092, -0.1128,  0.4132\],\
        \[-1.1143, -0.3662,  0.3042,  1.6374, -0.9294\],\
        \[-0.3269, -0.5745, -0.0382, -0.5922, -0.6759\]\])
\>>> torch.linalg.pinv(A)
tensor(\[\[ 0.0600, -0.1933, -0.2090\],\
        \[-0.0903, -0.0817, -0.4752\],\
        \[-0.7124, -0.1631, -0.2272\],\
        \[ 0.1356,  0.3933, -0.5023\],\
        \[-0.0308, -0.1725, -0.5216\]\])

\>>> A \= torch.randn(2, 6, 3)
\>>> Apinv \= torch.linalg.pinv(A)
\>>> torch.dist(Apinv @ A, torch.eye(3))
tensor(8.5633e-07)

\>>> A \= torch.randn(3, 3, dtype\=torch.complex64)
\>>> A \= A + A.T.conj()  \# creates a Hermitian matrix
\>>> Apinv \= torch.linalg.pinv(A, hermitian\=True)
\>>> torch.dist(Apinv @ A, torch.eye(3))
tensor(1.0830e-06)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.linalg.pinv.rst.txt)

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