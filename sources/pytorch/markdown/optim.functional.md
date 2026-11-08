Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/optim.functional.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/optim.functional.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/optim.functional.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/optim.functional.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/optim.functional.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/optim.functional.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/optim.functional.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/optim.functional.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/optim.functional.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/optim.functional.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/optim.functional.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/optim.functional.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/optim.functional.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/optim.functional.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/optim.functional.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/optim.functional.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/optim.functional.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/optim.functional.html)
[v1.13](https://docs.pytorch.org/docs/1.13/optim.functional.html)
[v1.12](https://docs.pytorch.org/docs/1.12/optim.functional.html)
[v1.11](https://docs.pytorch.org/docs/1.11/optim.functional.html)
[v1.10](https://docs.pytorch.org/docs/1.10/optim.functional.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/optim.functional.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/optim.functional.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/optim.functional.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/optim.functional.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/optim.functional.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/optim.functional.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/optim.functional.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/optim.functional.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/optim.functional.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/optim.functional.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/optim.functional.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/optim.functional.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/optim.functional.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/optim.functional.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/optim.functional.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/optim.functional.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/optim.functional.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/optim.functional.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/optim.functional.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/optim.functional.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/optim.functional.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/optim.functional.html)

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

torch.optim.functional[#](https://docs.pytorch.org/docs/2.15/optim.functional.html#torch-optim-functional "Link to this heading")

==================================================================================================================================

Created On: Aug 27, 2026 | Last Updated On: Aug 27, 2026

Functional optimizer APIs give callers complete control over the parameters, gradients, and optimizer state. They are not pure functions; they update parameters and optimizer-state tensors in place. See [Functional optimizer API](https://docs.pytorch.org/docs/2.15/optim.html#functional-optimizer-api)
 for their common contract and usage examples.

Functional optimizer APIs.

|     |     |
| --- | --- |
| [`adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adadelta.html#torch.optim.functional.adadelta "torch.optim.functional.adadelta") | Functional API that performs Adadelta algorithm computation. |
| [`adafactor`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adafactor.html#torch.optim.functional.adafactor "torch.optim.functional.adafactor") | Functional API that performs Adafactor algorithm computation. |
| [`adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adagrad.html#torch.optim.functional.adagrad "torch.optim.functional.adagrad") | Functional API that performs Adagrad algorithm computation. |
| [`adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adam.html#torch.optim.functional.adam "torch.optim.functional.adam") | Functional API that performs Adam algorithm computation. |
| [`adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adamax.html#torch.optim.functional.adamax "torch.optim.functional.adamax") | Functional API that performs Adamax algorithm computation. |
| [`adamw`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.adamw.html#torch.optim.functional.adamw "torch.optim.functional.adamw") | Functional API that performs AdamW algorithm computation. |
| [`asgd`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.asgd.html#torch.optim.functional.asgd "torch.optim.functional.asgd") | Functional API that performs ASGD algorithm computation. |
| [`muon`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.muon.html#torch.optim.functional.muon "torch.optim.functional.muon") | Functional API that performs Muon algorithm computation. |
| [`nadam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.nadam.html#torch.optim.functional.nadam "torch.optim.functional.nadam") | Functional API that performs NAdam algorithm computation. |
| [`radam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.radam.html#torch.optim.functional.radam "torch.optim.functional.radam") | Functional API that performs RAdam algorithm computation. |
| [`rmsprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.rmsprop.html#torch.optim.functional.rmsprop "torch.optim.functional.rmsprop") | Functional API that performs RMSprop algorithm computation. |
| [`rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.rprop.html#torch.optim.functional.rprop "torch.optim.functional.rprop") | Functional API that performs Rprop algorithm computation. |
| [`sgd`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.sgd.html#torch.optim.functional.sgd "torch.optim.functional.sgd") | Functional API that performs SGD algorithm computation. |
| [`sparse_adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.functional.sparse_adam.html#torch.optim.functional.sparse_adam "torch.optim.functional.sparse_adam") | Functional API that performs SparseAdam algorithm computation. |

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/optim.functional.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/optim.functional.md.txt)

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