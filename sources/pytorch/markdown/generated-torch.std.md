Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.std.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.std.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.std.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.std.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.std.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.std.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.std.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.std.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.std.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.std.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.std.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.std.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.std.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.std.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.std.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.std.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.std.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.std.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.std.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.std.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.std.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.std.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.std.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.std.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.std.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.std.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.std.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.std.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.std.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.std.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.std.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.std.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.std.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.std.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.std.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.std.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.std.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.std.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.std.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.std.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.std.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.std.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.std.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.std.html)

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

torch.std[#](https://docs.pytorch.org/docs/2.15/generated/torch.std.html#torch-std "Link to this heading")

===========================================================================================================

torch.std(_input_, _dim\=None_, _\*_, _correction\=1_, _keepdim\=False_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.std.html#torch.std "Link to this definition")

Calculates the standard deviation over the dimensions specified by `dim`. `dim` can be a single dimension, list of dimensions, or `None` to reduce over all dimensions.

The standard deviation (σ\\sigmaσ) is calculated as

σ\=1max⁡(0, N−δN)∑i\=0N−1(xi−xˉ)2\\sigma = \\sqrt{\\frac{1}{\\max(0,~N - \\delta N)}\\sum\_{i=0}^{N-1}(x\_i-\\bar{x})^2} σ\=max(0, N−δN)1​i\=0∑N−1​(xi​−xˉ)2​

where xxx is the sample set of elements, xˉ\\bar{x}xˉ is the sample mean, NNN is the number of samples and δN\\delta NδN is the `correction`.

If `keepdim` is `True`, the output tensor is of the same size as `input` except in the dimension(s) `dim` where it is of size 1. Otherwise, `dim` is squeezed (see [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")
), resulting in the output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _ints__,_ _optional_) – the dimension or dimensions to reduce. If `None`, all dimensions are reduced.
    

Keyword Arguments:

*   **correction** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) –
    
    difference between the sample size and sample degrees of freedom. Defaults to [Bessel’s correction](https://en.wikipedia.org/wiki/Bessel%27s_correction)
    , `correction=1`.
    
    Changed in version 2.0: Previously this argument was called `unbiased` and was a boolean with `True` corresponding to `correction=1` and `False` being `correction=0`.
    
*   **keepdim** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether the output tensor has `dim` retained or not. Default: `False`.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example

\>>> a \= torch.tensor(
...     \[\[ 0.2035,  1.2959,  1.8101, \-0.4644\],\
...      \[ 1.5027, \-0.3270,  0.5905,  0.6538\],\
...      \[\-1.5745,  1.3330, \-0.5596, \-0.6548\],\
...      \[ 0.1264, \-0.5080,  1.6420,  0.1992\]\]
... )  \# fmt: skip
\>>> torch.std(a, dim\=1, keepdim\=True)
tensor(\[\[1.0311\],\
        \[0.7477\],\
        \[1.2204\],\
        \[0.9087\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.std.rst.txt)

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