Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cross.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cross.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cross.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cross.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cross.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cross.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cross.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cross.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cross.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cross.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cross.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cross.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cross.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cross.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cross.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cross.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cross.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cross.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cross.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cross.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cross.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cross.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cross.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cross.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cross.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cross.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cross.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cross.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cross.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cross.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cross.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cross.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cross.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cross.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cross.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cross.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cross.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cross.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cross.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cross.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cross.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cross.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cross.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cross.html)

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

torch.cross[#](https://docs.pytorch.org/docs/2.15/generated/torch.cross.html#torch-cross "Link to this heading")

=================================================================================================================

torch.cross(_input_, _other_, _dim\=None_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cross.html#torch.cross "Link to this definition")

Returns the cross product of vectors in dimension `dim` of `input` and `other`.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches of vectors, for which it computes the product along the dimension `dim`. In this case, the output has the same batch dimensions as the inputs.

Warning

If `dim` is not given, it defaults to the first dimension found with the size 3. Note that this might be unexpected.

This behavior is deprecated and will be changed to match that of [`torch.linalg.cross()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cross.html#torch.linalg.cross "torch.linalg.cross")
 in a future release.

See also

[`torch.linalg.cross()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.cross.html#torch.linalg.cross "torch.linalg.cross")
 which has dim=-1 as default.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second input tensor
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the dimension to take the cross-product in.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.randn(4, 3)
\>>> a
tensor(\[\[-0.3956,  1.1455,  1.6895\],\
        \[-0.5849,  1.3672,  0.3599\],\
        \[-1.1626,  0.7180, -0.0521\],\
        \[-0.1339,  0.9902, -2.0225\]\])
\>>> b \= torch.randn(4, 3)
\>>> b
tensor(\[\[-0.0257, -1.4725, -1.2251\],\
        \[-1.1479, -0.7005, -1.9757\],\
        \[-1.3904,  0.3726, -1.1836\],\
        \[-0.9688, -0.7153,  0.2159\]\])
\>>> torch.cross(a, b, dim\=1)
tensor(\[\[ 1.0844, -0.5281,  0.6120\],\
        \[-2.4490, -1.5687,  1.9792\],\
        \[-0.8304, -1.3037,  0.5650\],\
        \[-1.2329,  1.9883,  1.0551\]\])
\>>> torch.cross(a, b)
tensor(\[\[ 1.0844, -0.5281,  0.6120\],\
        \[-2.4490, -1.5687,  1.9792\],\
        \[-0.8304, -1.3037,  0.5650\],\
        \[-1.2329,  1.9883,  1.0551\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cross.rst.txt)

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