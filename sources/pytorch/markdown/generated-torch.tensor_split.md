Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.tensor_split.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.tensor_split.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.tensor_split.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.tensor_split.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.tensor_split.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.tensor_split.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.tensor_split.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.tensor_split.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.tensor_split.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.tensor_split.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.tensor_split.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.tensor_split.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.tensor_split.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.tensor_split.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.tensor_split.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.tensor_split.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.tensor_split.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.tensor_split.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.tensor_split.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.tensor_split.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.tensor_split.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.tensor_split.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.tensor_split.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.tensor_split.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.tensor_split.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.tensor_split.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.tensor_split.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.tensor_split.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.tensor_split.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.tensor_split.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.tensor_split.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.tensor_split.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.tensor_split.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.tensor_split.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.tensor_split.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.tensor_split.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.tensor_split.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.tensor_split.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.tensor_split.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.tensor_split.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.tensor_split.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.tensor_split.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.tensor_split.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.tensor_split.html)

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

torch.tensor\_split[#](https://docs.pytorch.org/docs/2.15/generated/torch.tensor_split.html#torch-tensor-split "Link to this heading")

=======================================================================================================================================

torch.tensor\_split(_input_, _indices\_or\_sections_, _dim\=0_) → List of Tensors[#](https://docs.pytorch.org/docs/2.15/generated/torch.tensor_split.html#torch.tensor_split "Link to this definition")

Splits a tensor into multiple sub-tensors, all of which are views of `input`, along dimension `dim` according to the indices or number of sections specified by `indices_or_sections`. This function is based on NumPy’s [`numpy.array_split()`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "(in NumPy v2.5)")
.

torch.tensor\_split(_input_, _sections_, _dim\=0_) → List of Tensors

Splits `input` into `sections` sections along dimension `dim`. If `input` is divisible by `sections` along dimension `dim`, each section will be of equal size, `input.size(dim) / sections`. If `input` is not divisible by `sections`, the sizes of the first `int(input.size(dim) % sections)` sections will have size `int(input.size(dim) / sections) + 1`, and the rest will have size `int(input.size(dim) / sections)`.

`sections` can also be a zero-dimensional long tensor.

torch.tensor\_split(_input_, _indices_, _dim\=0_) → List of Tensors

Splits `input` along dimension `dim` at each of the indices in `indices`. For instance, `indices=[2, 3]` and `dim=0` would result in the tensors `input[:2]`, `input[2:3]`, and `input[3:]`.

`indices` can be a list or tuple of ints, or a one-dimensional long tensor on the CPU.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to split
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – dimension along which to split the tensor. Default: `0`
    

Example:

\>>> x \= torch.arange(8)
\>>> torch.tensor\_split(x, 3)
(tensor(\[0, 1, 2\]), tensor(\[3, 4, 5\]), tensor(\[6, 7\]))

\>>> x \= torch.arange(7)
\>>> torch.tensor\_split(x, 3)
(tensor(\[0, 1, 2\]), tensor(\[3, 4\]), tensor(\[5, 6\]))
\>>> torch.tensor\_split(x, (1, 6))
(tensor(\[0\]), tensor(\[1, 2, 3, 4, 5\]), tensor(\[6\]))

\>>> x \= torch.arange(14).reshape(2, 7)
\>>> x
tensor(\[\[ 0,  1,  2,  3,  4,  5,  6\],\
        \[ 7,  8,  9, 10, 11, 12, 13\]\])
\>>> torch.tensor\_split(x, 3, dim\=1)
(tensor(\[\[0, 1, 2\],\
        \[7, 8, 9\]\]),
 tensor(\[\[ 3,  4\],\
        \[10, 11\]\]),
 tensor(\[\[ 5,  6\],\
        \[12, 13\]\]))
\>>> torch.tensor\_split(x, (1, 6), dim\=1)
(tensor(\[\[0\],\
        \[7\]\]),
 tensor(\[\[ 1,  2,  3,  4,  5\],\
        \[ 8,  9, 10, 11, 12\]\]),
 tensor(\[\[ 6\],\
        \[13\]\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.tensor_split.rst.txt)

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