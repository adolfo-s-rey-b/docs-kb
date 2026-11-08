Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.optim.functional.adam.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.optim.functional.adam.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.optim.functional.adam.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.optim.functional.adam.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.optim.functional.adam.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.optim.functional.adam.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.optim.functional.adam.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.optim.functional.adam.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.optim.functional.adam.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.optim.functional.adam.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.optim.functional.adam.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.optim.functional.adam.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.optim.functional.adam.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.optim.functional.adam.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.optim.functional.adam.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.optim.functional.adam.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.optim.functional.adam.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.optim.functional.adam.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.optim.functional.adam.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.optim.functional.adam.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.optim.functional.adam.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.optim.functional.adam.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.optim.functional.adam.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.optim.functional.adam.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.optim.functional.adam.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.optim.functional.adam.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.optim.functional.adam.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.optim.functional.adam.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.optim.functional.adam.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.optim.functional.adam.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.optim.functional.adam.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.optim.functional.adam.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.optim.functional.adam.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.optim.functional.adam.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.optim.functional.adam.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.optim.functional.adam.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.optim.functional.adam.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.optim.functional.adam.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.optim.functional.adam.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.optim.functional.adam.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.optim.functional.adam.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.optim.functional.adam.html)

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

torch.optim.functional.adam[#](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html#torch-optim-functional-adam "Link to this heading")

=================================================================================================================================================================

torch.optim.functional.adam(_params_, _grads_, _exp\_avgs_, _exp\_avg\_sqs_, _max\_exp\_avg\_sqs_, _state\_steps_, _foreach\=None_, _capturable\=False_, _differentiable\=False_, _fused\=None_, _grad\_scale\=None_, _found\_inf\=None_, _has\_complex\=False_, _decoupled\_weight\_decay\=False_, _\*_, _amsgrad_, _beta1_, _beta2_, _lr_, _weight\_decay_, _eps_, _maximize_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/optim/adam.py#L903)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html#torch.optim.functional.adam "Link to this definition")

Functional API that performs Adam algorithm computation.

This function updates the provided parameters and optimizer state in place. The caller must initialize and retain optimizer state. Unless intentionally constructing a differentiable update with a supported `differentiable=True` argument, call this function under [`torch.no_grad`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")
. See [Functional optimizer API](https://docs.pytorch.org/docs/2.15/optim.html#functional-optimizer-api)
 for the common functional optimizer contract and examples, and [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html#torch.optim.Adam "torch.optim.Adam")
 for algorithm details.

Note

With `fused=True`, CUDA supports FP32 parameters and gradients with BF16 moment buffers. See [AdamW with BF16 optimizer state](https://docs.pytorch.org/docs/2.15/optim.html#functional-adamw-bf16-state)
 for an example.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.optim.functional.adam.rst.txt)

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