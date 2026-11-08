Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.searchsorted.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.searchsorted.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.searchsorted.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.searchsorted.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.searchsorted.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.searchsorted.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.searchsorted.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.searchsorted.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.searchsorted.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.searchsorted.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.searchsorted.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.searchsorted.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.searchsorted.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.searchsorted.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.searchsorted.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.searchsorted.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.searchsorted.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.searchsorted.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.searchsorted.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.searchsorted.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.searchsorted.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.searchsorted.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.searchsorted.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.searchsorted.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.searchsorted.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.searchsorted.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.searchsorted.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.searchsorted.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.searchsorted.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.searchsorted.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.searchsorted.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.searchsorted.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.searchsorted.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.searchsorted.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.searchsorted.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.searchsorted.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.searchsorted.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.searchsorted.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.searchsorted.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.searchsorted.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.searchsorted.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.searchsorted.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.searchsorted.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.searchsorted.html)

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

torch.searchsorted[#](https://docs.pytorch.org/docs/2.15/generated/torch.searchsorted.html#torch-searchsorted "Link to this heading")

======================================================================================================================================

torch.searchsorted(_sorted\_sequence_, _values_, _\*_, _out\_int32\=False_, _right\=False_, _side\=None_, _out\=None_, _sorter\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.searchsorted.html#torch.searchsorted "Link to this definition")

Find the indices from the _innermost_ dimension of `sorted_sequence` such that, if the corresponding values in `values` were inserted before the indices, when sorted, the order of the corresponding _innermost_ dimension within `sorted_sequence` would be preserved. Return a new tensor with the same size as `values`. More formally, the returned index satisfies the following rules:

  
| `sorted_sequence` | `right` | _returned index satisfies_ |
| --- | --- | --- |
| 1-D | False | `sorted_sequence[i-1] < values[m][n]...[l][x] <= sorted_sequence[i]` |
| 1-D | True | `sorted_sequence[i-1] <= values[m][n]...[l][x] < sorted_sequence[i]` |
| N-D | False | `sorted_sequence[m][n]...[l][i-1] < values[m][n]...[l][x] <= sorted_sequence[m][n]...[l][i]` |
| N-D | True | `sorted_sequence[m][n]...[l][i-1] <= values[m][n]...[l][x] < sorted_sequence[m][n]...[l][i]` |

Parameters:

*   **sorted\_sequence** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – N-D or 1-D tensor, containing monotonically increasing sequence on the _innermost_ dimension unless `sorter` is provided, in which case the sequence does not need to be sorted. PyTorch does not validate this condition when `sorter` is not provided, and the behavior is undefined if the sequence is not sorted.
    
*   **values** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Scalar_) – N-D tensor or a Scalar containing the search value(s).
    

Keyword Arguments:

*   **out\_int32** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – indicate the output data type. torch.int32 if True, torch.int64 otherwise. Default value is False, i.e. default output data type is torch.int64.
    
*   **right** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if False, return the first suitable location that is found. If True, return the last such index. If no suitable index found, return 0 for non-numerical value (eg. nan, inf) or the size of _innermost_ dimension within `sorted_sequence` (one pass the last index of the _innermost_ dimension). In other words, if False, gets the lower bound index for each value in `values` on the corresponding _innermost_ dimension of the `sorted_sequence`. If True, gets the upper bound index instead. Default value is False. `side` does the same and is preferred. It will error if `side` is set to “left” while this is True.
    
*   **side** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – the same as `right` but preferred. “left” corresponds to False for `right` and “right” corresponds to True for `right`. It will error if this is set to “left” while `right` is True. Default value is None.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor, must be the same size as `values` if provided.
    
*   **sorter** (_LongTensor__,_ _optional_) – if provided, a tensor matching the shape of the unsorted `sorted_sequence` containing a sequence of indices that sort it in the ascending order on the innermost dimension
    

Example:

\>>> sorted\_sequence \= torch.tensor(\[\[1, 3, 5, 7, 9\], \[2, 4, 6, 8, 10\]\])
\>>> sorted\_sequence
tensor(\[\[ 1,  3,  5,  7,  9\],\
        \[ 2,  4,  6,  8, 10\]\])
\>>> values \= torch.tensor(\[\[3, 6, 9\], \[3, 6, 9\]\])
\>>> values
tensor(\[\[3, 6, 9\],\
        \[3, 6, 9\]\])
\>>> torch.searchsorted(sorted\_sequence, values)
tensor(\[\[1, 3, 4\],\
        \[1, 2, 4\]\])
\>>> torch.searchsorted(sorted\_sequence, values, side\='right')
tensor(\[\[2, 3, 5\],\
        \[1, 3, 4\]\])

\>>> sorted\_sequence\_1d \= torch.tensor(\[1, 3, 5, 7, 9\])
\>>> sorted\_sequence\_1d
tensor(\[1, 3, 5, 7, 9\])
\>>> torch.searchsorted(sorted\_sequence\_1d, values)
tensor(\[\[1, 3, 4\],\
        \[1, 3, 4\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.searchsorted.rst.txt)

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