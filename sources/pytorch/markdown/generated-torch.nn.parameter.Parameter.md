Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.parameter.Parameter.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.parameter.Parameter.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.parameter.Parameter.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.parameter.Parameter.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.parameter.Parameter.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.parameter.Parameter.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.parameter.Parameter.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.parameter.Parameter.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.parameter.Parameter.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.parameter.Parameter.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.parameter.Parameter.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.parameter.Parameter.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.parameter.Parameter.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.parameter.Parameter.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.parameter.Parameter.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.parameter.Parameter.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.parameter.Parameter.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.parameter.Parameter.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.parameter.Parameter.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.parameter.Parameter.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.parameter.Parameter.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.parameter.Parameter.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.parameter.Parameter.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.parameter.Parameter.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.parameter.Parameter.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.parameter.Parameter.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.parameter.Parameter.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.parameter.Parameter.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.parameter.Parameter.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.parameter.Parameter.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.parameter.Parameter.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.parameter.Parameter.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.parameter.Parameter.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.parameter.Parameter.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.parameter.Parameter.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.parameter.Parameter.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.parameter.Parameter.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.parameter.Parameter.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.parameter.Parameter.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.parameter.Parameter.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.parameter.Parameter.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.parameter.Parameter.html)

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

Parameter[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#parameter "Link to this heading")

==============================================================================================================================

_class_ torch.nn.parameter.Parameter(_data\=None_, _requires\_grad\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/parameter.py#L30)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "Link to this definition")

A kind of Tensor that is to be considered a module parameter.

Parameters are [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 subclasses, that have a very special property when used with `Module` s - when they’re assigned as Module attributes they are automatically added to the list of its parameters, and will appear e.g. in `parameters()` iterator. Assigning a Tensor doesn’t have such effect. This is because one might want to cache some temporary state, like last hidden state of the RNN, in the model. If there was no such class as [`Parameter`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "torch.nn.parameter.Parameter")
, these temporaries would get registered too.

Parameters:

*   **data** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – parameter tensor.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if the parameter requires gradient. Note that the torch.no\_grad() context does NOT affect the default behavior of Parameter creation–the Parameter will still have requires\_grad=True in `no_grad` mode. See [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/notes/autograd.html#locally-disable-grad-doc)
     for more details. Default: True
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.parameter.Parameter.rst.txt)

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