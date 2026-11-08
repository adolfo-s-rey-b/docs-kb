Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch_environment_variables.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch_environment_variables.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch_environment_variables.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch_environment_variables.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch_environment_variables.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch_environment_variables.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch_environment_variables.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch_environment_variables.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch_environment_variables.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch_environment_variables.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch_environment_variables.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch_environment_variables.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch_environment_variables.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch_environment_variables.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch_environment_variables.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch_environment_variables.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch_environment_variables.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch_environment_variables.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch_environment_variables.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch_environment_variables.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch_environment_variables.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch_environment_variables.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch_environment_variables.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch_environment_variables.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch_environment_variables.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch_environment_variables.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch_environment_variables.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch_environment_variables.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch_environment_variables.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch_environment_variables.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch_environment_variables.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch_environment_variables.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch_environment_variables.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch_environment_variables.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch_environment_variables.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch_environment_variables.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch_environment_variables.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch_environment_variables.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch_environment_variables.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch_environment_variables.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch_environment_variables.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch_environment_variables.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch_environment_variables.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch_environment_variables.html)

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

Torch Environment Variables[#](https://docs.pytorch.org/docs/2.15/torch_environment_variables.html#torch-environment-variables "Link to this heading")

=======================================================================================================================================================

Created On: Feb 15, 2024 | Last Updated On: Jun 10, 2025

PyTorch leverages environment variables for adjusting various settings that influence its runtime behavior. These variables offer control over key functionalities, such as displaying the C++ stack trace upon encountering errors, synchronizing the execution of CUDA kernels, specifying the number of threads for parallel processing tasks and many more.

Moreover, PyTorch leverages several high-performance libraries, such as MKL and cuDNN, which also utilize environment variables to modify their functionality. This interplay of settings allows for a highly customizable development environment that can be optimized for efficiency, debugging, and computational resource management.

Please note that while this documentation covers a broad spectrum of environment variables relevant to PyTorch and its associated libraries, it is not exhaustive. If you find anything in this documentation that is missing, incorrect, or could be improved, please let us know by filing an issue or opening a pull request.

*   [Threading Environment Variables](https://docs.pytorch.org/docs/2.15/threading_environment_variables.html)
    
*   [CUDA Environment Variables](https://docs.pytorch.org/docs/2.15/cuda_environment_variables.html)
    
*   [MPS Environment Variables](https://docs.pytorch.org/docs/2.15/mps_environment_variables.html)
    
*   [Debugging Environment Variables](https://docs.pytorch.org/docs/2.15/debugging_environment_variables.html)
    
*   [Miscellaneous Environment Variables](https://docs.pytorch.org/docs/2.15/miscellaneous_environment_variables.html)
    
*   [torch.\_logging](https://docs.pytorch.org/docs/2.15/logging.html)
    
*   [PYTORCH ProcessGroupNCCL Environment Variables](https://docs.pytorch.org/docs/2.15/torch_nccl_environment_variables.html)
    

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch_environment_variables.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch_environment_variables.md.txt)

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