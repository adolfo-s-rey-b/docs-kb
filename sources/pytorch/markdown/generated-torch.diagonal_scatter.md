Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_scatter.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.diagonal_scatter.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_scatter.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.diagonal_scatter.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.diagonal_scatter.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.diagonal_scatter.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.diagonal_scatter.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.diagonal_scatter.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.diagonal_scatter.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.diagonal_scatter.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.diagonal_scatter.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.diagonal_scatter.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.diagonal_scatter.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.diagonal_scatter.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.diagonal_scatter.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.diagonal_scatter.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.diagonal_scatter.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.diagonal_scatter.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.diagonal_scatter.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.diagonal_scatter.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.diagonal_scatter.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.diagonal_scatter.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.diagonal_scatter.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.diagonal_scatter.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.diagonal_scatter.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.diagonal_scatter.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.diagonal_scatter.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.diagonal_scatter.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.diagonal_scatter.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.diagonal_scatter.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.diagonal_scatter.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.diagonal_scatter.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.diagonal_scatter.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.diagonal_scatter.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.diagonal_scatter.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.diagonal_scatter.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.diagonal_scatter.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.diagonal_scatter.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.diagonal_scatter.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.diagonal_scatter.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.diagonal_scatter.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.diagonal_scatter.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.diagonal_scatter.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.diagonal_scatter.html)

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

torch.diagonal\_scatter[#](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_scatter.html#torch-diagonal-scatter "Link to this heading")

===================================================================================================================================================

torch.diagonal\_scatter(_input_, _src_, _offset\=0_, _dim1\=0_, _dim2\=1_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_scatter.html#torch.diagonal_scatter "Link to this definition")

Embeds the values of the `src` tensor into `input` along the diagonal elements of `input`, with respect to `dim1` and `dim2`.

This function returns a tensor with fresh storage; it does not return a view.

The argument `offset` controls which diagonal to consider:

*   If `offset` = 0, it is the main diagonal.
    
*   If `offset` > 0, it is above the main diagonal.
    
*   If `offset` < 0, it is below the main diagonal.
    

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor. Must be at least 2-dimensional.
    
*   **src** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to embed into `input`.
    
*   **offset** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – which diagonal to consider. Default: 0 (main diagonal).
    
*   **dim1** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – first dimension with respect to which to take diagonal. Default: 0.
    
*   **dim2** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – second dimension with respect to which to take diagonal. Default: 1.
    

Note

`src` must be of the proper size in order to be embedded into `input`. Specifically, it should have the same shape as `torch.diagonal(input, offset, dim1, dim2)`

Examples:

\>>> a \= torch.zeros(3, 3)
\>>> a
tensor(\[\[0., 0., 0.\],\
        \[0., 0., 0.\],\
        \[0., 0., 0.\]\])

\>>> torch.diagonal\_scatter(a, torch.ones(3), 0)
tensor(\[\[1., 0., 0.\],\
        \[0., 1., 0.\],\
        \[0., 0., 1.\]\])

\>>> torch.diagonal\_scatter(a, torch.ones(2), 1)
tensor(\[\[0., 1., 0.\],\
        \[0., 0., 1.\],\
        \[0., 0., 0.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.diagonal_scatter.rst.txt)

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