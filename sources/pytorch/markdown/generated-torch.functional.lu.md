Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.lu.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.lu.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.lu.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.lu.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.lu.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.lu.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.lu.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.lu.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.lu.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.lu.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.lu.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.lu.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.lu.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.lu.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.lu.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.lu.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.lu.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.lu.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.lu.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.lu.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.lu.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.lu.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.lu.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.lu.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.lu.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.lu.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.lu.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.lu.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.lu.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.lu.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.lu.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.lu.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.lu.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.lu.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.lu.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.lu.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.lu.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.lu.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.lu.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.lu.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.lu.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.lu.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.lu.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.lu.html)

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

torch.functional.lu[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.lu.html#torch-functional-lu "Link to this heading")

=========================================================================================================================================

torch.functional.lu(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_jit_internal.py#L627)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.lu.html#torch.functional.lu "Link to this definition")

Computes the LU factorization of a matrix or batches of matrices `A`. Returns a tuple containing the LU factorization and pivots of `A`. Pivoting is done if `pivot` is set to `True`.

Warning

[`torch.lu()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu.html#torch.lu "torch.lu")
 is deprecated in favor of [`torch.linalg.lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")
 and [`torch.linalg.lu_factor_ex()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor_ex.html#torch.linalg.lu_factor_ex "torch.linalg.lu_factor_ex")
. [`torch.lu()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu.html#torch.lu "torch.lu")
 will be removed in a future PyTorch release. `LU, pivots, info = torch.lu(A, compute_pivots)` should be replaced with

LU, pivots \= torch.linalg.lu\_factor(A, compute\_pivots)

Copy to clipboard

`LU, pivots, info = torch.lu(A, compute_pivots, get_infos=True)` should be replaced with

LU, pivots, info \= torch.linalg.lu\_factor\_ex(A, compute\_pivots)

Copy to clipboard

Note

*   The returned permutation matrix for every matrix in the batch is represented by a 1-indexed vector of size `min(A.shape[-2], A.shape[-1])`. `pivots[i] == j` represents that in the `i`\-th step of the algorithm, the `i`\-th row was permuted with the `j-1`\-th row.
    
*   LU factorization with `pivot` = `False` is not available for CPU, and attempting to do so will throw an error. However, LU factorization with `pivot` = `False` is available for CUDA.
    
*   This function does not check if the factorization was successful or not if `get_infos` is `True` since the status of the factorization is present in the third element of the return tuple.
    
*   In the case of batches of square matrices with size less or equal to 32 on a CUDA device, the LU factorization is repeated for singular matrices due to the bug in the MAGMA library (see magma issue 13).
    
*   `L`, `U`, and `P` can be derived using [`torch.lu_unpack()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_unpack.html#torch.lu_unpack "torch.lu_unpack")
    .
    

Warning

The gradients of this function will only be finite when `A` is full rank. This is because the LU decomposition is just differentiable at full rank matrices. Furthermore, if `A` is close to not being full rank, the gradient will be numerically unstable as it depends on the computation of L−1L^{-1}L−1 and U−1U^{-1}U−1.

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to factor of size (∗,m,n)(\*, m, n)(∗,m,n)
    
*   **pivot** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to compute the LU decomposition with partial pivoting, or the regular LU decomposition. `pivot`\= False not supported on CPU. Default: True.
    
*   **get\_infos** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if set to `True`, returns an info IntTensor. Default: `False`
    
*   **out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – optional output tuple. If `get_infos` is `True`, then the elements in the tuple are Tensor, IntTensor, and IntTensor. If `get_infos` is `False`, then the elements in the tuple are Tensor, IntTensor. Default: `None`
    

Returns:

A tuple of tensors containing

> *   **factorization** (_Tensor_): the factorization of size (∗,m,n)(\*, m, n)(∗,m,n)
>     
> *   **pivots** (_IntTensor_): the pivots of size (∗,min(m,n))(\*, \\text{min}(m, n))(∗,min(m,n)). `pivots` stores all the intermediate transpositions of rows. The final permutation `perm` could be reconstructed by applying `swap(perm[i], perm[pivots[i] - 1])` for `i = 0, ..., pivots.size(-1) - 1`, where `perm` is initially the identity permutation of mmm elements (essentially this is what [`torch.lu_unpack()`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_unpack.html#torch.lu_unpack "torch.lu_unpack")
>      is doing).
>     
> *   **infos** (_IntTensor_, _optional_): if `get_infos` is `True`, this is a tensor of size (∗)(\*)(∗) where non-zero values indicate whether factorization for the matrix or each minibatch has succeeded or failed
>     

Return type:

([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, IntTensor, IntTensor (optional))

Example:

\>>> A \= torch.randn(2, 3, 3)
\>>> A\_LU, pivots \= torch.lu(A)
\>>> A\_LU
tensor(\[\[\[ 1.3506,  2.5558, -0.0816\],\
         \[ 0.1684,  1.1551,  0.1940\],\
         \[ 0.1193,  0.6189, -0.5497\]\],\
\
        \[\[ 0.4526,  1.2526, -0.3285\],\
         \[-0.7988,  0.7175, -0.9701\],\
         \[ 0.2634, -0.9255, -0.3459\]\]\])
\>>> pivots
tensor(\[\[ 3,  3,  3\],\
        \[ 3,  3,  3\]\], dtype=torch.int32)
\>>> A\_LU, pivots, info \= torch.lu(A, get\_infos\=True)
\>>> if info.nonzero().size(0) \== 0:
...     print('LU factorization succeeded for all samples!')
LU factorization succeeded for all samples!

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.lu.rst.txt)

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