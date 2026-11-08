Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.kthvalue.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.kthvalue.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.kthvalue.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.kthvalue.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.kthvalue.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.kthvalue.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.kthvalue.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.kthvalue.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.kthvalue.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.kthvalue.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.kthvalue.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.kthvalue.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.kthvalue.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.kthvalue.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.kthvalue.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.kthvalue.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.kthvalue.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.kthvalue.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.kthvalue.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.kthvalue.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.kthvalue.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.kthvalue.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.kthvalue.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.kthvalue.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.kthvalue.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.kthvalue.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.kthvalue.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.kthvalue.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.kthvalue.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.kthvalue.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.kthvalue.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.kthvalue.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.kthvalue.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.kthvalue.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.kthvalue.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.kthvalue.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.kthvalue.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.kthvalue.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.kthvalue.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.kthvalue.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.kthvalue.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.kthvalue.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.kthvalue.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.kthvalue.html)

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

torch.kthvalue[#](https://docs.pytorch.org/docs/2.15/generated/torch.kthvalue.html#torch-kthvalue "Link to this heading")

==========================================================================================================================

torch.kthvalue(_input_, _k_, _dim\=None_, _keepdim\=False_, _\*_, _out\=None_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.kthvalue.html#torch.kthvalue "Link to this definition")

Returns a namedtuple `(values, indices)` where `values` is the `k` th smallest element of each row of the `input` tensor in the given dimension `dim`. And `indices` is the index location of each element found.

If `dim` is not given, the last dimension of the input is chosen.

If `keepdim` is `True`, both the `values` and `indices` tensors are the same size as `input`, except in the dimension `dim` where they are of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in both the `values` and `indices` tensors having 1 fewer dimension than the `input` tensor.

Note

When `input` is a CUDA tensor and there are multiple valid `k` th values, this function may nondeterministically return `indices` for any of them.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **k** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – k for the k-th smallest element
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to find the kth value along
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
_,_ _optional_) – the output tuple of (Tensor, LongTensor) can be optionally given to be used as output buffers

Example:

\>>> x \= torch.arange(1., 6.)
\>>> x
tensor(\[ 1.,  2.,  3.,  4.,  5.\])
\>>> torch.kthvalue(x, 4)
torch.return\_types.kthvalue(values=tensor(4.), indices=tensor(3))

\>>> x\=torch.arange(1.,7.).resize\_(2,3)
\>>> x
tensor(\[\[ 1.,  2.,  3.\],\
        \[ 4.,  5.,  6.\]\])
\>>> torch.kthvalue(x, 2, 0, True)
torch.return\_types.kthvalue(values=tensor(\[\[4., 5., 6.\]\]), indices=tensor(\[\[1, 1, 1\]\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.kthvalue.rst.txt)

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