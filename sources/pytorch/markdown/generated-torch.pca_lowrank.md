Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.pca_lowrank.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.pca_lowrank.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.pca_lowrank.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.pca_lowrank.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.pca_lowrank.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.pca_lowrank.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.pca_lowrank.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.pca_lowrank.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.pca_lowrank.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.pca_lowrank.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.pca_lowrank.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.pca_lowrank.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.pca_lowrank.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.pca_lowrank.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.pca_lowrank.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.pca_lowrank.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.pca_lowrank.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.pca_lowrank.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.pca_lowrank.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.pca_lowrank.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.pca_lowrank.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.pca_lowrank.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.pca_lowrank.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.pca_lowrank.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.pca_lowrank.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.pca_lowrank.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.pca_lowrank.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.pca_lowrank.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.pca_lowrank.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.pca_lowrank.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.pca_lowrank.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.pca_lowrank.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.pca_lowrank.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.pca_lowrank.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.pca_lowrank.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.pca_lowrank.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.pca_lowrank.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.pca_lowrank.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.pca_lowrank.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.pca_lowrank.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.pca_lowrank.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.pca_lowrank.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.pca_lowrank.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.pca_lowrank.html)

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

torch.pca\_lowrank[#](https://docs.pytorch.org/docs/2.15/generated/torch.pca_lowrank.html#torch-pca-lowrank "Link to this heading")

====================================================================================================================================

torch.pca\_lowrank(_A_, _q\=None_, _center\=True_, _niter\=2_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_lowrank.py#L183)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.pca_lowrank.html#torch.pca_lowrank "Link to this definition")

Performs linear Principal Component Analysis (PCA) on a low-rank matrix, batches of such matrices, or sparse matrix.

This function returns a namedtuple `(U, S, V)` which is the nearly optimal approximation of a singular value decomposition of a centered matrix AAA such that A≈Udiag⁡(S)VHA \\approx U \\operatorname{diag}(S) V^{\\text{H}}A≈Udiag(S)VH

Note

The relation of `(U, S, V)` to PCA is as follows:

*   AAA is a data matrix with `m` samples and `n` features
    
*   the VVV columns represent the principal directions
    
*   S∗∗2/(m−1)S \*\* 2 / (m - 1)S∗∗2/(m−1) contains the eigenvalues of ATA/(m−1)A^T A / (m - 1)ATA/(m−1) which is the covariance of `A` when `center=True` is provided.
    
*   `matmul(A, V[:, :k])` projects data to the first k principal components
    

Note

Different from the standard SVD, the size of returned matrices depend on the specified rank and q values as follows:

> *   UUU is m x q matrix
>     
> *   SSS is q-vector
>     
> *   VVV is n x q matrix
>     

Note

To obtain repeatable results, reset the seed for the pseudorandom number generator

Parameters:

*   **A** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor of size (∗,m,n)(\*, m, n)(∗,m,n)
    
*   **q** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – a slightly overestimated rank of AAA. By default, `q = min(6, m, n)`.
    
*   **center** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if True, center the input tensor, otherwise, assume that the input is centered.
    
*   **niter** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the number of subspace iterations to conduct; niter must be a nonnegative integer, and defaults to 2.
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

References:

\- Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
  structure with randomness: probabilistic algorithms for
  constructing approximate matrix decompositions,
  arXiv:0909.4061 \[math.NA; math.PR\], 2009 (available at
  \`arXiv <http://arxiv.org/abs/0909.4061>\`\_).

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.pca_lowrank.rst.txt)

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