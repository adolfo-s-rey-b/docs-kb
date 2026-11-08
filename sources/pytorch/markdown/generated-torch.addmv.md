Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.addmv.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.addmv.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.addmv.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.addmv.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.addmv.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.addmv.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.addmv.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.addmv.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.addmv.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.addmv.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.addmv.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.addmv.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.addmv.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.addmv.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.addmv.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.addmv.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.addmv.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.addmv.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.addmv.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.addmv.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.addmv.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.addmv.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.addmv.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.addmv.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.addmv.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.addmv.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.addmv.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.addmv.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.addmv.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.addmv.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.addmv.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.addmv.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.addmv.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.addmv.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.addmv.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.addmv.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.addmv.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.addmv.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.addmv.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.addmv.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.addmv.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.addmv.html)

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

torch.addmv[#](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html#torch-addmv "Link to this heading")

=================================================================================================================

torch.addmv(_input_, _mat_, _vec_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html#torch.addmv "Link to this definition")

Performs a matrix-vector product of the matrix `mat` and the vector `vec`. The vector `input` is added to the final result.

If `mat` is a (n×m)(n \\times m)(n×m) tensor, `vec` is a 1-D tensor of size m, then `input` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with a 1-D tensor of size n and `out` will be 1-D tensor of size n.

`alpha` and `beta` are scaling factors on matrix-vector product between `mat` and `vec` and the added tensor `input` respectively.

out\=β input+α (mat@vec)\\text{out} = \\beta\\ \\text{input} + \\alpha\\ (\\text{mat} \\mathbin{@} \\text{vec}) out\=β input+α (mat@vec)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and `alpha` must be real numbers, otherwise they should be integers.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – vector to be added
    
*   **mat** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – matrix to be matrix multiplied
    
*   **vec** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – vector to be matrix multiplied
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for mat@vecmat @ vecmat@vec (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> M \= torch.randn(2)
\>>> mat \= torch.randn(2, 3)
\>>> vec \= torch.randn(3)
\>>> torch.addmv(M, mat, vec)
tensor(\[-0.3768, -5.5565\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.addmv.rst.txt)

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