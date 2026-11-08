Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_compressed_tensor.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.sparse_compressed_tensor.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_compressed_tensor.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.sparse_compressed_tensor.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.sparse_compressed_tensor.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.sparse_compressed_tensor.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.sparse_compressed_tensor.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.sparse_compressed_tensor.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.sparse_compressed_tensor.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.sparse_compressed_tensor.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.sparse_compressed_tensor.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.sparse_compressed_tensor.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.sparse_compressed_tensor.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.sparse_compressed_tensor.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.sparse_compressed_tensor.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.sparse_compressed_tensor.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.sparse_compressed_tensor.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.sparse_compressed_tensor.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.sparse_compressed_tensor.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.sparse_compressed_tensor.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.sparse_compressed_tensor.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.sparse_compressed_tensor.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.sparse_compressed_tensor.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.sparse_compressed_tensor.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.sparse_compressed_tensor.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.sparse_compressed_tensor.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.sparse_compressed_tensor.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.sparse_compressed_tensor.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.sparse_compressed_tensor.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.sparse_compressed_tensor.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.sparse_compressed_tensor.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.sparse_compressed_tensor.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.sparse_compressed_tensor.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.sparse_compressed_tensor.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.sparse_compressed_tensor.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.sparse_compressed_tensor.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.sparse_compressed_tensor.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.sparse_compressed_tensor.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.sparse_compressed_tensor.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.sparse_compressed_tensor.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.sparse_compressed_tensor.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.sparse_compressed_tensor.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.sparse_compressed_tensor.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.sparse_compressed_tensor.html)

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

torch.sparse\_compressed\_tensor[#](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_compressed_tensor.html#torch-sparse-compressed-tensor "Link to this heading")

============================================================================================================================================================================

torch.sparse\_compressed\_tensor(_compressed\_indices_, _plain\_indices_, _values_, _size\=None_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _pin\_memory\=False_, _requires\_grad\=False_, _check\_invariants\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_compressed_tensor.html#torch.sparse_compressed_tensor "Link to this definition")

Constructs a [sparse tensor in Compressed Sparse format - CSR, CSC, BSR, or BSC -](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-compressed-docs)
 with specified values at the given `compressed_indices` and `plain_indices`. Sparse matrix multiplication operations in Compressed Sparse format are typically faster than that for sparse tensors in COO format. Make you have a look at [the note on the data type of the indices](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-compressed-docs)
.

Note

If the `device` argument is not specified the device of the given `values` and indices tensor(s) must match. If, however, the argument is specified the input Tensors will be converted to the given device and in turn determine the device of the constructed sparse tensor.

Parameters:

*   **compressed\_indices** (_array\_like_) – (B+1)-dimensional array of size `(*batchsize, compressed_dim_size + 1)`. The last element of each batch is the number of non-zero elements or blocks. This tensor encodes the index in `values` and `plain_indices` depending on where the given compressed dimension (row or column) starts. Each successive number in the tensor subtracted by the number before it denotes the number of elements or blocks in a given compressed dimension.
    
*   **plain\_indices** (_array\_like_) – Plain dimension (column or row) coordinates of each element or block in values. (B+1)-dimensional tensor with the same length as values.
    
*   **values** (_array\_list_) – Initial values for the tensor. Can be a list, tuple, NumPy `ndarray`, scalar, and other types. that represents a (1+K)-dimensional (for CSR and CSC layouts) or (1+2+K)-dimensional tensor (for BSR and BSC layouts) where `K` is the number of dense dimensions.
    
*   **size** (list, tuple, [`torch.Size`](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
    , optional) – Size of the sparse tensor: `(*batchsize, nrows * blocksize[0], ncols * blocksize[1], *densesize)` where `blocksize[0] == blocksize[1] == 1` for CSR and CSC formats. If not provided, the size will be inferred as the minimum size big enough to hold all non-zero elements or blocks.
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if None, infers data type from `values`.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , required) – the desired layout of returned tensor: `torch.sparse_csr`, `torch.sparse_csc`, `torch.sparse_bsr`, or `torch.sparse_bsc`.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if None, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    
*   **check\_invariants** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If sparse tensor invariants are checked. Default: as returned by [`torch.sparse.check_sparse_tensor_invariants.is_enabled()`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse.check_sparse_tensor_invariants.html#torch.sparse.check_sparse_tensor_invariants.is_enabled "torch.sparse.check_sparse_tensor_invariants.is_enabled")
    , initially False.
    

Example:

\>>> compressed\_indices \= \[0, 2, 4\]
\>>> plain\_indices \= \[0, 1, 0, 1\]
\>>> values \= \[1, 2, 3, 4\]
\>>> torch.sparse\_compressed\_tensor(torch.tensor(compressed\_indices, dtype\=torch.int64),
...                                torch.tensor(plain\_indices, dtype\=torch.int64),
...                                torch.tensor(values), dtype\=torch.double, layout\=torch.sparse\_csr)
tensor(crow\_indices=tensor(\[0, 2, 4\]),
       col\_indices=tensor(\[0, 1, 0, 1\]),
       values=tensor(\[1., 2., 3., 4.\]), size=(2, 2), nnz=4,
       dtype=torch.float64, layout=torch.sparse\_csr)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.sparse_compressed_tensor.rst.txt)

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