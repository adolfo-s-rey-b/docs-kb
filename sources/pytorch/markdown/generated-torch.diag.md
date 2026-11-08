Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.diag.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.diag.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.diag.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.diag.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.diag.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.diag.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.diag.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.diag.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.diag.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.diag.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.diag.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.diag.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.diag.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.diag.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.diag.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.diag.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.diag.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.diag.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.diag.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.diag.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.diag.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.diag.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.diag.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.diag.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.diag.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.diag.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.diag.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.diag.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.diag.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.diag.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.diag.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.diag.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.diag.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.diag.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.diag.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.diag.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.diag.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.diag.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.diag.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.diag.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.diag.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.diag.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.diag.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.diag.html)

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

torch.diag[#](https://docs.pytorch.org/docs/2.15/generated/torch.diag.html#torch-diag "Link to this heading")

==============================================================================================================

torch.diag(_input_, _diagonal\=0_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.diag.html#torch.diag "Link to this definition")

*   If `input` is a vector (1-D tensor), then returns a 2-D square tensor with the elements of `input` as the diagonal.
    
*   If `input` is a matrix (2-D tensor), then returns a 1-D tensor with the diagonal elements of `input`.
    

The argument [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 controls which diagonal to consider:

*   If [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
     = 0, it is the main diagonal.
    
*   If [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
     > 0, it is above the main diagonal.
    
*   If [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
     < 0, it is below the main diagonal.
    

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **diagonal** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the diagonal to consider
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

See also

[`torch.diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")
 always returns the diagonal of its input.

[`torch.diagflat()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagflat.html#torch.diagflat "torch.diagflat")
 always constructs a tensor with diagonal elements specified by the input.

Examples:

Get the square matrix where the input vector is the diagonal:

\>>> a \= torch.randn(3)
\>>> a
tensor(\[ 0.5950,-0.0872, 2.3298\])
\>>> torch.diag(a)
tensor(\[\[ 0.5950, 0.0000, 0.0000\],\
        \[ 0.0000,-0.0872, 0.0000\],\
        \[ 0.0000, 0.0000, 2.3298\]\])
\>>> torch.diag(a, 1)
tensor(\[\[ 0.0000, 0.5950, 0.0000, 0.0000\],\
        \[ 0.0000, 0.0000,-0.0872, 0.0000\],\
        \[ 0.0000, 0.0000, 0.0000, 2.3298\],\
        \[ 0.0000, 0.0000, 0.0000, 0.0000\]\])

Copy to clipboard

Get the k-th diagonal of a given matrix:

\>>> a \= torch.randn(3, 3)
\>>> a
tensor(\[\[-0.4264, 0.0255,-0.1064\],\
        \[ 0.8795,-0.2429, 0.1374\],\
        \[ 0.1029,-0.6482,-1.6300\]\])
\>>> torch.diag(a, 0)
tensor(\[-0.4264,-0.2429,-1.6300\])
\>>> torch.diag(a, 1)
tensor(\[ 0.0255, 0.1374\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.diag.rst.txt)

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