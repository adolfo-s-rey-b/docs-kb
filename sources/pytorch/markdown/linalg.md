Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/linalg.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/linalg.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/linalg.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/linalg.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/linalg.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/linalg.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/linalg.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/linalg.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/linalg.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/linalg.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/linalg.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/linalg.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/linalg.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/linalg.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/linalg.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/linalg.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/linalg.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/linalg.html)
[v1.13](https://docs.pytorch.org/docs/1.13/linalg.html)
[v1.12](https://docs.pytorch.org/docs/1.12/linalg.html)
[v1.11](https://docs.pytorch.org/docs/1.11/linalg.html)
[v1.10](https://docs.pytorch.org/docs/1.10/linalg.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/linalg.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/linalg.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/linalg.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/linalg.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/linalg.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/linalg.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/linalg.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/linalg.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/linalg.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/linalg.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/linalg.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/linalg.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/linalg.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/linalg.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/linalg.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/linalg.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/linalg.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/linalg.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/linalg.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/linalg.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/linalg.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/linalg.html)

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

torch.linalg[#](https://docs.pytorch.org/docs/2.15/linalg.html#torch-linalg "Link to this heading")

====================================================================================================

Created On: Aug 07, 2020 | Last Updated On: Jun 27, 2026

Common linear algebra operations.

See [Linear algebra (torch.linalg)](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#linear-algebra-stability)
 for some common numerical edge-cases.

Matrix Properties[#](https://docs.pytorch.org/docs/2.15/linalg.html#matrix-properties "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`norm`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch.linalg.norm "torch.linalg.norm") | Computes a vector or matrix norm. |
| [`vector_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.vector_norm.html#torch.linalg.vector_norm "torch.linalg.vector_norm") | Computes a vector norm. |
| [`matrix_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_norm.html#torch.linalg.matrix_norm "torch.linalg.matrix_norm") | Computes a matrix norm. |
| [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.diagonal.html#torch.linalg.diagonal "torch.linalg.diagonal") | Alias for [`torch.diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")<br> with defaults `dim1`\= -2, `dim2`\= -1. |
| [`det`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.det.html#torch.linalg.det "torch.linalg.det") | Computes the determinant of a square matrix. |
| [`slogdet`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.slogdet.html#torch.linalg.slogdet "torch.linalg.slogdet") | Computes the sign and natural logarithm of the absolute value of the determinant of a square matrix. |
| [`cond`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cond.html#torch.linalg.cond "torch.linalg.cond") | Computes the condition number of a matrix with respect to a matrix norm. |
| [`matrix_rank`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_rank.html#torch.linalg.matrix_rank "torch.linalg.matrix_rank") | Computes the numerical rank of a matrix. |

Decompositions[#](https://docs.pytorch.org/docs/2.15/linalg.html#decompositions "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cholesky`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cholesky.html#torch.linalg.cholesky "torch.linalg.cholesky") | Computes the Cholesky decomposition of a complex Hermitian or real symmetric positive-definite matrix. |
| [`qr`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.qr.html#torch.linalg.qr "torch.linalg.qr") | Computes the QR decomposition of a matrix. |
| [`polar`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.polar.html#torch.linalg.polar "torch.linalg.polar") | Computes the polar decomposition of a matrix. |
| [`lu`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu.html#torch.linalg.lu "torch.linalg.lu") | Computes the LU decomposition with partial pivoting of a matrix. |
| [`lu_factor`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor") | Computes a compact representation of the LU factorization with partial pivoting of a matrix. |
| [`eig`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eig.html#torch.linalg.eig "torch.linalg.eig") | Computes the eigenvalue decomposition of a square matrix if it exists. |
| [`eigvals`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigvals.html#torch.linalg.eigvals "torch.linalg.eigvals") | Computes the eigenvalues of a square matrix. |
| [`eigh`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigh.html#torch.linalg.eigh "torch.linalg.eigh") | Computes the eigenvalue decomposition of a complex Hermitian or real symmetric matrix. |
| [`eigvalsh`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.eigvalsh.html#torch.linalg.eigvalsh "torch.linalg.eigvalsh") | Computes the eigenvalues of a complex Hermitian or real symmetric matrix. |
| [`svd`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd") | Computes the singular value decomposition (SVD) of a matrix. |
| [`svdvals`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svdvals.html#torch.linalg.svdvals "torch.linalg.svdvals") | Computes the singular values of a matrix. |

Solvers[#](https://docs.pytorch.org/docs/2.15/linalg.html#solvers "Link to this heading")

------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`solve`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve.html#torch.linalg.solve "torch.linalg.solve") | Computes the solution of a square system of linear equations with a unique solution. |
| [`solve_triangular`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve_triangular.html#torch.linalg.solve_triangular "torch.linalg.solve_triangular") | Computes the solution of a triangular system of linear equations with a unique solution. |
| [`lu_solve`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_solve.html#torch.linalg.lu_solve "torch.linalg.lu_solve") | Computes the solution of a square system of linear equations with a unique solution given an LU decomposition. |
| [`lstsq`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lstsq.html#torch.linalg.lstsq "torch.linalg.lstsq") | Computes a solution to the least squares problem of a system of linear equations. |

Inverses[#](https://docs.pytorch.org/docs/2.15/linalg.html#inverses "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`inv`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv.html#torch.linalg.inv "torch.linalg.inv") | Computes the inverse of a square matrix if it exists. |
| [`pinv`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html#torch.linalg.pinv "torch.linalg.pinv") | Computes the pseudoinverse (Moore-Penrose inverse) of a matrix. |

Matrix Functions[#](https://docs.pytorch.org/docs/2.15/linalg.html#matrix-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`matrix_exp`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_exp.html#torch.linalg.matrix_exp "torch.linalg.matrix_exp") | Computes the matrix exponential of a square matrix. |
| [`matrix_sqrth`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_sqrth.html#torch.linalg.matrix_sqrth "torch.linalg.matrix_sqrth") | Computes the principal square root of a symmetric (resp. |
| [`matrix_power`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_power.html#torch.linalg.matrix_power "torch.linalg.matrix_power") | Computes the n\-th power of a square matrix for an integer n. |

Matrix Products[#](https://docs.pytorch.org/docs/2.15/linalg.html#matrix-products "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cross`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cross.html#torch.linalg.cross "torch.linalg.cross") | Computes the cross product of two 3-dimensional vectors. |
| [`matmul`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matmul.html#torch.linalg.matmul "torch.linalg.matmul") | Alias for [`torch.matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul") |
| [`vecdot`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.vecdot.html#torch.linalg.vecdot "torch.linalg.vecdot") | Computes the dot product of two batches of vectors along a dimension. |
| [`multi_dot`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.multi_dot.html#torch.linalg.multi_dot "torch.linalg.multi_dot") | Efficiently multiplies two or more matrices by reordering the multiplications so that the fewest arithmetic operations are performed. |
| [`householder_product`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.householder_product.html#torch.linalg.householder_product "torch.linalg.householder_product") | Computes the first n columns of a product of Householder matrices. |

Tensor Operations[#](https://docs.pytorch.org/docs/2.15/linalg.html#tensor-operations "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`tensorinv`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.tensorinv.html#torch.linalg.tensorinv "torch.linalg.tensorinv") | Computes the multiplicative inverse of [`torch.tensordot()`](https://docs.pytorch.org/docs/2.15/generated/torch.tensordot.html#torch.tensordot "torch.tensordot")<br>. |
| [`tensorsolve`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.tensorsolve.html#torch.linalg.tensorsolve "torch.linalg.tensorsolve") | Computes the solution X to the system torch.tensordot(A, X) = B. |

Misc[#](https://docs.pytorch.org/docs/2.15/linalg.html#misc "Link to this heading")

------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`vander`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.vander.html#torch.linalg.vander "torch.linalg.vander") | Generates a Vandermonde matrix. |

Experimental Functions[#](https://docs.pytorch.org/docs/2.15/linalg.html#experimental-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cholesky_ex`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cholesky_ex.html#torch.linalg.cholesky_ex "torch.linalg.cholesky_ex") | Computes the Cholesky decomposition of a complex Hermitian or real symmetric positive-definite matrix. |
| [`inv_ex`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv_ex.html#torch.linalg.inv_ex "torch.linalg.inv_ex") | Computes the inverse of a square matrix if it is invertible. |
| [`solve_ex`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve_ex.html#torch.linalg.solve_ex "torch.linalg.solve_ex") | A version of [`solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve.html#torch.linalg.solve "torch.linalg.solve")<br> that does not perform error checks unless `check_errors`\= True. |
| [`lu_factor_ex`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor_ex.html#torch.linalg.lu_factor_ex "torch.linalg.lu_factor_ex") | This is a version of [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")<br> that does not perform error checks unless `check_errors`\= True. |
| [`ldl_factor`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.ldl_factor.html#torch.linalg.ldl_factor "torch.linalg.ldl_factor") | Computes a compact representation of the LDL factorization of a Hermitian or symmetric (possibly indefinite) matrix. |
| [`ldl_factor_ex`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.ldl_factor_ex.html#torch.linalg.ldl_factor_ex "torch.linalg.ldl_factor_ex") | This is a version of [`ldl_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.ldl_factor.html#torch.linalg.ldl_factor "torch.linalg.ldl_factor")<br> that does not perform error checks unless `check_errors`\= True. |
| [`ldl_solve`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.ldl_solve.html#torch.linalg.ldl_solve "torch.linalg.ldl_solve") | Computes the solution of a system of linear equations using the LDL factorization. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/linalg.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/linalg.md.txt)

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