Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/performance.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/performance.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/performance.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/user_guide/torch_compiler/performance.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/user_guide/torch_compiler/performance.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/user_guide/torch_compiler/performance.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/user_guide/torch_compiler/performance.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/user_guide/torch_compiler/performance.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/user_guide/torch_compiler/performance.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/user_guide/torch_compiler/performance.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/user_guide/torch_compiler/performance.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/user_guide/torch_compiler/performance.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/user_guide/torch_compiler/performance.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/user_guide/torch_compiler/performance.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/user_guide/torch_compiler/performance.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/user_guide/torch_compiler/performance.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/user_guide/torch_compiler/performance.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/user_guide/torch_compiler/performance.html)
[v1.13](https://docs.pytorch.org/docs/1.13/user_guide/torch_compiler/performance.html)
[v1.12](https://docs.pytorch.org/docs/1.12/user_guide/torch_compiler/performance.html)
[v1.11](https://docs.pytorch.org/docs/1.11/user_guide/torch_compiler/performance.html)
[v1.10](https://docs.pytorch.org/docs/1.10/user_guide/torch_compiler/performance.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/user_guide/torch_compiler/performance.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/user_guide/torch_compiler/performance.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/user_guide/torch_compiler/performance.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/user_guide/torch_compiler/performance.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/user_guide/torch_compiler/performance.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/user_guide/torch_compiler/performance.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/user_guide/torch_compiler/performance.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/user_guide/torch_compiler/performance.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/user_guide/torch_compiler/performance.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/user_guide/torch_compiler/performance.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/user_guide/torch_compiler/performance.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/user_guide/torch_compiler/performance.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/user_guide/torch_compiler/performance.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/user_guide/torch_compiler/performance.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/user_guide/torch_compiler/performance.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/user_guide/torch_compiler/performance.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/user_guide/torch_compiler/performance.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/user_guide/torch_compiler/performance.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/user_guide/torch_compiler/performance.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/user_guide/torch_compiler/performance.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/user_guide/torch_compiler/performance.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/user_guide/torch_compiler/performance.html)

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

Performance[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/performance.html#performance "Link to this heading")

=================================================================================================================================

Created On: Dec 03, 2025 | Last Updated On: Dec 03, 2025

Learn how to profile, benchmark, and optimize your models with `torch.compile`.

*   [PyTorch 2.0 Performance Dashboard](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_performance_dashboard.html)
    
*   [TorchInductor GPU Profiling](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_inductor_profiling.html)
    
*   [Profiling to understand torch.compile performance](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_profiling_torch_compile.html)
    
*   [Finding graph breaks: “Torch-Compiled Region” and “CompiledFunction”](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_profiling_torch_compile.html#finding-graph-breaks-torch-compiled-region-and-compiledfunction)
    
*   [CUDAGraph Trees](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_cudagraph_trees.html)
    

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/user_guide/torch_compiler/performance.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/user_guide/torch_compiler/performance.md.txt)

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