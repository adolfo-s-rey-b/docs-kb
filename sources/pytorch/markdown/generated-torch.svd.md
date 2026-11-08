Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.svd.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.svd.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.svd.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.svd.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.svd.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.svd.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.svd.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.svd.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.svd.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.svd.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.svd.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.svd.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.svd.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.svd.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.svd.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.svd.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.svd.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.svd.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.svd.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.svd.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.svd.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.svd.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.svd.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.svd.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.svd.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.svd.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.svd.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.svd.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.svd.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.svd.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.svd.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.svd.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.svd.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.svd.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.svd.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.svd.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.svd.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.svd.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.svd.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.svd.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.svd.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.svd.html)

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

torch.svd[#](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch-svd "Link to this heading")

===========================================================================================================

torch.svd(_input_, _some\=True_, _compute\_uv\=True_, _\*_, _out\=None_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch.svd "Link to this definition")

Computes the singular value decomposition of either a matrix or batch of matrices `input`. The singular value decomposition is represented as a namedtuple (U, S, V), such that `input` \=Udiag(S)VH\= U \\text{diag}(S) V^{\\text{H}}\=Udiag(S)VH. where VHV^{\\text{H}}VH is the transpose of V for real inputs, and the conjugate transpose of V for complex inputs. If `input` is a batch of matrices, then U, S, and V are also batched with the same batch dimensions as `input`.

If `some` is True (default), the method returns the reduced singular value decomposition. In this case, if the last two dimensions of `input` are m and n, then the returned U and V matrices will contain only min(n, m) orthonormal columns.

If `compute_uv` is False, the returned U and V will be zero-filled matrices of shape (m, m) and (n, n) respectively, and the same device as `input`. The argument `some` has no effect when `compute_uv` is False.

Supports `input` of float, double, cfloat and cdouble data types. The dtypes of U and V are the same as `input`’s. S will always be real-valued, even if `input` is complex.

Warning

[`torch.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch.svd "torch.svd")
 is deprecated in favor of [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 and will be removed in a future PyTorch release.

`U, S, V = torch.svd(A, some=some, compute_uv=True)` (default) should be replaced with

U, S, Vh \= torch.linalg.svd(A, full\_matrices\=not some)
V \= Vh.mH

Copy to clipboard

`_, S, _ = torch.svd(A, some=some, compute_uv=False)` should be replaced with

S \= torch.linalg.svdvals(A)

Copy to clipboard

Note

Differences with [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
:

*   `some` is the opposite of [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
    ’s `full_matrices`. Note that default value for both is True, so the default behavior is effectively the opposite.
    
*   [`torch.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch.svd "torch.svd")
     returns V, whereas [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
     returns Vh, that is, VHV^{\\text{H}}VH.
    
*   If `compute_uv` is False, [`torch.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch.svd "torch.svd")
     returns zero-filled tensors for U and Vh, whereas [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
     returns empty tensors.
    

Note

The singular values are returned in descending order. If `input` is a batch of matrices, then the singular values of each matrix in the batch are returned in descending order.

Note

The S tensor can only be used to compute gradients if `compute_uv` is True.

Note

When `some` is False, the gradients on U\[…, :, min(m, n):\] and V\[…, :, min(m, n):\] will be ignored in the backward pass, as those vectors can be arbitrary bases of the corresponding subspaces.

Note

The implementation of [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 on CPU uses LAPACK’s routine ?gesdd (a divide-and-conquer algorithm) instead of ?gesvd for speed. Analogously, on GPU, it uses cuSOLVER’s routines gesvdj and gesvdjBatched.

Note

The returned U will not be contiguous. The matrix (or batch of matrices) will be represented as a column-major matrix (i.e. Fortran-contiguous).

Warning

The gradients with respect to U and V will only be finite when the input does not have zero nor repeated singular values.

Warning

If the distance between any two singular values is close to zero, the gradients with respect to U and V will be numerically unstable, as they depends on 1min⁡i≠jσi2−σj2\\frac{1}{\\min\_{i \\neq j} \\sigma\_i^2 - \\sigma\_j^2}mini\=j​σi2​−σj2​1​. The same happens when the matrix has small singular values, as these gradients also depend on S^{-1}.

Warning

For complex-valued `input` the singular value decomposition is not unique, as U and V may be multiplied by an arbitrary phase factor eiϕe^{i \\phi}eiϕ on every column. The same happens when `input` has repeated singular values, where one may multiply the columns of the spanning subspace in U and V by a rotation matrix and [the resulting vectors will span the same subspace](https://docs.pytorch.org/docs/2.15/generated/(https://en.wikipedia.org/wiki/Singular_value_decomposition#Singular_values,_singular_vectors,_and_their_relation_to_the_SVD))
. Different platforms, like NumPy, or inputs on different device types, may produce different U and V tensors.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor of size (\*, m, n) where \* is zero or more batch dimensions consisting of (m, n) matrices.
    
*   **some** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls whether to compute the reduced or full decomposition, and consequently, the shape of returned U and V. Default: True.
    
*   **compute\_uv** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls whether to compute U and V. Default: True.
    

Keyword Arguments:

**out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
_,_ _optional_) – the output tuple of tensors

Example:

\>>> a \= torch.randn(5, 3)
\>>> a
tensor(\[\[ 0.2364, -0.7752,  0.6372\],\
        \[ 1.7201,  0.7394, -0.0504\],\
        \[-0.3371, -1.0584,  0.5296\],\
        \[ 0.3550, -0.4022,  1.5569\],\
        \[ 0.2445, -0.0158,  1.1414\]\])
\>>> u, s, v \= torch.svd(a)
\>>> u
tensor(\[\[ 0.4027,  0.0287,  0.5434\],\
        \[-0.1946,  0.8833,  0.3679\],\
        \[ 0.4296, -0.2890,  0.5261\],\
        \[ 0.6604,  0.2717, -0.2618\],\
        \[ 0.4234,  0.2481, -0.4733\]\])
\>>> s
tensor(\[2.3289, 2.0315, 0.7806\])
\>>> v
tensor(\[\[-0.0199,  0.8766,  0.4809\],\
        \[-0.5080,  0.4054, -0.7600\],\
        \[ 0.8611,  0.2594, -0.4373\]\])
\>>> torch.dist(a, torch.mm(torch.mm(u, torch.diag(s)), v.t()))
tensor(8.6531e-07)
\>>> a\_big \= torch.randn(7, 5, 3)
\>>> u, s, v \= torch.svd(a\_big)
\>>> torch.dist(a\_big, torch.matmul(torch.matmul(u, torch.diag\_embed(s)), v.mT))
tensor(2.6503e-06)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.svd.rst.txt)

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