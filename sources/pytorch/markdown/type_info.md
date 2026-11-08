Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/type_info.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/type_info.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/type_info.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/type_info.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/type_info.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/type_info.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/type_info.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/type_info.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/type_info.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/type_info.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/type_info.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/type_info.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/type_info.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/type_info.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/type_info.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/type_info.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/type_info.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/type_info.html)
[v1.13](https://docs.pytorch.org/docs/1.13/type_info.html)
[v1.12](https://docs.pytorch.org/docs/1.12/type_info.html)
[v1.11](https://docs.pytorch.org/docs/1.11/type_info.html)
[v1.10](https://docs.pytorch.org/docs/1.10/type_info.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/type_info.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/type_info.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/type_info.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/type_info.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/type_info.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/type_info.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/type_info.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/type_info.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/type_info.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/type_info.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/type_info.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/type_info.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/type_info.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/type_info.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/type_info.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/type_info.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/type_info.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/type_info.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/type_info.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/type_info.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/type_info.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/type_info.html)

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

Type Info[#](https://docs.pytorch.org/docs/2.15/type_info.html#type-info "Link to this heading")

=================================================================================================

Created On: Jun 06, 2025 | Last Updated On: Aug 14, 2025

The numerical properties of a [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 can be accessed through either the [`torch.finfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "torch.torch.finfo")
 or the [`torch.iinfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.iinfo "torch.torch.iinfo")
.

torch.finfo[#](https://docs.pytorch.org/docs/2.15/type_info.html#torch-finfo "Link to this heading")

-----------------------------------------------------------------------------------------------------

_class_ torch.finfo[#](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "Link to this definition")

A [`torch.finfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "torch.torch.finfo")
 is an object that represents the numerical properties of a floating point [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
, (i.e. `torch.float32`, `torch.float64`, `torch.float16`, and `torch.bfloat16`). This is similar to [numpy.finfo](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html)
.

A [`torch.finfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "torch.torch.finfo")
 provides the following attributes:

| Name | Type | Description |
| --- | --- | --- |
| bits | int | The number of bits occupied by the type. |
| eps | float | The difference between 1.0 and the next smallest representable float larger than 1.0. |
| max | float | The largest representable number. |
| min | float | The smallest representable number (typically `-max`). |
| tiny | float | The smallest positive normal number. Equivalent to `smallest_normal`. |
| smallest\_normal | float | The smallest positive normal number. See notes. |
| resolution | float | The approximate decimal resolution of this type, i.e., `10**-precision`. |

Note

The constructor of [`torch.finfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.finfo "torch.torch.finfo")
 can be called without argument, in which case the class is created for the pytorch default dtype (as returned by [`torch.get_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.get_default_dtype.html#torch.get_default_dtype "torch.get_default_dtype")
).

Note

`smallest_normal` returns the smallest _normal_ number, but there are smaller subnormal numbers. See https://en.wikipedia.org/wiki/Denormal\_number for more information.

torch.iinfo[#](https://docs.pytorch.org/docs/2.15/type_info.html#torch-iinfo "Link to this heading")

-----------------------------------------------------------------------------------------------------

_class_ torch.iinfo[#](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.iinfo "Link to this definition")

A [`torch.iinfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.iinfo "torch.torch.iinfo")
 is an object that represents the numerical properties of a integer [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 (i.e. `torch.uint8`, `torch.int8`, `torch.int16`, `torch.int32`, and `torch.int64`). This is similar to [numpy.iinfo](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html)
.

A [`torch.iinfo`](https://docs.pytorch.org/docs/2.15/type_info.html#torch.torch.iinfo "torch.torch.iinfo")
 provides the following attributes:

| Name | Type | Description |
| --- | --- | --- |
| bits | int | The number of bits occupied by the type. |
| max | int | The largest representable number. |
| min | int | The smallest representable number. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/type_info.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/type_info.md.txt)

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