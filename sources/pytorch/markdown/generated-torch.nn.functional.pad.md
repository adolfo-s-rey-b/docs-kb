Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.functional.pad.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.pad.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.pad.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.functional.pad.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.pad.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.functional.pad.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.functional.pad.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.pad.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.functional.pad.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.functional.pad.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.functional.pad.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.functional.pad.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.functional.pad.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.functional.pad.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.functional.pad.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.functional.pad.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.functional.pad.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.functional.pad.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.functional.pad.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.functional.pad.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.functional.pad.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.functional.pad.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.functional.pad.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.functional.pad.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.functional.pad.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.functional.pad.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.functional.pad.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.functional.pad.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.functional.pad.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.functional.pad.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.functional.pad.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.functional.pad.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.functional.pad.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.functional.pad.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.functional.pad.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.functional.pad.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.functional.pad.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.functional.pad.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.functional.pad.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.functional.pad.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.functional.pad.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.functional.pad.html)

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

torch.nn.functional.pad[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#torch-nn-functional-pad "Link to this heading")

=====================================================================================================================================================

torch.nn.functional.pad(_input_, _pad_, _mode\='constant'_, _value\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/functional.py#L5808)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#torch.nn.functional.pad "Link to this definition")

Pads tensor.

Padding size:

The padding size by which to pad some dimensions of `input` are described starting from the last dimension and moving forward. ⌊len(pad)2⌋\\left\\lfloor\\frac{\\text{len(pad)}}{2}\\right\\rfloor⌊2len(pad)​⌋ dimensions of `input` will be padded. For example, to pad only the last dimension of the input tensor, then [`pad`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#torch.nn.functional.pad "torch.nn.functional.pad")
 has the form (padding\_left,padding\_right)(\\text{padding\\\_left}, \\text{padding\\\_right})(padding\_left,padding\_right); to pad the last 2 dimensions of the input tensor, then use (padding\_left,padding\_right,(\\text{padding\\\_left}, \\text{padding\\\_right},(padding\_left,padding\_right, padding\_top,padding\_bottom)\\text{padding\\\_top}, \\text{padding\\\_bottom})padding\_top,padding\_bottom); to pad the last 3 dimensions, use (padding\_left,padding\_right,(\\text{padding\\\_left}, \\text{padding\\\_right},(padding\_left,padding\_right, padding\_top,padding\_bottom\\text{padding\\\_top}, \\text{padding\\\_bottom}padding\_top,padding\_bottom padding\_front,padding\_back)\\text{padding\\\_front}, \\text{padding\\\_back})padding\_front,padding\_back).

Padding mode:

See [`torch.nn.CircularPad2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CircularPad2d.html#torch.nn.CircularPad2d "torch.nn.CircularPad2d")
, [`torch.nn.ConstantPad2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.ConstantPad2d.html#torch.nn.ConstantPad2d "torch.nn.ConstantPad2d")
, [`torch.nn.ReflectionPad2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.ReflectionPad2d.html#torch.nn.ReflectionPad2d "torch.nn.ReflectionPad2d")
, and [`torch.nn.ReplicationPad2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.ReplicationPad2d.html#torch.nn.ReplicationPad2d "torch.nn.ReplicationPad2d")
 for concrete examples on how each of the padding modes works. Constant padding is implemented for arbitrary dimensions. Circular, replicate and reflection padding are implemented for padding the last 3 dimensions of a 4D or 5D input tensor, the last 2 dimensions of a 3D or 4D input tensor, or the last dimension of a 2D or 3D input tensor.

Note

When using the CUDA backend, this operation may induce nondeterministic behaviour in its backward pass that is not easily switched off. Please see the notes on [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for background.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – N-dimensional tensor
    
*   **pad** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – m-elements tuple, where m2≤\\frac{m}{2} \\leq2m​≤ input dimensions and mmm is even.
    
*   **mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – `'constant'`, `'reflect'`, `'replicate'` or `'circular'`. Default: `'constant'`
    
*   **value** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – fill value for `'constant'` padding. Default: `0`
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples:

\>>> t4d \= torch.empty(3, 3, 4, 2)
\>>> p1d \= (1, 1) \# pad last dim by 1 on each side
\>>> out \= F.pad(t4d, p1d, "constant", 0)  \# effectively zero padding
\>>> print(out.size())
torch.Size(\[3, 3, 4, 4\])
\>>> p2d \= (1, 1, 2, 2) \# pad last dim by (1, 1) and 2nd to last by (2, 2)
\>>> out \= F.pad(t4d, p2d, "constant", 0)
\>>> print(out.size())
torch.Size(\[3, 3, 8, 4\])
\>>> t4d \= torch.empty(3, 3, 4, 2)
\>>> p3d \= (0, 1, 2, 1, 3, 3) \# pad by (0, 1), (2, 1), and (3, 3)
\>>> out \= F.pad(t4d, p3d, "constant", 0)
\>>> print(out.size())
torch.Size(\[3, 9, 7, 3\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.functional.pad.rst.txt)

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