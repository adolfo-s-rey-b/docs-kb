Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Softmax.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Softmax.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Softmax.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Softmax.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Softmax.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Softmax.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Softmax.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Softmax.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Softmax.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Softmax.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Softmax.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Softmax.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Softmax.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Softmax.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Softmax.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Softmax.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Softmax.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Softmax.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Softmax.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Softmax.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Softmax.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Softmax.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Softmax.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Softmax.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Softmax.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Softmax.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Softmax.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Softmax.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Softmax.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Softmax.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Softmax.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Softmax.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Softmax.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Softmax.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Softmax.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Softmax.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Softmax.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Softmax.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Softmax.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Softmax.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Softmax.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Softmax.html)

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

Softmax[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html#softmax "Link to this heading")

==============================================================================================================

_class_ torch.nn.Softmax(_dim\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1766)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html#torch.nn.Softmax "Link to this definition")

Applies the Softmax function to an n-dimensional input Tensor.

Rescales them so that the elements of the n-dimensional output Tensor lie in the range \[0,1\] and sum to 1.

Softmax is defined as:

Softmax(xi)\=exp⁡(xi)∑jexp⁡(xj)\\text{Softmax}(x\_{i}) = \\frac{\\exp(x\_i)}{\\sum\_j \\exp(x\_j)} Softmax(xi​)\=∑j​exp(xj​)exp(xi​)​

When the input Tensor is a sparse tensor then the unspecified values are treated as `-inf`.

Shape:

*   Input: (∗)(\*)(∗) where \* means, any number of additional dimensions
    
*   Output: (∗)(\*)(∗), same shape as the input
    

Returns:

a Tensor of the same dimension and shape as the input with values in the range \[0, 1\]

Parameters:

**dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – A dimension along which Softmax will be computed (so every slice along dim will sum to 1).

Return type:

None

Note

This module doesn’t work directly with NLLLoss, which expects the Log to be computed between the Softmax and itself. Use LogSoftmax instead (it’s faster and has better numerical properties).

Examples:

\>>> m \= nn.Softmax(dim\=1)
\>>> input \= torch.randn(2, 3)
\>>> output \= m(input)

Copy to clipboard

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1826)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html#torch.nn.Softmax.extra_repr "Link to this definition")

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1820)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Softmax.html#torch.nn.Softmax.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Softmax.rst.txt)

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