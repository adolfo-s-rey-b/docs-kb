Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Linear.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Linear.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Linear.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Linear.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Linear.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Linear.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Linear.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Linear.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Linear.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Linear.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Linear.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Linear.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Linear.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Linear.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Linear.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Linear.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Linear.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Linear.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Linear.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Linear.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Linear.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Linear.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Linear.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Linear.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Linear.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Linear.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Linear.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Linear.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Linear.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Linear.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Linear.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Linear.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Linear.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Linear.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Linear.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Linear.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Linear.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Linear.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Linear.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Linear.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Linear.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Linear.html)

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

Linear[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#linear "Link to this heading")

===========================================================================================================

_class_ torch.nn.Linear(_in\_features_, _out\_features_, _bias\=True_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/linear.py#L53)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear "Link to this definition")

Applies an affine linear transformation to the incoming data: y\=xAT+by = xA^T + by\=xAT+b.

This module supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

Parameters:

*   **in\_features** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – size of each input sample
    
*   **out\_features** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – size of each output sample
    
*   **bias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to `False`, the layer will not learn an additive bias. Default: `True`
    

Shape:

*   Input: (∗,Hin)(\*, H\_\\text{in})(∗,Hin​) where ∗\*∗ means any number of dimensions including none and Hin\=in\_featuresH\_\\text{in} = \\text{in\\\_features}Hin​\=in\_features.
    
*   Output: (∗,Hout)(\*, H\_\\text{out})(∗,Hout​) where all but the last dimension are the same shape as the input and Hout\=out\_featuresH\_\\text{out} = \\text{out\\\_features}Hout​\=out\_features.
    

Variables:

*   **weight** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the learnable weights of the module of shape (out\_features,in\_features)(\\text{out\\\_features}, \\text{in\\\_features})(out\_features,in\_features). The values are initialized from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​), where k\=1in\_featuresk = \\frac{1}{\\text{in\\\_features}}k\=in\_features1​
    
*   **bias** – the learnable bias of the module of shape (out\_features)(\\text{out\\\_features})(out\_features). If `bias` is `True`, the values are initialized from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​) where k\=1in\_featuresk = \\frac{1}{\\text{in\\\_features}}k\=in\_features1​
    

Examples:

\>>> m \= nn.Linear(20, 30)
\>>> input \= torch.randn(128, 20)
\>>> output \= m(input)
\>>> print(output.size())
torch.Size(\[128, 30\])

Copy to clipboard

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/linear.py#L136)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear.extra_repr "Link to this definition")

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/linear.py#L130)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

reset\_parameters()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/linear.py#L117)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear.reset_parameters "Link to this definition")

Resets parameters based on their initialization used in `__init__`.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Linear.rst.txt)

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