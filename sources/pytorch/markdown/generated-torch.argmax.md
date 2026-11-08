Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.argmax.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.argmax.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.argmax.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.argmax.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.argmax.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.argmax.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.argmax.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.argmax.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.argmax.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.argmax.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.argmax.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.argmax.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.argmax.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.argmax.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.argmax.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.argmax.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.argmax.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.argmax.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.argmax.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.argmax.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.argmax.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.argmax.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.argmax.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.argmax.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.argmax.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.argmax.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.argmax.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.argmax.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.argmax.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.argmax.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.argmax.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.argmax.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.argmax.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.argmax.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.argmax.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.argmax.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.argmax.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.argmax.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.argmax.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.argmax.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.argmax.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.argmax.html)

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

torch.argmax[#](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#torch-argmax "Link to this heading")

====================================================================================================================

torch.argmax(_input_) → LongTensor[#](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#torch.argmax "Link to this definition")

Returns the indices of the maximum value of all elements in the `input` tensor.

This is the second value returned by [`torch.max()`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")
. See its documentation for the exact semantics of this method.

Note

If there are multiple maximal values then the indices of the first maximal value are returned.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Example:

\>>> a \= torch.randn(4, 4)
\>>> a
tensor(\[\[ 1.3398,  0.2663, -0.2686,  0.2450\],\
        \[-0.7401, -0.8805, -0.3402, -1.1936\],\
        \[ 0.4907, -1.3948, -1.0691, -0.3132\],\
        \[-1.6092,  0.5419, -0.2993,  0.3195\]\])
\>>> torch.argmax(a)
tensor(0)

Copy to clipboard

torch.argmax(_input_, _dim_, _keepdim\=False_) → LongTensor

Returns the indices of the maximum values of a tensor across a dimension.

This is the second value returned by [`torch.max()`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")
. See its documentation for the exact semantics of this method.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **dim** – the dimension to reduce.
    

Example:

\>>> a \= torch.randn(4, 4)
\>>> a
tensor(\[\[ 1.3398,  0.2663, -0.2686,  0.2450\],\
        \[-0.7401, -0.8805, -0.3402, -1.1936\],\
        \[ 0.4907, -1.3948, -1.0691, -0.3132\],\
        \[-1.6092,  0.5419, -0.2993,  0.3195\]\])
\>>> torch.argmax(a, dim\=1)
tensor(\[ 0,  2,  0,  1\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.argmax.rst.txt)

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