Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.triangular_solve.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.triangular_solve.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.triangular_solve.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.triangular_solve.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.triangular_solve.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.triangular_solve.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.triangular_solve.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.triangular_solve.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.triangular_solve.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.triangular_solve.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.triangular_solve.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.triangular_solve.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.triangular_solve.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.triangular_solve.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.triangular_solve.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.triangular_solve.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.triangular_solve.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.triangular_solve.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.triangular_solve.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.triangular_solve.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.triangular_solve.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.triangular_solve.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.triangular_solve.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.triangular_solve.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.triangular_solve.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.triangular_solve.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.triangular_solve.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.triangular_solve.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.triangular_solve.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.triangular_solve.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.triangular_solve.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.triangular_solve.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.triangular_solve.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.triangular_solve.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.triangular_solve.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.triangular_solve.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.triangular_solve.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.triangular_solve.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.triangular_solve.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.triangular_solve.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.triangular_solve.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.triangular_solve.html)

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

torch.triangular\_solve[#](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html#torch-triangular-solve "Link to this heading")

===================================================================================================================================================

torch.triangular\_solve(_b_, _A_, _upper\=True_, _transpose\=False_, _unitriangular\=False_, _\*_, _out\=None_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html#torch.triangular_solve "Link to this definition")

Solves a system of equations with a square upper or lower triangular invertible matrix AAA and multiple right-hand sides bbb.

In symbols, it solves AX\=bAX = bAX\=b and assumes AAA is square upper-triangular (or lower-triangular if `upper`\= False) and does not have zeros on the diagonal.

torch.triangular\_solve(b, A) can take in 2D inputs b, A or inputs that are batches of 2D matrices. If the inputs are batches, then returns batched outputs X

If the diagonal of `A` contains zeros or elements that are very close to zero and `unitriangular`\= False (default) or if the input matrix is badly conditioned, the result may contain NaN s.

Supports input of float, double, cfloat and cdouble data types.

Warning

[`torch.triangular_solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html#torch.triangular_solve "torch.triangular_solve")
 is deprecated in favor of [`torch.linalg.solve_triangular()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve_triangular.html#torch.linalg.solve_triangular "torch.linalg.solve_triangular")
 and will be removed in a future PyTorch release. [`torch.linalg.solve_triangular()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve_triangular.html#torch.linalg.solve_triangular "torch.linalg.solve_triangular")
 has its arguments reversed and does not return a copy of one of the inputs.

`X = torch.triangular_solve(B, A).solution` should be replaced with

X \= torch.linalg.solve\_triangular(A, B)

Copy to clipboard

Parameters:

*   **b** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – multiple right-hand sides of size (∗,m,k)(\*, m, k)(∗,m,k) where ∗\*∗ is zero of more batch dimensions
    
*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input triangular coefficient matrix of size (∗,m,m)(\*, m, m)(∗,m,m) where ∗\*∗ is zero or more batch dimensions
    
*   **upper** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether AAA is upper or lower triangular. Default: `True`.
    
*   **transpose** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – solves op(A)X = b where op(A) = A^T if this flag is `True`, and op(A) = A if it is `False`. Default: `False`.
    
*   **unitriangular** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether AAA is unit triangular. If True, the diagonal elements of AAA are assumed to be 1 and not referenced from AAA. Default: `False`.
    

Keyword Arguments:

**out** (_(_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_)__,_ _optional_) – tuple of two tensors to write the output to. Ignored if None. Default: None.

Returns:

A namedtuple (solution, cloned\_coefficient) where cloned\_coefficient is a clone of AAA and solution is the solution XXX to AX\=bAX = bAX\=b (or whatever variant of the system of equations, depending on the keyword arguments.)

Examples:

\>>> A \= torch.randn(2, 2).triu()
\>>> A
tensor(\[\[ 1.1527, -1.0753\],\
        \[ 0.0000,  0.7986\]\])
\>>> b \= torch.randn(2, 3)
\>>> b
tensor(\[\[-0.0210,  2.3513, -1.5492\],\
        \[ 1.5429,  0.7403, -1.0243\]\])
\>>> torch.triangular\_solve(b, A)
torch.return\_types.triangular\_solve(
solution=tensor(\[\[ 1.7841,  2.9046, -2.5405\],\
        \[ 1.9320,  0.9270, -1.2826\]\]),
cloned\_coefficient=tensor(\[\[ 1.1527, -1.0753\],\
        \[ 0.0000,  0.7986\]\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.triangular_solve.rst.txt)

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