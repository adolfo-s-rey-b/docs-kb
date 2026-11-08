Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_reduce_.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.index_reduce_.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_reduce_.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.index_reduce_.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.index_reduce_.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.index_reduce_.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.index_reduce_.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.index_reduce_.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.index_reduce_.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.index_reduce_.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.index_reduce_.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.index_reduce_.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.index_reduce_.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.index_reduce_.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.index_reduce_.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.index_reduce_.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.index_reduce_.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.index_reduce_.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.index_reduce_.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.index_reduce_.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.index_reduce_.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.index_reduce_.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.index_reduce_.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.index_reduce_.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.index_reduce_.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.index_reduce_.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.index_reduce_.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.index_reduce_.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.index_reduce_.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.index_reduce_.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.index_reduce_.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.index_reduce_.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.index_reduce_.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.index_reduce_.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.index_reduce_.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.index_reduce_.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.index_reduce_.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.index_reduce_.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.index_reduce_.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.index_reduce_.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.index_reduce_.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.index_reduce_.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.index_reduce_.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.index_reduce_.html)

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

torch.Tensor.index\_reduce\_[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_reduce_.html#torch-tensor-index-reduce "Link to this heading")

===============================================================================================================================================================

Tensor.index\_reduce\_(_dim_, _index_, _source_, _reduce_, _\*_, _include\_self\=True_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_reduce_.html#torch.Tensor.index_reduce_ "Link to this definition")

Accumulate the elements of `source` into the `self` tensor by accumulating to the indices in the order given in `index` using the reduction given by the `reduce` argument. For example, if `dim == 0`, `index[i] == j`, `reduce == prod` and `include_self == True` then the `i`th row of `source` is multiplied by the `j`th row of `self`. If `include_self="True"`, the values in the `self` tensor are included in the reduction, otherwise, rows in the `self` tensor that are accumulated to are treated as if they were filled with the reduction identities.

The [`dim`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.dim.html#torch.Tensor.dim "torch.Tensor.dim")
th dimension of `source` must have the same size as the length of `index` (which must be a vector), and all other dimensions must match `self`, or an error will be raised.

For a 3-D tensor with `reduce="prod"` and `include_self=True` the output is given as:

self\[index\[i\], :, :\] \*= src\[i, :, :\]  \# if dim == 0
self\[:, index\[i\], :\] \*= src\[:, i, :\]  \# if dim == 1
self\[:, :, index\[i\]\] \*= src\[:, :, i\]  \# if dim == 2

Copy to clipboard

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for more information.

Note

This function only supports floating point tensors.

Warning

This function is in beta and may change in the near future.

Parameters:

*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – dimension along which to index
    
*   **index** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – indices of `self` to accumulate into, should have dtype either torch.int64 or torch.int32
    
*   **source** (_FloatTensor_) – the tensor containing values to accumulate
    
*   **reduce** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – the reduction operation to apply (`"prod"`, `"mean"`, `"amax"`, `"amin"`)
    

Keyword Arguments:

**include\_self** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – whether the elements from the `self` tensor are included in the reduction

Example:

\>>> x \= torch.empty(5, 3).fill\_(2)
\>>> t \= torch.tensor(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], \[10, 11, 12\]\], dtype\=torch.float)
\>>> index \= torch.tensor(\[0, 4, 2, 0\])
\>>> x.index\_reduce\_(0, index, t, 'prod')
tensor(\[\[20., 44., 72.\],\
        \[ 2.,  2.,  2.\],\
        \[14., 16., 18.\],\
        \[ 2.,  2.,  2.\],\
        \[ 8., 10., 12.\]\])
\>>> x \= torch.empty(5, 3).fill\_(2)
\>>> x.index\_reduce\_(0, index, t, 'prod', include\_self\=False)
tensor(\[\[10., 22., 36.\],\
        \[ 2.,  2.,  2.\],\
        \[ 7.,  8.,  9.\],\
        \[ 2.,  2.,  2.\],\
        \[ 4.,  5.,  6.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.index_reduce_.rst.txt)

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