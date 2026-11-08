Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.linalg.lu.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.lu.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.linalg.lu.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.linalg.lu.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.linalg.lu.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.linalg.lu.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.linalg.lu.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.linalg.lu.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.linalg.lu.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.linalg.lu.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.linalg.lu.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.linalg.lu.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.linalg.lu.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.linalg.lu.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.linalg.lu.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.linalg.lu.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.linalg.lu.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.linalg.lu.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.linalg.lu.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.linalg.lu.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.linalg.lu.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.linalg.lu.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.linalg.lu.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.linalg.lu.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.linalg.lu.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.linalg.lu.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.linalg.lu.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.linalg.lu.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.linalg.lu.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.linalg.lu.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.linalg.lu.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.linalg.lu.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.linalg.lu.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.linalg.lu.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.linalg.lu.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.linalg.lu.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.linalg.lu.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.linalg.lu.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.linalg.lu.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.linalg.lu.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.linalg.lu.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.linalg.lu.html)

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

torch.linalg.lu[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html#torch-linalg-lu "Link to this heading")

=============================================================================================================================

torch.linalg.lu(_A_, _\*_, _pivot\=True_, _out\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/linalg/__init__.py#L2641)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html#torch.linalg.lu "Link to this definition")

Computes the LU decomposition with partial pivoting of a matrix.

Letting K\\mathbb{K}K be R\\mathbb{R}R or C\\mathbb{C}C, the **LU decomposition with partial pivoting** of a matrix A∈Km×nA \\in \\mathbb{K}^{m \\times n}A∈Km×n is defined as

A\=PLUP∈Km×m,L∈Km×k,U∈Kk×nA = PLU\\mathrlap{\\qquad P \\in \\mathbb{K}^{m \\times m}, L \\in \\mathbb{K}^{m \\times k}, U \\in \\mathbb{K}^{k \\times n}}A\=PLUP∈Km×m,L∈Km×k,U∈Kk×n

where k = min(m,n), PPP is a [permutation matrix](https://en.wikipedia.org/wiki/Permutation_matrix)
, LLL is lower triangular with ones on the diagonal and UUU is upper triangular.

If `pivot`\= False and `A` is on GPU, then the **LU decomposition without pivoting** is computed

A\=LUL∈Km×k,U∈Kk×nA = LU\\mathrlap{\\qquad L \\in \\mathbb{K}^{m \\times k}, U \\in \\mathbb{K}^{k \\times n}}A\=LUL∈Km×k,U∈Kk×n

When `pivot`\= False, the returned matrix `P` will be empty. The LU decomposition without pivoting [may not exist](https://en.wikipedia.org/wiki/LU_decomposition#Definitions)
 if any of the principal minors of `A` is singular. In this case, the output matrix may contain inf or NaN.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches of matrices, and if `A` is a batch of matrices then the output has the same batch dimensions.

See also

[`torch.linalg.solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve.html#torch.linalg.solve "torch.linalg.solve")
 solves a system of linear equations using the LU decomposition with partial pivoting.

Warning

The LU decomposition is almost never unique, as often there are different permutation matrices that can yield different LU decompositions. As such, different platforms, like SciPy, or inputs on different devices, may produce different valid decompositions.

Warning

Gradient computations are only supported if the input matrix is full-rank. If this condition is not met, no error will be thrown, but the gradient may not be finite. This is because the LU decomposition with pivoting is not differentiable at these points.

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor of shape (\*, m, n) where \* is zero or more batch dimensions.
    
*   **pivot** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Controls whether to compute the LU decomposition with partial pivoting or no pivoting. Default: True.
    

Keyword Arguments:

**out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
_,_ _optional_) – output tuple of three tensors. Ignored if None. Default: None.

Returns:

A named tuple (P, L, U).

Examples:

\>>> A \= torch.randn(3, 2)
\>>> P, L, U \= torch.linalg.lu(A)
\>>> P
tensor(\[\[0., 1., 0.\],\
        \[0., 0., 1.\],\
        \[1., 0., 0.\]\])
\>>> L
tensor(\[\[1.0000, 0.0000\],\
        \[0.5007, 1.0000\],\
        \[0.0633, 0.9755\]\])
\>>> U
tensor(\[\[0.3771, 0.0489\],\
        \[0.0000, 0.9644\]\])
\>>> torch.dist(A, P @ L @ U)
tensor(5.9605e-08)

\>>> A \= torch.randn(2, 5, 7, device\="cuda")
\>>> P, L, U \= torch.linalg.lu(A, pivot\=False)
\>>> P
tensor(\[\], device='cuda:0')
\>>> torch.dist(A, L @ U)
tensor(1.0376e-06, device='cuda:0')

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.linalg.lu.rst.txt)

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