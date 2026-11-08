Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.sparse.sum.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.sparse.sum.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.sparse.sum.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.sparse.sum.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.sparse.sum.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.sparse.sum.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.sparse.sum.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.sparse.sum.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.sparse.sum.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.sparse.sum.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.sparse.sum.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.sparse.sum.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.sparse.sum.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.sparse.sum.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.sparse.sum.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.sparse.sum.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.sparse.sum.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.sparse.sum.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.sparse.sum.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.sparse.sum.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.sparse.sum.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.sparse.sum.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.sparse.sum.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.sparse.sum.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.sparse.sum.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.sparse.sum.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.sparse.sum.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.sparse.sum.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.sparse.sum.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.sparse.sum.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.sparse.sum.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.sparse.sum.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.sparse.sum.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.sparse.sum.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.sparse.sum.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.sparse.sum.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.sparse.sum.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.sparse.sum.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.sparse.sum.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.sparse.sum.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.sparse.sum.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.sparse.sum.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.sparse.sum.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.sparse.sum.html)

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

torch.sparse.sum[#](https://docs.pytorch.org/docs/2.15/generated/torch.sparse.sum.html#torch-sparse-sum "Link to this heading")

================================================================================================================================

torch.sparse.sum(_input_, _dim\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/sparse/__init__.py#L217)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.sparse.sum.html#torch.sparse.sum "Link to this definition")

Return the sum of each row of the given sparse tensor.

Returns the sum of each row of the sparse tensor `input` in the given dimensions `dim`. If `dim` is a list of dimensions, reduce over all of them. When sum over all `sparse_dim`, this method returns a dense tensor instead of a sparse tensor.

All summed `dim` are squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting an output tensor having `dim` fewer dimensions than `input`.

During backward, only gradients at `nnz` locations of `input` will propagate back. Note that the gradients of `input` is coalesced.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input sparse tensor
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints_) – a dimension or a list of dimensions to reduce. Default: reduce over all dims.
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned Tensor. Default: dtype of `input`.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> nnz \= 3
\>>> dims \= \[5, 5, 2, 3\]
\>>> I \= torch.cat(\[torch.randint(0, dims\[0\], size\=(nnz,)),\
                   torch.randint(0, dims\[1\], size=(nnz,))\], 0).reshape(2, nnz)
\>>> V \= torch.randn(nnz, dims\[2\], dims\[3\])
\>>> size \= torch.Size(dims)
\>>> with torch.sparse.check\_sparse\_tensor\_invariants():
...     S \= torch.sparse\_coo\_tensor(I, V, size)
\>>> S
tensor(indices=tensor(\[\[2, 0, 3\],\
                       \[2, 4, 1\]\]),
       values=tensor(\[\[\[-0.6438, -1.6467,  1.4004\],\
                       \[ 0.3411,  0.0918, -0.2312\]\],\
\
                      \[\[ 0.5348,  0.0634, -2.0494\],\
                       \[-0.7125, -1.0646,  2.1844\]\],\
\
                      \[\[ 0.1276,  0.1874, -0.6334\],\
                       \[-1.9682, -0.5340,  0.7483\]\]\]),
       size=(5, 5, 2, 3), nnz=3, layout=torch.sparse\_coo)

\# when sum over only part of sparse\_dims, return a sparse tensor
\>>> torch.sparse.sum(S, \[1, 3\])
tensor(indices=tensor(\[\[0, 2, 3\]\]),
       values=tensor(\[\[-1.4512,  0.4073\],\
                      \[-0.8901,  0.2017\],\
                      \[-0.3183, -1.7539\]\]),
       size=(5, 2), nnz=3, layout=torch.sparse\_coo)

\# when sum over all sparse dim, return a dense tensor
\# with summed dims squeezed
\>>> torch.sparse.sum(S, \[0, 1, 3\])
tensor(\[-2.6596, -1.1450\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.sparse.sum.rst.txt)

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