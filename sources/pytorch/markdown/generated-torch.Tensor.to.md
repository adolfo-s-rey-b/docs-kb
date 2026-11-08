Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.to.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.to.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.to.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.to.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.to.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.to.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.to.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.to.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.to.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.to.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.to.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.to.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.to.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.to.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.to.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.to.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.to.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.to.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.to.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.to.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.to.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.to.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.to.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.to.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.to.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.to.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.to.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.to.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.to.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.to.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.to.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.to.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.to.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.to.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.to.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.to.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.to.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.to.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.to.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.to.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.to.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.to.html)

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

torch.Tensor.to[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch-tensor-to "Link to this heading")

=============================================================================================================================

Tensor.to(_\*args_, _\*\*kwargs_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch.Tensor.to "Link to this definition")

Performs Tensor dtype and/or device conversion. A [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 and [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 are inferred from the arguments of `self.to(*args, **kwargs)`.

Note

If the `self` Tensor already has the correct [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 and [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
, then `self` is returned. Otherwise, the returned tensor is a copy of `self` with the desired [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 and [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
.

Note

If `self` requires gradients (`requires_grad=True`) but the target `dtype` specified is an integer type, the returned tensor will implicitly set `requires_grad=False`. This is because only tensors with floating-point or complex dtypes can require gradients.

Here are the ways to call `to`:

to(_dtype_, _non\_blocking\=False_, _copy\=False_, _memory\_format\=torch.preserve\_format_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

> Returns a Tensor with the specified [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
> 
> Args:
> 
> memory\_format ([`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
> , optional): the desired memory format of returned Tensor. Default: `torch.preserve_format`.

Note

According to [C++ type conversion rules](https://en.cppreference.com/w/cpp/language/implicit_conversion.html)
, converting floating point value to integer type will truncate the fractional part. If the truncated value cannot fit into the target type (e.g., casting `torch.inf` to `torch.long`), the behavior is undefined and the result may vary across platforms.

torch.to(_device\=None_, _dtype\=None_, _non\_blocking\=False_, _copy\=False_, _memory\_format\=torch.preserve\_format_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

> Returns a Tensor with the specified [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
>  and (optional) [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
> . If [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
>  is `None` it is inferred to be `self.dtype`. When `non_blocking` is set to `True`, the function attempts to perform the conversion asynchronously with respect to the host, if possible. This asynchronous behavior applies to both pinned and pageable memory. However, caution is advised when using this feature. For more information, refer to the [tutorial on good usage of non\_blocking and pin\_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html)
> . When `copy` is set, a new Tensor is created even when the Tensor already matches the desired conversion.
> 
> Args:
> 
> memory\_format ([`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
> , optional): the desired memory format of returned Tensor. Default: `torch.preserve_format`.

torch.to(_other_, _non\_blocking\=False_, _copy\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

> Returns a Tensor with same [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
>  and [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
>  as the Tensor `other`. When `non_blocking` is set to `True`, the function attempts to perform the conversion asynchronously with respect to the host, if possible. This asynchronous behavior applies to both pinned and pageable memory. However, caution is advised when using this feature. For more information, refer to the [tutorial on good usage of non\_blocking and pin\_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html)
> . When `copy` is set, a new Tensor is created even when the Tensor already matches the desired conversion.

Note

When `non_blocking` is `True` and the conversion is issued on a non-default CUDA stream, the caller is responsible for proper cross-stream synchronization. See [CUDA streams](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-stream-semantics)
 for the required pattern.

Example:

\>>> tensor \= torch.randn(2, 2)  \# Initially dtype=float32, device=cpu
\>>> tensor.to(torch.float64)
tensor(\[\[-0.5044,  0.0005\],\
        \[ 0.3310, -0.0584\]\], dtype=torch.float64)

\>>> cuda0 \= torch.device('cuda:0')
\>>> tensor.to(cuda0)
tensor(\[\[-0.5044,  0.0005\],\
        \[ 0.3310, -0.0584\]\], device='cuda:0')

\>>> tensor.to(cuda0, dtype\=torch.float64)
tensor(\[\[-0.5044,  0.0005\],\
        \[ 0.3310, -0.0584\]\], dtype=torch.float64, device='cuda:0')

\>>> other \= torch.randn((), dtype\=torch.float64, device\=cuda0)
\>>> tensor.to(other, non\_blocking\=True)
tensor(\[\[-0.5044,  0.0005\],\
        \[ 0.3310, -0.0584\]\], dtype=torch.float64, device='cuda:0')

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.to.rst.txt)

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