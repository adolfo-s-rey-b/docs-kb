Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.addmm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.addmm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.addmm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.addmm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.addmm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.addmm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.addmm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.addmm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.addmm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.addmm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.addmm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.addmm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.addmm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.addmm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.addmm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.addmm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.addmm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.addmm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.addmm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.addmm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.addmm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.addmm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.addmm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.addmm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.addmm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.addmm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.addmm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.addmm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.addmm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.addmm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.addmm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.addmm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.addmm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.addmm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.addmm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.addmm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.addmm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.addmm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.addmm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.addmm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.addmm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.addmm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.addmm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.addmm.html)

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

torch.addmm[#](https://docs.pytorch.org/docs/2.15/generated/torch.addmm.html#torch-addmm "Link to this heading")

=================================================================================================================

torch.addmm(_input_, _mat1_, _mat2_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.addmm.html#torch.addmm "Link to this definition")

Performs a matrix multiplication of the matrices `mat1` and `mat2`. The matrix `input` is added to the final result.

If `mat1` is a (n×m)(n \\times m)(n×m) tensor, `mat2` is a (m×p)(m \\times p)(m×p) tensor, then `input` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with a (n×p)(n \\times p)(n×p) tensor and `out` will be a (n×p)(n \\times p)(n×p) tensor.

`alpha` and `beta` are scaling factors on matrix-vector product between `mat1` and `mat2` and the added matrix `input` respectively.

out\=β input+α (mat1i@mat2i)\\text{out} = \\beta\\ \\text{input} + \\alpha\\ (\\text{mat1}\_i \\mathbin{@} \\text{mat2}\_i) out\=β input+α (mat1i​@mat2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and `alpha` must be real numbers, otherwise they should be integers.

This operation has support for arguments with [sparse layouts](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-docs)
. If `input` is sparse the result will have the same layout and if `out` is provided it must have the same layout as `input`.

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported, or may not have autograd support. If you notice missing functionality please open a feature request.

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – matrix to be added
    
*   **mat1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first matrix to be matrix multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second matrix to be matrix multiplied
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> M \= torch.randn(2, 3)
\>>> mat1 \= torch.randn(2, 3)
\>>> mat2 \= torch.randn(3, 3)
\>>> torch.addmm(M, mat1, mat2)
tensor(\[\[-4.8716,  1.4671, -1.3746\],\
        \[ 0.7573, -3.9555, -2.8681\]\])

Copy to clipboard

torch.addmm(_input_, _mat1_, _mat2_, _out\_dtype_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – matrix to be added
    
*   **mat1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first matrix to be matrix multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second matrix to be matrix multiplied
    
*   **out\_dtype** ([_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the dtype of the output tensor. On CUDA and XPU, only `torch.float32` is supported given `torch.float16`/`torch.bfloat16` input dtypes. Other backends (including out-of-tree accelerators) may support additional input/output dtype combinations.
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.addmm.rst.txt)

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