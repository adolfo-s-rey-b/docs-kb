Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.repeat_interleave.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.repeat_interleave.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.repeat_interleave.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.repeat_interleave.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.repeat_interleave.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.repeat_interleave.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.repeat_interleave.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.repeat_interleave.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.repeat_interleave.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.repeat_interleave.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.repeat_interleave.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.repeat_interleave.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.repeat_interleave.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.repeat_interleave.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.repeat_interleave.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.repeat_interleave.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.repeat_interleave.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.repeat_interleave.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.repeat_interleave.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.repeat_interleave.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.repeat_interleave.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.repeat_interleave.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.repeat_interleave.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.repeat_interleave.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.repeat_interleave.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.repeat_interleave.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.repeat_interleave.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.repeat_interleave.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.repeat_interleave.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.repeat_interleave.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.repeat_interleave.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.repeat_interleave.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.repeat_interleave.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.repeat_interleave.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.repeat_interleave.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.repeat_interleave.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.repeat_interleave.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.repeat_interleave.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.repeat_interleave.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.repeat_interleave.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.repeat_interleave.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.repeat_interleave.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.repeat_interleave.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.repeat_interleave.html)

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

torch.repeat\_interleave[#](https://docs.pytorch.org/docs/2.15/generated/torch.repeat_interleave.html#torch-repeat-interleave "Link to this heading")

======================================================================================================================================================

torch.repeat\_interleave(_input_, _repeats_, _dim\=None_, _\*_, _output\_size\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.repeat_interleave.html#torch.repeat_interleave "Link to this definition")

Repeat elements of a tensor.

Warning

This is different from [`torch.Tensor.repeat()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.repeat.html#torch.Tensor.repeat "torch.Tensor.repeat")
 but similar to `numpy.repeat`.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **repeats** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The number of repetitions for each element. repeats is broadcasted to fit the shape of the given axis.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – The dimension along which to repeat values. By default, use the flattened input array, and return a flat output array.
    

Keyword Arguments:

**output\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – Total output size for the given axis ( e.g. sum of repeats). If given, it will avoid stream synchronization needed to calculate output shape of the tensor.

Returns:

Repeated tensor which has the same shape as input, except along the given axis.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> x \= torch.tensor(\[1, 2, 3\])
\>>> x.repeat\_interleave(2)
tensor(\[1, 1, 2, 2, 3, 3\])
\>>> y \= torch.tensor(\[\[1, 2\], \[3, 4\]\])
\>>> torch.repeat\_interleave(y, 2)
tensor(\[1, 1, 2, 2, 3, 3, 4, 4\])
\>>> torch.repeat\_interleave(y, 3, dim\=1)
tensor(\[\[1, 1, 1, 2, 2, 2\],\
        \[3, 3, 3, 4, 4, 4\]\])
\>>> torch.repeat\_interleave(y, torch.tensor(\[1, 2\]), dim\=0)
tensor(\[\[1, 2\],\
        \[3, 4\],\
        \[3, 4\]\])
\>>> torch.repeat\_interleave(y, torch.tensor(\[1, 2\]), dim\=0, output\_size\=3)
tensor(\[\[1, 2\],\
        \[3, 4\],\
        \[3, 4\]\])

Copy to clipboard

If the repeats is tensor(\[n1, n2, n3, …\]), then the output will be tensor(\[0, 0, …, 1, 1, …, 2, 2, …, …\]) where 0 appears n1 times, 1 appears n2 times, 2 appears n3 times, etc.

torch.repeat\_interleave(_repeats_, _\*_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Repeats 0 repeats\[0\] times, 1 repeats\[1\] times, 2 repeats\[2\] times, etc.

Parameters:

**repeats** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – The number of repetitions for each element.

Returns:

Repeated tensor of size sum(repeats).

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> torch.repeat\_interleave(torch.tensor(\[1, 2, 3\]))
tensor(\[0, 1, 1, 2, 2, 2\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.repeat_interleave.rst.txt)

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