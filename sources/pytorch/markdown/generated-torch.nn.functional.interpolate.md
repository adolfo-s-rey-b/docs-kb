Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.functional.interpolate.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.interpolate.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.interpolate.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.functional.interpolate.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.interpolate.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.functional.interpolate.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.functional.interpolate.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.interpolate.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.functional.interpolate.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.functional.interpolate.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.functional.interpolate.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.functional.interpolate.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.functional.interpolate.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.functional.interpolate.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.functional.interpolate.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.functional.interpolate.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.functional.interpolate.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.functional.interpolate.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.functional.interpolate.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.functional.interpolate.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.functional.interpolate.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.functional.interpolate.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.functional.interpolate.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.functional.interpolate.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.functional.interpolate.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.functional.interpolate.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.functional.interpolate.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.functional.interpolate.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.functional.interpolate.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.functional.interpolate.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.functional.interpolate.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.functional.interpolate.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.functional.interpolate.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.functional.interpolate.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.functional.interpolate.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.functional.interpolate.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.functional.interpolate.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.functional.interpolate.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.functional.interpolate.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.functional.interpolate.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.functional.interpolate.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.functional.interpolate.html)

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

torch.nn.functional.interpolate[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#torch-nn-functional-interpolate "Link to this heading")

=============================================================================================================================================================================

torch.nn.functional.interpolate(_input_, _size\=None_, _scale\_factor\=None_, _mode\='nearest'_, _align\_corners\=None_, _recompute\_scale\_factor\=None_, _antialias\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/functional.py#L5035)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#torch.nn.functional.interpolate "Link to this definition")

Down/up samples the input.

Tensor interpolated to either the given `size` or the given `scale_factor`

The algorithm used for interpolation is determined by `mode`.

Currently temporal, spatial and volumetric sampling are supported, i.e. expected inputs are 3-D, 4-D or 5-D in shape.

The input dimensions are interpreted in the form: mini-batch x channels x \[optional depth\] x \[optional height\] x width.

The modes available for resizing are: nearest, linear (3D-only), bilinear, bicubic (4D-only), trilinear (5D-only), lanczos (4D-only, CPU only), area, nearest-exact

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor
    
*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\] or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – output spatial size.
    
*   **scale\_factor** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ _Tuple__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – multiplier for spatial size. If scale\_factor is a tuple, its length has to match the number of spatial dimensions; input.dim() - 2.
    
*   **mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – algorithm used for upsampling: `'nearest'` | `'linear'` | `'bilinear'` | `'bicubic'` | `'trilinear'` | `'lanczos'` | `'area'` | `'nearest-exact'`. Default: `'nearest'`
    
*   **align\_corners** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Geometrically, we consider the pixels of the input and output as squares rather than points. If set to `True`, the input and output tensors are aligned by the center points of their corner pixels, preserving the values at the corner pixels. If set to `False`, the input and output tensors are aligned by the corner points of their corner pixels, and the interpolation uses edge value padding for out-of-boundary values, making this operation _independent_ of input size when `scale_factor` is kept the same. This only has an effect when `mode` is `'linear'`, `'bilinear'`, `'bicubic'` or `'trilinear'`. Default: `None`. `None` leaves `align_corners` unset for modes that do not use it. For modes that use `align_corners`, `None` is treated as `False`.
    
*   **recompute\_scale\_factor** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – recompute the scale\_factor for use in the interpolation calculation. If recompute\_scale\_factor is `True`, then scale\_factor must be passed in and scale\_factor is used to compute the output size. The computed output size will be used to infer new scales for the interpolation. Note that when scale\_factor is floating-point, it may differ from the recomputed scale\_factor due to rounding and precision issues. If recompute\_scale\_factor is `False`, then size or scale\_factor will be used directly for interpolation. Default: `None`.
    
*   **antialias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – flag to apply anti-aliasing. Default: `False`. Using anti-alias option together with `align_corners=False`, interpolation result would match Pillow result for downsampling operation. Supported modes: `'bilinear'`, `'bicubic'`, `'lanczos'`.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Note

With `mode='bicubic'` or `mode='lanczos'`, it’s possible to cause overshoot. For some dtypes, it can produce negative values or values greater than 255 for images. Explicitly call `result.clamp(min=0,max=255)` if you want to reduce the overshoot when displaying the image. For `uint8` inputs, it already performs saturating cast operation. So, no manual clamp operation is needed.

Note

Mode `mode='lanczos'` uses a Lanczos-3 windowed sinc filter (6 taps) and requires `antialias=True`. It only supports 4-D input (i.e. 2D spatial) and CPU. With `antialias=True` and `align_corners=False`, the result matches PIL’s `Image.LANCZOS` resampling filter.

Note

Mode `mode='nearest-exact'` matches Scikit-Image and PIL nearest neighbours interpolation algorithms and fixes known issues with `mode='nearest'`. This mode is introduced to keep backward compatibility. Mode `mode='nearest'` matches buggy OpenCV’s `INTER_NEAREST` interpolation algorithm.

Note

The gradients for the dtype `float16` on CUDA may be inaccurate in the upsample operation when using modes `['linear', 'bilinear', 'bicubic', 'trilinear', 'area']`. For more details, please refer to the discussion in [issue#104157](https://github.com/pytorch/pytorch/issues/104157)
.

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for more information.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.functional.interpolate.rst.txt)

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