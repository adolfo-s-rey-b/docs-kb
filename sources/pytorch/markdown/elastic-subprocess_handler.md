Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/subprocess_handler.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/subprocess_handler.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/subprocess_handler.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/subprocess_handler.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/subprocess_handler.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/subprocess_handler.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/subprocess_handler.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/subprocess_handler.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/subprocess_handler.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/subprocess_handler.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/subprocess_handler.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/subprocess_handler.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/subprocess_handler.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/subprocess_handler.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/subprocess_handler.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/subprocess_handler.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/subprocess_handler.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/subprocess_handler.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/subprocess_handler.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/subprocess_handler.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/subprocess_handler.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/subprocess_handler.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/subprocess_handler.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/subprocess_handler.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/subprocess_handler.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/subprocess_handler.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/subprocess_handler.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/subprocess_handler.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/subprocess_handler.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/subprocess_handler.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/subprocess_handler.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/subprocess_handler.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/subprocess_handler.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/subprocess_handler.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/subprocess_handler.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/subprocess_handler.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/subprocess_handler.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/subprocess_handler.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/subprocess_handler.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/subprocess_handler.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/subprocess_handler.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/subprocess_handler.html)

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

Subprocess Handling[#](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#module-torch.distributed.elastic.multiprocessing.subprocess_handler "Link to this heading")

======================================================================================================================================================================================

Created On: Mar 08, 2024 | Last Updated On: May 08, 2026

Retrieve SubprocessHandler[#](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#retrieve-subprocesshandler "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

torch.distributed.elastic.multiprocessing.subprocess\_handler.handlers.get\_subprocess\_handler(_entrypoint_, _args_, _env_, _stdout_, _stderr_, _local\_rank\_id_, _numa\_options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/subprocess_handler/handlers.py#L16)
[#](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#torch.distributed.elastic.multiprocessing.subprocess_handler.handlers.get_subprocess_handler "Link to this definition")

Return type:

[_SubprocessHandler_](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#torch.distributed.elastic.multiprocessing.subprocess_handler.subprocess_handler.SubprocessHandler "torch.distributed.elastic.multiprocessing.subprocess_handler.subprocess_handler.SubprocessHandler")

SubprocessHandler[#](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#subprocesshandler "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

_class_ torch.distributed.elastic.multiprocessing.subprocess\_handler.subprocess\_handler.SubprocessHandler(_entrypoint_, _args_, _env_, _stdout_, _stderr_, _local\_rank\_id_, _numa\_options_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/multiprocessing/subprocess_handler/subprocess_handler.py#L30)
[#](https://docs.pytorch.org/docs/2.15/elastic/subprocess_handler.html#torch.distributed.elastic.multiprocessing.subprocess_handler.subprocess_handler.SubprocessHandler "Link to this definition")

Convenience wrapper around python’s `subprocess.Popen`. Keeps track of meta-objects associated to the process (e.g. stdout and stderr redirect fds).

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/subprocess_handler.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/subprocess_handler.md.txt)

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