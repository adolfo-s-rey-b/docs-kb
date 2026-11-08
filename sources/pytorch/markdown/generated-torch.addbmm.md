Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.addbmm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.addbmm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.addbmm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.addbmm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.addbmm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.addbmm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.addbmm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.addbmm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.addbmm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.addbmm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.addbmm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.addbmm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.addbmm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.addbmm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.addbmm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.addbmm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.addbmm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.addbmm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.addbmm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.addbmm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.addbmm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.addbmm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.addbmm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.addbmm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.addbmm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.addbmm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.addbmm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.addbmm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.addbmm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.addbmm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.addbmm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.addbmm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.addbmm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.addbmm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.addbmm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.addbmm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.addbmm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.addbmm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.addbmm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.addbmm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.addbmm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.addbmm.html)

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

torch.addbmm[#](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html#torch-addbmm "Link to this heading")

====================================================================================================================

torch.addbmm(_input_, _batch1_, _batch2_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html#torch.addbmm "Link to this definition")

Performs a batch matrix-matrix product of matrices stored in `batch1` and `batch2`, with a reduced add step (all matrix multiplications get accumulated along the first dimension). `input` is added to the final result.

`batch1` and `batch2` must be 3-D tensors each containing the same number of matrices.

If `batch1` is a (b×n×m)(b \\times n \\times m)(b×n×m) tensor, `batch2` is a (b×m×p)(b \\times m \\times p)(b×m×p) tensor, `input` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with a (n×p)(n \\times p)(n×p) tensor and `out` will be a (n×p)(n \\times p)(n×p) tensor.

out\=β input+α (∑i\=0b−1batch1i@batch2i)out = \\beta\\ \\text{input} + \\alpha\\ (\\sum\_{i=0}^{b-1} \\text{batch1}\_i \\mathbin{@} \\text{batch2}\_i) out\=β input+α (i\=0∑b−1​batch1i​@batch2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and `alpha` must be real numbers, otherwise they should be integers.

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – matrix to be added
    
*   **batch1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first batch of matrices to be multiplied
    
*   **batch2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second batch of matrices to be multiplied
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for batch1 @ batch2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> M \= torch.randn(3, 5)
\>>> batch1 \= torch.randn(10, 3, 4)
\>>> batch2 \= torch.randn(10, 4, 5)
\>>> torch.addbmm(M, batch1, batch2)
tensor(\[\[  6.6311,   0.0503,   6.9768, -12.0362,  -2.1653\],\
        \[ -4.8185,  -1.4255,  -6.6760,   8.9453,   2.5743\],\
        \[ -3.8202,   4.3691,   1.0943,  -1.1109,   5.4730\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.addbmm.rst.txt)

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