Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.median.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.median.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.median.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.median.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.median.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.median.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.median.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.median.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.median.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.median.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.median.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.median.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.median.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.median.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.median.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.median.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.median.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.median.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.median.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.median.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.median.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.median.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.median.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.median.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.median.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.median.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.median.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.median.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.median.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.median.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.median.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.median.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.median.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.median.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.median.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.median.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.median.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.median.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.median.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.median.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.median.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.median.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.median.html)

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

torch.median[#](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch-median "Link to this heading")

====================================================================================================================

torch.median(_input_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "Link to this definition")

Returns the median of the values in `input`.

Note

The median is not unique for `input` tensors with an even number of elements. In this case the lower of the two medians is returned. To compute the mean of both medians, use [`torch.quantile()`](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch.quantile "torch.quantile")
 with `q=0.5` instead.

Warning

This function produces deterministic (sub)gradients unlike `median(dim=0)`

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Example:

\>>> a \= torch.randn(1, 3)
\>>> a
tensor(\[\[ 1.5219, -1.5212,  0.2202\]\])
\>>> torch.median(a)
tensor(0.2202)

Copy to clipboard

torch.median(_input_, _dim\=\-1_, _keepdim\=False_, _\*_, _out\=None_)

Returns a namedtuple `(values, indices)` where `values` contains the median of each row of `input` in the dimension `dim`, and `indices` contains the index of the median values found in the dimension `dim`.

By default, `dim` is the last dimension of the `input` tensor.

If `keepdim` is `True`, the output tensors are of the same size as `input` except in the dimension `dim` where they are of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the outputs tensor having 1 fewer dimension than `input`.

Note

The median is not unique for `input` tensors with an even number of elements in the dimension `dim`. In this case the lower of the two medians is returned. To compute the mean of both medians in `input`, use [`torch.quantile()`](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch.quantile "torch.quantile")
 with `q=0.5` instead.

Warning

`indices` does not necessarily contain the first occurrence of each median value found, unless it is unique. The exact implementation details are device-specific. Do not expect the same result when run on CPU and GPU in general. For the same reason do not expect the gradients to be deterministic.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to reduce. If `None`, all dimensions are reduced.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**out** (_(_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_)__,_ _optional_) – The first tensor will be populated with the median values and the second tensor, which must have dtype long, with their indices in the dimension `dim` of `input`.

Example:

\>>> a \= torch.randn(4, 5)
\>>> a
tensor(\[\[ 0.2505, -0.3982, -0.9948,  0.3518, -1.3131\],\
        \[ 0.3180, -0.6993,  1.0436,  0.0438,  0.2270\],\
        \[-0.2751,  0.7303,  0.2192,  0.3321,  0.2488\],\
        \[ 1.0778, -1.9510,  0.7048,  0.4742, -0.7125\]\])
\>>> torch.median(a, 1)
torch.return\_types.median(values=tensor(\[-0.3982,  0.2270,  0.2488,  0.4742\]), indices=tensor(\[1, 4, 4, 3\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.median.rst.txt)

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