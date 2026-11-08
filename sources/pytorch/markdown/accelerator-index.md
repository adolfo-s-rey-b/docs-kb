Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/index.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/index.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/index.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/index.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/index.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/index.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/index.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/index.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/index.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/index.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/index.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/index.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/index.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/index.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/index.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/index.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/index.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/index.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/index.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/index.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/index.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/index.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/index.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/index.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/index.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/index.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/index.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/index.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/index.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/index.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/index.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/index.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/index.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/index.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/index.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/index.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/index.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/index.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/index.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/index.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/index.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/index.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/index.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/index.html)

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

Accelerator Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/index.html#accelerator-integration "Link to this heading")

=====================================================================================================================================

Created On: Sep 02, 2025 | Last Updated On: May 18, 2026

Since PyTorch 2.1, the community has made significant progress in streamlining the process of integrating new accelerators into the PyTorch ecosystem. These improvements include, but are not limited to: refinements to the `PrivateUse1` Dispatch Key, the introduction and enhancement of core subsystem extension mechanisms, and the device-agnostic refactoring of key modules (e.g., `torch.accelerator`, `memory management`). Taken together, these advances provide the foundation for a **robust**, **flexible**, and **developer-friendly** pathway for accelerator integration.

Note

This guide is a work in progress. For more details, please refer to the [roadmap](https://github.com/pytorch/pytorch/issues/158917)
.

Why Does This Matter?[#](https://docs.pytorch.org/docs/2.15/accelerator/index.html#why-does-this-matter "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

This integration pathway offers several major benefits:

*   **Speed**: Extensibility is built into all core PyTorch modules. Developers can integrate new accelerators into their downstream codebases independently—without modifying upstream code and without being limited by community review bandwidth.
    
*   **Future-proofing**: This is the default integration path for all future PyTorch features, meaning that as new modules and features are added, they will automatically support scaling to new accelerators if this path is followed.
    
*   **Autonomy**: Vendors maintain full control over their accelerator integration timelines, enabling fast iteration cycles and reducing reliance on upstream coordination.
    

Target Audience[#](https://docs.pytorch.org/docs/2.15/accelerator/index.html#target-audience "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

This document is intended for:

*   **Accelerator Developers** who are integrating accelerator into PyTorch;
    
*   **Advanced PyTorch Users** interested in the inner workings of key modules;
    

About This Document[#](https://docs.pytorch.org/docs/2.15/accelerator/index.html#about-this-document "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

This guide aims to provide a **comprehensive overview of the modern integration pathway** for new accelerator in PyTorch. It walks through the full integration surface, from low-level device primitives to higher-level domain modules like compilation and quantization. The structure follows a **modular and scenario-driven approach**, where each topic is paired with corresponding code examples from [torch\_openreg](https://github.com/pytorch/pytorch/tree/main/test/cpp_extensions/open_registration_extension/torch_openreg "OpenReg URL")
, an official reference implementation, and this series is structured around four major axes:

*   **Runtime**: Covers core components such as Event, Stream, Memory, Generator, Guard, Hooks, as well as the supporting C++ scaffolding.
    
*   **Operators**: Involve the minimum necessary set of operators, forward and backward operators, fallback operators, fallthroughs, STUBs, etc. in both C++ and Python implementations.
    
*   **Python Frontend**: Focuses on Python bindings for modules and device-agnostic APIs.
    
*   **High-level Modules**: Explores integration with major subsystems such as `AMP`, `Compiler`, `ONNX`, and `Distributed` and so on.
    

The goal is to help developers:

*   Understand the full scope of accelerator integration;
    
*   Follow best practices to quickly launch new accelerators;
    
*   Avoid common pitfalls through clear, targeted examples.
    

Next, we will delve into each chapter of this guide. Each chapter focuses on a key aspect of integration, providing detailed explanations and illustrative examples. Since some chapters build upon previous ones, readers are encouraged to follow the sequence to achieve a more coherent understanding.

*   [Device Management](https://docs.pytorch.org/docs/2.15/accelerator/device.html)
    
*   [Accelerator Hooks](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html)
    
*   [Guard](https://docs.pytorch.org/docs/2.15/accelerator/guard.html)
    
*   [Autoload Mechanism](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html)
    
*   [Operator Registration](https://docs.pytorch.org/docs/2.15/accelerator/operators.html)
    
*   [Automatic Mixed Precision](https://docs.pytorch.org/docs/2.15/accelerator/amp.html)
    
*   [Profiler Integration](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html)
    
*   [Distributed Training Integration](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html)
    
*   [CI Integration](https://docs.pytorch.org/docs/2.15/accelerator/ci.html)
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/index.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/index.md.txt)

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