Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.argsort.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.argsort.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.argsort.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.argsort.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.argsort.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.argsort.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.argsort.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.argsort.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.argsort.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.argsort.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.argsort.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.argsort.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.argsort.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.argsort.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.argsort.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.argsort.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.argsort.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.argsort.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.argsort.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.argsort.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.argsort.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.argsort.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.argsort.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.argsort.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.argsort.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.argsort.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.argsort.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.argsort.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.argsort.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.argsort.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.argsort.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.argsort.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.argsort.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.argsort.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.argsort.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.argsort.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.argsort.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.argsort.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.argsort.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.argsort.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.argsort.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.argsort.html)

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

torch.argsort[#](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html#torch-argsort "Link to this heading")

=======================================================================================================================

torch.argsort(_input_, _dim\=\-1_, _descending\=False_, _\*_, _stable\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html#torch.argsort "Link to this definition")

Returns the indices that sort a tensor along a given dimension in ascending order by value.

This is the second value returned by [`torch.sort()`](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#torch.sort "torch.sort")
. See its documentation for the exact semantics of this method.

If `stable` is `True` then the sorting routine becomes stable, preserving the order of equivalent elements. If `False`, the relative order of values which compare equal is not guaranteed. `True` is slower.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to sort along
    
*   **descending** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls the sorting order (ascending or descending)
    

Keyword Arguments:

**stable** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_,_ _optional_) – controls the relative order of equivalent elements

Example:

\>>> a \= torch.randn(4, 4)
\>>> a
tensor(\[\[ 0.0785,  1.5267, -0.8521,  0.4065\],\
        \[ 0.1598,  0.0788, -0.0745, -1.2700\],\
        \[ 1.2208,  1.0722, -0.7064,  1.2564\],\
        \[ 0.0669, -0.2318, -0.8229, -0.9280\]\])

\>>> torch.argsort(a, dim\=1)
tensor(\[\[2, 0, 3, 1\],\
        \[3, 2, 1, 0\],\
        \[2, 1, 0, 3\],\
        \[3, 2, 1, 0\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.argsort.rst.txt)

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