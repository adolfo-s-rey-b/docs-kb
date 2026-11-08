Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/meta.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/meta.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/meta.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/meta.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/meta.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/meta.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/meta.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/meta.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/meta.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/meta.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/meta.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/meta.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/meta.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/meta.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/meta.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/meta.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/meta.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/meta.html)
[v1.13](https://docs.pytorch.org/docs/1.13/meta.html)
[v1.12](https://docs.pytorch.org/docs/1.12/meta.html)
[v1.11](https://docs.pytorch.org/docs/1.11/meta.html)
[v1.10](https://docs.pytorch.org/docs/1.10/meta.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/meta.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/meta.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/meta.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/meta.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/meta.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/meta.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/meta.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/meta.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/meta.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/meta.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/meta.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/meta.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/meta.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/meta.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/meta.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/meta.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/meta.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/meta.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/meta.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/meta.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/meta.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/meta.html)

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

Meta device[#](https://docs.pytorch.org/docs/2.15/meta.html#meta-device "Link to this heading")

================================================================================================

Created On: Jun 17, 2025 | Last Updated On: Jun 17, 2025

The “meta” device is an abstract device which denotes a tensor which records only metadata, but no actual data. Meta tensors have two primary use cases:

*   Models can be loaded on the meta device, allowing you to load a representation of the model without actually loading the actual parameters into memory. This can be helpful if you need to make transformations on the model before you load the actual data.
    
*   Most operations can be performed on meta tensors, producing new meta tensors that describe what the result would have been if you performed the operation on a real tensor. You can use this to perform abstract analysis without needing to spend time on compute or space to represent the actual tensors. Because meta tensors do not have real data, you cannot perform data-dependent operations like [`torch.nonzero()`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero")
     or [`item()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.item.html#torch.Tensor.item "torch.Tensor.item")
    . In some cases, not all device types (e.g., CPU and CUDA) have exactly the same output metadata for an operation; we typically prefer representing the CUDA behavior faithfully in this situation.
    

Warning

Although in principle meta tensor computation should always be faster than an equivalent CPU/CUDA computation, many meta tensor implementations are implemented in Python and have not been ported to C++ for speed, so you may find that you get lower absolute framework latency with small CPU tensors.

Idioms for working with meta tensors[#](https://docs.pytorch.org/docs/2.15/meta.html#idioms-for-working-with-meta-tensors "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

An object can be loaded with [`torch.load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
 onto meta device by specifying `map_location='meta'`:

\>>> torch.save(torch.randn(2), 'foo.pt')
\>>> torch.load('foo.pt', map\_location\='meta')
tensor(..., device='meta', size=(2,))

Copy to clipboard

If you have some arbitrary code which performs some tensor construction without explicitly specifying a device, you can override it to instead construct on meta device by using the [`torch.device()`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 context manager:

\>>> with torch.device('meta'):
...     print(torch.randn(30, 30))
...
tensor(..., device='meta', size=(30, 30))

Copy to clipboard

This is especially helpful NN module construction, where you often are not able to explicitly pass in a device for initialization:

\>>> from torch.nn.modules import Linear
\>>> with torch.device('meta'):
...     print(Linear(20, 30))
...
Linear(in\_features=20, out\_features=30, bias=True)

Copy to clipboard

You cannot convert a meta tensor directly to a CPU/CUDA tensor, because the meta tensor stores no data and we do not know what the correct data values for your new tensor are:

\>>> torch.ones(5, device\='meta').to("cpu")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: Cannot copy out of meta tensor; no data!

Copy to clipboard

Use a factory function like [`torch.empty_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_like.html#torch.empty_like "torch.empty_like")
 to explicitly specify how you would like the missing data to be filled in.

NN modules have a convenience method [`torch.nn.Module.to_empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.to_empty "torch.nn.Module.to_empty")
 that allows you to move the module to another device, leaving all parameters uninitialized. You are expected to explicitly reinitialize the parameters manually:

\>>> from torch.nn.modules import Linear
\>>> with torch.device('meta'):
...     m \= Linear(20, 30)
\>>> m.to\_empty(device\="cpu")
Linear(in\_features=20, out\_features=30, bias=True)

Copy to clipboard

`torch._subclasses.meta_utils` contains undocumented utilities for taking an arbitrary Tensor and constructing an equivalent meta Tensor with high fidelity. These APIs are experimental and may be changed in a BC breaking way at any time.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/meta.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/meta.md.txt)

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