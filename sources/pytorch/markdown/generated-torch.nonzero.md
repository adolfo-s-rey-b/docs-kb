Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nonzero.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nonzero.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nonzero.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nonzero.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nonzero.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nonzero.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nonzero.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nonzero.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nonzero.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nonzero.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nonzero.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nonzero.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nonzero.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nonzero.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nonzero.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nonzero.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nonzero.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nonzero.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nonzero.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nonzero.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nonzero.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nonzero.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nonzero.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nonzero.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nonzero.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nonzero.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nonzero.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nonzero.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nonzero.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nonzero.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nonzero.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nonzero.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nonzero.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nonzero.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nonzero.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nonzero.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nonzero.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nonzero.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nonzero.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nonzero.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nonzero.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nonzero.html)

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

torch.nonzero[#](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch-nonzero "Link to this heading")

=======================================================================================================================

torch.nonzero(_input_, _\*_, _out\=None_, _as\_tuple\=False_) → LongTensor or tuple of LongTensors[#](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "Link to this definition")

Note

[`torch.nonzero(..., as_tuple=False)`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero")
 (default) returns a 2-D tensor where each row is the index for a nonzero value.

[`torch.nonzero(..., as_tuple=True)`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero")
 returns a tuple of 1-D index tensors, allowing for advanced indexing, so `x[x.nonzero(as_tuple=True)]` gives all nonzero values of tensor `x`. Of the returned tuple, each index tensor contains nonzero indices for a certain dimension.

See below for more details on the two behaviors.

When `input` is on CUDA, [`torch.nonzero()`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero")
 causes host-device synchronization.

**When** `as_tuple` **is** `False` **(default)**:

Returns a tensor containing the indices of all non-zero elements of `input`. Each row in the result contains the indices of a non-zero element in `input`. The result is sorted lexicographically, with the last index changing the fastest (C-style).

If `input` has nnn dimensions, then the resulting indices tensor `out` is of size (z×n)(z \\times n)(z×n), where zzz is the total number of non-zero elements in the `input` tensor.

**When** `as_tuple` **is** `True`:

Returns a tuple of 1-D tensors, one for each dimension in `input`, each containing the indices (in that dimension) of all non-zero elements of `input` .

If `input` has nnn dimensions, then the resulting tuple contains nnn tensors of size zzz, where zzz is the total number of non-zero elements in the `input` tensor.

As a special case, when `input` has zero dimensions and a nonzero scalar value, it is treated as a one-dimensional tensor with one element.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** (_LongTensor__,_ _optional_) – the output tensor containing indices

Returns:

If `as_tuple` is `False`, the output tensor containing indices. If `as_tuple` is `True`, one 1-D tensor for each dimension, containing the indices of each nonzero element along that dimension.

Return type:

LongTensor or [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
 of LongTensor

Example:

\>>> torch.nonzero(torch.tensor(\[1, 1, 1, 0, 1\]))
tensor(\[\[ 0\],\
        \[ 1\],\
        \[ 2\],\
        \[ 4\]\])
\>>> torch.nonzero(torch.tensor(\[\[0.6, 0.0, 0.0, 0.0\],\
...                             \[0.0, 0.4, 0.0, 0.0\],\
...                             \[0.0, 0.0, 1.2, 0.0\],\
...                             \[0.0, 0.0, 0.0,\-0.4\]\]))
tensor(\[\[ 0,  0\],\
        \[ 1,  1\],\
        \[ 2,  2\],\
        \[ 3,  3\]\])
\>>> torch.nonzero(torch.tensor(\[1, 1, 1, 0, 1\]), as\_tuple\=True)
(tensor(\[0, 1, 2, 4\]),)
\>>> torch.nonzero(torch.tensor(\[\[0.6, 0.0, 0.0, 0.0\],\
...                             \[0.0, 0.4, 0.0, 0.0\],\
...                             \[0.0, 0.0, 1.2, 0.0\],\
...                             \[0.0, 0.0, 0.0,\-0.4\]\]), as\_tuple\=True)
(tensor(\[0, 1, 2, 3\]), tensor(\[0, 1, 2, 3\]))
\>>> torch.nonzero(torch.tensor(5), as\_tuple\=True)
(tensor(\[0\]),)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nonzero.rst.txt)

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