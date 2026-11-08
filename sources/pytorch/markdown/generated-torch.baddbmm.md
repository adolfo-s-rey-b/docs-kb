Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.baddbmm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.baddbmm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.baddbmm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.baddbmm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.baddbmm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.baddbmm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.baddbmm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.baddbmm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.baddbmm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.baddbmm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.baddbmm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.baddbmm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.baddbmm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.baddbmm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.baddbmm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.baddbmm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.baddbmm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.baddbmm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.baddbmm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.baddbmm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.baddbmm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.baddbmm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.baddbmm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.baddbmm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.baddbmm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.baddbmm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.baddbmm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.baddbmm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.baddbmm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.baddbmm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.baddbmm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.baddbmm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.baddbmm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.baddbmm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.baddbmm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.baddbmm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.baddbmm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.baddbmm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.baddbmm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.baddbmm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.baddbmm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.baddbmm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.baddbmm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.baddbmm.html)

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

torch.baddbmm[#](https://docs.pytorch.org/docs/2.15/generated/torch.baddbmm.html#torch-baddbmm "Link to this heading")

=======================================================================================================================

torch.baddbmm(_input_, _batch1_, _batch2_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.baddbmm.html#torch.baddbmm "Link to this definition")

Performs a batch matrix-matrix product of matrices in `batch1` and `batch2`. `input` is added to the final result.

`batch1` and `batch2` must be 3-D tensors each containing the same number of matrices.

If `batch1` is a (b×n×m)(b \\times n \\times m)(b×n×m) tensor, `batch2` is a (b×m×p)(b \\times m \\times p)(b×m×p) tensor, then `input` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with a (b×n×p)(b \\times n \\times p)(b×n×p) tensor and `out` will be a (b×n×p)(b \\times n \\times p)(b×n×p) tensor. Both `alpha` and `beta` mean the same as the scaling factors used in [`torch.addbmm()`](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html#torch.addbmm "torch.addbmm")
.

outi\=β inputi+α (batch1i@batch2i)\\text{out}\_i = \\beta\\ \\text{input}\_i + \\alpha\\ (\\text{batch1}\_i \\mathbin{@} \\text{batch2}\_i) outi​\=β inputi​+α (batch1i​@batch2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and `alpha` must be real numbers, otherwise they should be integers.

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to be added
    
*   **batch1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first batch of matrices to be multiplied
    
*   **batch2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second batch of matrices to be multiplied
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for batch1@batch2\\text{batch1} \\mathbin{@} \\text{batch2}batch1@batch2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> M \= torch.randn(10, 3, 5)
\>>> batch1 \= torch.randn(10, 3, 4)
\>>> batch2 \= torch.randn(10, 4, 5)
\>>> torch.baddbmm(M, batch1, batch2).size()
torch.Size(\[10, 3, 5\])

Copy to clipboard

torch.baddbmm(_input_, _batch1_, _batch2_, _out\_dtype_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to be added
    
*   **batch1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first batch of matrices to be multiplied
    
*   **batch2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second batch of matrices to be multiplied
    
*   **out\_dtype** ([_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the dtype of the output tensor. On CUDA and XPU, only `torch.float32` is supported given `torch.float16`/`torch.bfloat16` input dtypes. Other backends (including out-of-tree accelerators) may support additional input/output dtype combinations.
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for batch1@batch2\\text{batch1} \\mathbin{@} \\text{batch2}batch1@batch2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.baddbmm.rst.txt)

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