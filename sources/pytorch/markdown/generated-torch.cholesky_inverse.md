Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cholesky_inverse.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cholesky_inverse.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cholesky_inverse.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cholesky_inverse.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cholesky_inverse.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cholesky_inverse.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cholesky_inverse.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cholesky_inverse.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cholesky_inverse.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cholesky_inverse.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cholesky_inverse.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cholesky_inverse.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cholesky_inverse.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cholesky_inverse.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cholesky_inverse.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cholesky_inverse.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cholesky_inverse.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cholesky_inverse.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cholesky_inverse.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cholesky_inverse.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cholesky_inverse.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cholesky_inverse.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cholesky_inverse.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cholesky_inverse.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cholesky_inverse.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cholesky_inverse.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cholesky_inverse.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cholesky_inverse.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cholesky_inverse.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cholesky_inverse.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cholesky_inverse.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cholesky_inverse.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cholesky_inverse.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cholesky_inverse.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cholesky_inverse.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cholesky_inverse.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cholesky_inverse.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cholesky_inverse.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cholesky_inverse.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cholesky_inverse.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cholesky_inverse.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cholesky_inverse.html)

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

torch.cholesky\_inverse[#](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html#torch-cholesky-inverse "Link to this heading")

===================================================================================================================================================

torch.cholesky\_inverse(_L_, _upper\=False_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html#torch.cholesky_inverse "Link to this definition")

Computes the inverse of a complex Hermitian or real symmetric positive-definite matrix given its Cholesky decomposition.

Let AAA be a complex Hermitian or real symmetric positive-definite matrix, and LLL its Cholesky decomposition such that:

A\=LLHA = LL^{\\text{H}}A\=LLH

where LHL^{\\text{H}}LH is the conjugate transpose when LLL is complex, and the transpose when LLL is real-valued.

Computes the inverse matrix A−1A^{-1}A−1.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches of matrices, and if AAA is a batch of matrices then the output has the same batch dimensions.

Parameters:

*   **L** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor of shape (\*, n, n) where \* is zero or more batch dimensions consisting of lower or upper triangular Cholesky decompositions of symmetric or Hermitian positive-definite matrices.
    
*   **upper** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – flag that indicates whether LLL is lower triangular or upper triangular. Default: `False`
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – output tensor. Ignored if None. Default: None.

Example:

\>>> A \= torch.randn(3, 3)
\>>> A \= A @ A.T + torch.eye(3) \* 1e-3 \# Creates a symmetric positive-definite matrix
\>>> L \= torch.linalg.cholesky(A) \# Extract Cholesky decomposition
\>>> torch.cholesky\_inverse(L)
tensor(\[\[ 1.9314,  1.2251, -0.0889\],\
        \[ 1.2251,  2.4439,  0.2122\],\
        \[-0.0889,  0.2122,  0.1412\]\])
\>>> A.inverse()
tensor(\[\[ 1.9314,  1.2251, -0.0889\],\
        \[ 1.2251,  2.4439,  0.2122\],\
        \[-0.0889,  0.2122,  0.1412\]\])

\>>> A \= torch.randn(3, 2, 2, dtype\=torch.complex64)
\>>> A \= A @ A.mH + torch.eye(2) \* 1e-3 \# Batch of Hermitian positive-definite matrices
\>>> L \= torch.linalg.cholesky(A)
\>>> torch.dist(torch.inverse(A), torch.cholesky\_inverse(L))
tensor(5.6358e-7)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cholesky_inverse.rst.txt)

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