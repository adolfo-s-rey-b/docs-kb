Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.addr.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.addr.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.addr.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.addr.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.addr.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.addr.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.addr.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.addr.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.addr.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.addr.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.addr.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.addr.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.addr.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.addr.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.addr.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.addr.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.addr.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.addr.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.addr.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.addr.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.addr.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.addr.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.addr.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.addr.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.addr.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.addr.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.addr.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.addr.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.addr.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.addr.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.addr.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.addr.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.addr.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.addr.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.addr.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.addr.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.addr.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.addr.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.addr.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.addr.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.addr.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.addr.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.addr.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.addr.html)

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

torch.addr[#](https://docs.pytorch.org/docs/2.15/generated/torch.addr.html#torch-addr "Link to this heading")

==============================================================================================================

torch.addr(_input_, _vec1_, _vec2_, _\*_, _beta\=1_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.addr.html#torch.addr "Link to this definition")

Performs the outer-product of vectors `vec1` and `vec2` and adds it to the matrix `input`.

Optional values `beta` and `alpha` are scaling factors on the outer product between `vec1` and `vec2` and the added matrix `input` respectively.

out\=β input+α (vec1⊗vec2)\\text{out} = \\beta\\ \\text{input} + \\alpha\\ (\\text{vec1} \\otimes \\text{vec2}) out\=β input+α (vec1⊗vec2)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in it will not be propagated.

If `vec1` is a vector of size n and `vec2` is a vector of size m, then `input` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 with a matrix of size (n×m)(n \\times m)(n×m) and `out` will be a matrix of size (n×m)(n \\times m)(n×m).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – matrix to be added
    
*   **vec1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first vector of the outer product
    
*   **vec2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second vector of the outer product
    

Keyword Arguments:

*   **beta** (_Number__,_ _optional_) – multiplier for `input` (β\\betaβ)
    
*   **alpha** (_Number__,_ _optional_) – multiplier for vec1⊗vec2\\text{vec1} \\otimes \\text{vec2}vec1⊗vec2 (α\\alphaα)
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> vec1 \= torch.arange(1., 4.)
\>>> vec2 \= torch.arange(1., 3.)
\>>> M \= torch.zeros(3, 2)
\>>> torch.addr(M, vec1, vec2)
tensor(\[\[ 1.,  2.\],\
        \[ 2.,  4.\],\
        \[ 3.,  6.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.addr.rst.txt)

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