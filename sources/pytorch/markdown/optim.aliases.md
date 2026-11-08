Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/optim.aliases.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/optim.aliases.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/optim.aliases.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/optim.aliases.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/optim.aliases.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/optim.aliases.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/optim.aliases.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/optim.aliases.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/optim.aliases.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/optim.aliases.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/optim.aliases.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/optim.aliases.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/optim.aliases.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/optim.aliases.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/optim.aliases.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/optim.aliases.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/optim.aliases.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/optim.aliases.html)
[v1.13](https://docs.pytorch.org/docs/1.13/optim.aliases.html)
[v1.12](https://docs.pytorch.org/docs/1.12/optim.aliases.html)
[v1.11](https://docs.pytorch.org/docs/1.11/optim.aliases.html)
[v1.10](https://docs.pytorch.org/docs/1.10/optim.aliases.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/optim.aliases.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/optim.aliases.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/optim.aliases.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/optim.aliases.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/optim.aliases.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/optim.aliases.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/optim.aliases.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/optim.aliases.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/optim.aliases.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/optim.aliases.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/optim.aliases.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/optim.aliases.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/optim.aliases.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/optim.aliases.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/optim.aliases.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/optim.aliases.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/optim.aliases.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/optim.aliases.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/optim.aliases.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/optim.aliases.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/optim.aliases.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/optim.aliases.html)

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

Aliases in torch.optim[#](https://docs.pytorch.org/docs/2.15/optim.aliases.html#aliases-in-torch-optim "Link to this heading")

===============================================================================================================================

Created On: Jul 18, 2025 | Last Updated On: Aug 27, 2026

Most optimizer classes are available both from `torch.optim` and from the nested module in which they are defined. For example, `torch.optim.Adam` and `torch.optim.adam.Adam` refer to the same class. While some functional optimizer APIs are exposed in their respective nested modules, all functional optimizer APIs are available in the [`torch.optim.functional`](https://docs.pytorch.org/docs/2.15/optim.functional.html#module-torch.optim.functional "torch.optim.functional")
 namespace; see [Functional optimizer API](https://docs.pytorch.org/docs/2.15/optim.html#functional-optimizer-api)
 for usage guidance.

|     |     |
| --- | --- |
| [`Adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adadelta.Adadelta_class.html#torch.optim.adadelta.Adadelta "torch.optim.adadelta.Adadelta") | Implements Adadelta algorithm. |
| [`adadelta`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adadelta.adadelta_function.html#torch.optim.adadelta.adadelta "torch.optim.adadelta.adadelta") | Functional API that performs Adadelta algorithm computation. |

|     |     |
| --- | --- |
| [`Adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adagrad.Adagrad_class.html#torch.optim.adagrad.Adagrad "torch.optim.adagrad.Adagrad") | Implements Adagrad algorithm. |
| [`adagrad`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adagrad.adagrad_function.html#torch.optim.adagrad.adagrad "torch.optim.adagrad.adagrad") | Functional API that performs Adagrad algorithm computation. |

|     |     |
| --- | --- |
| [`Adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adam.Adam_class.html#torch.optim.adam.Adam "torch.optim.adam.Adam") | Implements Adam algorithm. |
| [`adam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adam.adam_function.html#torch.optim.adam.adam "torch.optim.adam.adam") | Functional API that performs Adam algorithm computation. |

|     |     |
| --- | --- |
| [`Adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adamax.Adamax_class.html#torch.optim.adamax.Adamax "torch.optim.adamax.Adamax") | Implements Adamax algorithm (a variant of Adam based on infinity norm). |
| [`adamax`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adamax.adamax_function.html#torch.optim.adamax.adamax "torch.optim.adamax.adamax") | Functional API that performs Adamax algorithm computation. |

|     |     |
| --- | --- |
| [`AdamW`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adamw.AdamW_class.html#torch.optim.adamw.AdamW "torch.optim.adamw.AdamW") | Implements AdamW algorithm, where weight decay does not accumulate in the momentum nor variance. |
| [`adamw`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.adamw.adamw_function.html#torch.optim.adamw.adamw "torch.optim.adamw.adamw") | Functional API that performs AdamW algorithm computation. |

|     |     |
| --- | --- |
| [`ASGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.asgd.ASGD_class.html#torch.optim.asgd.ASGD "torch.optim.asgd.ASGD") | Implements Averaged Stochastic Gradient Descent. |
| [`asgd`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.asgd.asgd_function.html#torch.optim.asgd.asgd "torch.optim.asgd.asgd") | Functional API that performs ASGD algorithm computation. |

|     |     |
| --- | --- |
| [`LBFGS`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.lbfgs.LBFGS.html#torch.optim.lbfgs.LBFGS "torch.optim.lbfgs.LBFGS") | Implements L-BFGS algorithm. |

Implementation for the NAdam algorithm.

|     |     |
| --- | --- |
| [`NAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.nadam.NAdam_class.html#torch.optim.nadam.NAdam "torch.optim.nadam.NAdam") | Implements NAdam algorithm. |
| [`nadam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.nadam.nadam_function.html#torch.optim.nadam.nadam "torch.optim.nadam.nadam") | Functional API that performs NAdam algorithm computation. |

Implementation for the RAdam algorithm.

|     |     |
| --- | --- |
| [`RAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.radam.RAdam_class.html#torch.optim.radam.RAdam "torch.optim.radam.RAdam") | Implements RAdam algorithm. |
| [`radam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.radam.radam_function.html#torch.optim.radam.radam "torch.optim.radam.radam") | Functional API that performs RAdam algorithm computation. |

Implementation for the RMSprop algorithm.

|     |     |
| --- | --- |
| [`RMSprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.rmsprop.RMSprop_class.html#torch.optim.rmsprop.RMSprop "torch.optim.rmsprop.RMSprop") | Implements RMSprop algorithm. |
| [`rmsprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.rmsprop.rmsprop_function.html#torch.optim.rmsprop.rmsprop "torch.optim.rmsprop.rmsprop") | Functional API that performs RMSprop algorithm computation. |

Implementation for the Resilient backpropagation.

|     |     |
| --- | --- |
| [`Rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.rprop.Rprop_class.html#torch.optim.rprop.Rprop "torch.optim.rprop.Rprop") | Implements the resilient backpropagation algorithm. |
| [`rprop`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.rprop.rprop_function.html#torch.optim.rprop.rprop "torch.optim.rprop.rprop") | Functional API that performs Rprop algorithm computation. |

Implementation for Stochastic Gradient Descent optimizer.

|     |     |
| --- | --- |
| [`SGD`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.sgd.SGD_class.html#torch.optim.sgd.SGD "torch.optim.sgd.SGD") | Implements stochastic gradient descent (optionally with momentum). |
| [`sgd`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.sgd.sgd_function.html#torch.optim.sgd.sgd "torch.optim.sgd.sgd") | Functional API that performs SGD algorithm computation. |

|     |     |
| --- | --- |
| [`SparseAdam`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.sparse_adam.SparseAdam.html#torch.optim.sparse_adam.SparseAdam "torch.optim.sparse_adam.SparseAdam") | SparseAdam implements a masked version of the Adam algorithm suitable for sparse gradients. |

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/optim.aliases.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/optim.aliases.md.txt)

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