Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.matmul.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.matmul.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.matmul.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.matmul.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.matmul.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.matmul.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.matmul.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.matmul.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.matmul.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.matmul.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.matmul.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.matmul.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.matmul.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.matmul.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.matmul.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.matmul.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.matmul.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.matmul.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.matmul.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.matmul.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.matmul.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.matmul.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.matmul.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.matmul.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.matmul.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.matmul.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.matmul.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.matmul.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.matmul.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.matmul.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.matmul.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.matmul.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.matmul.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.matmul.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.matmul.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.matmul.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.matmul.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.matmul.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.matmul.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.matmul.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.matmul.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.matmul.html)

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

torch.matmul[#](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch-matmul "Link to this heading")

====================================================================================================================

torch.matmul(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "Link to this definition")

Matrix product of two tensors.

The behavior depends on the dimensionality of the tensors as follows:

*   If both tensors are 1-dimensional, the dot product (scalar) is returned.
    
*   If both arguments are 2-dimensional, the matrix-matrix product is returned.
    
*   If the first argument is 1-dimensional and the second argument is 2-dimensional, a 1 is prepended to its dimension for the purpose of the matrix multiply. After the matrix multiply, the prepended dimension is removed.
    
*   If the first argument is 2-dimensional and the second argument is 1-dimensional, the matrix-vector product is returned.
    
*   If both arguments are at least 1-dimensional and at least one argument is N-dimensional (where N > 2), then a batched matrix multiply is returned. If the first argument is 1-dimensional, a 1 is prepended to its dimension for the purpose of the batched matrix multiply and removed after. If the second argument is 1-dimensional, a 1 is appended to its dimension for the purpose of the batched matrix multiply and removed after.
    
    The first N-2 dimensions of each argument, the batch dimensions, are [broadcast](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
     (and thus must be broadcastable). The last 2, the matrix dimensions, are handled as in the matrix-matrix product.
    
    For example, if `input` is a (j×1×n×m)(j \\times 1 \\times n \\times m)(j×1×n×m) tensor and `other` is a (k×m×p)(k \\times m \\times p)(k×m×p) tensor, the batch dimensions are (j×1)(j \\times 1)(j×1) and (k)(k)(k), and the matrix dimensions are (n×m)(n \\times m)(n×m) and (m×p)(m \\times p)(m×p). `out` will be a (j×k×n×p)(j \\times k \\times n \\times p)(j×k×n×p) tensor.
    

This operation has support for arguments with [sparse layouts](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-docs)
. In particular the matrix-matrix (both arguments 2-dimensional) supports sparse arguments with the same restrictions as [`torch.mm()`](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#torch.mm "torch.mm")

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported, or may not have autograd support. If you notice missing functionality please open a feature request.

This operator supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Note

The 1-dimensional dot product version of this function does not support an `out` parameter.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first tensor to be multiplied
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second tensor to be multiplied
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> \# vector x vector
\>>> tensor1 \= torch.randn(3)
\>>> tensor2 \= torch.randn(3)
\>>> torch.matmul(tensor1, tensor2).size()
torch.Size(\[\])
\>>> \# matrix x vector
\>>> tensor1 \= torch.randn(3, 4)
\>>> tensor2 \= torch.randn(4)
\>>> torch.matmul(tensor1, tensor2).size()
torch.Size(\[3\])
\>>> \# batched matrix x broadcasted vector
\>>> tensor1 \= torch.randn(10, 3, 4)
\>>> tensor2 \= torch.randn(4)
\>>> torch.matmul(tensor1, tensor2).size()
torch.Size(\[10, 3\])
\>>> \# batched matrix x batched matrix
\>>> tensor1 \= torch.randn(10, 3, 4)
\>>> tensor2 \= torch.randn(10, 4, 5)
\>>> torch.matmul(tensor1, tensor2).size()
torch.Size(\[10, 3, 5\])
\>>> \# batched matrix x broadcasted matrix
\>>> tensor1 \= torch.randn(10, 3, 4)
\>>> tensor2 \= torch.randn(4, 5)
\>>> torch.matmul(tensor1, tensor2).size()
torch.Size(\[10, 3, 5\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.matmul.rst.txt)

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