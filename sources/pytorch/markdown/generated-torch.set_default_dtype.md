Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.set_default_dtype.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.set_default_dtype.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.set_default_dtype.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.set_default_dtype.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.set_default_dtype.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.set_default_dtype.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.set_default_dtype.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.set_default_dtype.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.set_default_dtype.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.set_default_dtype.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.set_default_dtype.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.set_default_dtype.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.set_default_dtype.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.set_default_dtype.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.set_default_dtype.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.set_default_dtype.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.set_default_dtype.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.set_default_dtype.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.set_default_dtype.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.set_default_dtype.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.set_default_dtype.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.set_default_dtype.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.set_default_dtype.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.set_default_dtype.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.set_default_dtype.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.set_default_dtype.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.set_default_dtype.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.set_default_dtype.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.set_default_dtype.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.set_default_dtype.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.set_default_dtype.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.set_default_dtype.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.set_default_dtype.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.set_default_dtype.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.set_default_dtype.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.set_default_dtype.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.set_default_dtype.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.set_default_dtype.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.set_default_dtype.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.set_default_dtype.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.set_default_dtype.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.set_default_dtype.html)

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

torch.set\_default\_dtype[#](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch-set-default-dtype "Link to this heading")

=======================================================================================================================================================

torch.set\_default\_dtype(_d_, _/_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1712)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "Link to this definition")

Sets the default floating point dtype to `d`. Supports floating point dtype as inputs. Other dtypes will cause torch to raise an exception.

When PyTorch is initialized its default floating point dtype is torch.float32, and the intent of set\_default\_dtype(torch.float64) is to facilitate NumPy-like type inference. The default floating point dtype is used to:

1.  Implicitly determine the default complex dtype. When the default floating type is float16, the default complex dtype is complex32. For float32, the default complex dtype is complex64. For float64, it is complex128. For bfloat16, an exception will be raised because there is no corresponding complex type for bfloat16.
    
2.  Infer the dtype for tensors constructed using Python floats or complex Python numbers. See examples below.
    
3.  Determine the result of type promotion between bool and integer tensors and Python floats and complex Python numbers.
    

Parameters:

**d** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
) – the floating point dtype to make the default.

Example

\>>> \# initial default for floating point is torch.float32
\>>> \# Python floats are interpreted as float32
\>>> torch.tensor(\[1.2, 3\]).dtype
torch.float32
\>>> \# initial default for floating point is torch.complex64
\>>> \# Complex Python numbers are interpreted as complex64
\>>> torch.tensor(\[1.2, 3j\]).dtype
torch.complex64

Copy to clipboard

\>>> torch.set\_default\_dtype(torch.float64)
\>>> \# Python floats are now interpreted as float64
\>>> torch.tensor(\[1.2, 3\]).dtype  \# a new floating point tensor
torch.float64
\>>> \# Complex Python numbers are now interpreted as complex128
\>>> torch.tensor(\[1.2, 3j\]).dtype  \# a new complex tensor
torch.complex128

Copy to clipboard

\>>> torch.set\_default\_dtype(torch.float16)
\>>> \# Python floats are now interpreted as float16
\>>> torch.tensor(\[1.2, 3\]).dtype  \# a new floating point tensor
torch.float16
\>>> \# Complex Python numbers are now interpreted as complex128
\>>> torch.tensor(\[1.2, 3j\]).dtype  \# a new complex tensor
torch.complex32

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.set_default_dtype.rst.txt)

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