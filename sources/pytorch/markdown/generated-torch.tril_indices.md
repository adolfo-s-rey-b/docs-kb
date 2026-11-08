Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.tril_indices.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.tril_indices.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.tril_indices.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.tril_indices.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.tril_indices.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.tril_indices.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.tril_indices.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.tril_indices.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.tril_indices.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.tril_indices.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.tril_indices.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.tril_indices.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.tril_indices.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.tril_indices.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.tril_indices.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.tril_indices.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.tril_indices.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.tril_indices.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.tril_indices.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.tril_indices.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.tril_indices.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.tril_indices.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.tril_indices.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.tril_indices.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.tril_indices.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.tril_indices.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.tril_indices.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.tril_indices.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.tril_indices.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.tril_indices.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.tril_indices.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.tril_indices.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.tril_indices.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.tril_indices.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.tril_indices.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.tril_indices.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.tril_indices.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.tril_indices.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.tril_indices.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.tril_indices.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.tril_indices.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.tril_indices.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.tril_indices.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.tril_indices.html)

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

torch.tril\_indices[#](https://docs.pytorch.org/docs/2.15/generated/torch.tril_indices.html#torch-tril-indices "Link to this heading")

=======================================================================================================================================

torch.tril\_indices(_row_, _col_, _offset\=0_, _\*_, _dtype\=torch.long_, _device\='cpu'_, _layout\=torch.strided_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.tril_indices.html#torch.tril_indices "Link to this definition")

Returns the indices of the lower triangular part of a `row`\-by- `col` matrix in a 2-by-N Tensor, where the first row contains row coordinates of all indices and the second row contains column coordinates. Indices are ordered based on rows and then columns.

The lower triangular part of the matrix is defined as the elements on and below the diagonal.

The argument `offset` controls which diagonal to consider. If `offset` = 0, all elements on and below the main diagonal are retained. A positive value includes just as many diagonals above the main diagonal, and similarly a negative value excludes just as many diagonals below the main diagonal. The main diagonal are the set of indices {(i,i)}\\lbrace (i, i) \\rbrace{(i,i)} for i∈\[0,min⁡{d1,d2}−1\]i \\in \[0, \\min\\{d\_{1}, d\_{2}\\} - 1\]i∈\[0,min{d1​,d2​}−1\] where d1,d2d\_{1}, d\_{2}d1​,d2​ are the dimensions of the matrix.

Note

When running on CUDA, `row * col` must be less than 2592^{59}259 to prevent overflow during calculation.

Parameters:

*   **row** (`int`) – number of rows in the 2-D matrix.
    
*   **col** (`int`) – number of columns in the 2-D matrix.
    
*   **offset** (`int`) – diagonal offset from the main diagonal. Default: if not provided, 0.
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor, only support `torch.int`, `torch.long`. Default: if `None`, `torch.long`.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). [`device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – currently only support `torch.strided`.
    

Example:

\>>> a \= torch.tril\_indices(3, 3)
\>>> a
tensor(\[\[0, 1, 1, 2, 2, 2\],\
        \[0, 0, 1, 0, 1, 2\]\])

\>>> a \= torch.tril\_indices(4, 3, \-1)
\>>> a
tensor(\[\[1, 2, 2, 3, 3, 3\],\
        \[0, 0, 1, 0, 1, 2\]\])

\>>> a \= torch.tril\_indices(4, 3, 1)
\>>> a
tensor(\[\[0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3\],\
        \[0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.tril_indices.rst.txt)

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