Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cond.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.linalg.cond.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cond.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.cond.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.linalg.cond.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.linalg.cond.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.linalg.cond.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.linalg.cond.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.linalg.cond.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.linalg.cond.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.linalg.cond.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.linalg.cond.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.linalg.cond.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.linalg.cond.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.linalg.cond.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.linalg.cond.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.linalg.cond.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.linalg.cond.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.linalg.cond.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.linalg.cond.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.linalg.cond.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.linalg.cond.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.linalg.cond.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.linalg.cond.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.linalg.cond.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.linalg.cond.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.linalg.cond.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.linalg.cond.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.linalg.cond.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.linalg.cond.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.linalg.cond.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.linalg.cond.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.linalg.cond.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.linalg.cond.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.linalg.cond.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.linalg.cond.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.linalg.cond.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.linalg.cond.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.linalg.cond.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.linalg.cond.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.linalg.cond.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.linalg.cond.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.linalg.cond.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.linalg.cond.html)

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

torch.linalg.cond[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cond.html#torch-linalg-cond "Link to this heading")

===================================================================================================================================

torch.linalg.cond(_A_, _p\=None_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/linalg/__init__.py#L1938)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cond.html#torch.linalg.cond "Link to this definition")

Computes the condition number of a matrix with respect to a matrix norm.

Letting K\\mathbb{K}K be R\\mathbb{R}R or C\\mathbb{C}C, the **condition number** κ\\kappaκ of a matrix A∈Kn×nA \\in \\mathbb{K}^{n \\times n}A∈Kn×n is defined as

κ(A)\=∥A∥p∥A−1∥p\\kappa(A) = \\|A\\|\_p\\|A^{-1}\\|\_pκ(A)\=∥A∥p​∥A−1∥p​

The condition number of `A` measures the numerical stability of the linear system AX = B with respect to a matrix norm.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches of matrices, and if `A` is a batch of matrices then the output has the same batch dimensions.

`p` defines the matrix norm that is computed. The following norms are supported:

| `p` | matrix norm |
| --- | --- |
| None | 2\-norm (largest singular value) |
| ‘fro’ | Frobenius norm |
| ‘nuc’ | nuclear norm |
| inf | max(sum(abs(x), dim=1)) |
| \-inf | min(sum(abs(x), dim=1)) |
| 1   | max(sum(abs(x), dim=0)) |
| \-1 | min(sum(abs(x), dim=0)) |
| 2   | largest singular value |
| \-2 | smallest singular value |

where inf refers to float(‘inf’), NumPy’s inf object, or any equivalent object.

For `p` is one of (‘fro’, ‘nuc’, inf, -inf, 1, -1), this function uses [`torch.linalg.norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.norm.html#torch.linalg.norm "torch.linalg.norm")
 and [`torch.linalg.inv()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv.html#torch.linalg.inv "torch.linalg.inv")
. As such, in this case, the matrix (or every matrix in the batch) `A` has to be square and invertible.

For `p` in (2, -2), this function can be computed in terms of the singular values σ1≥…≥σn\\sigma\_1 \\geq \\ldots \\geq \\sigma\_nσ1​≥…≥σn​

κ2(A)\=σ1σnκ−2(A)\=σnσ1\\kappa\_2(A) = \\frac{\\sigma\_1}{\\sigma\_n}\\qquad \\kappa\_{-2}(A) = \\frac{\\sigma\_n}{\\sigma\_1}κ2​(A)\=σn​σ1​​κ−2​(A)\=σ1​σn​​

In these cases, it is computed using [`torch.linalg.svdvals()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svdvals.html#torch.linalg.svdvals "torch.linalg.svdvals")
. For these norms, the matrix (or every matrix in the batch) `A` may have any shape.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU if `p` is one of (‘fro’, ‘nuc’, inf, -inf, 1, -1).

See also

[`torch.linalg.solve()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.solve.html#torch.linalg.solve "torch.linalg.solve")
 for a function that solves linear systems of square matrices.

[`torch.linalg.lstsq()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lstsq.html#torch.linalg.lstsq "torch.linalg.lstsq")
 for a function that solves linear systems of general matrices.

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor of shape (\*, m, n) where \* is zero or more batch dimensions for `p` in (2, -2), and of shape (\*, n, n) where every matrix is invertible for `p` in (‘fro’, ‘nuc’, inf, -inf, 1, -1).
    
*   **p** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _inf__,_ _\-inf__,_ _'fro'__,_ _'nuc'__,_ _optional_) – the type of the matrix norm to use in the computations (see above). Default: None
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – output tensor. Ignored if None. Default: None.

Returns:

A real-valued tensor, even when `A` is complex.

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – if `p` is one of (‘fro’, ‘nuc’, inf, -inf, 1, -1) and the `A` matrix or any matrix in the batch `A` is not square or invertible.

Examples:

\>>> A \= torch.randn(3, 4, 4, dtype\=torch.complex64)
\>>> torch.linalg.cond(A)
\>>> A \= torch.tensor(\[\[1., 0, \-1\], \[0, 1, 0\], \[1, 0, 1\]\])
\>>> torch.linalg.cond(A)
tensor(\[1.4142\])
\>>> torch.linalg.cond(A, 'fro')
tensor(3.1623)
\>>> torch.linalg.cond(A, 'nuc')
tensor(9.2426)
\>>> torch.linalg.cond(A, float('inf'))
tensor(2.)
\>>> torch.linalg.cond(A, float('-inf'))
tensor(1.)
\>>> torch.linalg.cond(A, 1)
tensor(2.)
\>>> torch.linalg.cond(A, \-1)
tensor(1.)
\>>> torch.linalg.cond(A, 2)
tensor(\[1.4142\])
\>>> torch.linalg.cond(A, \-2)
tensor(\[0.7071\])

\>>> A \= torch.randn(2, 3, 3)
\>>> torch.linalg.cond(A)
tensor(\[\[9.5917\],\
        \[3.2538\]\])
\>>> A \= torch.randn(2, 3, 3, dtype\=torch.complex64)
\>>> torch.linalg.cond(A)
tensor(\[\[4.6245\],\
        \[4.5671\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.linalg.cond.rst.txt)

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