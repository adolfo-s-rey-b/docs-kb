Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.from_dlpack.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.from_dlpack.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.from_dlpack.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.from_dlpack.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.from_dlpack.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.from_dlpack.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.from_dlpack.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.from_dlpack.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.from_dlpack.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.from_dlpack.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.from_dlpack.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.from_dlpack.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.from_dlpack.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.from_dlpack.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.from_dlpack.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.from_dlpack.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.from_dlpack.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.from_dlpack.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.from_dlpack.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.from_dlpack.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.from_dlpack.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.from_dlpack.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.from_dlpack.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.from_dlpack.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.from_dlpack.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.from_dlpack.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.from_dlpack.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.from_dlpack.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.from_dlpack.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.from_dlpack.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.from_dlpack.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.from_dlpack.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.from_dlpack.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.from_dlpack.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.from_dlpack.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.from_dlpack.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.from_dlpack.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.from_dlpack.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.from_dlpack.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.from_dlpack.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.from_dlpack.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.from_dlpack.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.from_dlpack.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.from_dlpack.html)

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

torch.from\_dlpack[#](https://docs.pytorch.org/docs/2.15/generated/torch.from_dlpack.html#torch-from-dlpack "Link to this heading")

====================================================================================================================================

torch.from\_dlpack(_ext\_tensor_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/dlpack.py#L124)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.from_dlpack.html#torch.from_dlpack "Link to this definition")

Converts a tensor from an external library into a `torch.Tensor`.

The returned PyTorch tensor will share the memory with the input tensor (which may have come from another library). Note that in-place operations will therefore also affect the data of the input tensor. This may lead to unexpected issues (e.g., other libraries may have read-only flags or immutable data structures), so the user should only do this if they know for sure that this is fine.

Parameters:

*   **ext\_tensor** (object with `__dlpack__` attribute, or a DLPack capsule) –
    
    The tensor or DLPack capsule to convert.
    
    If `ext_tensor` is a tensor (or ndarray) object, it must support the `__dlpack__` protocol (i.e., have a `ext_tensor.__dlpack__` method). Otherwise `ext_tensor` may be a DLPack capsule, which is an opaque `PyCapsule` instance, typically produced by a `to_dlpack` function or method.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ _None_) – An optional PyTorch device specifying where to place the new tensor. If None (default), the new tensor will be on the same device as `ext_tensor`.
    
*   **copy** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _or_ _None_) – An optional boolean indicating whether or not to copy `self`. If None, PyTorch will copy only if necessary.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples:

\>>> import torch.utils.dlpack
\>>> t \= torch.arange(4)

\# Convert a tensor directly (supported in PyTorch >= 1.10)
\>>> t2 \= torch.from\_dlpack(t)
\>>> t2\[:2\] \= \-1  \# show that memory is shared
\>>> t2
tensor(\[-1, -1,  2,  3\])
\>>> t
tensor(\[-1, -1,  2,  3\])

\# The old-style DLPack usage, with an intermediate capsule object
\>>> capsule \= torch.utils.dlpack.to\_dlpack(t)
\>>> capsule
<capsule object "dltensor" at ...>
\>>> t3 \= torch.from\_dlpack(capsule)
\>>> t3
tensor(\[-1, -1,  2,  3\])
\>>> t3\[0\] \= \-9  \# now we're sharing memory between 3 tensors
\>>> t3
tensor(\[-9, -1,  2,  3\])
\>>> t2
tensor(\[-9, -1,  2,  3\])
\>>> t
tensor(\[-9, -1,  2,  3\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.from_dlpack.rst.txt)

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