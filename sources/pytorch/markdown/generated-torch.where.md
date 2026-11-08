Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.where.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.where.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.where.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.where.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.where.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.where.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.where.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.where.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.where.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.where.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.where.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.where.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.where.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.where.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.where.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.where.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.where.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.where.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.where.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.where.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.where.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.where.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.where.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.where.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.where.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.where.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.where.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.where.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.where.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.where.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.where.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.where.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.where.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.where.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.where.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.where.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.where.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.where.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.where.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.where.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.where.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.where.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.where.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.where.html)

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

torch.where[#](https://docs.pytorch.org/docs/2.15/generated/torch.where.html#torch-where "Link to this heading")

=================================================================================================================

torch.where(_condition_, _input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.where.html#torch.where "Link to this definition")

Return a tensor of elements selected from either `input` or `other`, depending on `condition`.

The operation is defined as:

outi\={inputiif conditioniotheriotherwise\\text{out}\_i = \\begin{cases} \\text{input}\_i & \\text{if } \\text{condition}\_i \\\\ \\text{other}\_i & \\text{otherwise} \\\\ \\end{cases} outi​\={inputi​otheri​​if conditioni​otherwise​

Note

The tensors `condition`, `input`, `other` must be [broadcastable](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
.

Parameters:

*   **condition** (_BoolTensor_) – When True (nonzero), yield input, otherwise yield other
    
*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Scalar_) – value (if `input` is a scalar) or values selected at indices where `condition` is `True`
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Scalar_) – value (if `other` is a scalar) or values selected at indices where `condition` is `False`
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Returns:

A tensor of shape equal to the broadcasted shape of `condition`, `input`, `other`

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> x \= torch.randn(3, 2)
\>>> y \= torch.ones(3, 2)
\>>> x
tensor(\[\[-0.4620,  0.3139\],\
        \[ 0.3898, -0.7197\],\
        \[ 0.0478, -0.1657\]\])
\>>> torch.where(x \> 0, 1.0, 0.0)
tensor(\[\[0., 1.\],\
        \[1., 0.\],\
        \[1., 0.\]\])
\>>> torch.where(x \> 0, x, y)
tensor(\[\[ 1.0000,  0.3139\],\
        \[ 0.3898,  1.0000\],\
        \[ 0.0478,  1.0000\]\])
\>>> x \= torch.randn(2, 2, dtype\=torch.double)
\>>> x
tensor(\[\[ 1.0779,  0.0383\],\
        \[-0.8785, -1.1089\]\], dtype=torch.float64)
\>>> torch.where(x \> 0, x, 0.)
tensor(\[\[1.0779, 0.0383\],\
        \[0.0000, 0.0000\]\], dtype=torch.float64)

Copy to clipboard

torch.where(_condition_) → tuple of LongTensor

`torch.where(condition)` is identical to `torch.nonzero(condition, as_tuple=True)`.

Note

See also [`torch.nonzero()`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero")
.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.where.rst.txt)

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