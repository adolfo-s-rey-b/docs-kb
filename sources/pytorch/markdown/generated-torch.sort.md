Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.sort.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.sort.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.sort.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.sort.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.sort.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.sort.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.sort.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.sort.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.sort.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.sort.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.sort.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.sort.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.sort.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.sort.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.sort.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.sort.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.sort.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.sort.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.sort.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.sort.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.sort.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.sort.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.sort.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.sort.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.sort.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.sort.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.sort.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.sort.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.sort.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.sort.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.sort.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.sort.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.sort.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.sort.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.sort.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.sort.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.sort.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.sort.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.sort.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.sort.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.sort.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.sort.html)

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

torch.sort[#](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#torch-sort "Link to this heading")

==============================================================================================================

torch.sort(_input_, _dim\=\-1_, _descending\=False_, _\*_, _stable\=False_, _out\=None_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#torch.sort "Link to this definition")

Sorts the elements of the `input` tensor along a given dimension in ascending order by value.

If `dim` is not given, the last dimension of the input is chosen.

If `descending` is `True` then the elements are sorted in descending order by value.

If `stable` is `True` then the sorting routine becomes stable, preserving the order of equivalent elements.

A namedtuple of (values, indices) is returned, where the values are the sorted values and indices are the indices of the elements in the original input tensor.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to sort along
    
*   **descending** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls the sorting order (ascending or descending)
    

Keyword Arguments:

*   **stable** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – makes the sorting routine stable, which guarantees that the order of equivalent elements is preserved.
    
*   **out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – the output tuple of (Tensor, LongTensor) that can be optionally given to be used as output buffers
    

Example:

\>>> x \= torch.randn(3, 4)
\>>> sorted, indices \= torch.sort(x)
\>>> sorted
tensor(\[\[-0.2162,  0.0608,  0.6719,  2.3332\],\
        \[-0.5793,  0.0061,  0.6058,  0.9497\],\
        \[-0.5071,  0.3343,  0.9553,  1.0960\]\])
\>>> indices
tensor(\[\[ 1,  0,  2,  3\],\
        \[ 3,  1,  0,  2\],\
        \[ 0,  3,  1,  2\]\])

\>>> sorted, indices \= torch.sort(x, 0)
\>>> sorted
tensor(\[\[-0.5071, -0.2162,  0.6719, -0.5793\],\
        \[ 0.0608,  0.0061,  0.9497,  0.3343\],\
        \[ 0.6058,  0.9553,  1.0960,  2.3332\]\])
\>>> indices
tensor(\[\[ 2,  0,  0,  1\],\
        \[ 0,  1,  1,  2\],\
        \[ 1,  2,  2,  0\]\])
\>>> x \= torch.tensor(\[0, 1\] \* 9)
\>>> x.sort()
torch.return\_types.sort(
    values=tensor(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1\]),
    indices=tensor(\[ 2, 16,  4,  6, 14,  8,  0, 10, 12,  9, 17, 15, 13, 11,  7,  5,  3,  1\]))
\>>> x.sort(stable\=True)
torch.return\_types.sort(
    values=tensor(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1\]),
    indices=tensor(\[ 0,  2,  4,  6,  8, 10, 12, 14, 16,  1,  3,  5,  7,  9, 11, 13, 15, 17\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.sort.rst.txt)

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