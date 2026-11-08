Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.unique.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.unique.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.unique.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.unique.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.unique.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.unique.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.unique.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.unique.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.unique.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.unique.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.unique.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.unique.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.unique.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.unique.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.unique.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.unique.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.unique.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.unique.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.unique.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.unique.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.unique.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.unique.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.unique.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.unique.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.unique.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.unique.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.unique.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.unique.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.unique.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.unique.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.unique.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.unique.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.unique.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.unique.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.unique.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.unique.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.unique.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.unique.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.unique.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.unique.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.unique.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.unique.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.unique.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.unique.html)

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

torch.unique[#](https://docs.pytorch.org/docs/2.15/generated/torch.unique.html#torch-unique "Link to this heading")

====================================================================================================================

torch.unique(_input_, _sorted\=True_, _return\_inverse\=False_, _return\_counts\=False_, _dim\=None_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_jit_internal.py#L627)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.unique.html#torch.unique "Link to this definition")

Returns the unique elements of the input tensor.

Note

This function is different from [`torch.unique_consecutive()`](https://docs.pytorch.org/docs/2.15/generated/torch.unique_consecutive.html#torch.unique_consecutive "torch.unique_consecutive")
 in the sense that this function also eliminates non-consecutive duplicate values.

Note

Currently in the CUDA implementation and the CPU implementation, torch.unique always sort the tensor at the beginning regardless of the sort argument. Sorting could be slow, so if your input tensor is already sorted, it is recommended to use [`torch.unique_consecutive()`](https://docs.pytorch.org/docs/2.15/generated/torch.unique_consecutive.html#torch.unique_consecutive "torch.unique_consecutive")
 which avoids the sorting.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor
    
*   **sorted** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to sort the unique elements in ascending order before returning as output.
    
*   **return\_inverse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to also return the indices for where elements in the original input ended up in the returned unique list.
    
*   **return\_counts** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to also return the counts for each unique element.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to operate upon. If `None`, the unique of the flattened input is returned. Otherwise, each of the tensors indexed by the given dimension is treated as one of the elements to apply the unique operation upon. **Important:** when `dim` is specified, the operation finds unique sub-tensors (e.g., unique rows or columns), not unique scalar values. This means individual values may appear multiple times in the output if they exist in different sub-tensors. See examples for more details. Default: `None`
    

Returns:

A tensor or a tuple of tensors containing

> *   **output** (_Tensor_): the output list of unique scalar elements if `dim` is `None`; otherwise, the unique sub-tensors along the specified dimension. Note that when `dim` is specified, scalar values may repeat in the output.
>     
> *   **inverse\_indices** (_Tensor_): (optional) if `return_inverse` is True, there will be an additional returned tensor (same shape as input) representing the indices for where elements in the original input map to in the output; otherwise, this function will only return a single tensor.
>     
> *   **counts** (_Tensor_): (optional) if `return_counts` is True, there will be an additional returned tensor (same shape as output or output.size(dim), if dim was specified) representing the number of occurrences for each unique value or tensor.
>     

Return type:

([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 (optional), [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 (optional))

Example:

\>>> output \= torch.unique(torch.tensor(\[1, 3, 2, 3\], dtype\=torch.long))
\>>> output
tensor(\[1, 2, 3\])

\>>> output, inverse\_indices \= torch.unique(
...     torch.tensor(\[1, 3, 2, 3\], dtype\=torch.long), sorted\=True, return\_inverse\=True)
\>>> output
tensor(\[1, 2, 3\])
\>>> inverse\_indices
tensor(\[0, 2, 1, 2\])

\>>> output, inverse\_indices \= torch.unique(
...     torch.tensor(\[\[1, 3\], \[2, 3\]\], dtype\=torch.long), sorted\=True, return\_inverse\=True)
\>>> output
tensor(\[1, 2, 3\])
\>>> inverse\_indices
tensor(\[\[0, 2\],\
        \[1, 2\]\])

\>>> \# When using dim, the operation finds unique sub-tensors, not unique values.
\>>> \# Notice how values can repeat in the output:
\>>> x \= torch.tensor(\[\[1, 3, 2, 3\], \[1, 2, 1, 2\]\], dtype\=torch.long)
\>>> torch.unique(x, dim\=0)  \# unique rows
tensor(\[\[1, 2, 1, 2\],\
        \[1, 3, 2, 3\]\])
\>>> \# Both rows are kept because they're different from each other,
\>>> \# even though values 1, 2, 3 appear multiple times in the output.
\>>> torch.unique(x, dim\=1)  \# unique columns
tensor(\[\[1, 2, 3\],\
        \[1, 1, 2\]\])
\>>> \# The value 1 appears twice because we're comparing columns, not values.
\>>> \# Compare with flattened (no dim):
\>>> torch.unique(x)
tensor(\[1, 2, 3\])

\>>> a \= torch.tensor(\[\
...     \[\
...         \[1, 1, 0, 0\],\
...         \[1, 1, 0, 0\],\
...         \[0, 0, 1, 1\],\
...     \],\
...     \[\
...         \[0, 0, 1, 1\],\
...         \[0, 0, 1, 1\],\
...         \[1, 1, 1, 1\],\
...     \],\
...     \[\
...         \[1, 1, 0, 0\],\
...         \[1, 1, 0, 0\],\
...         \[0, 0, 1, 1\],\
...     \],\
... \])

\>>> \# If we call \`torch.unique(a, dim=0)\`, each of the tensors \`a\[idx, :, :\]\`
\>>> \# will be compared. We can see that \`a\[0, :, :\]\` and \`a\[2, :, :\]\` match
\>>> \# each other, so one of them will be removed.
\>>> (a\[0, :, :\] \== a\[2, :, :\]).all()
tensor(True)
\>>> a\_unique\_dim0 \= torch.unique(a, dim\=0)
\>>> a\_unique\_dim0
tensor(\[\[\[0, 0, 1, 1\],\
         \[0, 0, 1, 1\],\
         \[1, 1, 1, 1\]\],\
        \[\[1, 1, 0, 0\],\
         \[1, 1, 0, 0\],\
         \[0, 0, 1, 1\]\]\])

\>>> \# Notice which sub-tensors from \`a\` match with the sub-tensors from
\>>> \# \`a\_unique\_dim0\`:
\>>> (a\_unique\_dim0\[0, :, :\] \== a\[1, :, :\]).all()
tensor(True)
\>>> (a\_unique\_dim0\[1, :, :\] \== a\[0, :, :\]).all()
tensor(True)

\>>> \# For \`torch.unique(a, dim=1)\`, each of the tensors \`a\[:, idx, :\]\` are
\>>> \# compared. \`a\[:, 0, :\]\` and \`a\[:, 1, :\]\` match each other, so one of
\>>> \# them will be removed.
\>>> (a\[:, 0, :\] \== a\[:, 1, :\]).all()
tensor(True)
\>>> torch.unique(a, dim\=1)
tensor(\[\[\[0, 0, 1, 1\],\
         \[1, 1, 0, 0\]\],\
        \[\[1, 1, 1, 1\],\
         \[0, 0, 1, 1\]\],\
        \[\[0, 0, 1, 1\],\
         \[1, 1, 0, 0\]\]\])

\>>> \# For \`torch.unique(a, dim=2)\`, the tensors \`a\[:, :, idx\]\` are compared.
\>>> \# \`a\[:, :, 0\]\` and \`a\[:, :, 1\]\` match each other. Also, \`a\[:, :, 2\]\` and
\>>> \# \`a\[:, :, 3\]\` match each other as well. So in this case, two of the
\>>> \# sub-tensors will be removed.
\>>> (a\[:, :, 0\] \== a\[:, :, 1\]).all()
tensor(True)
\>>> (a\[:, :, 2\] \== a\[:, :, 3\]).all()
tensor(True)
\>>> torch.unique(a, dim\=2)
tensor(\[\[\[0, 1\],\
         \[0, 1\],\
         \[1, 0\]\],\
        \[\[1, 0\],\
         \[1, 0\],\
         \[1, 1\]\],\
        \[\[0, 1\],\
         \[0, 1\],\
         \[1, 0\]\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.unique.rst.txt)

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