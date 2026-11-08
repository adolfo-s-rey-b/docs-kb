Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/module_tracker.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/module_tracker.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/module_tracker.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/module_tracker.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/module_tracker.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/module_tracker.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/module_tracker.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/module_tracker.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/module_tracker.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/module_tracker.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/module_tracker.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/module_tracker.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/module_tracker.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/module_tracker.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/module_tracker.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/module_tracker.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/module_tracker.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/module_tracker.html)
[v1.13](https://docs.pytorch.org/docs/1.13/module_tracker.html)
[v1.12](https://docs.pytorch.org/docs/1.12/module_tracker.html)
[v1.11](https://docs.pytorch.org/docs/1.11/module_tracker.html)
[v1.10](https://docs.pytorch.org/docs/1.10/module_tracker.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/module_tracker.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/module_tracker.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/module_tracker.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/module_tracker.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/module_tracker.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/module_tracker.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/module_tracker.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/module_tracker.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/module_tracker.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/module_tracker.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/module_tracker.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/module_tracker.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/module_tracker.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/module_tracker.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/module_tracker.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/module_tracker.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/module_tracker.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/module_tracker.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/module_tracker.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/module_tracker.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/module_tracker.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/module_tracker.html)

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

torch.utils.module\_tracker[#](https://docs.pytorch.org/docs/2.15/module_tracker.html#module-torch.utils.module_tracker "Link to this heading")

================================================================================================================================================

Created On: May 04, 2024 | Last Updated On: Jun 11, 2025

This utility can be used to track the current position inside an [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 hierarchy. It can be used within other tracking tools to be able to easily associate measured quantities to user-friendly names. This is used in particular in the FlopCounterMode today.

_class_ torch.utils.module\_tracker.ModuleTracker[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/module_tracker.py#L25)
[#](https://docs.pytorch.org/docs/2.15/module_tracker.html#torch.utils.module_tracker.ModuleTracker "Link to this definition")

`ModuleTracker` is a context manager that tracks the nn.Module hierarchy during execution so that other system can query which Module is currently being executed (or its backward is being executed).

You can access the `parents` attribute on this context manager to get the set of all the Modules currently being executed via their fqn (fully qualified name, also used as the key within the state\_dict). You can access the `is_bw` attribute to know if you are currently running in backward or not.

Note that `parents` is never empty and always contains the “Global” key. The `is_bw` flag will remain `True` after the forward until another Module is executed. If you need it to be more accurate, please submit an issue requesting this. Adding a map from fqn to the module instance is possible but not done yet, please submit an issue requesting this if you need it.

Example usage

mod \= torch.nn.Linear(2, 2)

with ModuleTracker() as tracker:
    \# Access anything during the forward pass
    def my\_linear(m1, m2, bias):
        print(f"Current modules: {tracker.parents}")
        return torch.mm(m1, m2.t()) + bias

    torch.nn.functional.linear \= my\_linear

    mod(torch.rand(2, 2))

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/module_tracker.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/module_tracker.md.txt)

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