Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.add.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.add.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.add.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.add.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.add.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.add.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.add.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.add.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.add.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.add.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.add.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.add.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.add.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.add.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.add.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.add.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.add.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.add.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.add.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.add.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.add.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.add.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.add.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.add.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.add.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.add.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.add.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.add.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.add.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.add.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.add.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.add.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.add.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.add.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.add.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.add.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.add.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.add.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.add.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.add.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.add.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.add.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.add.html)

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

torch.add[#](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch-add "Link to this heading")

===========================================================================================================

torch.add(_input_, _other_, _\*_, _alpha\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "Link to this definition")

Adds `other`, scaled by `alpha`, to `input`.

outi\=inputi+alpha×otheri\\text{{out}}\_i = \\text{{input}}\_i + \\text{{alpha}} \\times \\text{{other}}\_i outi​\=inputi​+alpha×otheri​

Supports [broadcasting to a common shape](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
, [type promotion](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#type-promotion-doc)
, and integer, float, and complex inputs.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Number_) – the tensor or number to add to `input`.
    

Keyword Arguments:

*   **alpha** (_Number_) – the multiplier for `other`.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Examples:

\>>> a \= torch.randn(4)
\>>> a
tensor(\[ 0.0202,  1.0985,  1.3506, -0.6056\])
\>>> torch.add(a, 20)
tensor(\[ 20.0202,  21.0985,  21.3506,  19.3944\])

\>>> b \= torch.randn(4)
\>>> b
tensor(\[-0.9732, -0.3497,  0.6245,  0.4022\])
\>>> c \= torch.randn(4, 1)
\>>> c
tensor(\[\[ 0.3743\],\
        \[-1.7724\],\
        \[-0.5811\],\
        \[-0.8017\]\])
\>>> torch.add(b, c, alpha\=10)
tensor(\[\[  2.7695,   3.3930,   4.3672,   4.1450\],\
        \[-18.6971, -18.0736, -17.0994, -17.3216\],\
        \[ -6.7845,  -6.1610,  -5.1868,  -5.4090\],\
        \[ -8.9902,  -8.3667,  -7.3925,  -7.6147\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.add.rst.txt)

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