Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Upsample.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Upsample.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Upsample.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Upsample.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Upsample.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Upsample.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Upsample.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Upsample.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Upsample.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Upsample.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Upsample.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Upsample.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Upsample.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Upsample.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Upsample.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Upsample.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Upsample.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Upsample.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Upsample.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Upsample.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Upsample.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Upsample.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Upsample.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Upsample.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Upsample.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Upsample.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Upsample.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Upsample.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Upsample.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Upsample.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Upsample.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Upsample.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Upsample.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Upsample.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Upsample.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Upsample.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Upsample.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Upsample.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Upsample.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Upsample.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Upsample.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Upsample.html)

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

Upsample[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html#upsample "Link to this heading")

=================================================================================================================

_class_ torch.nn.Upsample(_size\=None_, _scale\_factor\=None_, _mode\='nearest'_, _align\_corners\=None_, _recompute\_scale\_factor\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/upsampling.py#L13)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html#torch.nn.Upsample "Link to this definition")

Upsamples a given multi-channel 1D (temporal), 2D (spatial) or 3D (volumetric) data.

The input data is assumed to be of the form minibatch x channels x \[optional depth\] x \[optional height\] x width. Hence, for spatial inputs, we expect a 4D Tensor and for volumetric inputs, we expect a 5D Tensor.

The algorithms available for upsampling are nearest neighbor and linear, bilinear, bicubic and trilinear for 3D, 4D and 5D input Tensor, respectively.

One can either give a `scale_factor` or the target output `size` to calculate the output size. (You cannot give both, as it is ambiguous)

Parameters:

*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _optional_) – output spatial sizes
    
*   **scale\_factor** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ _Tuple__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _,_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]__,_ _optional_) – multiplier for spatial size. Has to match input size if it is a tuple.
    
*   **mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – the upsampling algorithm: one of `'nearest'`, `'linear'`, `'bilinear'`, `'bicubic'` and `'trilinear'`. Default: `'nearest'`
    
*   **align\_corners** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, the corner pixels of the input and output tensors are aligned, and thus preserving the values at those pixels. This only has effect when `mode` is `'linear'`, `'bilinear'`, `'bicubic'`, or `'trilinear'`. Default: `False`
    
*   **recompute\_scale\_factor** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – recompute the scale\_factor for use in the interpolation calculation. If recompute\_scale\_factor is `True`, then scale\_factor must be passed in and scale\_factor is used to compute the output size. The computed output size will be used to infer new scales for the interpolation. Note that when scale\_factor is floating-point, it may differ from the recomputed scale\_factor due to rounding and precision issues. If recompute\_scale\_factor is `False`, then size or scale\_factor will be used directly for interpolation.
    

Shape:

*   Input: (N,C,Win)(N, C, W\_{in})(N,C,Win​), (N,C,Hin,Win)(N, C, H\_{in}, W\_{in})(N,C,Hin​,Win​) or (N,C,Din,Hin,Win)(N, C, D\_{in}, H\_{in}, W\_{in})(N,C,Din​,Hin​,Win​)
    
*   Output: (N,C,Wout)(N, C, W\_{out})(N,C,Wout​), (N,C,Hout,Wout)(N, C, H\_{out}, W\_{out})(N,C,Hout​,Wout​) or (N,C,Dout,Hout,Wout)(N, C, D\_{out}, H\_{out}, W\_{out})(N,C,Dout​,Hout​,Wout​), where
    

Dout\=⌊Din×scale\_factor⌋D\_{out} = \\left\\lfloor D\_{in} \\times \\text{scale\\\_factor} \\right\\rfloor Dout​\=⌊Din​×scale\_factor⌋

Hout\=⌊Hin×scale\_factor⌋H\_{out} = \\left\\lfloor H\_{in} \\times \\text{scale\\\_factor} \\right\\rfloor Hout​\=⌊Hin​×scale\_factor⌋

Wout\=⌊Win×scale\_factor⌋W\_{out} = \\left\\lfloor W\_{in} \\times \\text{scale\\\_factor} \\right\\rfloor Wout​\=⌊Win​×scale\_factor⌋

Warning

With `align_corners = True`, the linearly interpolating modes (linear, bilinear, bicubic, and trilinear) don’t proportionally align the output and input pixels, and thus the output values can depend on the input size. This was the default behavior for these modes up to version 0.3.1. Since then, the default behavior is `align_corners = False`. See below for concrete examples on how this affects the outputs.

Note

If you want downsampling/general resizing, you should use `interpolate()`.

Examples:

\>>> input \= torch.arange(1, 5, dtype\=torch.float32).view(1, 1, 2, 2)
\>>> input
tensor(\[\[\[\[1., 2.\],\
          \[3., 4.\]\]\]\])

\>>> m \= nn.Upsample(scale\_factor\=2, mode\='nearest')
\>>> m(input)
tensor(\[\[\[\[1., 1., 2., 2.\],\
          \[1., 1., 2., 2.\],\
          \[3., 3., 4., 4.\],\
          \[3., 3., 4., 4.\]\]\]\])

\>>> m \= nn.Upsample(scale\_factor\=2, mode\='bilinear')  \# align\_corners=False
\>>> m(input)
tensor(\[\[\[\[1.0000, 1.2500, 1.7500, 2.0000\],\
          \[1.5000, 1.7500, 2.2500, 2.5000\],\
          \[2.5000, 2.7500, 3.2500, 3.5000\],\
          \[3.0000, 3.2500, 3.7500, 4.0000\]\]\]\])

\>>> m \= nn.Upsample(scale\_factor\=2, mode\='bilinear', align\_corners\=True)
\>>> m(input)
tensor(\[\[\[\[1.0000, 1.3333, 1.6667, 2.0000\],\
          \[1.6667, 2.0000, 2.3333, 2.6667\],\
          \[2.3333, 2.6667, 3.0000, 3.3333\],\
          \[3.0000, 3.3333, 3.6667, 4.0000\]\]\]\])

\>>> \# Try scaling the same data in a larger tensor
\>>> input\_3x3 \= torch.zeros(3, 3).view(1, 1, 3, 3)
\>>> input\_3x3\[:, :, :2, :2\].copy\_(input)
tensor(\[\[\[\[1., 2.\],\
          \[3., 4.\]\]\]\])
\>>> input\_3x3
tensor(\[\[\[\[1., 2., 0.\],\
          \[3., 4., 0.\],\
          \[0., 0., 0.\]\]\]\])

\>>> m \= nn.Upsample(scale\_factor\=2, mode\='bilinear')  \# align\_corners=False
\>>> \# Notice that values in top left corner are the same as the small input (except at boundary)
\>>> m(input\_3x3)
tensor(\[\[\[\[1.0000, 1.2500, 1.7500, 1.5000, 0.5000, 0.0000\],\
          \[1.5000, 1.7500, 2.2500, 1.8750, 0.6250, 0.0000\],\
          \[2.5000, 2.7500, 3.2500, 2.6250, 0.8750, 0.0000\],\
          \[2.2500, 2.4375, 2.8125, 2.2500, 0.7500, 0.0000\],\
          \[0.7500, 0.8125, 0.9375, 0.7500, 0.2500, 0.0000\],\
          \[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000\]\]\]\])

\>>> m \= nn.Upsample(scale\_factor\=2, mode\='bilinear', align\_corners\=True)
\>>> \# Notice that values in top left corner are now changed
\>>> m(input\_3x3)
tensor(\[\[\[\[1.0000, 1.4000, 1.8000, 1.6000, 0.8000, 0.0000\],\
          \[1.8000, 2.2000, 2.6000, 2.2400, 1.1200, 0.0000\],\
          \[2.6000, 3.0000, 3.4000, 2.8800, 1.4400, 0.0000\],\
          \[2.4000, 2.7200, 3.0400, 2.5600, 1.2800, 0.0000\],\
          \[1.2000, 1.3600, 1.5200, 1.2800, 0.6400, 0.0000\],\
          \[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000\]\]\]\])

Copy to clipboard

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/upsampling.py#L189)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html#torch.nn.Upsample.extra_repr "Link to this definition")

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/upsampling.py#L170)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Upsample.html#torch.nn.Upsample.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Upsample.rst.txt)

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