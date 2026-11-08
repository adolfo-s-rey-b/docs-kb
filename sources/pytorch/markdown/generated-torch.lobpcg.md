Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.lobpcg.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.lobpcg.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.lobpcg.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.lobpcg.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.lobpcg.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.lobpcg.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.lobpcg.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.lobpcg.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.lobpcg.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.lobpcg.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.lobpcg.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.lobpcg.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.lobpcg.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.lobpcg.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.lobpcg.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.lobpcg.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.lobpcg.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.lobpcg.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.lobpcg.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.lobpcg.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.lobpcg.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.lobpcg.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.lobpcg.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.lobpcg.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.lobpcg.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.lobpcg.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.lobpcg.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.lobpcg.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.lobpcg.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.lobpcg.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.lobpcg.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.lobpcg.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.lobpcg.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.lobpcg.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.lobpcg.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.lobpcg.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.lobpcg.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.lobpcg.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.lobpcg.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.lobpcg.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.lobpcg.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.lobpcg.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.lobpcg.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.lobpcg.html)

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

torch.lobpcg[#](https://docs.pytorch.org/docs/2.15/generated/torch.lobpcg.html#torch-lobpcg "Link to this heading")

====================================================================================================================

torch.lobpcg(_A_, _k\=None_, _B\=None_, _X\=None_, _n\=None_, _iK\=None_, _niter\=None_, _tol\=None_, _largest\=None_, _method\=None_, _tracker\=None_, _ortho\_iparams\=None_, _ortho\_fparams\=None_, _ortho\_bparams\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_lobpcg.py#L343)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.lobpcg.html#torch.lobpcg "Link to this definition")

Find the k largest (or smallest) eigenvalues and the corresponding eigenvectors of a symmetric positive definite generalized eigenvalue problem using matrix-free LOBPCG methods.

This function is a front-end to the following LOBPCG algorithms selectable via method argument:

> method=”basic” - the LOBPCG method introduced by Andrew Knyazev, see \[Knyazev2001\]. A less robust method, may fail when Cholesky is applied to singular input.
> 
> method=”ortho” - the LOBPCG method with orthogonal basis selection \[StathopoulosEtal2002\]. A robust method.

Supported inputs are dense, sparse, and batches of dense matrices.

Note

In general, the basic method spends least time per iteration. However, the robust methods converge much faster and are more stable. So, the usage of the basic method is generally not recommended but there exist cases where the usage of the basic method may be preferred.

Warning

The backward method does not support sparse and complex inputs. It works only when B is not provided (i.e. B == None). We are actively working on extensions, and the details of the algorithms are going to be published promptly.

Warning

While it is assumed that A is symmetric, A.grad is not. To make sure that A.grad is symmetric, so that A - t \* A.grad is symmetric in first-order optimization routines, prior to running lobpcg we do the following symmetrization map: A -> (A + A.t()) / 2. The map is performed only when the A requires gradients.

Warning

LOBPCG algorithm is not applicable when the number of A’s rows is smaller than 3x the number of requested eigenpairs n.

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor of size (∗,m,m)(\*, m, m)(∗,m,m)
    
*   **k** (_integer__,_ _optional_) – the number of requested eigenpairs. Default is the number of XXX columns (when specified) or 1.
    
*   **B** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the input tensor of size (∗,m,m)(\*, m, m)(∗,m,m). When not specified, B is interpreted as identity matrix.
    
*   **X** (_tensor__,_ _optional_) – the input tensor of size (∗,m,n)(\*, m, n)(∗,m,n) where k <= n <= m. When specified, it is used as initial approximation of eigenvectors. X must be a dense tensor.
    
*   **n** (_integer__,_ _optional_) – if XXX is not specified then n specifies the size of the generated random approximation of eigenvectors. Default value for n is k. If XXX is specified, any provided value of n is ignored and n is automatically set to the number of columns in XXX.
    
*   **iK** (_tensor__,_ _optional_) – the input tensor of size (∗,m,m)(\*, m, m)(∗,m,m). When specified, it will be used as preconditioner.
    
*   **niter** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – maximum number of iterations. When reached, the iteration process is hard-stopped and the current approximation of eigenpairs is returned. For infinite iteration but until convergence criteria is met, use \-1.
    
*   **tol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – residual tolerance for stopping criterion. Default is feps \*\* 0.5 where feps is smallest non-zero floating-point number of the given input tensor A data type.
    
*   **largest** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – when True, solve the eigenproblem for the largest eigenvalues. Otherwise, solve the eigenproblem for smallest eigenvalues. Default is True.
    
*   **method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – select LOBPCG method. See the description of the function above. Default is “ortho”.
    
*   **tracker** (_callable__,_ _optional_) –
    
    a function for tracing the iteration process. When specified, it is called at each iteration step with LOBPCG instance as an argument. The LOBPCG instance holds the full state of the iteration process in the following attributes:
    
    > iparams, fparams, bparams - dictionaries of integer, float, and boolean valued input parameters, respectively
    > 
    > ivars, fvars, bvars, tvars - dictionaries of integer, float, boolean, and Tensor valued iteration variables, respectively.
    > 
    > A, B, iK - input Tensor arguments.
    > 
    > E, X, S, R - iteration Tensor variables.
    
    For instance:
    
    > ivars\[“istep”\] - the current iteration step X - the current approximation of eigenvectors E - the current approximation of eigenvalues R - the current residual ivars\[“converged\_count”\] - the current number of converged eigenpairs tvars\[“rerr”\] - the current state of convergence criteria
    
    Note that when tracker stores Tensor objects from the LOBPCG instance, it must make copies of these.
    
    If tracker sets bvars\[“force\_stop”\] = True, the iteration process will be hard-stopped.
    
*   **ortho\_iparams** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – various parameters to LOBPCG algorithm when using method=”ortho”.
    
*   **ortho\_fparams** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – various parameters to LOBPCG algorithm when using method=”ortho”.
    
*   **ortho\_bparams** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – various parameters to LOBPCG algorithm when using method=”ortho”.
    

Returns:

tensor of eigenvalues of size (∗,k)(\*, k)(∗,k)

X (Tensor): tensor of eigenvectors of size (∗,m,k)(\*, m, k)(∗,m,k)

Return type:

E ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

References

\[Knyazev2001\] Andrew V. Knyazev. (2001) Toward the Optimal Preconditioned Eigensolver: Locally Optimal Block Preconditioned Conjugate Gradient Method. SIAM J. Sci. Comput., 23(2), 517-541. (25 pages) [https://epubs.siam.org/doi/abs/10.1137/S1064827500366124](https://epubs.siam.org/doi/abs/10.1137/S1064827500366124)

\[StathopoulosEtal2002\] Andreas Stathopoulos and Kesheng Wu. (2002) A Block Orthogonalization Procedure with Constant Synchronization Requirements. SIAM J. Sci. Comput., 23(6), 2165-2182. (18 pages) [https://epubs.siam.org/doi/10.1137/S1064827500370883](https://epubs.siam.org/doi/10.1137/S1064827500370883)

\[DuerschEtal2018\] Jed A. Duersch, Meiyue Shao, Chao Yang, Ming Gu. (2018) A Robust and Efficient Implementation of LOBPCG. SIAM J. Sci. Comput., 40(5), C655-C676. (22 pages) [https://arxiv.org/abs/1704.07458](https://arxiv.org/abs/1704.07458)

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.lobpcg.rst.txt)

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