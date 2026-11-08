Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.addcmul.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.addcmul.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.addcmul.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.addcmul.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.addcmul.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.addcmul.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.addcmul.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.addcmul.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.addcmul.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.addcmul.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.addcmul.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.addcmul.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.addcmul.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.addcmul.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.addcmul.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.addcmul.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.addcmul.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.addcmul.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.addcmul.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.addcmul.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.addcmul.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.addcmul.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.addcmul.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.addcmul.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.addcmul.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.addcmul.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.addcmul.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.addcmul.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.addcmul.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.addcmul.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.addcmul.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.addcmul.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.addcmul.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.addcmul.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.addcmul.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.addcmul.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.addcmul.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.addcmul.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.addcmul.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.addcmul.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.addcmul.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.addcmul.html)

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

torch.addcmul[#](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#torch-addcmul "Link to this heading")

=======================================================================================================================

torch.addcmul(_input_, _tensor1_, _tensor2_, _\*_, _value\=1_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#torch.addcmul "Link to this definition")

Performs the element-wise multiplication of `tensor1` by `tensor2`, multiplies the result by the scalar `value` and adds it to `input`.

outi\=inputi+value×tensor1i×tensor2i\\text{out}\_i = \\text{input}\_i + \\text{value} \\times \\text{tensor1}\_i \\times \\text{tensor2}\_i outi​\=inputi​+value×tensor1i​×tensor2i​

The shapes of [`tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch.tensor "torch.tensor")
, `tensor1`, and `tensor2` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
.

For inputs of type FloatTensor or DoubleTensor, `value` must be a real number, otherwise an integer.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to be added
    
*   **tensor1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to be multiplied
    
*   **tensor2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to be multiplied
    

Keyword Arguments:

*   **value** (_Number__,_ _optional_) – multiplier for tensor1.∗tensor2tensor1 .\* tensor2tensor1.∗tensor2
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> t \= torch.randn(1, 3)
\>>> t1 \= torch.randn(3, 1)
\>>> t2 \= torch.randn(1, 3)
\>>> torch.addcmul(t, t1, t2, value\=0.1)
tensor(\[\[-0.8635, -0.6391,  1.6174\],\
        \[-0.7617, -0.5879,  1.7388\],\
        \[-0.8353, -0.6249,  1.6511\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.addcmul.rst.txt)

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