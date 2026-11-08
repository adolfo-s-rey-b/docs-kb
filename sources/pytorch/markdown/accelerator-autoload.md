Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/autoload.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/autoload.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/autoload.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/autoload.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/autoload.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/autoload.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/autoload.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/autoload.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/autoload.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/autoload.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/autoload.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/autoload.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/autoload.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/autoload.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/autoload.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/autoload.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/autoload.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/autoload.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/autoload.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/autoload.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/autoload.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/autoload.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/autoload.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/autoload.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/autoload.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/autoload.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/autoload.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/autoload.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/autoload.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/autoload.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/autoload.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/autoload.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/autoload.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/autoload.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/autoload.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/autoload.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/autoload.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/autoload.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/autoload.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/autoload.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/autoload.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/autoload.html)

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

Autoload Mechanism[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#autoload-mechanism "Link to this heading")

==============================================================================================================================

Created On: Sep 12, 2025 | Last Updated On: Sep 20, 2026

The **Autoload** mechanism in PyTorch simplifies the integration of a custom backend by enabling automatic discovery and initialization at runtime. This eliminates the need for explicit imports or manual initialization, allowing developers to seamlessly integrate a new accelerator or backend into PyTorch.

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#background "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The **Autoload Device Extension** proposal in PyTorch is centered on improving support for various hardware backend devices, especially those implemented as out-of-the-tree extensions (not part of PyTorch’s main codebase). Currently, users must manually import or load these device-specific extensions to use them, which complicates the experience and increases cognitive overhead.

In contrast, in-tree devices (devices officially supported within PyTorch) are seamlessly integrated—users don’t need extra imports or steps. The goal of autoloading is to make out-of-the-tree devices just as easy to use, so users can follow the standard PyTorch device programming model without explicit loading or code changes. This would allow existing PyTorch applications to run on new devices without any modification, making hardware support more user-friendly and reducing barriers to adoption.

For more information about the background of **Autoload**, please refer to its [RFC](https://github.com/pytorch/pytorch/issues/122468)
.

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#design "Link to this heading")

------------------------------------------------------------------------------------------------------

The core idea of **Autoload** is to Use Python’s plugin discovery (entry points) so PyTorch automatically loads out-of-tree device extensions when torch is imported—no explicit user import needed.

For more instructions of the design of **Autoload**, please refer to [**How it works**](https://docs.pytorch.org/tutorials/unstable/python_extension_autoload.html#how-it-works)
.

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#implementation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

This tutorial will take **OpenReg** as a new out-of-the-tree device and guide you through the steps to enable and use the **Autoload** mechanism.

### Entry Point Setup[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#entry-point-setup "Link to this heading")

To enable **Autoload**, register the `_autoload` function as an entry point in [setup.py](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/setup.py)
 file.

 Python

 1    setup(
 2        packages\=find\_packages(),
 3        package\_data\=package\_data,
 4        ext\_modules\=ext\_modules,
 5        cmdclass\={
 6            "clean": BuildClean,  \# type: ignore\[misc\]
 7        },
 8        include\_package\_data\=False,
 9        entry\_points\={
10            "torch.backends": \[\
11                "torch\_openreg = torch\_openreg:\_autoload",\
12            \],
13        },
14    )

Copy to clipboard

### Backend Setup[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#backend-setup "Link to this heading")

Define the initialization hook `_autoload` for backend initialization in [torch\_openreg](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/torch_openreg/__init__.py)
. This hook will be automatically invoked by PyTorch during startup.

 PYTHON

1def \_autoload():
2    \# It is a placeholder function here to be registered as an entry point.
3    pass
4
5

Copy to clipboard

### Lazy Inductor Backend Initialization[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#lazy-inductor-backend-initialization "Link to this heading")

Integrating with torch.compile typically means registering device-specific codegen classes, decompositions, and passes with Inductor. Doing all of that inside `_autoload` would make every user pay the cost at `import torch`, even those who never compile. To defer it, define an `_inductor_backend_init` method on the device module class passed to `torch._register_device_module`: a no-arg callable that Inductor invokes at the first Inductor compilation, on every entry point (`torch.compile`, direct `compile_fx()`, and AOTInductor), and again on later compilations until it has registered the device. Until registration succeeds, backend-feature queries may invoke the hook multiple times within one compilation, so the hook must be safe and cheap to retry. Inductor looks it up with a plain attribute lookup, so it works the same whether the device module is a class (methods, as below) or a module object (attribute assignment).

from torch.\_inductor.codegen.common import register\_backend\_for\_device

class MyDeviceModule:
    \# ... other device module APIs (is\_available, device\_count, ...)

    @staticmethod
    def \_inductor\_backend\_init():
        \# Runs on the first inductor compile, not at import time.
        from my\_backend.\_inductor import MyCppWrapperCodegen, MyScheduling, MyWrapperCodegen

        register\_backend\_for\_device(
            "my\_device", MyScheduling, MyWrapperCodegen, MyCppWrapperCodegen
        )
        \# May also register decompositions, device op overrides, and custom passes.

torch.utils.rename\_privateuse1\_backend("my\_device")
torch.\_register\_device\_module("my\_device", MyDeviceModule)

Copy to clipboard

The hook must call `register_backend_for_device` itself; that registration is what stops Inductor from invoking the hook again on later compilations. Concurrent callers wait for an in-flight hook invocation to finish. Because the hook runs under Dynamo’s compile lock, it must not wait on another thread that may import the same integration or invoke `torch.compile`, and it should not fork. If the hook raises, the exception propagates out of the compile, and the hook is invoked again on the next compile unless it registered the device before raising. Note that the hook is not gated on the compiled device: while the device is unregistered it fires on every Inductor compile, whichever device that graph targets. On the `compile_fx` paths, the hook runs before that compilation selects its decomposition table.

Device modules that instead expose `Scheduling`, `PythonWrapperCodegen`, and `CppWrapperCodegen` attributes directly are still supported, but that form imports the codegen classes eagerly at `import torch`. A device that is already registered (for example eagerly from `_autoload`) skips the hook entirely.

A backend that keeps its options in a `ConfigModule` can expose them through `torch.compile(options=...)`: register the module as `device_custom_config`, and its keys become addressable as `"<device>.<key>"` options. The values are patched onto the owning module for the duration of the compilation, instead of `torch._inductor.config`.

register\_backend\_for\_device(
    "my\_device",
    MyScheduling,
    MyWrapperCodegen,
    MyCppWrapperCodegen,
    device\_custom\_config\=my\_backend\_config,
)

torch.compile(model, options\={"my\_device.my\_config\_key": 1})

Copy to clipboard

Result[#](https://docs.pytorch.org/docs/2.15/accelerator/autoload.html#result "Link to this heading")

------------------------------------------------------------------------------------------------------

After setting up the entry point and backend, build and install your backend. Now, we can use the new accelerator without explicitly importing it.

Without Autoload

\>>> import torch
\>>> import torch\_openreg
\>>> torch.tensor(1, device\="openreg")
tensor(1, device='openreg:0')

Copy to clipboard

With Autoload

\>>> import torch \# Automatically import torch\_openreg
\>>>
\>>> torch.tensor(1, device\="openreg")
tensor(1, device='openreg:0')

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/autoload.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/autoload.md.txt)

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