Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.mm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.mm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.mm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.mm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.mm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.mm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.mm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.mm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.mm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.mm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.mm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.mm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.mm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.mm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.mm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.mm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.mm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.mm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.mm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.mm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.mm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.mm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.mm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.mm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.mm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.mm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.mm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.mm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.mm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.mm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.mm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.mm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.mm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.mm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.mm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.mm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.mm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.mm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.mm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.mm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.mm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.mm.html)

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

torch.mm[#](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#torch-mm "Link to this heading")

========================================================================================================

torch.mm(_input_, _mat2_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#torch.mm "Link to this definition")

Performs a matrix multiplication of the matrices `input` and `mat2`.

If `input` is a (n×m)(n \\times m)(n×m) tensor, `mat2` is a (m×p)(m \\times p)(m×p) tensor, `out` will be a (n×p)(n \\times p)(n×p) tensor.

Note

This function does not [broadcast](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
. For broadcasting matrix products, see [`torch.matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul")
.

Supports strided and sparse 2-D tensors as inputs, autograd with respect to strided inputs.

This operation has support for arguments with [sparse layouts](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-docs)
. If `out` is provided its layout will be used. Otherwise, the result layout will be deduced from that of `input`.

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported, or may not have autograd support. If you notice missing functionality please open a feature request.

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first matrix to be matrix multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second matrix to be matrix multiplied
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> mat1 \= torch.randn(2, 3)
\>>> mat2 \= torch.randn(3, 3)
\>>> torch.mm(mat1, mat2)
tensor(\[\[ 0.4851,  0.5037, -0.3633\],\
        \[-0.0760, -3.6705,  2.4784\]\])

Copy to clipboard

torch.mm(_input_, _mat2_, _out\_dtype_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first matrix to be matrix multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second matrix to be matrix multiplied
    
*   **out\_dtype** ([_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the dtype of the output tensor. On CUDA and XPU, only `torch.float32` is supported given `torch.float16`/`torch.bfloat16` input dtypes. Other backends (including out-of-tree accelerators) may support additional input/output dtype combinations.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.mm.rst.txt)

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