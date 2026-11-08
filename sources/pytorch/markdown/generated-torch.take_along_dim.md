Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.take_along_dim.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.take_along_dim.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.take_along_dim.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.take_along_dim.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.take_along_dim.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.take_along_dim.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.take_along_dim.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.take_along_dim.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.take_along_dim.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.take_along_dim.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.take_along_dim.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.take_along_dim.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.take_along_dim.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.take_along_dim.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.take_along_dim.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.take_along_dim.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.take_along_dim.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.take_along_dim.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.take_along_dim.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.take_along_dim.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.take_along_dim.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.take_along_dim.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.take_along_dim.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.take_along_dim.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.take_along_dim.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.take_along_dim.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.take_along_dim.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.take_along_dim.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.take_along_dim.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.take_along_dim.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.take_along_dim.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.take_along_dim.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.take_along_dim.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.take_along_dim.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.take_along_dim.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.take_along_dim.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.take_along_dim.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.take_along_dim.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.take_along_dim.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.take_along_dim.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.take_along_dim.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.take_along_dim.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.take_along_dim.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.take_along_dim.html)

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

torch.take\_along\_dim[#](https://docs.pytorch.org/docs/2.15/generated/torch.take_along_dim.html#torch-take-along-dim "Link to this heading")

==============================================================================================================================================

torch.take\_along\_dim(_input_, _indices_, _dim\=None_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.take_along_dim.html#torch.take_along_dim "Link to this definition")

Selects values from `input` at the 1-dimensional indices from `indices` along the given `dim`.

If `dim` is None, the input array is treated as if it has been flattened to 1d.

Functions that return indices along a dimension, like [`torch.argmax()`](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#torch.argmax "torch.argmax")
 and [`torch.argsort()`](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html#torch.argsort "torch.argsort")
, are designed to work with this function. See the examples below.

Note

This function is similar to NumPy’s take\_along\_axis. See also [`torch.gather()`](https://docs.pytorch.org/docs/2.15/generated/torch.gather.html#torch.gather "torch.gather")
.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **indices** (_LongTensor_) – the indices into `input`. Must have long dtype.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – dimension to select along. Default: None.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> t \= torch.tensor(\[\[10, 30, 20\], \[60, 40, 50\]\])
\>>> max\_idx \= torch.argmax(t)
\>>> torch.take\_along\_dim(t, max\_idx)
tensor(\[60\])
\>>> sorted\_idx \= torch.argsort(t, dim\=1)
\>>> torch.take\_along\_dim(t, sorted\_idx, dim\=1)
tensor(\[\[10, 20, 30\],\
        \[40, 50, 60\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.take_along_dim.rst.txt)

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