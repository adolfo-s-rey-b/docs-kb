Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.set_default_device.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.set_default_device.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.set_default_device.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.set_default_device.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.set_default_device.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.set_default_device.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.set_default_device.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.set_default_device.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.set_default_device.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.set_default_device.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.set_default_device.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.set_default_device.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.set_default_device.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.set_default_device.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.set_default_device.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.set_default_device.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.set_default_device.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.set_default_device.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.set_default_device.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.set_default_device.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.set_default_device.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.set_default_device.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.set_default_device.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.set_default_device.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.set_default_device.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.set_default_device.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.set_default_device.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.set_default_device.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.set_default_device.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.set_default_device.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.set_default_device.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.set_default_device.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.set_default_device.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.set_default_device.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.set_default_device.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.set_default_device.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.set_default_device.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.set_default_device.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.set_default_device.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.set_default_device.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.set_default_device.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.set_default_device.html)

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

torch.set\_default\_device[#](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch-set-default-device "Link to this heading")

==========================================================================================================================================================

torch.set\_default\_device(_device_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1617)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "Link to this definition")

Sets the default `torch.Tensor` to be allocated on `device`. This does not affect factory function calls which are called with an explicit `device` argument. Factory calls will be performed as if they were passed `device` as an argument.

To only temporarily change the default device instead of setting it globally, use `with torch.device(device):` instead.

The default device is initially `cpu`. If you set the default tensor device to another device (e.g., `cuda`) without a device index, tensors will be allocated on whatever the current device for the device type, even after [`torch.cuda.set_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_device.html#torch.cuda.set_device "torch.cuda.set_device")
 is called.

Warning

This function imposes a slight performance cost on every Python call to the torch API (not just factory functions). If this is causing problems for you, please comment on [pytorch/pytorch#92701](https://github.com/pytorch/pytorch/issues/92701)

Note

This doesn’t affect functions that create tensors that share the same memory as the input, like: [`torch.from_numpy()`](https://docs.pytorch.org/docs/2.15/generated/torch.from_numpy.html#torch.from_numpy "torch.from_numpy")
 and [`torch.frombuffer()`](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html#torch.frombuffer "torch.frombuffer")

Parameters:

**device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
, str, int, or None) – the device to set as default, or `None` to clear the override. An integer is interpreted as an index for the current accelerator.

Example:

\>>> torch.get\_default\_device()
device(type='cpu')
\>>> torch.set\_default\_device('cuda')  \# current device is 0
\>>> torch.get\_default\_device()
device(type='cuda', index=0)
\>>> torch.set\_default\_device('cuda')
\>>> torch.cuda.set\_device('cuda:1')  \# current device is 1
\>>> torch.get\_default\_device()
device(type='cuda', index=1)
\>>> torch.set\_default\_device('cuda:1')
\>>> torch.get\_default\_device()
device(type='cuda', index=1)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.set_default_device.rst.txt)

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