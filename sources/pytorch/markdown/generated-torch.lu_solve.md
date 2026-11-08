Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.lu_solve.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.lu_solve.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.lu_solve.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.lu_solve.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.lu_solve.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.lu_solve.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.lu_solve.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.lu_solve.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.lu_solve.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.lu_solve.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.lu_solve.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.lu_solve.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.lu_solve.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.lu_solve.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.lu_solve.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.lu_solve.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.lu_solve.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.lu_solve.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.lu_solve.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.lu_solve.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.lu_solve.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.lu_solve.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.lu_solve.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.lu_solve.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.lu_solve.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.lu_solve.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.lu_solve.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.lu_solve.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.lu_solve.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.lu_solve.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.lu_solve.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.lu_solve.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.lu_solve.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.lu_solve.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.lu_solve.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.lu_solve.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.lu_solve.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.lu_solve.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.lu_solve.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.lu_solve.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.lu_solve.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.lu_solve.html)

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

torch.lu\_solve[#](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#torch-lu-solve "Link to this heading")

===========================================================================================================================

torch.lu\_solve(_b_, _LU\_data_, _LU\_pivots_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#torch.lu_solve "Link to this definition")

Returns the LU solve of the linear system Ax\=bAx = bAx\=b using the partially pivoted LU factorization of A from [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")
.

This function supports `float`, `double`, `cfloat` and `cdouble` dtypes for `input`.

Warning

[`torch.lu_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#torch.lu_solve "torch.lu_solve")
 is deprecated in favor of [`torch.linalg.lu_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_solve.html#torch.linalg.lu_solve "torch.linalg.lu_solve")
. [`torch.lu_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#torch.lu_solve "torch.lu_solve")
 will be removed in a future PyTorch release. `X = torch.lu_solve(B, LU, pivots)` should be replaced with

X \= linalg.lu\_solve(LU, pivots, B)

Copy to clipboard

Parameters:

*   **b** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the RHS tensor of size (∗,m,k)(\*, m, k)(∗,m,k), where ∗\*∗ is zero or more batch dimensions.
    
*   **LU\_data** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the pivoted LU factorization of A from [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")
     of size (∗,m,m)(\*, m, m)(∗,m,m), where ∗\*∗ is zero or more batch dimensions.
    
*   **LU\_pivots** (_IntTensor_) – the pivots of the LU factorization from [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")
     of size (∗,m)(\*, m)(∗,m), where ∗\*∗ is zero or more batch dimensions. The batch dimensions of `LU_pivots` must be equal to the batch dimensions of `LU_data`.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> A \= torch.randn(2, 3, 3)
\>>> b \= torch.randn(2, 3, 1)
\>>> LU, pivots \= torch.linalg.lu\_factor(A)
\>>> x \= torch.lu\_solve(b, LU, pivots)
\>>> torch.dist(A @ x, b)
tensor(1.00000e-07 \*
       2.8312)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.lu_solve.rst.txt)

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