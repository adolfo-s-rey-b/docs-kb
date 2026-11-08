Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.svd_lowrank.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.svd_lowrank.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.svd_lowrank.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.svd_lowrank.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.svd_lowrank.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.svd_lowrank.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.svd_lowrank.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.svd_lowrank.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.svd_lowrank.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.svd_lowrank.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.svd_lowrank.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.svd_lowrank.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.svd_lowrank.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.svd_lowrank.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.svd_lowrank.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.svd_lowrank.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.svd_lowrank.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.svd_lowrank.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.svd_lowrank.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.svd_lowrank.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.svd_lowrank.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.svd_lowrank.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.svd_lowrank.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.svd_lowrank.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.svd_lowrank.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.svd_lowrank.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.svd_lowrank.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.svd_lowrank.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.svd_lowrank.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.svd_lowrank.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.svd_lowrank.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.svd_lowrank.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.svd_lowrank.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.svd_lowrank.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.svd_lowrank.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.svd_lowrank.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.svd_lowrank.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.svd_lowrank.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.svd_lowrank.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.svd_lowrank.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.svd_lowrank.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.svd_lowrank.html)

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

torch.svd\_lowrank[#](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html#torch-svd-lowrank "Link to this heading")

====================================================================================================================================

torch.svd\_lowrank(_A_, _q\=6_, _niter\=2_, _M\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_lowrank.py#L85)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html#torch.svd_lowrank "Link to this definition")

Return the singular value decomposition `(U, S, V)` of a matrix, batches of matrices, or a sparse matrix AAA such that A≈Udiag⁡(S)VHA \\approx U \\operatorname{diag}(S) V^{\\text{H}}A≈Udiag(S)VH. In case MMM is given, then SVD is computed for the matrix A−MA - MA−M.

Note

The implementation is based on the Algorithm 5.1 from Halko et al., 2009.

Note

For an adequate approximation of a k-rank matrix AAA, where k is not known in advance but could be estimated, the number of QQQ columns, q, can be chosen according to the following criteria: in general, k<\=q<\=min(2∗k,m,n)k <= q <= min(2\*k, m, n)k<=q<=min(2∗k,m,n). For large low-rank matrices, take q\=k+5..10q = k + 5..10q\=k+5..10. If k is relatively small compared to min(m,n)min(m, n)min(m,n), choosing q\=k+0..2q = k + 0..2q\=k+0..2 may be sufficient.

Note

This is a randomized method. To obtain repeatable results, set the seed for the pseudorandom number generator

Note

In general, use the full-rank SVD implementation [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 for dense matrices due to its 10x higher performance characteristics. The low-rank SVD will be useful for huge sparse matrices that [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 cannot handle.

Args::

A (Tensor): the input tensor of size (∗,m,n)(\*, m, n)(∗,m,n)

q (int, optional): a slightly overestimated rank of A.

niter (int, optional): the number of subspace iterations to

conduct; niter must be a nonnegative integer, and defaults to 2

M (Tensor, optional): the input tensor’s mean of size

(∗,m,n)(\*, m, n)(∗,m,n), which will be broadcasted to the size of A in this function.

References::

*   Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions, arXiv:0909.4061 \[math.NA; math.PR\], 2009 (available at [arXiv](https://arxiv.org/abs/0909.4061)
    ).
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.svd_lowrank.rst.txt)

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