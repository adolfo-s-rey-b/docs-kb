Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/future_mod.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/future_mod.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/future_mod.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/future_mod.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/future_mod.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/future_mod.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/future_mod.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/future_mod.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/future_mod.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/future_mod.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/future_mod.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/future_mod.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/future_mod.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/future_mod.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/future_mod.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/future_mod.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/future_mod.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/future_mod.html)
[v1.13](https://docs.pytorch.org/docs/1.13/future_mod.html)
[v1.12](https://docs.pytorch.org/docs/1.12/future_mod.html)
[v1.11](https://docs.pytorch.org/docs/1.11/future_mod.html)
[v1.10](https://docs.pytorch.org/docs/1.10/future_mod.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/future_mod.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/future_mod.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/future_mod.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/future_mod.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/future_mod.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/future_mod.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/future_mod.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/future_mod.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/future_mod.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/future_mod.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/future_mod.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/future_mod.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/future_mod.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/future_mod.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/future_mod.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/future_mod.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/future_mod.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/future_mod.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/future_mod.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/future_mod.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/future_mod.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/future_mod.html)

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

torch.\_\_future\_\_[#](https://docs.pytorch.org/docs/2.15/future_mod.html#module-torch.__future__ "Link to this heading")

===========================================================================================================================

Created On: Feb 05, 2024 | Last Updated On: Jun 12, 2025

torch.\_\_future\_\_.set\_overwrite\_module\_params\_on\_conversion(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__future__.py#L5)
[#](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.set_overwrite_module_params_on_conversion "Link to this definition")

Sets whether to assign new tensors to the parameters instead of changing the existing parameters in-place when converting an `nn.Module`.

When enabled, the following methods will assign new parameters to the module:

1.  `module.{device}()` (e.g. `nn.Module.cuda()`) for moving a module between devices
    
2.  `module.{dtype}()` (e.g. `nn.Module.float()`) for converting a module to a different dtype
    
3.  `nn.Module.to()`
    
4.  `nn.Module.to_empty()`
    

Parameters:

**value** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether to assign new tensors or not.

torch.\_\_future\_\_.get\_overwrite\_module\_params\_on\_conversion()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__future__.py#L25)
[#](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.get_overwrite_module_params_on_conversion "Link to this definition")

Returns whether to assign new tensors to the parameters instead of changing the existing parameters in-place when converting an [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
. Defaults to `False`.

See [`set_overwrite_module_params_on_conversion()`](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.set_overwrite_module_params_on_conversion "torch.__future__.set_overwrite_module_params_on_conversion")
 for more information.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.\_\_future\_\_.set\_swap\_module\_params\_on\_conversion(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__future__.py#L35)
[#](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.set_swap_module_params_on_conversion "Link to this definition")

Sets whether to use [`swap_tensors()`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors "torch.utils.swap_tensors")
 instead of setting `.data` to change the existing parameters in-place when converting an `nn.Module` and instead of `param.copy_(state_dict[key])` when loading a state dict into an `nn.Module`.

Note

This function takes precedence over [`get_overwrite_module_params_on_conversion()`](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.get_overwrite_module_params_on_conversion "torch.__future__.get_overwrite_module_params_on_conversion")

When enabled, the following methods will swap the existing parameters in-place:

1.  `module.{device}()` (e.g. `nn.Module.cuda()`) for moving a module between devices
    
2.  `module.{dtype}()` (e.g. `nn.Module.float()`) for converting a module to a different dtype
    
3.  `nn.Module.to()`
    
4.  `nn.Module.to_empty()`
    
5.  `nn.Module.load_state_dict()`
    

The semantics for `load_state_dict()` when this is set are as follows:

1.  For each parameter/buffer, its corresponding `state_dict['key']` is transformed via [`module_load()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.module_load.html#torch.Tensor.module_load "torch.Tensor.module_load")
     (i.e. `res = param.module_load(state_dict['key'])`)
    
2.  If necessary, `res` will be wrapped in an `Parameter`
    
3.  The parameter/buffer in the module will be swapped via [`swap_tensors()`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors "torch.utils.swap_tensors")
     with `res`
    

Parameters:

**value** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether to use [`swap_tensors()`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors "torch.utils.swap_tensors")
 or not.

torch.\_\_future\_\_.get\_swap\_module\_params\_on\_conversion()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__future__.py#L68)
[#](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "Link to this definition")

Returns whether to use [`swap_tensors()`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors "torch.utils.swap_tensors")
 instead of setting .data to change the existing parameters in-place when converting an `nn.Module`. Defaults to `False`.

See [`set_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.set_swap_module_params_on_conversion "torch.__future__.set_swap_module_params_on_conversion")
 for more information.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/future_mod.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/future_mod.md.txt)

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