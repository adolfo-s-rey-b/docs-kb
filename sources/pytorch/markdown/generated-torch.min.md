Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.min.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.min.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.min.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.min.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.min.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.min.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.min.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.min.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.min.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.min.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.min.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.min.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.min.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.min.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.min.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.min.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.min.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.min.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.min.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.min.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.min.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.min.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.min.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.min.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.min.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.min.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.min.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.min.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.min.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.min.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.min.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.min.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.min.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.min.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.min.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.min.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.min.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.min.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.min.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.min.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.min.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.min.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.min.html)

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

torch.min[#](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch-min "Link to this heading")

===========================================================================================================

torch.min(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "Link to this definition")

Returns the minimum value of all elements in the `input` tensor.

Note

The difference between `max`/`min` and `amax`/`amin` is:

*   `amax`/`amin` supports reducing on multiple dimensions,
    
*   `amax`/`amin` does not return indices.
    

Both `amax`/`amin` evenly distribute gradients between equal values when there are multiple input elements with the same minimum or maximum value.

For `max`/`min`:

*   If reduce over all dimensions(no dim specified), gradients evenly distribute between equally `max`/`min` values.
    
*   If reduce over one specified axis, only propagate to the indexed element.
    

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.randn(1, 3)
\>>> a
tensor(\[\[ 0.6750,  1.0857,  1.7197\]\])
\>>> torch.min(a)
tensor(0.6750)

Copy to clipboard

torch.min(_input_, _dim_, _keepdim\=False_, _\*_, _out\=None_)

Returns a namedtuple `(values, indices)` where `values` is the minimum value of each row of the `input` tensor in the given dimension `dim`. And `indices` is the index location of each minimum value found (argmin).

If `keepdim` is `True`, the output tensors are of the same size as `input` except in the dimension `dim` where they are of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the output tensors having 1 fewer dimension than `input`.

Note

If there are multiple minimal values in a reduced row then the indices of the first minimal value are returned.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to reduce. If omitted, all dimensions are reduced. Explicit `None` is not supported.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    

Keyword Arguments:

**out** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
_,_ _optional_) – the tuple of two output tensors (min, min\_indices)

Example:

\>>> a \= torch.randn(4, 4)
\>>> a
tensor(\[\[-0.6248,  1.1334, -1.1899, -0.2803\],\
        \[-1.4644, -0.2635, -0.3651,  0.6134\],\
        \[ 0.2457,  0.0384,  1.0128,  0.7015\],\
        \[-0.1153,  2.9849,  2.1458,  0.5788\]\])
\>>> torch.min(a, 1)
torch.return\_types.min(values=tensor(\[-1.1899, -1.4644,  0.0384, -0.1153\]), indices=tensor(\[2, 0, 1, 0\]))

Copy to clipboard

torch.min(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

See [`torch.minimum()`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum")
.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.min.rst.txt)

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