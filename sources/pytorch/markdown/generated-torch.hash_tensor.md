Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.hash_tensor.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.hash_tensor.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.hash_tensor.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.hash_tensor.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.hash_tensor.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.hash_tensor.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.hash_tensor.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.hash_tensor.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.hash_tensor.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.hash_tensor.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.hash_tensor.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.hash_tensor.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.hash_tensor.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.hash_tensor.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.hash_tensor.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.hash_tensor.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.hash_tensor.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.hash_tensor.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.hash_tensor.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.hash_tensor.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.hash_tensor.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.hash_tensor.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.hash_tensor.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.hash_tensor.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.hash_tensor.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.hash_tensor.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.hash_tensor.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.hash_tensor.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.hash_tensor.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.hash_tensor.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.hash_tensor.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.hash_tensor.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.hash_tensor.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.hash_tensor.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.hash_tensor.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.hash_tensor.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.hash_tensor.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.hash_tensor.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.hash_tensor.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.hash_tensor.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.hash_tensor.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.hash_tensor.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.hash_tensor.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.hash_tensor.html)

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

torch.hash\_tensor[#](https://docs.pytorch.org/docs/2.15/generated/torch.hash_tensor.html#torch-hash-tensor "Link to this heading")

====================================================================================================================================

torch.hash\_tensor(_input_, _\*_, _mode\=0_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.hash_tensor.html#torch.hash_tensor "Link to this definition")

Returns a hash of all elements in the `input` tensor.

Currently only mode=0 (reduction via xor) is supported. The output will always be of type `torch.uint64`. The elements of `input` are upcasted to their 64 bit float / integer equivalent and bitcasted to `torch.uint64` before reduction via xor.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**mode** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – The hash to use. Default: 0 (xor\_reduction)

Example:

\>>> a \= torch.randn(1, 3)
\>>> a
tensor(\[\[ 1.1918, -1.1813,  0.3373\]\])
\>>> torch.hash\_tensor(a)
tensor(13822780554648485888, dtype=torch.uint64)

Copy to clipboard

torch.hash\_tensor(_input_, _dim_, _\*_, _keepdim\=False_, _mode\=0_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Returns the hash of each row of the `input` tensor in the given dimension `dim` given by mode. If `dim` is a list of dimensions, reduce over all of them.

If `keepdim` is `True`, the output tensor is of the same size as `input` except in the dimension(s) `dim` where it is of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints__,_ _optional_) – the dimension or dimensions to reduce. If `None`, all dimensions are reduced.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**mode** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – The hash to use. Default: 0 (xor\_reduction)

Example:

\>>> a \= torch.randn(2, 4)
\>>> a
tensor(\[\[ 0.1317, -0.5554, -1.4724, -1.1391\],\
        \[ 0.0778, -0.6070,  0.6375,  0.1798\]\])
\>>> torch.hash\_tensor(a, 1)
tensor(\[9233691267014066176, 9255993250844508160\], dtype=torch.uint64)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.hash_tensor.rst.txt)

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