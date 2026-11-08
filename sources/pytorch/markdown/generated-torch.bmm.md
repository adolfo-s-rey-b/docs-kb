Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.bmm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.bmm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.bmm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.bmm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.bmm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.bmm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.bmm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.bmm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.bmm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.bmm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.bmm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.bmm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.bmm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.bmm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.bmm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.bmm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.bmm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.bmm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.bmm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.bmm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.bmm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.bmm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.bmm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.bmm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.bmm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.bmm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.bmm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.bmm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.bmm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.bmm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.bmm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.bmm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.bmm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.bmm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.bmm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.bmm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.bmm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.bmm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.bmm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.bmm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.bmm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.bmm.html)

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

torch.bmm[#](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html#torch-bmm "Link to this heading")

===========================================================================================================

torch.bmm(_input_, _mat2_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html#torch.bmm "Link to this definition")

Performs a batch matrix-matrix product of matrices stored in `input` and `mat2`.

`input` and `mat2` must be 3-D tensors each containing the same number of matrices.

If `input` is a (b×n×m)(b \\times n \\times m)(b×n×m) tensor, `mat2` is a (b×m×p)(b \\times m \\times p)(b×m×p) tensor, `out` will be a (b×n×p)(b \\times n \\times p)(b×n×p) tensor.

outi\=inputi@mat2i\\text{out}\_i = \\text{input}\_i \\mathbin{@} \\text{mat2}\_i outi​\=inputi​@mat2i​

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Note

This function does not [broadcast](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
. For broadcasting matrix products, see [`torch.matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul")
.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first batch of matrices to be multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second batch of matrices to be multiplied
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> input \= torch.randn(10, 3, 4)
\>>> mat2 \= torch.randn(10, 4, 5)
\>>> res \= torch.bmm(input, mat2)
\>>> res.size()
torch.Size(\[10, 3, 5\])

Copy to clipboard

torch.bmm(_input_, _mat2_, _out\_dtype_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first batch of matrices to be multiplied
    
*   **mat2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second batch of matrices to be multiplied
    
*   **out\_dtype** ([_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the dtype of the output tensor. On CUDA and XPU, only `torch.float32` is supported given `torch.float16`/`torch.bfloat16` input dtypes. Other backends (including out-of-tree accelerators) may support additional input/output dtype combinations.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.bmm.rst.txt)

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