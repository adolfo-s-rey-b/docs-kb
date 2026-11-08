Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Fold.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Fold.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Fold.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Fold.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Fold.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Fold.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Fold.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Fold.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Fold.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Fold.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Fold.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Fold.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Fold.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Fold.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Fold.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Fold.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Fold.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Fold.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Fold.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Fold.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Fold.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Fold.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Fold.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Fold.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Fold.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Fold.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Fold.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Fold.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Fold.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Fold.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Fold.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Fold.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Fold.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Fold.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Fold.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Fold.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Fold.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Fold.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Fold.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Fold.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Fold.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Fold.html)

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

Fold[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#fold "Link to this heading")

=====================================================================================================

_class_ torch.nn.Fold(_output\_size_, _kernel\_size_, _dilation\=1_, _padding\=0_, _stride\=1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/fold.py#L11)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#torch.nn.Fold "Link to this definition")

Combines an array of sliding local blocks into a large containing tensor.

Consider a batched `input` tensor containing sliding local blocks, e.g., patches of images, of shape (N,C×∏(kernel\_size),L)(N, C \\times \\prod(\\text{kernel\\\_size}), L)(N,C×∏(kernel\_size),L), where NNN is batch dimension, C×∏(kernel\_size)C \\times \\prod(\\text{kernel\\\_size})C×∏(kernel\_size) is the number of values within a block (a block has ∏(kernel\_size)\\prod(\\text{kernel\\\_size})∏(kernel\_size) spatial locations each containing a CCC\-channeled vector), and LLL is the total number of blocks. (This is exactly the same specification as the output shape of [`Unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Unfold.html#torch.nn.Unfold "torch.nn.Unfold")
.) This operation combines these local blocks into the large `output` tensor of shape (N,C,output\_size\[0\],output\_size\[1\],… )(N, C, \\text{output\\\_size}\[0\], \\text{output\\\_size}\[1\], \\dots)(N,C,output\_size\[0\],output\_size\[1\],…) by summing the overlapping values. Similar to [`Unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Unfold.html#torch.nn.Unfold "torch.nn.Unfold")
, the arguments must satisfy

L\=∏d⌊output\_size\[d\]+2×padding\[d\]−dilation\[d\]×(kernel\_size\[d\]−1)−1stride\[d\]+1⌋,L = \\prod\_d \\left\\lfloor\\frac{\\text{output\\\_size}\[d\] + 2 \\times \\text{padding}\[d\] % - \\text{dilation}\[d\] \\times (\\text{kernel\\\_size}\[d\] - 1) - 1}{\\text{stride}\[d\]} + 1\\right\\rfloor, L\=d∏​⌊stride\[d\]output\_size\[d\]+2×padding\[d\]−dilation\[d\]×(kernel\_size\[d\]−1)−1​+1⌋,

where ddd is over all spatial dimensions.

*   `output_size` describes the spatial shape of the large containing tensor of the sliding local blocks. It is useful to resolve the ambiguity when multiple input shapes map to same number of sliding blocks, e.g., with `stride > 0`.
    

The `padding`, `stride` and `dilation` arguments specify how the sliding blocks are retrieved.

*   `stride` controls the stride for the sliding blocks.
    
*   `padding` controls the amount of implicit zero-paddings on both sides for `padding` number of points for each dimension before reshaping.
    
*   `dilation` controls the spacing between the kernel points; also known as the à trous algorithm. It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
     has a nice visualization of what `dilation` does.
    

Parameters:

*   **output\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the shape of the spatial dimensions of the output (i.e., `output.sizes()[2:]`)
    
*   **kernel\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the size of the sliding blocks
    
*   **dilation** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – a parameter that controls the stride of elements within the neighborhood. Default: 1
    
*   **padding** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – implicit zero padding to be added on both sides of input. Default: 0
    
*   **stride** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the stride of the sliding blocks in the input spatial dimensions. Default: 1
    

*   If `output_size`, `kernel_size`, `dilation`, `padding` or `stride` is an int or a tuple of length 1 then their values will be replicated across all spatial dimensions.
    
*   For the case of two output spatial dimensions this operation is sometimes called `col2im`.
    

Note

[`Fold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#torch.nn.Fold "torch.nn.Fold")
 calculates each combined value in the resulting large tensor by summing all values from all containing blocks. [`Unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Unfold.html#torch.nn.Unfold "torch.nn.Unfold")
 extracts the values in the local blocks by copying from the large tensor. So, if the blocks overlap, they are not inverses of each other.

In general, folding and unfolding operations are related as follows. Consider [`Fold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#torch.nn.Fold "torch.nn.Fold")
 and [`Unfold`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Unfold.html#torch.nn.Unfold "torch.nn.Unfold")
 instances created with the same parameters:

\>>> fold\_params \= dict(kernel\_size\=..., dilation\=..., padding\=..., stride\=...)
\>>> fold \= nn.Fold(output\_size\=..., \*\*fold\_params)
\>>> unfold \= nn.Unfold(\*\*fold\_params)

Copy to clipboard

Then for any (supported) `input` tensor the following equality holds:

fold(unfold(input)) \== divisor \* input

Copy to clipboard

where `divisor` is a tensor that depends only on the shape and dtype of the `input`:

\>>> input\_ones \= torch.ones(input.shape, dtype\=input.dtype)
\>>> divisor \= fold(unfold(input\_ones))

Copy to clipboard

When the `divisor` tensor contains no zero elements, then `fold` and `unfold` operations are inverses of each other (up to constant divisor).

Warning

Currently, only unbatched (3D) or batched (4D) image-like output tensors are supported.

Shape:

*   Input: (N,C×∏(kernel\_size),L)(N, C \\times \\prod(\\text{kernel\\\_size}), L)(N,C×∏(kernel\_size),L) or (C×∏(kernel\_size),L)(C \\times \\prod(\\text{kernel\\\_size}), L)(C×∏(kernel\_size),L)
    
*   Output: (N,C,output\_size\[0\],output\_size\[1\],… )(N, C, \\text{output\\\_size}\[0\], \\text{output\\\_size}\[1\], \\dots)(N,C,output\_size\[0\],output\_size\[1\],…) or (C,output\_size\[0\],output\_size\[1\],… )(C, \\text{output\\\_size}\[0\], \\text{output\\\_size}\[1\], \\dots)(C,output\_size\[0\],output\_size\[1\],…) as described above
    

Examples:

\>>> fold \= nn.Fold(output\_size\=(4, 5), kernel\_size\=(2, 2))
\>>> input \= torch.randn(1, 3 \* 2 \* 2, 12)
\>>> output \= fold(input)
\>>> output.size()
torch.Size(\[1, 3, 4, 5\])

Copy to clipboard

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/fold.py#L162)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#torch.nn.Fold.extra_repr "Link to this definition")

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/fold.py#L149)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Fold.html#torch.nn.Fold.forward "Link to this definition")

Runs the forward pass.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Fold.rst.txt)

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