Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/control_plane.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/control_plane.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/control_plane.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/control_plane.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/control_plane.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/control_plane.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/control_plane.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/control_plane.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/control_plane.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/control_plane.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/control_plane.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/control_plane.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/control_plane.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/control_plane.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/control_plane.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/control_plane.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/control_plane.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/control_plane.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/control_plane.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/control_plane.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/control_plane.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/control_plane.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/control_plane.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/control_plane.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/control_plane.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/control_plane.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/control_plane.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/control_plane.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/control_plane.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/control_plane.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/control_plane.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/control_plane.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/control_plane.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/control_plane.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/control_plane.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/control_plane.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/control_plane.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/control_plane.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/control_plane.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/control_plane.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/control_plane.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/control_plane.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/control_plane.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/control_plane.html)

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

Control Plane[#](https://docs.pytorch.org/docs/2.15/elastic/control_plane.html#module-torch.distributed.elastic.control_plane "Link to this heading")

======================================================================================================================================================

Created On: May 30, 2024 | Last Updated On: May 06, 2026

This module contains optional helpers that add extra debug and control handlers into your application.

torch.distributed.elastic.control\_plane.worker\_main()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/control_plane.py#L26)
[#](https://docs.pytorch.org/docs/2.15/elastic/control_plane.html#torch.distributed.elastic.control_plane.worker_main "Link to this definition")

This is a context manager that wraps your main entry function. This combines the existing `errors.record` logic as well as a new `_WorkerServer` that exposes handlers via a unix socket specified by `TORCH_WORKER_SERVER_SOCKET`.

Example

@worker\_main()
def main():
    pass

if \_\_name\_\_ \== "\_\_main\_\_":
    main()

Copy to clipboard

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")
\[None, None, None\]

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/control_plane.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/control_plane.md.txt)

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