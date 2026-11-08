Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.diag_embed.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.diag_embed.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.diag_embed.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.diag_embed.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.diag_embed.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.diag_embed.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.diag_embed.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.diag_embed.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.diag_embed.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.diag_embed.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.diag_embed.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.diag_embed.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.diag_embed.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.diag_embed.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.diag_embed.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.diag_embed.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.diag_embed.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.diag_embed.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.diag_embed.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.diag_embed.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.diag_embed.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.diag_embed.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.diag_embed.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.diag_embed.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.diag_embed.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.diag_embed.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.diag_embed.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.diag_embed.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.diag_embed.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.diag_embed.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.diag_embed.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.diag_embed.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.diag_embed.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.diag_embed.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.diag_embed.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.diag_embed.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.diag_embed.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.diag_embed.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.diag_embed.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.diag_embed.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.diag_embed.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.diag_embed.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.diag_embed.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.diag_embed.html)

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

torch.diag\_embed[#](https://docs.pytorch.org/docs/2.15/generated/torch.diag_embed.html#torch-diag-embed "Link to this heading")

=================================================================================================================================

torch.diag\_embed(_input_, _offset\=0_, _dim1\=\-2_, _dim2\=\-1_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.diag_embed.html#torch.diag_embed "Link to this definition")

Creates a tensor whose diagonals of certain 2D planes (specified by `dim1` and `dim2`) are filled by `input`. To facilitate creating batched diagonal matrices, the 2D planes formed by the last two dimensions of the returned tensor are chosen by default.

The argument `offset` controls which diagonal to consider:

*   If `offset` = 0, it is the main diagonal.
    
*   If `offset` > 0, it is above the main diagonal.
    
*   If `offset` < 0, it is below the main diagonal.
    

The size of the new matrix will be calculated to make the specified diagonal of the size of the last input dimension. Note that for `offset` other than 000, the order of `dim1` and `dim2` matters. Exchanging them is equivalent to changing the sign of `offset`.

Applying [`torch.diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 to the output of this function with the same arguments yields a matrix identical to input. However, [`torch.diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 has different default dimensions, so those need to be explicitly specified.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor. Must be at least 1-dimensional.
    
*   **offset** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – which diagonal to consider. Default: 0 (main diagonal).
    
*   **dim1** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – first dimension with respect to which to take diagonal. Default: -2.
    
*   **dim2** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – second dimension with respect to which to take diagonal. Default: -1.
    

Example:

\>>> a \= torch.randn(2, 3)
\>>> torch.diag\_embed(a)
tensor(\[\[\[ 1.5410,  0.0000,  0.0000\],\
         \[ 0.0000, -0.2934,  0.0000\],\
         \[ 0.0000,  0.0000, -2.1788\]\],\
\
        \[\[ 0.5684,  0.0000,  0.0000\],\
         \[ 0.0000, -1.0845,  0.0000\],\
         \[ 0.0000,  0.0000, -1.3986\]\]\])

\>>> torch.diag\_embed(a, offset\=1, dim1\=0, dim2\=2)
tensor(\[\[\[ 0.0000,  1.5410,  0.0000,  0.0000\],\
         \[ 0.0000,  0.5684,  0.0000,  0.0000\]\],\
\
        \[\[ 0.0000,  0.0000, -0.2934,  0.0000\],\
         \[ 0.0000,  0.0000, -1.0845,  0.0000\]\],\
\
        \[\[ 0.0000,  0.0000,  0.0000, -2.1788\],\
         \[ 0.0000,  0.0000,  0.0000, -1.3986\]\],\
\
        \[\[ 0.0000,  0.0000,  0.0000,  0.0000\],\
         \[ 0.0000,  0.0000,  0.0000,  0.0000\]\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.diag_embed.rst.txt)

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