Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.backward.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.backward.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.backward.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.backward.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.backward.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.backward.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.backward.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.backward.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.backward.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.backward.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.backward.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.backward.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.backward.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.backward.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.backward.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.backward.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.backward.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.backward.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.backward.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.backward.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.backward.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.backward.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.backward.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.backward.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.backward.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.backward.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.backward.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.backward.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.backward.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.backward.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.backward.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.backward.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.backward.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.backward.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.backward.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.backward.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.backward.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.backward.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.backward.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.backward.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.backward.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.backward.html)

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

torch.Tensor.backward[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch-tensor-backward "Link to this heading")

===============================================================================================================================================

Tensor.backward(_gradient\=None_, _retain\_graph\=None_, _create\_graph\=False_, _inputs\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_tensor.py#L566)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch.Tensor.backward "Link to this definition")

Computes the gradient of current tensor wrt graph leaves.

The graph is differentiated using the chain rule. If the tensor is non-scalar (i.e. its data has more than one element) and requires gradient, the function additionally requires specifying a `gradient`. It should be a tensor of matching type and shape, that represents the gradient of the differentiated function w.r.t. `self`.

This function accumulates gradients in the leaves - you might need to zero `.grad` attributes or set them to `None` before calling it. See [Default gradient layouts](https://docs.pytorch.org/docs/2.15/autograd.html#default-grad-layouts)
 for details on the memory layout of accumulated gradients.

Note

If you run any forward ops, create `gradient`, and/or call `backward` in a user-specified CUDA stream context, see [Stream semantics of backward passes](https://docs.pytorch.org/docs/2.15/notes/cuda.html#bwd-cuda-stream-semantics)
.

Note

When `inputs` are provided and a given input is not a leaf, the current implementation will call its grad\_fn (though it is not strictly needed to get this gradients). It is an implementation detail on which the user should not rely. See [pytorch/pytorch#60521](https://github.com/pytorch/pytorch/pull/60521#issuecomment-867061780)
 for more details.

Parameters:

*   **gradient** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – The gradient of the function being differentiated w.r.t. `self`. This argument can be omitted if `self` is a scalar. Defaults to `None`.
    
*   **retain\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, the graph used to compute the grads will be freed; If `True`, it will be retained. The default is `None`, in which case the value is inferred from `create_graph` (i.e., the graph is retained only when higher-order derivative tracking is requested). Note that in nearly all cases setting this option to True is not needed and often can be worked around in a much more efficient way.
    
*   **create\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, graph of the derivative will be constructed, allowing to compute higher order derivative products. Defaults to `False`.
    
*   **inputs** (_Sequence__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\] or_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]__,_ _optional_) – Inputs w.r.t. which the gradient will be accumulated into `.grad`. All other tensors will be ignored. If not provided, the gradient is accumulated into all the leaf Tensors that were used to compute the `tensors`. A dict of tensors (e.g. `dict(model.named_parameters())`) is also accepted. Defaults to `None`.
    

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.backward.rst.txt)

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