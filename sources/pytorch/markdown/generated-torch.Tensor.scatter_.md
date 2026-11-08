Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.scatter_.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.scatter_.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.scatter_.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.scatter_.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.scatter_.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.scatter_.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.scatter_.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.scatter_.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.scatter_.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.scatter_.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.scatter_.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.scatter_.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.scatter_.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.scatter_.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.scatter_.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.scatter_.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.scatter_.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.scatter_.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.scatter_.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.scatter_.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.scatter_.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.scatter_.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.scatter_.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.scatter_.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.scatter_.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.scatter_.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.scatter_.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.scatter_.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.scatter_.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.scatter_.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.scatter_.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.scatter_.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.scatter_.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.scatter_.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.scatter_.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.scatter_.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.scatter_.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.scatter_.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.scatter_.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.scatter_.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.scatter_.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.scatter_.html)

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

torch.Tensor.scatter\_[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_.html#torch-tensor-scatter "Link to this heading")

===============================================================================================================================================

Tensor.scatter\_(_dim_, _index_, _src_, _\*_, _reduce\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_ "Link to this definition")

Writes all values from the tensor `src` into `self` at the indices specified in the `index` tensor. For each value in `src`, its output index is specified by its index in `src` for `dimension != dim` and by the corresponding value in `index` for `dimension = dim`.

For a 3-D tensor, `self` is updated as:

self\[index\[i\]\[j\]\[k\]\]\[j\]\[k\] \= src\[i\]\[j\]\[k\]  \# if dim == 0
self\[i\]\[index\[i\]\[j\]\[k\]\]\[k\] \= src\[i\]\[j\]\[k\]  \# if dim == 1
self\[i\]\[j\]\[index\[i\]\[j\]\[k\]\] \= src\[i\]\[j\]\[k\]  \# if dim == 2

Copy to clipboard

This is the reverse operation of the manner described in [`gather()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.gather.html#torch.Tensor.gather "torch.Tensor.gather")
.

It is also required that `index.size(d) <= src.size(d)` for all dimensions `d`, and that `index.size(d) <= self.size(d)` for all dimensions `d != dim`. Note that `input` and `index` do not broadcast against each other for NPUs, so when running on NPUs, `input` and `index` must have the same number of dimensions. Standard broadcasting occurs in all other cases.

Moreover, as for [`gather()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.gather.html#torch.Tensor.gather "torch.Tensor.gather")
, the values of `index` must be between `0` and `self.size(dim) - 1` inclusive.

Warning

When indices are not unique, the behavior is non-deterministic (one of the values from `src` will be picked arbitrarily) and the gradient will be incorrect (it will be propagated to all locations in the source that correspond to the same index)!

Note

The backward pass is implemented only for `src.shape == index.shape`.

Additionally accepts an optional `reduce` argument that allows specification of an optional reduction operation, which is applied to all values in the tensor `src` into `self` at the indices specified in the `index`. For each value in `src`, the reduction operation is applied to an index in `self` which is specified by its index in `src` for `dimension != dim` and by the corresponding value in `index` for `dimension = dim`.

Given a 3-D tensor and reduction using the multiplication operation, `self` is updated as:

self\[index\[i\]\[j\]\[k\]\]\[j\]\[k\] \*= src\[i\]\[j\]\[k\]  \# if dim == 0
self\[i\]\[index\[i\]\[j\]\[k\]\]\[k\] \*= src\[i\]\[j\]\[k\]  \# if dim == 1
self\[i\]\[j\]\[index\[i\]\[j\]\[k\]\] \*= src\[i\]\[j\]\[k\]  \# if dim == 2

Copy to clipboard

Reducing with the addition operation is the same as using [`scatter_add_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_ "torch.Tensor.scatter_add_")
.

Warning

The reduce argument with Tensor `src` is deprecated and will be removed in a future PyTorch release. Please use [`scatter_reduce_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_ "torch.Tensor.scatter_reduce_")
 instead for more reduction options.

Parameters:

*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the axis along which to index
    
*   **index** (_LongTensor_) – the indices of elements to scatter, can be either empty or of the same dimensionality as `src`. When empty, the operation returns `self` unchanged.
    
*   **src** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the source element(s) to scatter.
    

Keyword Arguments:

**reduce** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_,_ _optional_) – reduction operation to apply, can be either `'add'` or `'multiply'`.

Example:

\>>> src \= torch.arange(1, 11).reshape((2, 5))
\>>> src
tensor(\[\[ 1,  2,  3,  4,  5\],\
        \[ 6,  7,  8,  9, 10\]\])
\>>> index \= torch.tensor(\[\[0, 1, 2, 0\]\])
\>>> torch.zeros(3, 5, dtype\=src.dtype).scatter\_(0, index, src)
tensor(\[\[1, 0, 0, 4, 0\],\
        \[0, 2, 0, 0, 0\],\
        \[0, 0, 3, 0, 0\]\])
\>>> index \= torch.tensor(\[\[0, 1, 2\], \[0, 1, 4\]\])
\>>> torch.zeros(3, 5, dtype\=src.dtype).scatter\_(1, index, src)
tensor(\[\[1, 2, 3, 0, 0\],\
        \[6, 7, 0, 0, 8\],\
        \[0, 0, 0, 0, 0\]\])

\>>> torch.full((2, 4), 2.).scatter\_(1, torch.tensor(\[\[2\], \[3\]\]),
...            1.23, reduce\='multiply')
tensor(\[\[2.0000, 2.0000, 2.4600, 2.0000\],\
        \[2.0000, 2.0000, 2.0000, 2.4600\]\])
\>>> torch.full((2, 4), 2.).scatter\_(1, torch.tensor(\[\[2\], \[3\]\]),
...            1.23, reduce\='add')
tensor(\[\[2.0000, 2.0000, 3.2300, 2.0000\],\
        \[2.0000, 2.0000, 2.0000, 3.2300\]\])

Copy to clipboard

scatter\_(_dim_, _index_, _value_, _\*_, _reduce\=None_) → Tensor:

Writes the value from `value` into `self` at the indices specified in the `index` tensor. This operation is equivalent to the previous version, with the `src` tensor filled entirely with `value`.

Parameters:

*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the axis along which to index
    
*   **index** (_LongTensor_) – the indices of elements to scatter, can be either empty or of the same dimensionality as `src`. When empty, the operation returns `self` unchanged.
    
*   **value** (_Scalar_) – the value to scatter.
    

Keyword Arguments:

**reduce** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_,_ _optional_) – reduction operation to apply, can be either `'add'` or `'multiply'`.

Example:

\>>> index \= torch.tensor(\[\[0, 1\]\])
\>>> value \= 2
\>>> torch.zeros(3, 5).scatter\_(0, index, value)
tensor(\[\[2., 0., 0., 0., 0.\],\
        \[0., 2., 0., 0., 0.\],\
        \[0., 0., 0., 0., 0.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.scatter_.rst.txt)

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