Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.isin.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.isin.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.isin.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.isin.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.isin.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.isin.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.isin.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.isin.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.isin.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.isin.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.isin.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.isin.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.isin.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.isin.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.isin.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.isin.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.isin.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.isin.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.isin.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.isin.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.isin.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.isin.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.isin.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.isin.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.isin.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.isin.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.isin.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.isin.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.isin.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.isin.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.isin.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.isin.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.isin.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.isin.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.isin.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.isin.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.isin.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.isin.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.isin.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.isin.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.isin.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.isin.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.isin.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.isin.html)

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

torch.isin[#](https://docs.pytorch.org/docs/2.15/generated/torch.isin.html#torch-isin "Link to this heading")

==============================================================================================================

torch.isin(_elements_, _test\_elements_, _\*_, _assume\_unique\=False_, _invert\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.isin.html#torch.isin "Link to this definition")

Tests if each element of `elements` is in `test_elements`. Returns a boolean tensor of the same shape as `elements` that is True for elements in `test_elements` and False otherwise.

Note

One of `elements` or `test_elements` can be a scalar, but not both.

Parameters:

*   **elements** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Scalar_) – Input elements
    
*   **test\_elements** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Scalar_) – Values against which to test for each input element
    
*   **assume\_unique** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, assumes both `elements` and `test_elements` contain unique elements, which can speed up the calculation. Default: False
    
*   **invert** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, inverts the boolean return tensor, resulting in True values for elements _not_ in `test_elements`. Default: False
    

Returns:

A boolean tensor of the same shape as `elements` that is True for elements in `test_elements` and False otherwise

Example

\>>> torch.isin(torch.tensor(\[\[1, 2\], \[3, 4\]\]), torch.tensor(\[2, 3\]))
tensor(\[\[False,  True\],\
        \[ True, False\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.isin.rst.txt)

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