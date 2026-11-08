Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/debugging_environment_variables.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/debugging_environment_variables.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/debugging_environment_variables.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/debugging_environment_variables.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/debugging_environment_variables.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/debugging_environment_variables.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/debugging_environment_variables.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/debugging_environment_variables.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/debugging_environment_variables.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/debugging_environment_variables.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/debugging_environment_variables.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/debugging_environment_variables.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/debugging_environment_variables.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/debugging_environment_variables.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/debugging_environment_variables.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/debugging_environment_variables.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/debugging_environment_variables.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/debugging_environment_variables.html)
[v1.13](https://docs.pytorch.org/docs/1.13/debugging_environment_variables.html)
[v1.12](https://docs.pytorch.org/docs/1.12/debugging_environment_variables.html)
[v1.11](https://docs.pytorch.org/docs/1.11/debugging_environment_variables.html)
[v1.10](https://docs.pytorch.org/docs/1.10/debugging_environment_variables.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/debugging_environment_variables.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/debugging_environment_variables.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/debugging_environment_variables.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/debugging_environment_variables.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/debugging_environment_variables.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/debugging_environment_variables.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/debugging_environment_variables.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/debugging_environment_variables.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/debugging_environment_variables.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/debugging_environment_variables.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/debugging_environment_variables.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/debugging_environment_variables.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/debugging_environment_variables.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/debugging_environment_variables.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/debugging_environment_variables.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/debugging_environment_variables.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/debugging_environment_variables.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/debugging_environment_variables.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/debugging_environment_variables.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/debugging_environment_variables.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/debugging_environment_variables.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/debugging_environment_variables.html)

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

Debugging Environment Variables[#](https://docs.pytorch.org/docs/2.15/debugging_environment_variables.html#debugging-environment-variables "Link to this heading")

===================================================================================================================================================================

Created On: Feb 15, 2024 | Last Updated On: Jul 30, 2026

| Variable | Description |
| --- | --- |
| `TORCH_SHOW_CPP_STACKTRACES` | If set to `1`, makes PyTorch print out a stack trace when it detects a C++ error. |
| `TORCH_CPP_LOG_LEVEL` | Set the log level of c10 logging facility (supports both GLOG and c10 loggers). Valid values are `INFO`, `WARNING`, `ERROR`, and `FATAL` or their numerical equivalents `0`, `1`, `2`, and `3`. |
| `TORCH_LOGS` | For a more in depth explanation of this environment variable, see [torch.\_logging](https://docs.pytorch.org/docs/2.15/logging.html)<br>. |
| `TORCH_DIST_NAN_CHECK` | If set to `1`, checks the input (send) buffers of every `torch.distributed` collective for NaNs, for any backend. Unlike `TORCH_NCCL_NAN_CHECK`, which is implemented natively by the NCCL backend, this is driven by the backend-agnostic `ProcessGroup` collective hooks. |

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/debugging_environment_variables.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/debugging_environment_variables.md.txt)

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