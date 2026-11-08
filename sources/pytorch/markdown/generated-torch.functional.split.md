Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.split.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.split.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.split.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.split.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.split.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.split.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.split.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.split.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.split.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.split.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.split.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.split.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.split.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.split.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.split.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.split.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.split.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.split.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.split.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.split.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.split.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.split.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.split.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.split.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.split.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.split.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.split.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.split.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.split.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.split.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.split.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.split.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.split.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.split.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.split.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.split.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.split.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.split.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.split.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.split.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.split.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.split.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.split.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.split.html)

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

torch.functional.split[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.split.html#torch-functional-split "Link to this heading")

==================================================================================================================================================

torch.functional.split(_tensor_, _split\_size\_or\_sections_, _dim\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L120)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.split.html#torch.functional.split "Link to this definition")

Splits the tensor into chunks. Each chunk is a view of the original tensor.

If `split_size_or_sections` is an integer type, then `tensor` will be split into equally sized chunks (if possible). Last chunk will be smaller if the tensor size along the given dimension `dim` is not divisible by `split_size`.

If `split_size_or_sections` is a list, then `tensor` will be split into `len(split_size_or_sections)` chunks with sizes in `dim` according to `split_size_or_sections`.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – tensor to split.
    
*   **split\_size\_or\_sections** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _) or_ _(_[_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _(_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _)_) – size of a single chunk or list of sizes for each chunk
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – dimension along which to split the tensor.
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, …\]

Example:

\>>> a \= torch.arange(10).reshape(5, 2)
\>>> a
tensor(\[\[0, 1\],\
        \[2, 3\],\
        \[4, 5\],\
        \[6, 7\],\
        \[8, 9\]\])
\>>> torch.split(a, 2)
(tensor(\[\[0, 1\],\
         \[2, 3\]\]),
 tensor(\[\[4, 5\],\
         \[6, 7\]\]),
 tensor(\[\[8, 9\]\]))
\>>> torch.split(a, \[1, 4\])
(tensor(\[\[0, 1\]\]),
 tensor(\[\[2, 3\],\
         \[4, 5\],\
         \[6, 7\],\
         \[8, 9\]\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.split.rst.txt)

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