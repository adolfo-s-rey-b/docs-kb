Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.autograd.Function.backward.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.autograd.Function.backward.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.autograd.Function.backward.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.autograd.Function.backward.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.autograd.Function.backward.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.autograd.Function.backward.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.autograd.Function.backward.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.autograd.Function.backward.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.autograd.Function.backward.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.autograd.Function.backward.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.autograd.Function.backward.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.autograd.Function.backward.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.autograd.Function.backward.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.autograd.Function.backward.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.autograd.Function.backward.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.autograd.Function.backward.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.autograd.Function.backward.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.autograd.Function.backward.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.autograd.Function.backward.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.autograd.Function.backward.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.autograd.Function.backward.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.autograd.Function.backward.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.autograd.Function.backward.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.autograd.Function.backward.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.autograd.Function.backward.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.autograd.Function.backward.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.autograd.Function.backward.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.autograd.Function.backward.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.autograd.Function.backward.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.autograd.Function.backward.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.autograd.Function.backward.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.autograd.Function.backward.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.autograd.Function.backward.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.autograd.Function.backward.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.autograd.Function.backward.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.autograd.Function.backward.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.autograd.Function.backward.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.autograd.Function.backward.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.autograd.Function.backward.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.autograd.Function.backward.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.autograd.Function.backward.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.autograd.Function.backward.html)

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

torch.autograd.Function.backward[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch-autograd-function-backward "Link to this heading")

================================================================================================================================================================================

_static_ Function.backward(_ctx_, _\*grad\_outputs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/function.py#L559)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "Link to this definition")

Define a formula for differentiating the operation with backward mode automatic differentiation.

This function is to be overridden by all subclasses. (Defining this function is equivalent to defining the `vjp` function.)

It must accept a context `ctx` as the first argument, followed by as many outputs as the [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 returned (None will be passed in for non tensor outputs of the forward function), and it should return as many tensors, as there were inputs to [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
. Each argument is the gradient w.r.t the given output, and each returned value should be the gradient w.r.t. the corresponding input. If an input is not a Tensor or is a Tensor not requiring grads, you can just pass None as a gradient for that input.

The strides of the gradients passed to [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
 are undefined: they are not guaranteed to be contiguous or to match the strides of the corresponding forward outputs, so implementations must not assume a particular memory layout.

The context can be used to retrieve tensors saved during the forward pass. It also has an attribute `ctx.needs_input_grad` as a tuple of booleans representing whether each input needs gradient. E.g., [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
 will have `ctx.needs_input_grad[0] = True` if the first input to [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 needs gradient computed w.r.t. the output.

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.autograd.Function.backward.rst.txt)

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