Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.functional.grid_sample.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.grid_sample.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.grid_sample.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.functional.grid_sample.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.functional.grid_sample.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.functional.grid_sample.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.functional.grid_sample.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.functional.grid_sample.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.functional.grid_sample.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.functional.grid_sample.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.functional.grid_sample.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.functional.grid_sample.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.functional.grid_sample.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.functional.grid_sample.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.functional.grid_sample.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.functional.grid_sample.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.functional.grid_sample.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.functional.grid_sample.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.functional.grid_sample.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.functional.grid_sample.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.functional.grid_sample.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.functional.grid_sample.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.functional.grid_sample.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.functional.grid_sample.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.functional.grid_sample.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.functional.grid_sample.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.functional.grid_sample.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.functional.grid_sample.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.functional.grid_sample.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.functional.grid_sample.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.functional.grid_sample.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.functional.grid_sample.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.functional.grid_sample.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.functional.grid_sample.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.functional.grid_sample.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.functional.grid_sample.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.functional.grid_sample.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.functional.grid_sample.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.functional.grid_sample.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.functional.grid_sample.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.functional.grid_sample.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.functional.grid_sample.html)

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

torch.nn.functional.grid\_sample[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#torch-nn-functional-grid-sample "Link to this heading")

==============================================================================================================================================================================

torch.nn.functional.grid\_sample(_input_, _grid_, _mode\='bilinear'_, _padding\_mode\='zeros'_, _align\_corners\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/functional.py#L5543)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#torch.nn.functional.grid_sample "Link to this definition")

Compute grid sample.

Given an `input` and a flow-field `grid`, computes the `output` using `input` values and pixel locations from `grid`.

Currently, only spatial (4-D) and volumetric (5-D) `input` are supported.

In the spatial (4-D) case, for `input` with shape (N,C,Hin,Win)(N, C, H\_\\text{in}, W\_\\text{in})(N,C,Hin​,Win​) and `grid` with shape (N,Hout,Wout,2)(N, H\_\\text{out}, W\_\\text{out}, 2)(N,Hout​,Wout​,2), the output will have shape (N,C,Hout,Wout)(N, C, H\_\\text{out}, W\_\\text{out})(N,C,Hout​,Wout​).

For each output location `output[n, :, h, w]`, the size-2 vector `grid[n, h, w]` specifies `input` pixel locations `x` and `y`, which are used to interpolate the output value `output[n, :, h, w]`. In the case of 5D inputs, `grid[n, d, h, w]` specifies the `x`, `y`, `z` pixel locations for interpolating `output[n, :, d, h, w]`. `mode` argument specifies `nearest`, `bilinear` or `bicubic` interpolation method to sample the input pixels.

`grid` specifies the sampling pixel locations normalized by the `input` spatial dimensions. Therefore, it should have most values in the range of `[-1, 1]`. For example, values `x = -1, y = -1` is the left-top pixel of `input`, and values `x = 1, y = 1` is the right-bottom pixel of `input`.

If `grid` has values outside the range of `[-1, 1]`, the corresponding outputs are handled as defined by `padding_mode`. Options are

> *   `padding_mode="zeros"`: use `0` for out-of-bound grid locations,
>     
> *   `padding_mode="border"`: use border values for out-of-bound grid locations,
>     
> *   `padding_mode="reflection"`: use values at locations reflected by the border for out-of-bound grid locations. For location far away from the border, it will keep being reflected until becoming in bound, e.g., (normalized) pixel location `x = -3.5` reflects by border `-1` and becomes `x' = 1.5`, then reflects by border `1` and becomes `x'' = -0.5`.
>     

Note

This function is often used in conjunction with [`affine_grid()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.affine_grid.html#torch.nn.functional.affine_grid "torch.nn.functional.affine_grid")
 to build [Spatial Transformer Networks](https://arxiv.org/abs/1506.02025)
 .

Note

When using the CUDA backend, this operation may induce nondeterministic behaviour in its backward pass that is not easily switched off. Please see the notes on [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for background.

Note

NaN values in `grid` would be interpreted as `-1`.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – input of shape (N,C,Hin,Win)(N, C, H\_\\text{in}, W\_\\text{in})(N,C,Hin​,Win​) (4-D case) or (N,C,Din,Hin,Win)(N, C, D\_\\text{in}, H\_\\text{in}, W\_\\text{in})(N,C,Din​,Hin​,Win​) (5-D case)
    
*   **grid** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – flow-field of shape (N,Hout,Wout,2)(N, H\_\\text{out}, W\_\\text{out}, 2)(N,Hout​,Wout​,2) (4-D case) or (N,Dout,Hout,Wout,3)(N, D\_\\text{out}, H\_\\text{out}, W\_\\text{out}, 3)(N,Dout​,Hout​,Wout​,3) (5-D case)
    
*   **mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – interpolation mode to calculate output values `'bilinear'` | `'nearest'` | `'bicubic'`. Default: `'bilinear'` When `mode='bilinear'` and the input is 5-D, the interpolation mode used internally will actually be trilinear. However, when the input is 4-D, the interpolation mode will legitimately be bilinear. Likewise `mode='bicubic'` is tricubic on a 5-D input, the separable cubic kernel extended over the third axis; CPU and CUDA, ROCm included, implement the 5-D case.
    
*   **padding\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – padding mode for outside grid values `'zeros'` | `'border'` | `'reflection'`. Default: `'zeros'`
    
*   **align\_corners** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Geometrically, we consider the pixels of the input as squares rather than points. If set to `True`, the extrema (`-1` and `1`) are considered as referring to the center points of the input’s corner pixels. If set to `False`, they are instead considered as referring to the corner points of the input’s corner pixels, making the sampling more resolution agnostic. This option parallels the `align_corners` option in [`interpolate()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#torch.nn.functional.interpolate "torch.nn.functional.interpolate")
    , and so whichever option is used here should also be used there to resize the input image before grid sampling. Default: `False`
    

Returns:

output Tensor

Return type:

output ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

Warning

When `align_corners = True`, the grid positions depend on the pixel size relative to the input image size, and so the locations sampled by [`grid_sample()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#torch.nn.functional.grid_sample "torch.nn.functional.grid_sample")
 will differ for the same input given at different resolutions (that is, after being upsampled or downsampled). The default behavior up to version 1.2.0 was `align_corners = True`. Since then, the default behavior has been changed to `align_corners = False`, in order to bring it in line with the default for [`interpolate()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.interpolate.html#torch.nn.functional.interpolate "torch.nn.functional.interpolate")
.

Note

`mode='bicubic'` is implemented using the [cubic convolution algorithm](https://en.wikipedia.org/wiki/Bicubic_interpolation)
 with α\=−0.75\\alpha=-0.75α\=−0.75. The constant α\\alphaα might be different from packages to packages. For example, [PIL](https://github.com/python-pillow/Pillow/blob/4634eafe3c695a014267eefdce830b4a825beed7/src/libImaging/Resample.c#L51)
 and [OpenCV](https://github.com/opencv/opencv/blob/f345ed564a06178670750bad59526cfa4033be55/modules/imgproc/src/resize.cpp#L908)
 use -0.5 and -0.75 respectively. This algorithm may “overshoot” the range of values it’s interpolating. For example, it may produce negative values or values greater than 255 when interpolating input in \[0, 255\]. Clamp the results with [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")
 to ensure they are within the valid range.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.functional.grid_sample.rst.txt)

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