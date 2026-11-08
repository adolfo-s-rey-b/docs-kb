Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch.html)

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

torch[#](https://docs.pytorch.org/docs/2.15/torch.html#module-torch "Link to this heading")

============================================================================================

Created On: Dec 23, 2016 | Last Updated On: Aug 20, 2026

The torch package contains data structures for multi-dimensional tensors and defines mathematical operations over these tensors. Additionally, it provides many utilities for efficient serialization of Tensors and arbitrary types, and other useful utilities.

It has a CUDA counterpart, that enables you to run your tensor computations on an NVIDIA GPU with compute capability >= 3.0.

Tensors[#](https://docs.pytorch.org/docs/2.15/torch.html#tensors "Link to this heading")

-----------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`is_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.is_tensor.html#torch.is_tensor "torch.is_tensor") | Returns True if obj is a PyTorch tensor. |
| [`is_storage`](https://docs.pytorch.org/docs/2.15/generated/torch.is_storage.html#torch.is_storage "torch.is_storage") | Returns True if obj is a PyTorch storage object. |
| [`is_complex`](https://docs.pytorch.org/docs/2.15/generated/torch.is_complex.html#torch.is_complex "torch.is_complex") | Returns True if the data type of `input` is a complex data type i.e., one of `torch.complex64`, and `torch.complex128`. |
| [`is_conj`](https://docs.pytorch.org/docs/2.15/generated/torch.is_conj.html#torch.is_conj "torch.is_conj") | Returns True if the `input` is a conjugated tensor, i.e. its conjugate bit is set to True. |
| [`is_floating_point`](https://docs.pytorch.org/docs/2.15/generated/torch.is_floating_point.html#torch.is_floating_point "torch.is_floating_point") | Returns True if the data type of `input` is a floating point data type i.e., one of `torch.float64`, `torch.float32`, `torch.float16`, and `torch.bfloat16`. |
| [`is_inference`](https://docs.pytorch.org/docs/2.15/generated/torch.is_inference.html#torch.is_inference "torch.is_inference") | Returns True if `input` is an inference tensor. |
| [`is_neg`](https://docs.pytorch.org/docs/2.15/generated/torch.is_neg.html#torch.is_neg "torch.is_neg") |     |
| [`is_nonzero`](https://docs.pytorch.org/docs/2.15/generated/torch.is_nonzero.html#torch.is_nonzero "torch.is_nonzero") | Returns True if the `input` is a single element tensor which is not equal to zero after type conversions. |
| [`is_same_size`](https://docs.pytorch.org/docs/2.15/generated/torch.is_same_size.html#torch.is_same_size "torch.is_same_size") |     |
| [`is_signed`](https://docs.pytorch.org/docs/2.15/generated/torch.is_signed.html#torch.is_signed "torch.is_signed") |     |
| [`set_default_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype") | Sets the default floating point dtype to `d`. |
| [`get_default_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_default_dtype.html#torch.get_default_dtype "torch.get_default_dtype") | Get the current default floating point [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")<br>. |
| [`set_default_device`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device") | Sets the default `torch.Tensor` to be allocated on `device`. |
| [`get_default_device`](https://docs.pytorch.org/docs/2.15/generated/torch.get_default_device.html#torch.get_default_device "torch.get_default_device") | Gets the default `torch.Tensor` to be allocated on `device` |
| [`set_default_tensor_type`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_tensor_type.html#torch.set_default_tensor_type "torch.set_default_tensor_type") |     |
| [`numel`](https://docs.pytorch.org/docs/2.15/generated/torch.numel.html#torch.numel "torch.numel") | Returns the total number of elements in the `input` tensor. |
| [`set_printoptions`](https://docs.pytorch.org/docs/2.15/generated/torch.set_printoptions.html#torch.set_printoptions "torch.set_printoptions") | Set options for printing. |
| [`set_flush_denormal`](https://docs.pytorch.org/docs/2.15/generated/torch.set_flush_denormal.html#torch.set_flush_denormal "torch.set_flush_denormal") | Disables denormal floating numbers on CPU. |

### Creation Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#creation-ops "Link to this heading")

Note

Random sampling creation ops are listed under [Random sampling](https://docs.pytorch.org/docs/2.15/torch.html#random-sampling)
 and include: [`torch.rand()`](https://docs.pytorch.org/docs/2.15/generated/torch.rand.html#torch.rand "torch.rand")
 [`torch.rand_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.rand_like.html#torch.rand_like "torch.rand_like")
 [`torch.randn()`](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#torch.randn "torch.randn")
 [`torch.randn_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.randn_like.html#torch.randn_like "torch.randn_like")
 [`torch.randint()`](https://docs.pytorch.org/docs/2.15/generated/torch.randint.html#torch.randint "torch.randint")
 [`torch.randint_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.randint_like.html#torch.randint_like "torch.randint_like")
 [`torch.randperm()`](https://docs.pytorch.org/docs/2.15/generated/torch.randperm.html#torch.randperm "torch.randperm")
 You may also use [`torch.empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty")
 with the [In-place random sampling](https://docs.pytorch.org/docs/2.15/torch.html#inplace-random-sampling)
 methods to create [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 s with values sampled from a broader range of distributions.

|     |     |
| --- | --- |
| [`tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch.tensor "torch.tensor") | Constructs a tensor with no autograd history (also known as a "leaf tensor", see [Autograd mechanics](https://docs.pytorch.org/docs/2.15/notes/autograd.html)<br>) by copying `data`. |
| [`sparse_coo_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_coo_tensor.html#torch.sparse_coo_tensor "torch.sparse_coo_tensor") | Constructs a [sparse tensor in COO(rdinate) format](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-coo-docs)<br> with specified values at the given `indices`. |
| [`sparse_csr_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_csr_tensor.html#torch.sparse_csr_tensor "torch.sparse_csr_tensor") | Constructs a [sparse tensor in CSR (Compressed Sparse Row)](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-csr-docs)<br> with specified values at the given `crow_indices` and `col_indices`. |
| [`sparse_csc_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_csc_tensor.html#torch.sparse_csc_tensor "torch.sparse_csc_tensor") | Constructs a [sparse tensor in CSC (Compressed Sparse Column)](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-csc-docs)<br> with specified values at the given `ccol_indices` and `row_indices`. |
| [`sparse_bsr_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_bsr_tensor.html#torch.sparse_bsr_tensor "torch.sparse_bsr_tensor") | Constructs a [sparse tensor in BSR (Block Compressed Sparse Row))](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-bsr-docs)<br> with specified 2-dimensional blocks at the given `crow_indices` and `col_indices`. |
| [`sparse_bsc_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.sparse_bsc_tensor.html#torch.sparse_bsc_tensor "torch.sparse_bsc_tensor") | Constructs a [sparse tensor in BSC (Block Compressed Sparse Column))](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-bsc-docs)<br> with specified 2-dimensional blocks at the given `ccol_indices` and `row_indices`. |
| [`asarray`](https://docs.pytorch.org/docs/2.15/generated/torch.asarray.html#torch.asarray "torch.asarray") | Converts `obj` to a tensor. |
| [`as_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.as_tensor.html#torch.as_tensor "torch.as_tensor") | Converts `data` into a tensor, sharing data and preserving autograd history if possible. |
| [`as_strided`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided.html#torch.as_strided "torch.as_strided") | Create a view of an existing torch.Tensor `input` with specified `size`, `stride` and `storage_offset`. |
| [`from_file`](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch.from_file "torch.from_file") | Creates a CPU tensor with a storage backed by a memory-mapped file. |
| [`from_numpy`](https://docs.pytorch.org/docs/2.15/generated/torch.from_numpy.html#torch.from_numpy "torch.from_numpy") | Creates a [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")<br> from a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")<br>. |
| [`from_dlpack`](https://docs.pytorch.org/docs/2.15/generated/torch.from_dlpack.html#torch.from_dlpack "torch.from_dlpack") | Converts a tensor from an external library into a `torch.Tensor`. |
| [`frombuffer`](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html#torch.frombuffer "torch.frombuffer") | Creates a 1-dimensional [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")<br> from an object that implements the Python buffer protocol. |
| [`zeros`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros") | Returns a tensor filled with the scalar value 0, with the shape defined by the variable argument `size`. |
| [`zeros_like`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros_like.html#torch.zeros_like "torch.zeros_like") | Returns a tensor filled with the scalar value 0, with the same size as `input`. |
| [`ones`](https://docs.pytorch.org/docs/2.15/generated/torch.ones.html#torch.ones "torch.ones") | Returns a tensor filled with the scalar value 1, with the shape defined by the variable argument `size`. |
| [`ones_like`](https://docs.pytorch.org/docs/2.15/generated/torch.ones_like.html#torch.ones_like "torch.ones_like") | Returns a tensor filled with the scalar value 1, with the same size as `input`. |
| [`arange`](https://docs.pytorch.org/docs/2.15/generated/torch.arange.html#torch.arange "torch.arange") | Returns a 1-D tensor of size ⌈end−startstep⌉\\left\\lceil \\frac{\\text{end} - \\text{start}}{\\text{step}} \\right\\rceil⌈stepend−start​⌉ with values from the interval `[start, end)` taken with common difference `step` beginning from start. |\
| [`range`](https://docs.pytorch.org/docs/2.15/generated/torch.range.html#torch.range "torch.range") | Returns a 1-D tensor of size ⌊end−startstep⌋+1\\left\\lfloor \\frac{\\text{end} - \\text{start}}{\\text{step}} \\right\\rfloor + 1⌊stepend−start​⌋+1 with values from `start` to `end` with step `step`. |\
| [`linspace`](https://docs.pytorch.org/docs/2.15/generated/torch.linspace.html#torch.linspace "torch.linspace") | Creates a one-dimensional tensor of size `steps` whose values are evenly spaced from `start` to `end`, inclusive. |\
| [`logspace`](https://docs.pytorch.org/docs/2.15/generated/torch.logspace.html#torch.logspace "torch.logspace") | Creates a one-dimensional tensor of size `steps` whose values are evenly spaced from basestart{{\\text{{base}}}}^{{\\text{{start}}}}basestart to baseend{{\\text{{base}}}}^{{\\text{{end}}}}baseend, inclusive, on a logarithmic scale with base `base`. |\
| [`eye`](https://docs.pytorch.org/docs/2.15/generated/torch.eye.html#torch.eye "torch.eye") | Returns a 2-D tensor with ones on the diagonal and zeros elsewhere. |\
| [`empty`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty") | Returns a tensor filled with uninitialized data. |\
| [`empty_like`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_like.html#torch.empty_like "torch.empty_like") | Returns an uninitialized tensor with the same size as `input`. |\
| [`empty_permuted`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_permuted.html#torch.empty_permuted "torch.empty_permuted") | Creates an uninitialized, non-overlapping and dense tensor with the specified `size`, with `physical_layout` specifying how the dimensions are physically laid out in memory (each logical dimension is listed from outermost to innermost). |\
| [`empty_quantized`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_quantized.html#torch.empty_quantized "torch.empty_quantized") |     |\
| [`empty_strided`](https://docs.pytorch.org/docs/2.15/generated/torch.empty_strided.html#torch.empty_strided "torch.empty_strided") | Creates a tensor with the specified `size` and `stride` and filled with undefined data. |\
| [`full`](https://docs.pytorch.org/docs/2.15/generated/torch.full.html#torch.full "torch.full") | Creates a tensor of size `size` filled with `fill_value`. |\
| [`full_like`](https://docs.pytorch.org/docs/2.15/generated/torch.full_like.html#torch.full_like "torch.full_like") | Returns a tensor with the same size as `input` filled with `fill_value`. |\
| [`quantize_per_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.quantize_per_tensor.html#torch.quantize_per_tensor "torch.quantize_per_tensor") | Converts a float tensor to a quantized tensor with given scale and zero point. |\
| [`quantize_per_tensor_dynamic`](https://docs.pytorch.org/docs/2.15/generated/torch.quantize_per_tensor_dynamic.html#torch.quantize_per_tensor_dynamic "torch.quantize_per_tensor_dynamic") | Converts a float tensor to a quantized tensor with scale and zero\_point calculated dynamically based on the input. |\
| [`quantize_per_channel`](https://docs.pytorch.org/docs/2.15/generated/torch.quantize_per_channel.html#torch.quantize_per_channel "torch.quantize_per_channel") | Converts a float tensor to a per-channel quantized tensor with given scales and zero points. |\
| [`dequantize`](https://docs.pytorch.org/docs/2.15/generated/torch.dequantize.html#torch.dequantize "torch.dequantize") | Returns an fp32 Tensor by dequantizing a quantized Tensor |\
| [`complex`](https://docs.pytorch.org/docs/2.15/generated/torch.complex.html#torch.complex "torch.complex") | Constructs a complex tensor with its real part equal to [`real`](https://docs.pytorch.org/docs/2.15/generated/torch.real.html#torch.real "torch.real")<br> and its imaginary part equal to [`imag`](https://docs.pytorch.org/docs/2.15/generated/torch.imag.html#torch.imag "torch.imag")<br>. |\
| [`polar`](https://docs.pytorch.org/docs/2.15/generated/torch.polar.html#torch.polar "torch.polar") | Constructs a complex tensor whose elements are Cartesian coordinates corresponding to the polar coordinates with absolute value [`abs`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs")<br> and angle [`angle`](https://docs.pytorch.org/docs/2.15/generated/torch.angle.html#torch.angle "torch.angle")<br>. |\
| [`scalar_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.scalar_tensor.html#torch.scalar_tensor "torch.scalar_tensor") |     |\
| [`heaviside`](https://docs.pytorch.org/docs/2.15/generated/torch.heaviside.html#torch.heaviside "torch.heaviside") | Computes the Heaviside step function for each element in `input`. |\
\
### Indexing, Slicing, Joining, Mutating Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#indexing-slicing-joining-mutating-ops "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`adjoint`](https://docs.pytorch.org/docs/2.15/generated/torch.adjoint.html#torch.adjoint "torch.adjoint") | Returns a view of the tensor conjugated and with the last two dimensions transposed. |\
| [`alias_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.alias_copy.html#torch.alias_copy "torch.alias_copy") | Performs the same operation as `torch.alias()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`argwhere`](https://docs.pytorch.org/docs/2.15/generated/torch.argwhere.html#torch.argwhere "torch.argwhere") | Returns a tensor containing the indices of all non-zero elements of `input`. |\
| [`as_strided_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided_copy.html#torch.as_strided_copy "torch.as_strided_copy") | Performs the same operation as [`torch.as_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided.html#torch.as_strided "torch.as_strided")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`as_strided_scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided_scatter.html#torch.as_strided_scatter "torch.as_strided_scatter") | Embeds the values of the `src` tensor into `input` along the elements corresponding to the result of calling input.as\_strided(size, stride, storage\_offset). |\
| [`cat`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat") | Concatenates the given sequence of tensors in `tensors` in the given dimension. |\
| [`ccol_indices_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.ccol_indices_copy.html#torch.ccol_indices_copy "torch.ccol_indices_copy") |     |\
| [`col_indices_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.col_indices_copy.html#torch.col_indices_copy "torch.col_indices_copy") | Performs the same operation as `torch.col_indices()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`concat`](https://docs.pytorch.org/docs/2.15/generated/torch.concat.html#torch.concat "torch.concat") | Alias of [`torch.cat()`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat")<br>. |\
| [`concatenate`](https://docs.pytorch.org/docs/2.15/generated/torch.concatenate.html#torch.concatenate "torch.concatenate") | Alias of [`torch.cat()`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat")<br>. |\
| [`conj`](https://docs.pytorch.org/docs/2.15/generated/torch.conj.html#torch.conj "torch.conj") | Returns a view of `input` with a flipped conjugate bit. |\
| [`chunk`](https://docs.pytorch.org/docs/2.15/generated/torch.chunk.html#torch.chunk "torch.chunk") | Attempts to split a tensor into the specified number of chunks. |\
| [`crow_indices_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.crow_indices_copy.html#torch.crow_indices_copy "torch.crow_indices_copy") | Performs the same operation as `torch.crow_indices()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`detach`](https://docs.pytorch.org/docs/2.15/generated/torch.detach.html#torch.detach "torch.detach") |     |\
| [`detach_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.detach_copy.html#torch.detach_copy "torch.detach_copy") | Performs the same operation as [`torch.detach()`](https://docs.pytorch.org/docs/2.15/generated/torch.detach.html#torch.detach "torch.detach")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`diagonal_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_copy.html#torch.diagonal_copy "torch.diagonal_copy") | Performs the same operation as [`torch.diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`dsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.dsplit.html#torch.dsplit "torch.dsplit") | Splits `input`, a tensor with three or more dimensions, into multiple tensors depthwise according to `indices_or_sections`. |\
| [`column_stack`](https://docs.pytorch.org/docs/2.15/generated/torch.column_stack.html#torch.column_stack "torch.column_stack") | Creates a new tensor by horizontally stacking the tensors in `tensors`. |\
| [`dstack`](https://docs.pytorch.org/docs/2.15/generated/torch.dstack.html#torch.dstack "torch.dstack") | Stack tensors in sequence depthwise (along third axis). |\
| [`expand_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.expand_copy.html#torch.expand_copy "torch.expand_copy") | Performs the same operation as [`torch.Tensor.expand()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand.html#torch.Tensor.expand "torch.Tensor.expand")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`fill`](https://docs.pytorch.org/docs/2.15/generated/torch.fill.html#torch.fill "torch.fill") |     |\
| [`gather`](https://docs.pytorch.org/docs/2.15/generated/torch.gather.html#torch.gather "torch.gather") | Gathers values along an axis specified by dim. |\
| [`hsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.hsplit.html#torch.hsplit "torch.hsplit") | Splits `input`, a tensor with one or more dimensions, into multiple tensors horizontally according to `indices_or_sections`. |\
| [`hstack`](https://docs.pytorch.org/docs/2.15/generated/torch.hstack.html#torch.hstack "torch.hstack") | Stack tensors in sequence horizontally (column wise). |\
| [`index_add`](https://docs.pytorch.org/docs/2.15/generated/torch.index_add.html#torch.index_add "torch.index_add") | See [`index_add_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_add_.html#torch.Tensor.index_add_ "torch.Tensor.index_add_")<br> for function description. |\
| [`index_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.index_copy.html#torch.index_copy "torch.index_copy") | See [`index_copy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_copy_.html#torch.Tensor.index_copy_ "torch.Tensor.index_copy_")<br> for function description. |\
| [`index_put_`](https://docs.pytorch.org/docs/2.15/generated/torch.index_put_.html#torch.index_put_ "torch.index_put_") |     |\
| [`index_reduce`](https://docs.pytorch.org/docs/2.15/generated/torch.index_reduce.html#torch.index_reduce "torch.index_reduce") | See [`index_reduce_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_reduce_.html#torch.Tensor.index_reduce_ "torch.Tensor.index_reduce_")<br> for function description. |\
| [`index_select`](https://docs.pytorch.org/docs/2.15/generated/torch.index_select.html#torch.index_select "torch.index_select") | Returns a new tensor which indexes the `input` tensor along dimension `dim` using the entries in `index`. |\
| [`indices_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.indices_copy.html#torch.indices_copy "torch.indices_copy") | Performs the same operation as `torch.indices()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`masked_fill`](https://docs.pytorch.org/docs/2.15/generated/torch.masked_fill.html#torch.masked_fill "torch.masked_fill") |     |\
| [`masked_select`](https://docs.pytorch.org/docs/2.15/generated/torch.masked_select.html#torch.masked_select "torch.masked_select") | Returns a new 1-D tensor which indexes the `input` tensor according to the boolean mask `mask` which is a BoolTensor. |\
| [`movedim`](https://docs.pytorch.org/docs/2.15/generated/torch.movedim.html#torch.movedim "torch.movedim") | Moves the dimension(s) of `input` at the position(s) in `source` to the position(s) in `destination`. |\
| [`moveaxis`](https://docs.pytorch.org/docs/2.15/generated/torch.moveaxis.html#torch.moveaxis "torch.moveaxis") | Alias for [`torch.movedim()`](https://docs.pytorch.org/docs/2.15/generated/torch.movedim.html#torch.movedim "torch.movedim")<br>. |\
| [`narrow`](https://docs.pytorch.org/docs/2.15/generated/torch.narrow.html#torch.narrow "torch.narrow") | Returns a new tensor that is a narrowed version of `input` tensor. |\
| [`narrow_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.narrow_copy.html#torch.narrow_copy "torch.narrow_copy") | Same as [`Tensor.narrow()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.narrow.html#torch.Tensor.narrow "torch.Tensor.narrow")<br> except this returns a copy rather than shared storage. |\
| [`nonzero`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero.html#torch.nonzero "torch.nonzero") |     |\
| [`nonzero_static`](https://docs.pytorch.org/docs/2.15/generated/torch.nonzero_static.html#torch.nonzero_static "torch.nonzero_static") | Returns a 2-D tensor where each row is the index for a non-zero value. |\
| [`permute`](https://docs.pytorch.org/docs/2.15/generated/torch.permute.html#torch.permute "torch.permute") | Returns a view of the original tensor `input` with its dimensions permuted. |\
| [`permute_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.permute_copy.html#torch.permute_copy "torch.permute_copy") | Performs the same operation as [`torch.permute()`](https://docs.pytorch.org/docs/2.15/generated/torch.permute.html#torch.permute "torch.permute")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`put`](https://docs.pytorch.org/docs/2.15/generated/torch.put.html#torch.put "torch.put") |     |\
| [`reshape`](https://docs.pytorch.org/docs/2.15/generated/torch.reshape.html#torch.reshape "torch.reshape") | Returns a tensor with the same data and number of elements as `input`, but with the specified shape. |\
| [`row_indices_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.row_indices_copy.html#torch.row_indices_copy "torch.row_indices_copy") |     |\
| [`row_stack`](https://docs.pytorch.org/docs/2.15/generated/torch.row_stack.html#torch.row_stack "torch.row_stack") | Alias of [`torch.vstack()`](https://docs.pytorch.org/docs/2.15/generated/torch.vstack.html#torch.vstack "torch.vstack")<br>. |\
| [`select`](https://docs.pytorch.org/docs/2.15/generated/torch.select.html#torch.select "torch.select") | Slices the `input` tensor along the selected dimension at the given index. |\
| [`select_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.select_copy.html#torch.select_copy "torch.select_copy") | Performs the same operation as [`torch.select()`](https://docs.pytorch.org/docs/2.15/generated/torch.select.html#torch.select "torch.select")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.scatter.html#torch.scatter "torch.scatter") | Out-of-place version of [`torch.Tensor.scatter_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_ "torch.Tensor.scatter_") |\
| [`diagonal_scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal_scatter.html#torch.diagonal_scatter "torch.diagonal_scatter") | Embeds the values of the `src` tensor into `input` along the diagonal elements of `input`, with respect to `dim1` and `dim2`. |\
| [`select_scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.select_scatter.html#torch.select_scatter "torch.select_scatter") | Embeds the values of the `src` tensor into `input` at the given index. |\
| [`slice_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.slice_copy.html#torch.slice_copy "torch.slice_copy") | Performs the same operation as `torch.slice()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`slice_inverse`](https://docs.pytorch.org/docs/2.15/generated/torch.slice_inverse.html#torch.slice_inverse "torch.slice_inverse") |     |\
| [`slice_scatter`](https://docs.pytorch.org/docs/2.15/generated/torch.slice_scatter.html#torch.slice_scatter "torch.slice_scatter") | Embeds the values of the `src` tensor into `input` at the given dimension. |\
| [`scatter_add`](https://docs.pytorch.org/docs/2.15/generated/torch.scatter_add.html#torch.scatter_add "torch.scatter_add") | Out-of-place version of [`torch.Tensor.scatter_add_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_ "torch.Tensor.scatter_add_") |\
| [`scatter_reduce`](https://docs.pytorch.org/docs/2.15/generated/torch.scatter_reduce.html#torch.scatter_reduce "torch.scatter_reduce") | Out-of-place version of [`torch.Tensor.scatter_reduce_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_ "torch.Tensor.scatter_reduce_") |\
| [`segment_reduce`](https://docs.pytorch.org/docs/2.15/generated/torch.segment_reduce.html#torch.segment_reduce "torch.segment_reduce") | Perform a segment reduction operation on the input tensor along the specified axis. |\
| [`split`](https://docs.pytorch.org/docs/2.15/generated/torch.split.html#torch.split "torch.split") | Splits the tensor into chunks. |\
| [`split_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.split_copy.html#torch.split_copy "torch.split_copy") | Performs the same operation as [`torch.split()`](https://docs.pytorch.org/docs/2.15/generated/torch.split.html#torch.split "torch.split")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`split_with_sizes_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.split_with_sizes_copy.html#torch.split_with_sizes_copy "torch.split_with_sizes_copy") | Performs the same operation as `torch.split_with_sizes()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`squeeze`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze") | Returns a tensor with all specified dimensions of `input` of size 1 removed. |\
| [`squeeze_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze_copy.html#torch.squeeze_copy "torch.squeeze_copy") | Performs the same operation as [`torch.squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.squeeze.html#torch.squeeze "torch.squeeze")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`stack`](https://docs.pytorch.org/docs/2.15/generated/torch.stack.html#torch.stack "torch.stack") | Concatenates a sequence of tensors along a new dimension. |\
| [`swapaxes`](https://docs.pytorch.org/docs/2.15/generated/torch.swapaxes.html#torch.swapaxes "torch.swapaxes") | Alias for [`torch.transpose()`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose.html#torch.transpose "torch.transpose")<br>. |\
| [`swapdims`](https://docs.pytorch.org/docs/2.15/generated/torch.swapdims.html#torch.swapdims "torch.swapdims") | Alias for [`torch.transpose()`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose.html#torch.transpose "torch.transpose")<br>. |\
| [`t`](https://docs.pytorch.org/docs/2.15/generated/torch.t.html#torch.t "torch.t") | Expects `input` to be <= 2-D tensor and transposes dimensions 0 and 1. |\
| [`t_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.t_copy.html#torch.t_copy "torch.t_copy") | Performs the same operation as [`torch.t()`](https://docs.pytorch.org/docs/2.15/generated/torch.t.html#torch.t "torch.t")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`take`](https://docs.pytorch.org/docs/2.15/generated/torch.take.html#torch.take "torch.take") | Returns a new tensor with the elements of `input` at the given indices. |\
| [`take_along_dim`](https://docs.pytorch.org/docs/2.15/generated/torch.take_along_dim.html#torch.take_along_dim "torch.take_along_dim") | Selects values from `input` at the 1-dimensional indices from `indices` along the given `dim`. |\
| [`tensor_split`](https://docs.pytorch.org/docs/2.15/generated/torch.tensor_split.html#torch.tensor_split "torch.tensor_split") | Splits a tensor into multiple sub-tensors, all of which are views of `input`, along dimension `dim` according to the indices or number of sections specified by `indices_or_sections`. |\
| [`tile`](https://docs.pytorch.org/docs/2.15/generated/torch.tile.html#torch.tile "torch.tile") | Constructs a tensor by repeating the elements of `input`. |\
| [`transpose`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose.html#torch.transpose "torch.transpose") | Returns a tensor that is a transposed version of `input`. |\
| [`transpose_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose_copy.html#torch.transpose_copy "torch.transpose_copy") | Performs the same operation as [`torch.transpose()`](https://docs.pytorch.org/docs/2.15/generated/torch.transpose.html#torch.transpose "torch.transpose")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`unbind`](https://docs.pytorch.org/docs/2.15/generated/torch.unbind.html#torch.unbind "torch.unbind") | Removes a tensor dimension. |\
| [`unbind_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.unbind_copy.html#torch.unbind_copy "torch.unbind_copy") | Performs the same operation as [`torch.unbind()`](https://docs.pytorch.org/docs/2.15/generated/torch.unbind.html#torch.unbind "torch.unbind")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`unfold_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.unfold_copy.html#torch.unfold_copy "torch.unfold_copy") | Performs the same operation as `torch.unfold()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`unravel_index`](https://docs.pytorch.org/docs/2.15/generated/torch.unravel_index.html#torch.unravel_index "torch.unravel_index") | Converts a tensor of flat indices into a tuple of coordinate tensors that index into an arbitrary tensor of the specified shape. |\
| [`unsqueeze`](https://docs.pytorch.org/docs/2.15/generated/torch.unsqueeze.html#torch.unsqueeze "torch.unsqueeze") | Returns a new tensor with a dimension of size one inserted at the specified position. |\
| [`unsqueeze_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.unsqueeze_copy.html#torch.unsqueeze_copy "torch.unsqueeze_copy") | Performs the same operation as [`torch.unsqueeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.unsqueeze.html#torch.unsqueeze "torch.unsqueeze")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`values_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.values_copy.html#torch.values_copy "torch.values_copy") | Performs the same operation as `torch.values()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`view_as_complex_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_complex_copy.html#torch.view_as_complex_copy "torch.view_as_complex_copy") | Performs the same operation as [`torch.view_as_complex()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_complex.html#torch.view_as_complex "torch.view_as_complex")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`view_as_real_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real_copy.html#torch.view_as_real_copy "torch.view_as_real_copy") | Performs the same operation as [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")<br>, but all output tensors are freshly created instead of aliasing the input. |\
| [`view_copy`](https://docs.pytorch.org/docs/2.15/generated/torch.view_copy.html#torch.view_copy "torch.view_copy") | Performs the same operation as `torch.view()`, but all output tensors are freshly created instead of aliasing the input. |\
| [`vsplit`](https://docs.pytorch.org/docs/2.15/generated/torch.vsplit.html#torch.vsplit "torch.vsplit") | Splits `input`, a tensor with two or more dimensions, into multiple tensors vertically according to `indices_or_sections`. |\
| [`vstack`](https://docs.pytorch.org/docs/2.15/generated/torch.vstack.html#torch.vstack "torch.vstack") | Stack tensors in sequence vertically (row wise). |\
| [`where`](https://docs.pytorch.org/docs/2.15/generated/torch.where.html#torch.where "torch.where") | Return a tensor of elements selected from either `input` or `other`, depending on `condition`. |\
\
Accelerators[#](https://docs.pytorch.org/docs/2.15/torch.html#accelerators "Link to this heading")\
\
---------------------------------------------------------------------------------------------------\
\
Within the PyTorch repo, we define an “Accelerator” as a [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 that is being used alongside a CPU to speed up computation. These devices use an asynchronous execution scheme, using [`torch.Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")\
 and [`torch.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")\
 as their main way to perform synchronization. We also assume that only one such accelerator can be available at once on a given host. This allows us to use the current accelerator as the default device for relevant concepts such as pinned memory, Stream device\_type, FSDP, etc.\
\
As of today, accelerator devices are (in no particular order) [“CUDA”](https://docs.pytorch.org/docs/2.15/cuda.html)\
, [“MTIA”](https://docs.pytorch.org/docs/2.15/mtia.html)\
, [“XPU”](https://docs.pytorch.org/docs/2.15/xpu.html)\
, [“MPS”](https://docs.pytorch.org/docs/2.15/mps.html)\
, “HPU”, and PrivateUse1 (many device not in the PyTorch repo itself).\
\
Many tools in the PyTorch Ecosystem use fork to create subprocesses (for example dataloading or intra-op parallelism), it is thus important to delay as much as possible any operation that would prevent further forks. This is especially important here as most accelerator’s initialization has such effect. In practice, you should keep in mind that checking [`torch.accelerator.current_accelerator()`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator "torch.accelerator.current_accelerator")\
 is a compile-time check by default, it is thus always fork-safe. On the contrary, passing the `check_available=True` flag to this function or calling [`torch.accelerator.is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.is_available.html#torch.accelerator.is_available "torch.accelerator.is_available")\
 will usually prevent later fork.\
\
Some backends provide an experimental opt-in option to make the runtime availability check fork-safe. When using the CUDA device `PYTORCH_NVML_BASED_CUDA_CHECK=1` can be used for example.\
\
|     |     |\
| --- | --- |\
| [`Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream") | An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order. |\
| [`Event`](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event") | Query and record Stream status to identify or control dependencies across Stream and measure timing. |\
\
Generators[#](https://docs.pytorch.org/docs/2.15/torch.html#generators "Link to this heading")\
\
-----------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator") |     |\
\
Random sampling[#](https://docs.pytorch.org/docs/2.15/torch.html#random-sampling "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`seed`](https://docs.pytorch.org/docs/2.15/generated/torch.seed.html#torch.seed "torch.seed") | Sets the seed for generating random numbers to a non-deterministic random number on all devices. |\
| [`manual_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.manual_seed.html#torch.manual_seed "torch.manual_seed") | Sets the seed for generating random numbers on all devices. |\
| [`initial_seed`](https://docs.pytorch.org/docs/2.15/generated/torch.initial_seed.html#torch.initial_seed "torch.initial_seed") | Returns the initial seed for generating random numbers as a Python long. |\
| [`get_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.get_rng_state.html#torch.get_rng_state "torch.get_rng_state") | Returns the random number generator state as a torch.ByteTensor. |\
| [`set_rng_state`](https://docs.pytorch.org/docs/2.15/generated/torch.set_rng_state.html#torch.set_rng_state "torch.set_rng_state") | Sets the random number generator state. |\
\
torch.default\_generator _Returns the default CPU torch.Generator_[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.torch.default_generator "Link to this definition")\
\
|     |     |\
| --- | --- |\
| [`bernoulli`](https://docs.pytorch.org/docs/2.15/generated/torch.bernoulli.html#torch.bernoulli "torch.bernoulli") | Draws binary random numbers (0 or 1) from a Bernoulli distribution. |\
| [`multinomial`](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#torch.multinomial "torch.multinomial") | Returns a tensor where each row contains `num_samples` indices sampled from the multinomial (a stricter definition would be multivariate, refer to [`torch.distributions.multinomial.Multinomial`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial "torch.distributions.multinomial.Multinomial")<br> for more details) probability distribution located in the corresponding row of tensor `input`. |\
| [`normal`](https://docs.pytorch.org/docs/2.15/generated/torch.normal.html#torch.normal "torch.normal") | Returns a tensor of random numbers drawn from separate normal distributions whose mean and standard deviation are given. |\
| [`poisson`](https://docs.pytorch.org/docs/2.15/generated/torch.poisson.html#torch.poisson "torch.poisson") | Returns a tensor of the same size as `input` with each element sampled from a Poisson distribution with rate parameter given by the corresponding element in `input` i.e., |\
| [`rand`](https://docs.pytorch.org/docs/2.15/generated/torch.rand.html#torch.rand "torch.rand") | Returns a tensor filled with random numbers from a uniform distribution on the interval \[0,1)\[0, 1)\[0,1) |\
| [`rand_like`](https://docs.pytorch.org/docs/2.15/generated/torch.rand_like.html#torch.rand_like "torch.rand_like") | Returns a tensor with the same size as `input` that is filled with random numbers from a uniform distribution on the interval \[0,1)\[0, 1)\[0,1). |\
| [`randint`](https://docs.pytorch.org/docs/2.15/generated/torch.randint.html#torch.randint "torch.randint") | Returns a tensor filled with random integers generated uniformly between `low` (inclusive) and `high` (exclusive). |\
| [`randint_like`](https://docs.pytorch.org/docs/2.15/generated/torch.randint_like.html#torch.randint_like "torch.randint_like") | Returns a tensor with the same shape as Tensor `input` filled with random integers generated uniformly between `low` (inclusive) and `high` (exclusive). |\
| [`randn`](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#torch.randn "torch.randn") | Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution). |\
| [`randn_like`](https://docs.pytorch.org/docs/2.15/generated/torch.randn_like.html#torch.randn_like "torch.randn_like") | Returns a tensor with the same size as `input` that is filled with random numbers from a normal distribution with mean 0 and variance 1. |\
| [`randperm`](https://docs.pytorch.org/docs/2.15/generated/torch.randperm.html#torch.randperm "torch.randperm") | Returns a random permutation of integers from `0` to `n - 1`. |\
\
### In-place random sampling[#](https://docs.pytorch.org/docs/2.15/torch.html#in-place-random-sampling "Link to this heading")\
\
There are a few more in-place random sampling functions defined on Tensors as well. Click through to refer to their documentation:\
\
*   [`torch.Tensor.bernoulli_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.bernoulli_.html#torch.Tensor.bernoulli_ "torch.Tensor.bernoulli_")\
     - in-place version of [`torch.bernoulli()`](https://docs.pytorch.org/docs/2.15/generated/torch.bernoulli.html#torch.bernoulli "torch.bernoulli")\
    \
*   [`torch.Tensor.cauchy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.cauchy_.html#torch.Tensor.cauchy_ "torch.Tensor.cauchy_")\
     - numbers drawn from the Cauchy distribution\
    \
*   [`torch.Tensor.exponential_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.exponential_.html#torch.Tensor.exponential_ "torch.Tensor.exponential_")\
     - numbers drawn from the exponential distribution\
    \
*   [`torch.Tensor.geometric_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.geometric_.html#torch.Tensor.geometric_ "torch.Tensor.geometric_")\
     - elements drawn from the geometric distribution\
    \
*   [`torch.Tensor.log_normal_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.log_normal_.html#torch.Tensor.log_normal_ "torch.Tensor.log_normal_")\
     - samples from the log-normal distribution\
    \
*   [`torch.Tensor.normal_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.normal_.html#torch.Tensor.normal_ "torch.Tensor.normal_")\
     - in-place version of [`torch.normal()`](https://docs.pytorch.org/docs/2.15/generated/torch.normal.html#torch.normal "torch.normal")\
    \
*   [`torch.Tensor.random_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.random_.html#torch.Tensor.random_ "torch.Tensor.random_")\
     - numbers sampled from the discrete uniform distribution\
    \
*   [`torch.Tensor.uniform_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.uniform_.html#torch.Tensor.uniform_ "torch.Tensor.uniform_")\
     - numbers sampled from the continuous uniform distribution\
    \
\
### Quasi-random sampling[#](https://docs.pytorch.org/docs/2.15/torch.html#quasi-random-sampling "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`quasirandom.SobolEngine`](https://docs.pytorch.org/docs/2.15/generated/torch.quasirandom.SobolEngine.html#torch.quasirandom.SobolEngine "torch.quasirandom.SobolEngine") | The [`torch.quasirandom.SobolEngine`](https://docs.pytorch.org/docs/2.15/generated/torch.quasirandom.SobolEngine.html#torch.quasirandom.SobolEngine "torch.quasirandom.SobolEngine")<br> is an engine for generating (scrambled) Sobol sequences. |\
\
Serialization[#](https://docs.pytorch.org/docs/2.15/torch.html#serialization "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`save`](https://docs.pytorch.org/docs/2.15/generated/torch.save.html#torch.save "torch.save") | Saves an object to a disk file. |\
| [`load`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load") | Loads an object saved with [`torch.save()`](https://docs.pytorch.org/docs/2.15/generated/torch.save.html#torch.save "torch.save")<br> from a file. |\
\
torch.serialization.check\_module\_version\_greater\_or\_equal(_module_, _req\_version\_tuple_, _error\_if\_malformed\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/serialization.py#L490)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.serialization.check_module_version_greater_or_equal "Link to this definition")\
\
Check if a module’s version satisfies requirements\
\
Usually, a module’s version string will be like ‘x.y.z’, which would be represented as a tuple (x, y, z), but sometimes it could be an unexpected format. If the version string does not match the given tuple’s format up to the length of the tuple, then error and exit or emit a warning.\
\
Parameters:\
\
*   **module** – the module to check the version of\
    \
*   **req\_version\_tuple** – tuple (usually of ints) representing the required version\
    \
*   **error\_if\_malformed** – whether we should exit if module version string is malformed\
    \
\
Returns:\
\
bool\
\
Return type:\
\
requirement\_is\_met\
\
torch.serialization.default\_restore\_location(_storage_, _location_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/serialization.py#L714)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.serialization.default_restore_location "Link to this definition")\
\
Restores storage using a deserializer function registered for the location.\
\
This function looks in the registry for deserializer functions that match the location. If found, it attempts to use them, in priority order, to restore storage until one returns a not None result. If no deserializer can be found in the registry, or all found fail to bear a result, it raises a RuntimeError.\
\
Parameters:\
\
*   **storage** (_STORAGE_) – the storage object to restore\
    \
*   **location** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – the location tag associated with the storage object\
    \
\
Returns:\
\
Optional\[STORAGE\]\
\
Return type:\
\
storage\
\
Raises:\
\
[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")\
 – If no deserializer matching location is found in the registry or if all matching ones return None.\
\
Parallelism[#](https://docs.pytorch.org/docs/2.15/torch.html#parallelism "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`fork`](https://docs.pytorch.org/docs/2.15/generated/torch.fork.html#torch.fork "torch.fork") |     |\
| [`get_num_threads`](https://docs.pytorch.org/docs/2.15/generated/torch.get_num_threads.html#torch.get_num_threads "torch.get_num_threads") | Returns the number of threads used for parallelizing CPU operations |\
| [`init_num_threads`](https://docs.pytorch.org/docs/2.15/generated/torch.init_num_threads.html#torch.init_num_threads "torch.init_num_threads") | init\_num\_threads() |\
| [`set_num_threads`](https://docs.pytorch.org/docs/2.15/generated/torch.set_num_threads.html#torch.set_num_threads "torch.set_num_threads") | Sets the number of threads used for intraop parallelism on CPU. |\
| [`get_num_interop_threads`](https://docs.pytorch.org/docs/2.15/generated/torch.get_num_interop_threads.html#torch.get_num_interop_threads "torch.get_num_interop_threads") | Returns the number of threads used for inter-op parallelism on CPU (e.g. in JIT interpreter). |\
| [`set_num_interop_threads`](https://docs.pytorch.org/docs/2.15/generated/torch.set_num_interop_threads.html#torch.set_num_interop_threads "torch.set_num_interop_threads") | Sets the number of threads used for interop parallelism (e.g. in JIT interpreter) on CPU. |\
| [`wait`](https://docs.pytorch.org/docs/2.15/generated/torch.wait.html#torch.wait "torch.wait") |     |\
\
Locally disabling gradient computation[#](https://docs.pytorch.org/docs/2.15/torch.html#locally-disabling-gradient-computation "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The context managers [`torch.no_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")\
, [`torch.enable_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.enable_grad.html#torch.enable_grad "torch.enable_grad")\
, and `torch.set_grad_enabled()` are helpful for locally disabling and enabling gradient computation. See [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/autograd.html#locally-disable-grad)\
 for more details on their usage. These context managers are thread local, so they won’t work if you send work to another thread using the `threading` module, etc.\
\
Examples:\
\
\>>> x \= torch.zeros(1, requires\_grad\=True)\
\>>> with torch.no\_grad():\
...     y \= x \* 2\
\>>> y.requires\_grad\
False\
\
\>>> is\_train \= False\
\>>> with torch.set\_grad\_enabled(is\_train):\
...     y \= x \* 2\
\>>> y.requires\_grad\
False\
\
\>>> torch.set\_grad\_enabled(True)  \# this can also be used as a function\
\>>> y \= x \* 2\
\>>> y.requires\_grad\
True\
\
\>>> torch.set\_grad\_enabled(False)\
\>>> y \= x \* 2\
\>>> y.requires\_grad\
False\
\
Copy to clipboard\
\
|     |     |\
| --- | --- |\
| [`no_grad`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad") | Context-manager that disables gradient calculation. |\
| [`enable_grad`](https://docs.pytorch.org/docs/2.15/generated/torch.enable_grad.html#torch.enable_grad "torch.enable_grad") | Context-manager that enables gradient calculation. |\
| [`autograd.grad_mode.set_grad_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad_mode.set_grad_enabled.html#torch.autograd.grad_mode.set_grad_enabled "torch.autograd.grad_mode.set_grad_enabled") | Context-manager that sets gradient calculation on or off. |\
| [`is_grad_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_grad_enabled.html#torch.is_grad_enabled "torch.is_grad_enabled") | Returns True if grad mode is currently enabled. |\
| [`autograd.grad_mode.inference_mode`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad_mode.inference_mode.html#torch.autograd.grad_mode.inference_mode "torch.autograd.grad_mode.inference_mode") | Context manager that enables or disables inference mode. |\
| [`is_inference_mode_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_inference_mode_enabled.html#torch.is_inference_mode_enabled "torch.is_inference_mode_enabled") | Returns True if inference mode is currently enabled. |\
\
Math operations[#](https://docs.pytorch.org/docs/2.15/torch.html#math-operations "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
### Constants[#](https://docs.pytorch.org/docs/2.15/torch.html#constants "Link to this heading")\
\
|     |     |\
| --- | --- |\
| `e` | Euler’s number, the base of natural logarithms (~2.7183). Alias for `math.e`. |\
| `inf` | A floating-point positive infinity. Alias for `math.inf`. |\
| `nan` | A floating-point “not a number” value. This value is not a legal number. Alias for `math.nan`. |\
| `pi` | The ratio of a circle’s circumference to its diameter (~3.1416). Alias for `math.pi`. |\
\
### Pointwise Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#pointwise-ops "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`abs`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs") | Computes the absolute value of each element in `input`. |\
| [`abs_`](https://docs.pytorch.org/docs/2.15/generated/torch.abs_.html#torch.abs_ "torch.abs_") | In-place version of [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs") |\
| [`absolute`](https://docs.pytorch.org/docs/2.15/generated/torch.absolute.html#torch.absolute "torch.absolute") | Alias for [`torch.abs()`](https://docs.pytorch.org/docs/2.15/generated/torch.abs.html#torch.abs "torch.abs") |\
| [`acos`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos") | Returns a new tensor with the arccosine (in radians) of each element in `input`. |\
| [`acos_`](https://docs.pytorch.org/docs/2.15/generated/torch.acos_.html#torch.acos_ "torch.acos_") | In-place version of [`torch.acos()`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos") |\
| [`arccos`](https://docs.pytorch.org/docs/2.15/generated/torch.arccos.html#torch.arccos "torch.arccos") | Alias for [`torch.acos()`](https://docs.pytorch.org/docs/2.15/generated/torch.acos.html#torch.acos "torch.acos")<br>. |\
| [`arccos_`](https://docs.pytorch.org/docs/2.15/generated/torch.arccos_.html#torch.arccos_ "torch.arccos_") | In-place version of [`torch.arccos()`](https://docs.pytorch.org/docs/2.15/generated/torch.arccos.html#torch.arccos "torch.arccos") |\
| [`acosh`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh.html#torch.acosh "torch.acosh") | Returns a new tensor with the inverse hyperbolic cosine of the elements of `input`. |\
| [`acosh_`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh_.html#torch.acosh_ "torch.acosh_") | In-place version of [`torch.acosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh.html#torch.acosh "torch.acosh") |\
| [`arccosh`](https://docs.pytorch.org/docs/2.15/generated/torch.arccosh.html#torch.arccosh "torch.arccosh") | Alias for [`torch.acosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.acosh.html#torch.acosh "torch.acosh")<br>. |\
| [`arccosh_`](https://docs.pytorch.org/docs/2.15/generated/torch.arccosh_.html#torch.arccosh_ "torch.arccosh_") | In-place version of [`torch.arccosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.arccosh.html#torch.arccosh "torch.arccosh") |\
| [`add`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add") | Adds `other`, scaled by `alpha`, to `input`. |\
| [`addcdiv`](https://docs.pytorch.org/docs/2.15/generated/torch.addcdiv.html#torch.addcdiv "torch.addcdiv") | Performs the element-wise division of `tensor1` by `tensor2`, multiplies the result by the scalar `value` and adds it to `input`. |\
| [`addcmul`](https://docs.pytorch.org/docs/2.15/generated/torch.addcmul.html#torch.addcmul "torch.addcmul") | Performs the element-wise multiplication of `tensor1` by `tensor2`, multiplies the result by the scalar `value` and adds it to `input`. |\
| [`angle`](https://docs.pytorch.org/docs/2.15/generated/torch.angle.html#torch.angle "torch.angle") | Computes the element-wise angle (in radians) of the given `input` tensor. |\
| [`asin`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin") | Returns a new tensor with the arcsine of the elements (in radians) in the `input` tensor. |\
| [`asin_`](https://docs.pytorch.org/docs/2.15/generated/torch.asin_.html#torch.asin_ "torch.asin_") | In-place version of [`torch.asin()`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin") |\
| [`arcsin`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsin.html#torch.arcsin "torch.arcsin") | Alias for [`torch.asin()`](https://docs.pytorch.org/docs/2.15/generated/torch.asin.html#torch.asin "torch.asin")<br>. |\
| [`arcsin_`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsin_.html#torch.arcsin_ "torch.arcsin_") | In-place version of [`torch.arcsin()`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsin.html#torch.arcsin "torch.arcsin") |\
| [`asinh`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh.html#torch.asinh "torch.asinh") | Returns a new tensor with the inverse hyperbolic sine of the elements of `input`. |\
| [`asinh_`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh_.html#torch.asinh_ "torch.asinh_") | In-place version of [`torch.asinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh.html#torch.asinh "torch.asinh") |\
| [`arcsinh`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsinh.html#torch.arcsinh "torch.arcsinh") | Alias for [`torch.asinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.asinh.html#torch.asinh "torch.asinh")<br>. |\
| [`arcsinh_`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsinh_.html#torch.arcsinh_ "torch.arcsinh_") | In-place version of [`torch.arcsinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.arcsinh.html#torch.arcsinh "torch.arcsinh") |\
| [`atan`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan") | Returns a new tensor with the arctangent of the elements (in radians) in the `input` tensor. |\
| [`atan_`](https://docs.pytorch.org/docs/2.15/generated/torch.atan_.html#torch.atan_ "torch.atan_") | In-place version of [`torch.atan()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan") |\
| [`arctan`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan.html#torch.arctan "torch.arctan") | Alias for [`torch.atan()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan.html#torch.atan "torch.atan")<br>. |\
| [`arctan_`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan_.html#torch.arctan_ "torch.arctan_") | In-place version of [`torch.arctan()`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan.html#torch.arctan "torch.arctan") |\
| [`atanh`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh.html#torch.atanh "torch.atanh") | Returns a new tensor with the inverse hyperbolic tangent of the elements of `input`. |\
| [`atanh_`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh_.html#torch.atanh_ "torch.atanh_") | In-place version of [`torch.atanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh.html#torch.atanh "torch.atanh") |\
| [`arctanh`](https://docs.pytorch.org/docs/2.15/generated/torch.arctanh.html#torch.arctanh "torch.arctanh") | Alias for [`torch.atanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.atanh.html#torch.atanh "torch.atanh")<br>. |\
| [`arctanh_`](https://docs.pytorch.org/docs/2.15/generated/torch.arctanh_.html#torch.arctanh_ "torch.arctanh_") | In-place version of [`torch.arctanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.arctanh.html#torch.arctanh "torch.arctanh") |\
| [`atan2`](https://docs.pytorch.org/docs/2.15/generated/torch.atan2.html#torch.atan2 "torch.atan2") | Element-wise arctangent of inputi/otheri\\text{input}\_{i} / \\text{other}\_{i}inputi​/otheri​ with consideration of the quadrant. |\
| [`arctan2`](https://docs.pytorch.org/docs/2.15/generated/torch.arctan2.html#torch.arctan2 "torch.arctan2") | Alias for [`torch.atan2()`](https://docs.pytorch.org/docs/2.15/generated/torch.atan2.html#torch.atan2 "torch.atan2")<br>. |\
| [`bitwise_not`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_not.html#torch.bitwise_not "torch.bitwise_not") | Computes the bitwise NOT of the given input tensor. |\
| [`bitwise_and`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_and.html#torch.bitwise_and "torch.bitwise_and") | Computes the bitwise AND of `input` and `other`. |\
| [`bitwise_or`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_or.html#torch.bitwise_or "torch.bitwise_or") | Computes the bitwise OR of `input` and `other`. |\
| [`bitwise_xor`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_xor.html#torch.bitwise_xor "torch.bitwise_xor") | Computes the bitwise XOR of `input` and `other`. |\
| [`bitwise_left_shift`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_left_shift.html#torch.bitwise_left_shift "torch.bitwise_left_shift") | Computes the left arithmetic shift of `input` by `other` bits. |\
| [`bitwise_right_shift`](https://docs.pytorch.org/docs/2.15/generated/torch.bitwise_right_shift.html#torch.bitwise_right_shift "torch.bitwise_right_shift") | Computes the right arithmetic shift of `input` by `other` bits. |\
| [`ceil`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil.html#torch.ceil "torch.ceil") | Returns a new tensor with the ceil of the elements of `input`, the smallest integer greater than or equal to each element. |\
| [`ceil_`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil_.html#torch.ceil_ "torch.ceil_") | In-place version of [`torch.ceil()`](https://docs.pytorch.org/docs/2.15/generated/torch.ceil.html#torch.ceil "torch.ceil") |\
| [`clamp`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp") | Clamps all elements in `input` into the range \[ [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min")<br>, [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")<br> \]. |\
| [`clamp_`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp_.html#torch.clamp_ "torch.clamp_") | In-place version of [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp") |\
| [`clamp_max_`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp_max_.html#torch.clamp_max_ "torch.clamp_max_") |     |\
| [`clamp_min_`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp_min_.html#torch.clamp_min_ "torch.clamp_min_") |     |\
| [`clip`](https://docs.pytorch.org/docs/2.15/generated/torch.clip.html#torch.clip "torch.clip") | Alias for [`torch.clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")<br>. |\
| [`clip_`](https://docs.pytorch.org/docs/2.15/generated/torch.clip_.html#torch.clip_ "torch.clip_") | In-place version of [`torch.clip()`](https://docs.pytorch.org/docs/2.15/generated/torch.clip.html#torch.clip "torch.clip") |\
| [`conj_physical`](https://docs.pytorch.org/docs/2.15/generated/torch.conj_physical.html#torch.conj_physical "torch.conj_physical") | Computes the element-wise conjugate of the given `input` tensor. |\
| [`conj_physical_`](https://docs.pytorch.org/docs/2.15/generated/torch.conj_physical_.html#torch.conj_physical_ "torch.conj_physical_") | In-place version of [`torch.conj_physical()`](https://docs.pytorch.org/docs/2.15/generated/torch.conj_physical.html#torch.conj_physical "torch.conj_physical") |\
| [`copysign`](https://docs.pytorch.org/docs/2.15/generated/torch.copysign.html#torch.copysign "torch.copysign") | Create a new floating-point tensor with the magnitude of `input` and the sign of `other`, elementwise. |\
| [`cos`](https://docs.pytorch.org/docs/2.15/generated/torch.cos.html#torch.cos "torch.cos") | Returns a new tensor with the cosine of the elements of `input` given in radians. |\
| [`cos_`](https://docs.pytorch.org/docs/2.15/generated/torch.cos_.html#torch.cos_ "torch.cos_") | In-place version of [`torch.cos()`](https://docs.pytorch.org/docs/2.15/generated/torch.cos.html#torch.cos "torch.cos") |\
| [`cosh`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh.html#torch.cosh "torch.cosh") | Returns a new tensor with the hyperbolic cosine of the elements of `input`. |\
| [`cosh_`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh_.html#torch.cosh_ "torch.cosh_") | In-place version of [`torch.cosh()`](https://docs.pytorch.org/docs/2.15/generated/torch.cosh.html#torch.cosh "torch.cosh") |\
| [`deg2rad`](https://docs.pytorch.org/docs/2.15/generated/torch.deg2rad.html#torch.deg2rad "torch.deg2rad") | Returns a new tensor with each of the elements of `input` converted from angles in degrees to radians. |\
| [`deg2rad_`](https://docs.pytorch.org/docs/2.15/generated/torch.deg2rad_.html#torch.deg2rad_ "torch.deg2rad_") | In-place version of [`torch.deg2rad()`](https://docs.pytorch.org/docs/2.15/generated/torch.deg2rad.html#torch.deg2rad "torch.deg2rad") |\
| [`div`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div") | Divides each element of the input `input` by the corresponding element of `other`. |\
| [`divide`](https://docs.pytorch.org/docs/2.15/generated/torch.divide.html#torch.divide "torch.divide") | Alias for [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br>. |\
| [`digamma`](https://docs.pytorch.org/docs/2.15/generated/torch.digamma.html#torch.digamma "torch.digamma") | Alias for [`torch.special.digamma()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.digamma "torch.special.digamma")<br>. |\
| [`erf`](https://docs.pytorch.org/docs/2.15/generated/torch.erf.html#torch.erf "torch.erf") | Alias for [`torch.special.erf()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erf "torch.special.erf")<br>. |\
| [`erf_`](https://docs.pytorch.org/docs/2.15/generated/torch.erf_.html#torch.erf_ "torch.erf_") | In-place version of [`torch.erf()`](https://docs.pytorch.org/docs/2.15/generated/torch.erf.html#torch.erf "torch.erf") |\
| [`erfc`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc.html#torch.erfc "torch.erfc") | Alias for [`torch.special.erfc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfc "torch.special.erfc")<br>. |\
| [`erfc_`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc_.html#torch.erfc_ "torch.erfc_") | In-place version of [`torch.erfc()`](https://docs.pytorch.org/docs/2.15/generated/torch.erfc.html#torch.erfc "torch.erfc") |\
| [`erfinv`](https://docs.pytorch.org/docs/2.15/generated/torch.erfinv.html#torch.erfinv "torch.erfinv") | Alias for [`torch.special.erfinv()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfinv "torch.special.erfinv")<br>. |\
| [`exp`](https://docs.pytorch.org/docs/2.15/generated/torch.exp.html#torch.exp "torch.exp") | Returns a new tensor with the exponential of the elements of the input tensor `input`. |\
| [`exp_`](https://docs.pytorch.org/docs/2.15/generated/torch.exp_.html#torch.exp_ "torch.exp_") | In-place version of [`torch.exp()`](https://docs.pytorch.org/docs/2.15/generated/torch.exp.html#torch.exp "torch.exp") |\
| [`exp2`](https://docs.pytorch.org/docs/2.15/generated/torch.exp2.html#torch.exp2 "torch.exp2") | Alias for [`torch.special.exp2()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.exp2 "torch.special.exp2")<br>. |\
| [`exp2_`](https://docs.pytorch.org/docs/2.15/generated/torch.exp2_.html#torch.exp2_ "torch.exp2_") | In-place version of [`torch.exp2()`](https://docs.pytorch.org/docs/2.15/generated/torch.exp2.html#torch.exp2 "torch.exp2") |\
| [`expm1`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1.html#torch.expm1 "torch.expm1") | Alias for [`torch.special.expm1()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expm1 "torch.special.expm1")<br>. |\
| [`expm1_`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1_.html#torch.expm1_ "torch.expm1_") | In-place version of [`torch.expm1()`](https://docs.pytorch.org/docs/2.15/generated/torch.expm1.html#torch.expm1 "torch.expm1") |\
| [`fake_quantize_per_channel_affine`](https://docs.pytorch.org/docs/2.15/generated/torch.fake_quantize_per_channel_affine.html#torch.fake_quantize_per_channel_affine "torch.fake_quantize_per_channel_affine") | Returns a new tensor with the data in `input` fake quantized per channel using `scale`, `zero_point`, `quant_min` and `quant_max`, across the channel specified by `axis`. |\
| [`fake_quantize_per_tensor_affine`](https://docs.pytorch.org/docs/2.15/generated/torch.fake_quantize_per_tensor_affine.html#torch.fake_quantize_per_tensor_affine "torch.fake_quantize_per_tensor_affine") | Returns a new tensor with the data in `input` fake quantized using `scale`, `zero_point`, `quant_min` and `quant_max`. |\
| [`fill_`](https://docs.pytorch.org/docs/2.15/generated/torch.fill_.html#torch.fill_ "torch.fill_") | In-place version of [`torch.fill()`](https://docs.pytorch.org/docs/2.15/generated/torch.fill.html#torch.fill "torch.fill") |\
| [`fix`](https://docs.pytorch.org/docs/2.15/generated/torch.fix.html#torch.fix "torch.fix") | Alias for [`torch.trunc()`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc") |\
| [`fix_`](https://docs.pytorch.org/docs/2.15/generated/torch.fix_.html#torch.fix_ "torch.fix_") | In-place version of [`torch.fix()`](https://docs.pytorch.org/docs/2.15/generated/torch.fix.html#torch.fix "torch.fix") |\
| [`float_power`](https://docs.pytorch.org/docs/2.15/generated/torch.float_power.html#torch.float_power "torch.float_power") | Raises `input` to the power of `exponent`, elementwise, in double precision. |\
| [`floor`](https://docs.pytorch.org/docs/2.15/generated/torch.floor.html#torch.floor "torch.floor") | Returns a new tensor with the floor of the elements of `input`, the largest integer less than or equal to each element. |\
| [`floor_`](https://docs.pytorch.org/docs/2.15/generated/torch.floor_.html#torch.floor_ "torch.floor_") | In-place version of [`torch.floor()`](https://docs.pytorch.org/docs/2.15/generated/torch.floor.html#torch.floor "torch.floor") |\
| [`floor_divide`](https://docs.pytorch.org/docs/2.15/generated/torch.floor_divide.html#torch.floor_divide "torch.floor_divide") |     |\
| [`fmod`](https://docs.pytorch.org/docs/2.15/generated/torch.fmod.html#torch.fmod "torch.fmod") | Applies C++'s [std::fmod](https://en.cppreference.com/w/cpp/numeric/math/fmod)<br> entrywise. |\
| [`frac`](https://docs.pytorch.org/docs/2.15/generated/torch.frac.html#torch.frac "torch.frac") | Computes the fractional portion of each element in `input`. |\
| [`frac_`](https://docs.pytorch.org/docs/2.15/generated/torch.frac_.html#torch.frac_ "torch.frac_") | In-place version of [`torch.frac()`](https://docs.pytorch.org/docs/2.15/generated/torch.frac.html#torch.frac "torch.frac") |\
| [`frexp`](https://docs.pytorch.org/docs/2.15/generated/torch.frexp.html#torch.frexp "torch.frexp") | Decomposes `input` into mantissa and exponent tensors such that input\=mantissa×2exponent\\text{input} = \\text{mantissa} \\times 2^{\\text{exponent}}input\=mantissa×2exponent. |\
| [`gradient`](https://docs.pytorch.org/docs/2.15/generated/torch.gradient.html#torch.gradient "torch.gradient") | Estimates the gradient of a function g:Rn→Rg : \\mathbb{R}^n \\rightarrow \\mathbb{R}g:Rn→R in one or more dimensions using the [second-order accurate central differences method](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf)<br> and either first or second order estimates at the boundaries. |\
| [`imag`](https://docs.pytorch.org/docs/2.15/generated/torch.imag.html#torch.imag "torch.imag") | Returns a new tensor containing imaginary values of the `self` tensor. |\
| [`ldexp`](https://docs.pytorch.org/docs/2.15/generated/torch.ldexp.html#torch.ldexp "torch.ldexp") | Multiplies `input` by 2 \*\* `other`. |\
| [`ldexp_`](https://docs.pytorch.org/docs/2.15/generated/torch.ldexp_.html#torch.ldexp_ "torch.ldexp_") | In-place version of [`torch.ldexp()`](https://docs.pytorch.org/docs/2.15/generated/torch.ldexp.html#torch.ldexp "torch.ldexp") |\
| [`lerp`](https://docs.pytorch.org/docs/2.15/generated/torch.lerp.html#torch.lerp "torch.lerp") | Does a linear interpolation of two tensors `start` (given by `input`) and `end` based on a scalar or tensor `weight` and returns the resulting `out` tensor. |\
| [`lgamma`](https://docs.pytorch.org/docs/2.15/generated/torch.lgamma.html#torch.lgamma "torch.lgamma") | Computes the natural logarithm of the absolute value of the gamma function on `input`. |\
| [`log`](https://docs.pytorch.org/docs/2.15/generated/torch.log.html#torch.log "torch.log") | Returns a new tensor with the natural logarithm of the elements of `input`. |\
| [`log_`](https://docs.pytorch.org/docs/2.15/generated/torch.log_.html#torch.log_ "torch.log_") | In-place version of [`torch.log()`](https://docs.pytorch.org/docs/2.15/generated/torch.log.html#torch.log "torch.log") |\
| [`log10`](https://docs.pytorch.org/docs/2.15/generated/torch.log10.html#torch.log10 "torch.log10") | Returns a new tensor with the logarithm to the base 10 of the elements of `input`. |\
| [`log10_`](https://docs.pytorch.org/docs/2.15/generated/torch.log10_.html#torch.log10_ "torch.log10_") | In-place version of [`torch.log10()`](https://docs.pytorch.org/docs/2.15/generated/torch.log10.html#torch.log10 "torch.log10") |\
| [`log1p`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p") | Returns a new tensor with the natural logarithm of (1 + `input`). |\
| [`log1p_`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p_.html#torch.log1p_ "torch.log1p_") | In-place version of [`torch.log1p()`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p") |\
| [`log2`](https://docs.pytorch.org/docs/2.15/generated/torch.log2.html#torch.log2 "torch.log2") | Returns a new tensor with the logarithm to the base 2 of the elements of `input`. |\
| [`log2_`](https://docs.pytorch.org/docs/2.15/generated/torch.log2_.html#torch.log2_ "torch.log2_") | In-place version of [`torch.log2()`](https://docs.pytorch.org/docs/2.15/generated/torch.log2.html#torch.log2 "torch.log2") |\
| [`logaddexp`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp.html#torch.logaddexp "torch.logaddexp") | Logarithm of the sum of exponentiations of the inputs. |\
| [`logaddexp2`](https://docs.pytorch.org/docs/2.15/generated/torch.logaddexp2.html#torch.logaddexp2 "torch.logaddexp2") | Logarithm of the sum of exponentiations of the inputs in base-2. |\
| [`logical_and`](https://docs.pytorch.org/docs/2.15/generated/torch.logical_and.html#torch.logical_and "torch.logical_and") | Computes the element-wise logical AND of the given input tensors. |\
| [`logical_not`](https://docs.pytorch.org/docs/2.15/generated/torch.logical_not.html#torch.logical_not "torch.logical_not") | Computes the element-wise logical NOT of the given input tensor. |\
| [`logical_or`](https://docs.pytorch.org/docs/2.15/generated/torch.logical_or.html#torch.logical_or "torch.logical_or") | Computes the element-wise logical OR of the given input tensors. |\
| [`logical_xor`](https://docs.pytorch.org/docs/2.15/generated/torch.logical_xor.html#torch.logical_xor "torch.logical_xor") | Computes the element-wise logical XOR of the given input tensors. |\
| [`logit`](https://docs.pytorch.org/docs/2.15/generated/torch.logit.html#torch.logit "torch.logit") | Alias for [`torch.special.logit()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.logit "torch.special.logit")<br>. |\
| [`logit_`](https://docs.pytorch.org/docs/2.15/generated/torch.logit_.html#torch.logit_ "torch.logit_") | In-place version of [`torch.logit()`](https://docs.pytorch.org/docs/2.15/generated/torch.logit.html#torch.logit "torch.logit") |\
| [`hypot`](https://docs.pytorch.org/docs/2.15/generated/torch.hypot.html#torch.hypot "torch.hypot") | Given the legs of a right triangle, return its hypotenuse. |\
| [`i0`](https://docs.pytorch.org/docs/2.15/generated/torch.i0.html#torch.i0 "torch.i0") | Alias for [`torch.special.i0()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i0 "torch.special.i0")<br>. |\
| [`i0_`](https://docs.pytorch.org/docs/2.15/generated/torch.i0_.html#torch.i0_ "torch.i0_") | In-place version of [`torch.i0()`](https://docs.pytorch.org/docs/2.15/generated/torch.i0.html#torch.i0 "torch.i0") |\
| [`igamma`](https://docs.pytorch.org/docs/2.15/generated/torch.igamma.html#torch.igamma "torch.igamma") | Alias for [`torch.special.gammainc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammainc "torch.special.gammainc")<br>. |\
| [`igammac`](https://docs.pytorch.org/docs/2.15/generated/torch.igammac.html#torch.igammac "torch.igammac") | Alias for [`torch.special.gammaincc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaincc "torch.special.gammaincc")<br>. |\
| [`mul`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul") | Multiplies `input` by `other`. |\
| [`multiply`](https://docs.pytorch.org/docs/2.15/generated/torch.multiply.html#torch.multiply "torch.multiply") | Alias for [`torch.mul()`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul")<br>. |\
| [`mvlgamma`](https://docs.pytorch.org/docs/2.15/generated/torch.mvlgamma.html#torch.mvlgamma "torch.mvlgamma") | Alias for [`torch.special.multigammaln()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.multigammaln "torch.special.multigammaln")<br>. |\
| [`nan_to_num`](https://docs.pytorch.org/docs/2.15/generated/torch.nan_to_num.html#torch.nan_to_num "torch.nan_to_num") | Replaces `NaN`, positive infinity, and negative infinity values in `input` with the values specified by `nan`, `posinf`, and `neginf`, respectively. |\
| [`nan_to_num_`](https://docs.pytorch.org/docs/2.15/generated/torch.nan_to_num_.html#torch.nan_to_num_ "torch.nan_to_num_") | In-place version of [`torch.nan_to_num()`](https://docs.pytorch.org/docs/2.15/generated/torch.nan_to_num.html#torch.nan_to_num "torch.nan_to_num") |\
| [`neg`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg") | Returns a new tensor with the negative of the elements of `input`. |\
| [`neg_`](https://docs.pytorch.org/docs/2.15/generated/torch.neg_.html#torch.neg_ "torch.neg_") | In-place version of [`torch.neg()`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg") |\
| [`negative`](https://docs.pytorch.org/docs/2.15/generated/torch.negative.html#torch.negative "torch.negative") | Alias for [`torch.neg()`](https://docs.pytorch.org/docs/2.15/generated/torch.neg.html#torch.neg "torch.neg") |\
| [`negative_`](https://docs.pytorch.org/docs/2.15/generated/torch.negative_.html#torch.negative_ "torch.negative_") | In-place version of [`torch.negative()`](https://docs.pytorch.org/docs/2.15/generated/torch.negative.html#torch.negative "torch.negative") |\
| [`nextafter`](https://docs.pytorch.org/docs/2.15/generated/torch.nextafter.html#torch.nextafter "torch.nextafter") | Return the next floating-point value after `input` towards `other`, elementwise. |\
| [`polygamma`](https://docs.pytorch.org/docs/2.15/generated/torch.polygamma.html#torch.polygamma "torch.polygamma") | Alias for [`torch.special.polygamma()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.polygamma "torch.special.polygamma")<br>. |\
| [`positive`](https://docs.pytorch.org/docs/2.15/generated/torch.positive.html#torch.positive "torch.positive") | Returns `input`. |\
| [`pow`](https://docs.pytorch.org/docs/2.15/generated/torch.pow.html#torch.pow "torch.pow") | Takes the power of each element in `input` with `exponent` and returns a tensor with the result. |\
| [`quantized_batch_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_batch_norm.html#torch.quantized_batch_norm "torch.quantized_batch_norm") | Applies batch normalization on a 4D (NCHW) quantized tensor. |\
| [`quantized_max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_max_pool1d.html#torch.quantized_max_pool1d "torch.quantized_max_pool1d") | Applies a 1D max pooling over an input quantized tensor composed of several input planes. |\
| [`quantized_max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_max_pool2d.html#torch.quantized_max_pool2d "torch.quantized_max_pool2d") | Applies a 2D max pooling over an input quantized tensor composed of several input planes. |\
| [`rad2deg`](https://docs.pytorch.org/docs/2.15/generated/torch.rad2deg.html#torch.rad2deg "torch.rad2deg") | Returns a new tensor with each of the elements of `input` converted from angles in radians to degrees. |\
| [`rad2deg_`](https://docs.pytorch.org/docs/2.15/generated/torch.rad2deg_.html#torch.rad2deg_ "torch.rad2deg_") | In-place version of [`torch.rad2deg()`](https://docs.pytorch.org/docs/2.15/generated/torch.rad2deg.html#torch.rad2deg "torch.rad2deg") |\
| [`real`](https://docs.pytorch.org/docs/2.15/generated/torch.real.html#torch.real "torch.real") | Returns a new tensor containing real values of the `self` tensor. |\
| [`reciprocal`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal.html#torch.reciprocal "torch.reciprocal") | Returns a new tensor with the reciprocal of the elements of `input` |\
| [`reciprocal_`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal_.html#torch.reciprocal_ "torch.reciprocal_") | In-place version of [`torch.reciprocal()`](https://docs.pytorch.org/docs/2.15/generated/torch.reciprocal.html#torch.reciprocal "torch.reciprocal") |\
| [`remainder`](https://docs.pytorch.org/docs/2.15/generated/torch.remainder.html#torch.remainder "torch.remainder") | Computes [Python's modulus operation](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)<br> entrywise. |\
| [`round`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round") | Rounds elements of `input` to the nearest integer. |\
| [`round_`](https://docs.pytorch.org/docs/2.15/generated/torch.round_.html#torch.round_ "torch.round_") | In-place version of [`torch.round()`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round") |\
| [`rsqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt.html#torch.rsqrt "torch.rsqrt") | Returns a new tensor with the reciprocal of the square-root of each of the elements of `input`. |\
| [`rsqrt_`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt_.html#torch.rsqrt_ "torch.rsqrt_") | In-place version of [`torch.rsqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.rsqrt.html#torch.rsqrt "torch.rsqrt") |\
| [`sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid.html#torch.sigmoid "torch.sigmoid") | Alias for [`torch.special.expit()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expit "torch.special.expit")<br>. |\
| [`sigmoid_`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid_.html#torch.sigmoid_ "torch.sigmoid_") | In-place version of [`torch.sigmoid()`](https://docs.pytorch.org/docs/2.15/generated/torch.sigmoid.html#torch.sigmoid "torch.sigmoid") |\
| [`sign`](https://docs.pytorch.org/docs/2.15/generated/torch.sign.html#torch.sign "torch.sign") | Returns a new tensor with the signs of the elements of `input`. |\
| [`sgn`](https://docs.pytorch.org/docs/2.15/generated/torch.sgn.html#torch.sgn "torch.sgn") | This function is an extension of torch.sign() to complex tensors. |\
| [`signbit`](https://docs.pytorch.org/docs/2.15/generated/torch.signbit.html#torch.signbit "torch.signbit") | Tests if each element of `input` has its sign bit set or not. |\
| [`sin`](https://docs.pytorch.org/docs/2.15/generated/torch.sin.html#torch.sin "torch.sin") | Returns a new tensor with the sine of the elements in the `input` tensor, where each value in this input tensor is in radians. |\
| [`sin_`](https://docs.pytorch.org/docs/2.15/generated/torch.sin_.html#torch.sin_ "torch.sin_") | In-place version of [`torch.sin()`](https://docs.pytorch.org/docs/2.15/generated/torch.sin.html#torch.sin "torch.sin") |\
| [`sinc`](https://docs.pytorch.org/docs/2.15/generated/torch.sinc.html#torch.sinc "torch.sinc") | Alias for [`torch.special.sinc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.sinc "torch.special.sinc")<br>. |\
| [`sinc_`](https://docs.pytorch.org/docs/2.15/generated/torch.sinc_.html#torch.sinc_ "torch.sinc_") | In-place version of [`torch.sinc()`](https://docs.pytorch.org/docs/2.15/generated/torch.sinc.html#torch.sinc "torch.sinc") |\
| [`sinh`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh.html#torch.sinh "torch.sinh") | Returns a new tensor with the hyperbolic sine of the elements of `input`. |\
| [`sinh_`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh_.html#torch.sinh_ "torch.sinh_") | In-place version of [`torch.sinh()`](https://docs.pytorch.org/docs/2.15/generated/torch.sinh.html#torch.sinh "torch.sinh") |\
| [`softmax`](https://docs.pytorch.org/docs/2.15/generated/torch.softmax.html#torch.softmax "torch.softmax") | Alias for [`torch.nn.functional.softmax()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.softmax.html#torch.nn.functional.softmax "torch.nn.functional.softmax")<br>. |\
| [`sqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt.html#torch.sqrt "torch.sqrt") | Returns a new tensor with the square-root of the elements of `input`. |\
| [`sqrt_`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt_.html#torch.sqrt_ "torch.sqrt_") | In-place version of [`torch.sqrt()`](https://docs.pytorch.org/docs/2.15/generated/torch.sqrt.html#torch.sqrt "torch.sqrt") |\
| [`square`](https://docs.pytorch.org/docs/2.15/generated/torch.square.html#torch.square "torch.square") | Returns a new tensor with the square of the elements of `input`. |\
| [`square_`](https://docs.pytorch.org/docs/2.15/generated/torch.square_.html#torch.square_ "torch.square_") | In-place version of [`torch.square()`](https://docs.pytorch.org/docs/2.15/generated/torch.square.html#torch.square "torch.square") |\
| [`sub`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub") | Subtracts `other`, scaled by `alpha`, from `input`. |\
| [`subtract`](https://docs.pytorch.org/docs/2.15/generated/torch.subtract.html#torch.subtract "torch.subtract") | Alias for [`torch.sub()`](https://docs.pytorch.org/docs/2.15/generated/torch.sub.html#torch.sub "torch.sub")<br>. |\
| [`tan`](https://docs.pytorch.org/docs/2.15/generated/torch.tan.html#torch.tan "torch.tan") | Returns a new tensor with the tangent of the elements in the `input` tensor, where each value in this input tensor is in radians. |\
| [`tan_`](https://docs.pytorch.org/docs/2.15/generated/torch.tan_.html#torch.tan_ "torch.tan_") | In-place version of [`torch.tan()`](https://docs.pytorch.org/docs/2.15/generated/torch.tan.html#torch.tan "torch.tan") |\
| [`tanh`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh.html#torch.tanh "torch.tanh") | Returns a new tensor with the hyperbolic tangent of the elements of `input`. |\
| [`tanh_`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh_.html#torch.tanh_ "torch.tanh_") | In-place version of [`torch.tanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.tanh.html#torch.tanh "torch.tanh") |\
| [`true_divide`](https://docs.pytorch.org/docs/2.15/generated/torch.true_divide.html#torch.true_divide "torch.true_divide") | Alias for [`torch.div()`](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "torch.div")<br> with `rounding_mode=None`. |\
| [`trunc`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc") | Returns a new tensor with the truncated integer values of the elements of `input`. |\
| [`trunc_`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc_.html#torch.trunc_ "torch.trunc_") | In-place version of [`torch.trunc()`](https://docs.pytorch.org/docs/2.15/generated/torch.trunc.html#torch.trunc "torch.trunc") |\
| [`xlogy`](https://docs.pytorch.org/docs/2.15/generated/torch.xlogy.html#torch.xlogy "torch.xlogy") | Alias for [`torch.special.xlogy()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.xlogy "torch.special.xlogy")<br>. |\
| [`xlogy_`](https://docs.pytorch.org/docs/2.15/generated/torch.xlogy_.html#torch.xlogy_ "torch.xlogy_") | In-place version of [`torch.xlogy()`](https://docs.pytorch.org/docs/2.15/generated/torch.xlogy.html#torch.xlogy "torch.xlogy") |\
| [`zero_`](https://docs.pytorch.org/docs/2.15/generated/torch.zero_.html#torch.zero_ "torch.zero_") |     |\
\
### Reduction Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#reduction-ops "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`argmax`](https://docs.pytorch.org/docs/2.15/generated/torch.argmax.html#torch.argmax "torch.argmax") | Returns the indices of the maximum value of all elements in the `input` tensor. |\
| [`argmin`](https://docs.pytorch.org/docs/2.15/generated/torch.argmin.html#torch.argmin "torch.argmin") | Returns the indices of the minimum value(s) of the flattened tensor or along a dimension |\
| [`amax`](https://docs.pytorch.org/docs/2.15/generated/torch.amax.html#torch.amax "torch.amax") | Returns the maximum value of each slice of the `input` tensor in the given dimension(s) `dim`. |\
| [`amin`](https://docs.pytorch.org/docs/2.15/generated/torch.amin.html#torch.amin "torch.amin") | Returns the minimum value of each slice of the `input` tensor in the given dimension(s) `dim`. |\
| [`aminmax`](https://docs.pytorch.org/docs/2.15/generated/torch.aminmax.html#torch.aminmax "torch.aminmax") | Computes the minimum and maximum values of the `input` tensor. |\
| [`all`](https://docs.pytorch.org/docs/2.15/generated/torch.all.html#torch.all "torch.all") | Tests if all elements in `input` evaluate to True. |\
| [`any`](https://docs.pytorch.org/docs/2.15/generated/torch.any.html#torch.any "torch.any") | Tests if any element in `input` evaluates to True. |\
| [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max") | Returns the maximum value of all elements in the `input` tensor. |\
| [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min") | Returns the minimum value of all elements in the `input` tensor. |\
| [`dist`](https://docs.pytorch.org/docs/2.15/generated/torch.dist.html#torch.dist "torch.dist") | Returns the p-norm of (`input` - `other`) |\
| [`logsumexp`](https://docs.pytorch.org/docs/2.15/generated/torch.logsumexp.html#torch.logsumexp "torch.logsumexp") | Returns the log of summed exponentials of each row of the `input` tensor in the given dimension `dim`. |\
| [`mean`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean") |     |\
| [`nanmean`](https://docs.pytorch.org/docs/2.15/generated/torch.nanmean.html#torch.nanmean "torch.nanmean") | Computes the mean of all non-NaN elements along the specified dimensions. |\
| [`median`](https://docs.pytorch.org/docs/2.15/generated/torch.median.html#torch.median "torch.median") | Returns the median of the values in `input`. |\
| [`nanmedian`](https://docs.pytorch.org/docs/2.15/generated/torch.nanmedian.html#torch.nanmedian "torch.nanmedian") | Returns the median of the values in `input`, ignoring `NaN` values. |\
| [`mode`](https://docs.pytorch.org/docs/2.15/generated/torch.mode.html#torch.mode "torch.mode") | Returns a namedtuple `(values, indices)` where `values` is the mode value of each row of the `input` tensor in the given dimension `dim`, i.e. a value which appears most often in that row, and `indices` is the index location of each mode value found. |\
| [`norm`](https://docs.pytorch.org/docs/2.15/generated/torch.norm.html#torch.norm "torch.norm") | Returns the matrix norm or vector norm of a given tensor. |\
| [`norm_except_dim`](https://docs.pytorch.org/docs/2.15/generated/torch.norm_except_dim.html#torch.norm_except_dim "torch.norm_except_dim") |     |\
| [`nuclear_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.nuclear_norm.html#torch.nuclear_norm "torch.nuclear_norm") |     |\
| [`nansum`](https://docs.pytorch.org/docs/2.15/generated/torch.nansum.html#torch.nansum "torch.nansum") | Returns the sum of all elements, treating Not a Numbers (NaNs) as zero. |\
| [`prod`](https://docs.pytorch.org/docs/2.15/generated/torch.prod.html#torch.prod "torch.prod") | Returns the product of all elements in the `input` tensor. |\
| [`quantile`](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch.quantile "torch.quantile") | Computes the q-th quantiles of each row of the `input` tensor along the dimension `dim`. |\
| [`nanquantile`](https://docs.pytorch.org/docs/2.15/generated/torch.nanquantile.html#torch.nanquantile "torch.nanquantile") | This is a variant of [`torch.quantile()`](https://docs.pytorch.org/docs/2.15/generated/torch.quantile.html#torch.quantile "torch.quantile")<br> that "ignores" `NaN` values, computing the quantiles `q` as if `NaN` values in `input` did not exist. |\
| [`std`](https://docs.pytorch.org/docs/2.15/generated/torch.std.html#torch.std "torch.std") | Calculates the standard deviation over the dimensions specified by `dim`. |\
| [`std_mean`](https://docs.pytorch.org/docs/2.15/generated/torch.std_mean.html#torch.std_mean "torch.std_mean") | Calculates the standard deviation and mean over the dimensions specified by `dim`. |\
| [`sum`](https://docs.pytorch.org/docs/2.15/generated/torch.sum.html#torch.sum "torch.sum") | Returns the sum of all elements in the `input` tensor. |\
| [`unique`](https://docs.pytorch.org/docs/2.15/generated/torch.unique.html#torch.unique "torch.unique") | Returns the unique elements of the input tensor. |\
| [`unique_consecutive`](https://docs.pytorch.org/docs/2.15/generated/torch.unique_consecutive.html#torch.unique_consecutive "torch.unique_consecutive") | Eliminates all but the first element from every consecutive group of equivalent elements. |\
| [`var`](https://docs.pytorch.org/docs/2.15/generated/torch.var.html#torch.var "torch.var") | Calculates the variance over the dimensions specified by `dim`. |\
| [`var_mean`](https://docs.pytorch.org/docs/2.15/generated/torch.var_mean.html#torch.var_mean "torch.var_mean") | Calculates the variance and mean over the dimensions specified by `dim`. |\
| [`count_nonzero`](https://docs.pytorch.org/docs/2.15/generated/torch.count_nonzero.html#torch.count_nonzero "torch.count_nonzero") | Counts the number of non-zero values in the tensor `input` along the given `dim`. |\
| [`hash_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.hash_tensor.html#torch.hash_tensor "torch.hash_tensor") | Returns a hash of all elements in the `input` tensor. |\
\
### Comparison Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#comparison-ops "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`allclose`](https://docs.pytorch.org/docs/2.15/generated/torch.allclose.html#torch.allclose "torch.allclose") | This function checks if `input` and `other` satisfy the condition: |\
| [`argsort`](https://docs.pytorch.org/docs/2.15/generated/torch.argsort.html#torch.argsort "torch.argsort") | Returns the indices that sort a tensor along a given dimension in ascending order by value. |\
| [`eq`](https://docs.pytorch.org/docs/2.15/generated/torch.eq.html#torch.eq "torch.eq") | Computes element-wise equality |\
| [`equal`](https://docs.pytorch.org/docs/2.15/generated/torch.equal.html#torch.equal "torch.equal") | `True` if two tensors have the same size and elements, `False` otherwise. |\
| [`ge`](https://docs.pytorch.org/docs/2.15/generated/torch.ge.html#torch.ge "torch.ge") | Computes input≥other\\text{input} \\geq \\text{other}input≥other element-wise. |\
| [`greater_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.greater_equal.html#torch.greater_equal "torch.greater_equal") | Alias for [`torch.ge()`](https://docs.pytorch.org/docs/2.15/generated/torch.ge.html#torch.ge "torch.ge")<br>. |\
| [`gt`](https://docs.pytorch.org/docs/2.15/generated/torch.gt.html#torch.gt "torch.gt") | Computes input\>other\\text{input} > \\text{other}input\>other element-wise. |\
| [`greater`](https://docs.pytorch.org/docs/2.15/generated/torch.greater.html#torch.greater "torch.greater") | Alias for [`torch.gt()`](https://docs.pytorch.org/docs/2.15/generated/torch.gt.html#torch.gt "torch.gt")<br>. |\
| [`isclose`](https://docs.pytorch.org/docs/2.15/generated/torch.isclose.html#torch.isclose "torch.isclose") | Returns a new tensor with boolean elements representing if each element of `input` is "close" to the corresponding element of `other`. |\
| [`isfinite`](https://docs.pytorch.org/docs/2.15/generated/torch.isfinite.html#torch.isfinite "torch.isfinite") | Returns a new tensor with boolean elements representing if each element is finite or not. |\
| [`isin`](https://docs.pytorch.org/docs/2.15/generated/torch.isin.html#torch.isin "torch.isin") | Tests if each element of `elements` is in `test_elements`. |\
| [`isinf`](https://docs.pytorch.org/docs/2.15/generated/torch.isinf.html#torch.isinf "torch.isinf") | Tests if each element of `input` is infinite (positive or negative infinity) or not. |\
| [`isposinf`](https://docs.pytorch.org/docs/2.15/generated/torch.isposinf.html#torch.isposinf "torch.isposinf") | Tests if each element of `input` is positive infinity or not. |\
| [`isneginf`](https://docs.pytorch.org/docs/2.15/generated/torch.isneginf.html#torch.isneginf "torch.isneginf") | Tests if each element of `input` is negative infinity or not. |\
| [`isnan`](https://docs.pytorch.org/docs/2.15/generated/torch.isnan.html#torch.isnan "torch.isnan") | Returns a new tensor with boolean elements representing if each element of `input` is NaN or not. |\
| [`isreal`](https://docs.pytorch.org/docs/2.15/generated/torch.isreal.html#torch.isreal "torch.isreal") | Returns a new tensor with boolean elements representing if each element of `input` is real-valued or not. |\
| [`kthvalue`](https://docs.pytorch.org/docs/2.15/generated/torch.kthvalue.html#torch.kthvalue "torch.kthvalue") | Returns a namedtuple `(values, indices)` where `values` is the `k` th smallest element of each row of the `input` tensor in the given dimension `dim`. |\
| [`le`](https://docs.pytorch.org/docs/2.15/generated/torch.le.html#torch.le "torch.le") | Computes input≤other\\text{input} \\leq \\text{other}input≤other element-wise. |\
| [`less_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.less_equal.html#torch.less_equal "torch.less_equal") | Alias for [`torch.le()`](https://docs.pytorch.org/docs/2.15/generated/torch.le.html#torch.le "torch.le")<br>. |\
| [`lt`](https://docs.pytorch.org/docs/2.15/generated/torch.lt.html#torch.lt "torch.lt") | Computes input<other\\text{input} < \\text{other}input<other element-wise. |\
| [`less`](https://docs.pytorch.org/docs/2.15/generated/torch.less.html#torch.less "torch.less") | Alias for [`torch.lt()`](https://docs.pytorch.org/docs/2.15/generated/torch.lt.html#torch.lt "torch.lt")<br>. |\
| [`maximum`](https://docs.pytorch.org/docs/2.15/generated/torch.maximum.html#torch.maximum "torch.maximum") | Computes the element-wise maximum of `input` and `other`. |\
| [`minimum`](https://docs.pytorch.org/docs/2.15/generated/torch.minimum.html#torch.minimum "torch.minimum") | Computes the element-wise minimum of `input` and `other`. |\
| [`fmax`](https://docs.pytorch.org/docs/2.15/generated/torch.fmax.html#torch.fmax "torch.fmax") | Computes the element-wise maximum of `input` and `other`. |\
| [`fmin`](https://docs.pytorch.org/docs/2.15/generated/torch.fmin.html#torch.fmin "torch.fmin") | Computes the element-wise minimum of `input` and `other`. |\
| [`ne`](https://docs.pytorch.org/docs/2.15/generated/torch.ne.html#torch.ne "torch.ne") | Computes input≠other\\text{input} \\neq \\text{other}input\=other element-wise. |\
| [`not_equal`](https://docs.pytorch.org/docs/2.15/generated/torch.not_equal.html#torch.not_equal "torch.not_equal") | Alias for [`torch.ne()`](https://docs.pytorch.org/docs/2.15/generated/torch.ne.html#torch.ne "torch.ne")<br>. |\
| [`sort`](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#torch.sort "torch.sort") | Sorts the elements of the `input` tensor along a given dimension in ascending order by value. |\
| [`topk`](https://docs.pytorch.org/docs/2.15/generated/torch.topk.html#torch.topk "torch.topk") | Returns the `k` largest elements of the given `input` tensor along a given dimension. |\
| [`msort`](https://docs.pytorch.org/docs/2.15/generated/torch.msort.html#torch.msort "torch.msort") | Sorts the elements of the `input` tensor along its first dimension in ascending order by value. |\
\
### Spectral Ops[#](https://docs.pytorch.org/docs/2.15/torch.html#spectral-ops "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`stft`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft") | Short-time Fourier transform (STFT). |\
| [`istft`](https://docs.pytorch.org/docs/2.15/generated/torch.istft.html#torch.istft "torch.istft") | Inverse short time Fourier Transform. |\
| [`bartlett_window`](https://docs.pytorch.org/docs/2.15/generated/torch.bartlett_window.html#torch.bartlett_window "torch.bartlett_window") | Bartlett window function. |\
| [`blackman_window`](https://docs.pytorch.org/docs/2.15/generated/torch.blackman_window.html#torch.blackman_window "torch.blackman_window") | Blackman window function. |\
| [`hamming_window`](https://docs.pytorch.org/docs/2.15/generated/torch.hamming_window.html#torch.hamming_window "torch.hamming_window") | Hamming window function. |\
| [`hann_window`](https://docs.pytorch.org/docs/2.15/generated/torch.hann_window.html#torch.hann_window "torch.hann_window") | Hann window function. |\
| [`kaiser_window`](https://docs.pytorch.org/docs/2.15/generated/torch.kaiser_window.html#torch.kaiser_window "torch.kaiser_window") | Computes the Kaiser window with window length `window_length` and shape parameter `beta`. |\
\
### Other Operations[#](https://docs.pytorch.org/docs/2.15/torch.html#other-operations "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`adaptive_avg_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.adaptive_avg_pool1d.html#torch.adaptive_avg_pool1d "torch.adaptive_avg_pool1d") | Applies a 1D adaptive average pooling over an input signal composed of several input planes. |\
| [`adaptive_max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.adaptive_max_pool1d.html#torch.adaptive_max_pool1d "torch.adaptive_max_pool1d") |     |\
| [`affine_grid_generator`](https://docs.pytorch.org/docs/2.15/generated/torch.affine_grid_generator.html#torch.affine_grid_generator "torch.affine_grid_generator") |     |\
| [`alpha_dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.alpha_dropout.html#torch.alpha_dropout "torch.alpha_dropout") |     |\
| [`alpha_dropout_`](https://docs.pytorch.org/docs/2.15/generated/torch.alpha_dropout_.html#torch.alpha_dropout_ "torch.alpha_dropout_") | In-place version of [`torch.alpha_dropout()`](https://docs.pytorch.org/docs/2.15/generated/torch.alpha_dropout.html#torch.alpha_dropout "torch.alpha_dropout") |\
| [`as_strided_`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided_.html#torch.as_strided_ "torch.as_strided_") | In-place version of [`torch.as_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided.html#torch.as_strided "torch.as_strided") |\
| [`atleast_1d`](https://docs.pytorch.org/docs/2.15/generated/torch.atleast_1d.html#torch.atleast_1d "torch.atleast_1d") | Returns a 1-dimensional view of each input tensor with zero dimensions. |\
| [`atleast_2d`](https://docs.pytorch.org/docs/2.15/generated/torch.atleast_2d.html#torch.atleast_2d "torch.atleast_2d") | Returns a 2-dimensional view of each input tensor with zero dimensions. |\
| [`atleast_3d`](https://docs.pytorch.org/docs/2.15/generated/torch.atleast_3d.html#torch.atleast_3d "torch.atleast_3d") | Returns a 3-dimensional view of each input tensor with zero dimensions. |\
| [`avg_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.avg_pool1d.html#torch.avg_pool1d "torch.avg_pool1d") | Applies a 1D average pooling over an input signal composed of several input planes. |\
| [`batch_norm_backward_elemt`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_backward_elemt.html#torch.batch_norm_backward_elemt "torch.batch_norm_backward_elemt") |     |\
| [`batch_norm_backward_reduce`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_backward_reduce.html#torch.batch_norm_backward_reduce "torch.batch_norm_backward_reduce") |     |\
| [`batch_norm_elemt`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_elemt.html#torch.batch_norm_elemt "torch.batch_norm_elemt") |     |\
| [`batch_norm_gather_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_gather_stats.html#torch.batch_norm_gather_stats "torch.batch_norm_gather_stats") |     |\
| [`batch_norm_gather_stats_with_counts`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_gather_stats_with_counts.html#torch.batch_norm_gather_stats_with_counts "torch.batch_norm_gather_stats_with_counts") |     |\
| [`batch_norm_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_stats.html#torch.batch_norm_stats "torch.batch_norm_stats") |     |\
| [`batch_norm_update_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.batch_norm_update_stats.html#torch.batch_norm_update_stats "torch.batch_norm_update_stats") |     |\
| [`bilinear`](https://docs.pytorch.org/docs/2.15/generated/torch.bilinear.html#torch.bilinear "torch.bilinear") | Applies a bilinear transformation to the incoming data: y\=x1TAx2+by = x\_1^T A x\_2 + by\=x1T​Ax2​+b |\
| [`bincount`](https://docs.pytorch.org/docs/2.15/generated/torch.bincount.html#torch.bincount "torch.bincount") | Count the frequency of each value in an array of non-negative ints. |\
| [`binomial`](https://docs.pytorch.org/docs/2.15/generated/torch.binomial.html#torch.binomial "torch.binomial") |     |\
| [`block_diag`](https://docs.pytorch.org/docs/2.15/generated/torch.block_diag.html#torch.block_diag "torch.block_diag") | Create a block diagonal matrix from provided tensors. |\
| [`broadcast_tensors`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_tensors.html#torch.broadcast_tensors "torch.broadcast_tensors") | Broadcasts the given tensors according to [Broadcasting semantics](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)<br>. |\
| [`broadcast_to`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_to.html#torch.broadcast_to "torch.broadcast_to") | Broadcasts `input` to the shape `shape`. |\
| [`broadcast_shapes`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_shapes.html#torch.broadcast_shapes "torch.broadcast_shapes") | Similar to [`broadcast_tensors()`](https://docs.pytorch.org/docs/2.15/generated/torch.broadcast_tensors.html#torch.broadcast_tensors "torch.broadcast_tensors")<br> but for shapes. |\
| [`bucketize`](https://docs.pytorch.org/docs/2.15/generated/torch.bucketize.html#torch.bucketize "torch.bucketize") | Returns the indices of the buckets to which each value in the `input` belongs, where the boundaries of the buckets are set by `boundaries`. |\
| [`cartesian_prod`](https://docs.pytorch.org/docs/2.15/generated/torch.cartesian_prod.html#torch.cartesian_prod "torch.cartesian_prod") | Do cartesian product of the given sequence of tensors. |\
| [`cdist`](https://docs.pytorch.org/docs/2.15/generated/torch.cdist.html#torch.cdist "torch.cdist") | Computes the batched p-norm distance between each pair of the two collections of row vectors. |\
| [`celu_`](https://docs.pytorch.org/docs/2.15/generated/torch.celu_.html#torch.celu_ "torch.celu_") | In-place version of `celu()`. |\
| [`channel_shuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.channel_shuffle.html#torch.channel_shuffle "torch.channel_shuffle") | Divide the channels in a tensor of shape (∗,C,H,W)(\*, C , H, W)(∗,C,H,W) into g groups and rearrange them as (∗,Cg,g,H,W)(\*, C \\frac g, g, H, W)(∗,C,g​g,H,W), while keeping the original tensor shape. |\
| [`choose_qparams_optimized`](https://docs.pytorch.org/docs/2.15/generated/torch.choose_qparams_optimized.html#torch.choose_qparams_optimized "torch.choose_qparams_optimized") |     |\
| [`clone`](https://docs.pytorch.org/docs/2.15/generated/torch.clone.html#torch.clone "torch.clone") | Returns a copy of `input`. |\
| [`combinations`](https://docs.pytorch.org/docs/2.15/generated/torch.combinations.html#torch.combinations "torch.combinations") | Compute combinations of length rrr of the given tensor. |\
| [`conv1d`](https://docs.pytorch.org/docs/2.15/generated/torch.conv1d.html#torch.conv1d "torch.conv1d") | Applies a 1D convolution over an input signal composed of several input planes. |\
| [`conv3d`](https://docs.pytorch.org/docs/2.15/generated/torch.conv3d.html#torch.conv3d "torch.conv3d") | Applies a 3D convolution over an input image composed of several input planes. |\
| [`conv_tbc`](https://docs.pytorch.org/docs/2.15/generated/torch.conv_tbc.html#torch.conv_tbc "torch.conv_tbc") | Applies a 1-dimensional sequence convolution over an input sequence. |\
| [`conv_transpose1d`](https://docs.pytorch.org/docs/2.15/generated/torch.conv_transpose1d.html#torch.conv_transpose1d "torch.conv_transpose1d") | Applies a 1D transposed convolution operator over an input signal composed of several input planes, sometimes also called "deconvolution". |\
| [`conv_transpose2d`](https://docs.pytorch.org/docs/2.15/generated/torch.conv_transpose2d.html#torch.conv_transpose2d "torch.conv_transpose2d") | Applies a 2D transposed convolution operator over an input image composed of several input planes, sometimes also called "deconvolution". |\
| [`conv_transpose3d`](https://docs.pytorch.org/docs/2.15/generated/torch.conv_transpose3d.html#torch.conv_transpose3d "torch.conv_transpose3d") | Applies a 3D transposed convolution operator over an input image composed of several input planes, sometimes also called "deconvolution" |\
| [`convolution`](https://docs.pytorch.org/docs/2.15/generated/torch.convolution.html#torch.convolution "torch.convolution") |     |\
| [`corrcoef`](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html#torch.corrcoef "torch.corrcoef") | Estimates the Pearson product-moment correlation coefficient matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations. |\
| [`cosine_embedding_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.cosine_embedding_loss.html#torch.cosine_embedding_loss "torch.cosine_embedding_loss") |     |\
| [`cosine_similarity`](https://docs.pytorch.org/docs/2.15/generated/torch.cosine_similarity.html#torch.cosine_similarity "torch.cosine_similarity") | Returns cosine similarity between `x1` and `x2`, computed along dim. |\
| [`cov`](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html#torch.cov "torch.cov") | Estimates the covariance matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations. |\
| [`cross`](https://docs.pytorch.org/docs/2.15/generated/torch.cross.html#torch.cross "torch.cross") | Returns the cross product of vectors in dimension `dim` of `input` and `other`. |\
| [`ctc_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.ctc_loss.html#torch.ctc_loss "torch.ctc_loss") |     |\
| [`cudnn_affine_grid_generator`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_affine_grid_generator.html#torch.cudnn_affine_grid_generator "torch.cudnn_affine_grid_generator") |     |\
| [`cudnn_batch_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_batch_norm.html#torch.cudnn_batch_norm "torch.cudnn_batch_norm") |     |\
| [`cudnn_convolution`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_convolution.html#torch.cudnn_convolution "torch.cudnn_convolution") |     |\
| [`cudnn_convolution_add_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_convolution_add_relu.html#torch.cudnn_convolution_add_relu "torch.cudnn_convolution_add_relu") |     |\
| [`cudnn_convolution_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_convolution_relu.html#torch.cudnn_convolution_relu "torch.cudnn_convolution_relu") |     |\
| [`cudnn_convolution_transpose`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_convolution_transpose.html#torch.cudnn_convolution_transpose "torch.cudnn_convolution_transpose") |     |\
| [`cudnn_grid_sampler`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_grid_sampler.html#torch.cudnn_grid_sampler "torch.cudnn_grid_sampler") |     |\
| [`cudnn_is_acceptable`](https://docs.pytorch.org/docs/2.15/generated/torch.cudnn_is_acceptable.html#torch.cudnn_is_acceptable "torch.cudnn_is_acceptable") |     |\
| [`cummax`](https://docs.pytorch.org/docs/2.15/generated/torch.cummax.html#torch.cummax "torch.cummax") | Returns a namedtuple `(values, indices)` where `values` is the cumulative maximum of elements of `input` in the dimension `dim`. |\
| [`cummin`](https://docs.pytorch.org/docs/2.15/generated/torch.cummin.html#torch.cummin "torch.cummin") | Returns a namedtuple `(values, indices)` where `values` is the cumulative minimum of elements of `input` in the dimension `dim`. |\
| [`cumprod`](https://docs.pytorch.org/docs/2.15/generated/torch.cumprod.html#torch.cumprod "torch.cumprod") | Returns the cumulative product of elements of `input` in the dimension `dim`. |\
| [`cumsum`](https://docs.pytorch.org/docs/2.15/generated/torch.cumsum.html#torch.cumsum "torch.cumsum") | Returns the cumulative sum of elements of `input` in the dimension `dim`. |\
| [`detach_`](https://docs.pytorch.org/docs/2.15/generated/torch.detach_.html#torch.detach_ "torch.detach_") | In-place version of [`torch.detach()`](https://docs.pytorch.org/docs/2.15/generated/torch.detach.html#torch.detach "torch.detach") |\
| [`diag`](https://docs.pytorch.org/docs/2.15/generated/torch.diag.html#torch.diag "torch.diag") | *   If `input` is a vector (1-D tensor), then returns a 2-D square tensor |\
| [`diag_embed`](https://docs.pytorch.org/docs/2.15/generated/torch.diag_embed.html#torch.diag_embed "torch.diag_embed") | Creates a tensor whose diagonals of certain 2D planes (specified by `dim1` and `dim2`) are filled by `input`. |\
| [`diagflat`](https://docs.pytorch.org/docs/2.15/generated/torch.diagflat.html#torch.diagflat "torch.diagflat") | *   If `input` is a vector (1-D tensor), then returns a 2-D square tensor |\
| [`diagonal`](https://docs.pytorch.org/docs/2.15/generated/torch.diagonal.html#torch.diagonal "torch.diagonal") | Returns a partial view of `input` with the its diagonal elements with respect to `dim1` and `dim2` appended as a dimension at the end of the shape. |\
| [`diff`](https://docs.pytorch.org/docs/2.15/generated/torch.diff.html#torch.diff "torch.diff") | Computes the n-th forward difference along the given dimension. |\
| [`dropout_`](https://docs.pytorch.org/docs/2.15/generated/torch.dropout_.html#torch.dropout_ "torch.dropout_") |     |\
| [`einsum`](https://docs.pytorch.org/docs/2.15/generated/torch.einsum.html#torch.einsum "torch.einsum") | Sums the product of the elements of the input `operands` along dimensions specified using a notation based on the Einstein summation convention. |\
| [`embedding`](https://docs.pytorch.org/docs/2.15/generated/torch.embedding.html#torch.embedding "torch.embedding") |     |\
| [`embedding_renorm_`](https://docs.pytorch.org/docs/2.15/generated/torch.embedding_renorm_.html#torch.embedding_renorm_ "torch.embedding_renorm_") |     |\
| [`fbgemm_linear_fp16_weight`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_linear_fp16_weight.html#torch.fbgemm_linear_fp16_weight "torch.fbgemm_linear_fp16_weight") |     |\
| [`fbgemm_linear_fp16_weight_fp32_activation`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_linear_fp16_weight_fp32_activation.html#torch.fbgemm_linear_fp16_weight_fp32_activation "torch.fbgemm_linear_fp16_weight_fp32_activation") |     |\
| [`fbgemm_linear_int8_weight`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_linear_int8_weight.html#torch.fbgemm_linear_int8_weight "torch.fbgemm_linear_int8_weight") |     |\
| [`fbgemm_linear_int8_weight_fp32_activation`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_linear_int8_weight_fp32_activation.html#torch.fbgemm_linear_int8_weight_fp32_activation "torch.fbgemm_linear_int8_weight_fp32_activation") |     |\
| [`fbgemm_linear_quantize_weight`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_linear_quantize_weight.html#torch.fbgemm_linear_quantize_weight "torch.fbgemm_linear_quantize_weight") |     |\
| [`fbgemm_pack_gemm_matrix_fp16`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_pack_gemm_matrix_fp16.html#torch.fbgemm_pack_gemm_matrix_fp16 "torch.fbgemm_pack_gemm_matrix_fp16") |     |\
| [`fbgemm_pack_quantized_matrix`](https://docs.pytorch.org/docs/2.15/generated/torch.fbgemm_pack_quantized_matrix.html#torch.fbgemm_pack_quantized_matrix "torch.fbgemm_pack_quantized_matrix") |     |\
| [`feature_alpha_dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_alpha_dropout.html#torch.feature_alpha_dropout "torch.feature_alpha_dropout") |     |\
| [`feature_alpha_dropout_`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_alpha_dropout_.html#torch.feature_alpha_dropout_ "torch.feature_alpha_dropout_") | In-place version of [`torch.feature_alpha_dropout()`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_alpha_dropout.html#torch.feature_alpha_dropout "torch.feature_alpha_dropout") |\
| [`feature_dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_dropout.html#torch.feature_dropout "torch.feature_dropout") |     |\
| [`feature_dropout_`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_dropout_.html#torch.feature_dropout_ "torch.feature_dropout_") | In-place version of [`torch.feature_dropout()`](https://docs.pytorch.org/docs/2.15/generated/torch.feature_dropout.html#torch.feature_dropout "torch.feature_dropout") |\
| [`flatten`](https://docs.pytorch.org/docs/2.15/generated/torch.flatten.html#torch.flatten "torch.flatten") | Flattens `input` by reshaping it into a one-dimensional tensor. |\
| [`flip`](https://docs.pytorch.org/docs/2.15/generated/torch.flip.html#torch.flip "torch.flip") | Reverse the order of an n-D tensor along given axis in dims. |\
| [`fliplr`](https://docs.pytorch.org/docs/2.15/generated/torch.fliplr.html#torch.fliplr "torch.fliplr") | Flip tensor in the left/right direction, returning a new tensor. |\
| [`flipud`](https://docs.pytorch.org/docs/2.15/generated/torch.flipud.html#torch.flipud "torch.flipud") | Flip tensor in the up/down direction, returning a new tensor. |\
| [`fused_moving_avg_obs_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.fused_moving_avg_obs_fake_quant.html#torch.fused_moving_avg_obs_fake_quant "torch.fused_moving_avg_obs_fake_quant") |     |\
| [`gcd`](https://docs.pytorch.org/docs/2.15/generated/torch.gcd.html#torch.gcd "torch.gcd") | Computes the element-wise greatest common divisor (GCD) of `input` and `other`. |\
| [`gcd_`](https://docs.pytorch.org/docs/2.15/generated/torch.gcd_.html#torch.gcd_ "torch.gcd_") | In-place version of [`torch.gcd()`](https://docs.pytorch.org/docs/2.15/generated/torch.gcd.html#torch.gcd "torch.gcd") |\
| [`grid_sampler_2d`](https://docs.pytorch.org/docs/2.15/generated/torch.grid_sampler_2d.html#torch.grid_sampler_2d "torch.grid_sampler_2d") |     |\
| [`grid_sampler_3d`](https://docs.pytorch.org/docs/2.15/generated/torch.grid_sampler_3d.html#torch.grid_sampler_3d "torch.grid_sampler_3d") |     |\
| [`group_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.group_norm.html#torch.group_norm "torch.group_norm") |     |\
| [`gru`](https://docs.pytorch.org/docs/2.15/generated/torch.gru.html#torch.gru "torch.gru") |     |\
| [`gru_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.gru_cell.html#torch.gru_cell "torch.gru_cell") |     |\
| [`hardshrink`](https://docs.pytorch.org/docs/2.15/generated/torch.hardshrink.html#torch.hardshrink "torch.hardshrink") | Applies the hard shrinkage function element-wise |\
| [`hinge_embedding_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.hinge_embedding_loss.html#torch.hinge_embedding_loss "torch.hinge_embedding_loss") |     |\
| [`histc`](https://docs.pytorch.org/docs/2.15/generated/torch.histc.html#torch.histc "torch.histc") | Computes the histogram of a tensor. |\
| [`histogram`](https://docs.pytorch.org/docs/2.15/generated/torch.histogram.html#torch.histogram "torch.histogram") | Computes a histogram of the values in a tensor. |\
| [`histogramdd`](https://docs.pytorch.org/docs/2.15/generated/torch.histogramdd.html#torch.histogramdd "torch.histogramdd") | Computes a multi-dimensional histogram of the values in a tensor. |\
| [`instance_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.instance_norm.html#torch.instance_norm "torch.instance_norm") |     |\
| [`int_repr`](https://docs.pytorch.org/docs/2.15/generated/torch.int_repr.html#torch.int_repr "torch.int_repr") |     |\
| [`kl_div`](https://docs.pytorch.org/docs/2.15/generated/torch.kl_div.html#torch.kl_div "torch.kl_div") |     |\
| [`kron`](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html#torch.kron "torch.kron") | Computes the Kronecker product, denoted by ⊗\\otimes⊗, of `input` and `other`. |\
| [`lcm`](https://docs.pytorch.org/docs/2.15/generated/torch.lcm.html#torch.lcm "torch.lcm") | Computes the element-wise least common multiple (LCM) of `input` and `other`. |\
| [`lcm_`](https://docs.pytorch.org/docs/2.15/generated/torch.lcm_.html#torch.lcm_ "torch.lcm_") | In-place version of [`torch.lcm()`](https://docs.pytorch.org/docs/2.15/generated/torch.lcm.html#torch.lcm "torch.lcm") |\
| [`logcumsumexp`](https://docs.pytorch.org/docs/2.15/generated/torch.logcumsumexp.html#torch.logcumsumexp "torch.logcumsumexp") | Returns the logarithm of the cumulative summation of the exponentiation of elements of `input` in the dimension `dim`. |\
| [`lstm`](https://docs.pytorch.org/docs/2.15/generated/torch.lstm.html#torch.lstm "torch.lstm") |     |\
| [`lstm_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.lstm_cell.html#torch.lstm_cell "torch.lstm_cell") |     |\
| [`margin_ranking_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.margin_ranking_loss.html#torch.margin_ranking_loss "torch.margin_ranking_loss") |     |\
| [`max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.max_pool1d.html#torch.max_pool1d "torch.max_pool1d") |     |\
| [`max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.max_pool3d.html#torch.max_pool3d "torch.max_pool3d") |     |\
| [`meshgrid`](https://docs.pytorch.org/docs/2.15/generated/torch.meshgrid.html#torch.meshgrid "torch.meshgrid") | Creates grids of coordinates specified by the 1D inputs in attr:tensors. |\
| [`miopen_batch_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_batch_norm.html#torch.miopen_batch_norm "torch.miopen_batch_norm") |     |\
| [`miopen_convolution`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_convolution.html#torch.miopen_convolution "torch.miopen_convolution") |     |\
| [`miopen_convolution_add_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_convolution_add_relu.html#torch.miopen_convolution_add_relu "torch.miopen_convolution_add_relu") |     |\
| [`miopen_convolution_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_convolution_relu.html#torch.miopen_convolution_relu "torch.miopen_convolution_relu") |     |\
| [`miopen_convolution_transpose`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_convolution_transpose.html#torch.miopen_convolution_transpose "torch.miopen_convolution_transpose") |     |\
| [`miopen_ctc_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_ctc_loss.html#torch.miopen_ctc_loss "torch.miopen_ctc_loss") |     |\
| [`miopen_depthwise_convolution`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_depthwise_convolution.html#torch.miopen_depthwise_convolution "torch.miopen_depthwise_convolution") |     |\
| [`miopen_rnn`](https://docs.pytorch.org/docs/2.15/generated/torch.miopen_rnn.html#torch.miopen_rnn "torch.miopen_rnn") |     |\
| [`mkldnn_adaptive_avg_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_adaptive_avg_pool2d.html#torch.mkldnn_adaptive_avg_pool2d "torch.mkldnn_adaptive_avg_pool2d") |     |\
| [`mkldnn_convolution`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_convolution.html#torch.mkldnn_convolution "torch.mkldnn_convolution") |     |\
| [`mkldnn_linear_backward_weights`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_linear_backward_weights.html#torch.mkldnn_linear_backward_weights "torch.mkldnn_linear_backward_weights") |     |\
| [`mkldnn_max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_max_pool2d.html#torch.mkldnn_max_pool2d "torch.mkldnn_max_pool2d") |     |\
| [`mkldnn_max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_max_pool3d.html#torch.mkldnn_max_pool3d "torch.mkldnn_max_pool3d") |     |\
| [`mkldnn_rnn_layer`](https://docs.pytorch.org/docs/2.15/generated/torch.mkldnn_rnn_layer.html#torch.mkldnn_rnn_layer "torch.mkldnn_rnn_layer") |     |\
| [`native_batch_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.native_batch_norm.html#torch.native_batch_norm "torch.native_batch_norm") |     |\
| [`native_channel_shuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.native_channel_shuffle.html#torch.native_channel_shuffle "torch.native_channel_shuffle") | Native kernel level implementation of the channel\_shuffle. |\
| [`native_group_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.native_group_norm.html#torch.native_group_norm "torch.native_group_norm") |     |\
| [`native_layer_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.native_layer_norm.html#torch.native_layer_norm "torch.native_layer_norm") |     |\
| [`native_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.native_norm.html#torch.native_norm "torch.native_norm") |     |\
| [`pairwise_distance`](https://docs.pytorch.org/docs/2.15/generated/torch.pairwise_distance.html#torch.pairwise_distance "torch.pairwise_distance") | See [`torch.nn.PairwiseDistance`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.PairwiseDistance.html#torch.nn.PairwiseDistance "torch.nn.PairwiseDistance")<br> for details |\
| [`pdist`](https://docs.pytorch.org/docs/2.15/generated/torch.pdist.html#torch.pdist "torch.pdist") | Computes the p-norm distance between every pair of row vectors in the input. |\
| [`pixel_unshuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.pixel_unshuffle.html#torch.pixel_unshuffle "torch.pixel_unshuffle") | Reverses the [`PixelShuffle`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.PixelShuffle.html#torch.nn.PixelShuffle "torch.nn.PixelShuffle")<br> operation by rearranging elements in a tensor of shape (∗,C,H×r,W×r)(\*, C, H \\times r, W \\times r)(∗,C,H×r,W×r) to a tensor of shape (∗,C×r2,H,W)(\*, C \\times r^2, H, W)(∗,C×r2,H,W), where r is the `downscale_factor`. |\
| [`poisson_nll_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.poisson_nll_loss.html#torch.poisson_nll_loss "torch.poisson_nll_loss") |     |\
| [`prelu`](https://docs.pytorch.org/docs/2.15/generated/torch.prelu.html#torch.prelu "torch.prelu") | Applies element-wise the function PReLU(x)\=max⁡(0,x)+weight∗min⁡(0,x)\\text{PReLU}(x) = \\max(0,x) + \\text{weight} \* \\min(0,x)PReLU(x)\=max(0,x)+weight∗min(0,x) where weight is a learnable parameter. |\
| [`q_per_channel_axis`](https://docs.pytorch.org/docs/2.15/generated/torch.q_per_channel_axis.html#torch.q_per_channel_axis "torch.q_per_channel_axis") |     |\
| [`q_per_channel_scales`](https://docs.pytorch.org/docs/2.15/generated/torch.q_per_channel_scales.html#torch.q_per_channel_scales "torch.q_per_channel_scales") |     |\
| [`q_per_channel_zero_points`](https://docs.pytorch.org/docs/2.15/generated/torch.q_per_channel_zero_points.html#torch.q_per_channel_zero_points "torch.q_per_channel_zero_points") |     |\
| [`q_scale`](https://docs.pytorch.org/docs/2.15/generated/torch.q_scale.html#torch.q_scale "torch.q_scale") |     |\
| [`q_zero_point`](https://docs.pytorch.org/docs/2.15/generated/torch.q_zero_point.html#torch.q_zero_point "torch.q_zero_point") |     |\
| [`quantized_gru_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_gru_cell.html#torch.quantized_gru_cell "torch.quantized_gru_cell") |     |\
| [`quantized_lstm_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_lstm_cell.html#torch.quantized_lstm_cell "torch.quantized_lstm_cell") |     |\
| [`quantized_max_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_max_pool3d.html#torch.quantized_max_pool3d "torch.quantized_max_pool3d") |     |\
| [`quantized_rnn_relu_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_rnn_relu_cell.html#torch.quantized_rnn_relu_cell "torch.quantized_rnn_relu_cell") |     |\
| [`quantized_rnn_tanh_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.quantized_rnn_tanh_cell.html#torch.quantized_rnn_tanh_cell "torch.quantized_rnn_tanh_cell") |     |\
| [`ravel`](https://docs.pytorch.org/docs/2.15/generated/torch.ravel.html#torch.ravel "torch.ravel") | Return a contiguous flattened tensor. |\
| [`relu_`](https://docs.pytorch.org/docs/2.15/generated/torch.relu_.html#torch.relu_ "torch.relu_") | In-place version of `relu()`. |\
| [`renorm`](https://docs.pytorch.org/docs/2.15/generated/torch.renorm.html#torch.renorm "torch.renorm") | Returns a tensor where each sub-tensor of `input` along dimension `dim` is normalized such that the p\-norm of the sub-tensor is lower than the value `maxnorm` |\
| [`repeat_interleave`](https://docs.pytorch.org/docs/2.15/generated/torch.repeat_interleave.html#torch.repeat_interleave "torch.repeat_interleave") | Repeat elements of a tensor. |\
| [`resize_as_`](https://docs.pytorch.org/docs/2.15/generated/torch.resize_as_.html#torch.resize_as_ "torch.resize_as_") |     |\
| [`resize_as_sparse_`](https://docs.pytorch.org/docs/2.15/generated/torch.resize_as_sparse_.html#torch.resize_as_sparse_ "torch.resize_as_sparse_") |     |\
| [`rms_norm`](https://docs.pytorch.org/docs/2.15/generated/torch.rms_norm.html#torch.rms_norm "torch.rms_norm") |     |\
| [`rnn_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.rnn_relu.html#torch.rnn_relu "torch.rnn_relu") |     |\
| [`rnn_relu_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.rnn_relu_cell.html#torch.rnn_relu_cell "torch.rnn_relu_cell") |     |\
| [`rnn_tanh`](https://docs.pytorch.org/docs/2.15/generated/torch.rnn_tanh.html#torch.rnn_tanh "torch.rnn_tanh") |     |\
| [`rnn_tanh_cell`](https://docs.pytorch.org/docs/2.15/generated/torch.rnn_tanh_cell.html#torch.rnn_tanh_cell "torch.rnn_tanh_cell") |     |\
| [`roll`](https://docs.pytorch.org/docs/2.15/generated/torch.roll.html#torch.roll "torch.roll") | Roll the tensor `input` along the given dimension(s). |\
| [`rot90`](https://docs.pytorch.org/docs/2.15/generated/torch.rot90.html#torch.rot90 "torch.rot90") | Rotate an n-D tensor by 90 degrees in the plane specified by dims axis. |\
| [`rrelu`](https://docs.pytorch.org/docs/2.15/generated/torch.rrelu.html#torch.rrelu "torch.rrelu") |     |\
| [`rrelu_`](https://docs.pytorch.org/docs/2.15/generated/torch.rrelu_.html#torch.rrelu_ "torch.rrelu_") | In-place version of [`rrelu()`](https://docs.pytorch.org/docs/2.15/generated/torch.rrelu.html#torch.rrelu "torch.rrelu")<br>. |\
| [`rsub`](https://docs.pytorch.org/docs/2.15/generated/torch.rsub.html#torch.rsub "torch.rsub") |     |\
| [`searchsorted`](https://docs.pytorch.org/docs/2.15/generated/torch.searchsorted.html#torch.searchsorted "torch.searchsorted") | Find the indices from the _innermost_ dimension of `sorted_sequence` such that, if the corresponding values in `values` were inserted before the indices, when sorted, the order of the corresponding _innermost_ dimension within `sorted_sequence` would be preserved. |\
| [`selu`](https://docs.pytorch.org/docs/2.15/generated/torch.selu.html#torch.selu "torch.selu") |     |\
| [`selu_`](https://docs.pytorch.org/docs/2.15/generated/torch.selu_.html#torch.selu_ "torch.selu_") | In-place version of [`selu()`](https://docs.pytorch.org/docs/2.15/generated/torch.selu.html#torch.selu "torch.selu")<br>. |\
| [`tensordot`](https://docs.pytorch.org/docs/2.15/generated/torch.tensordot.html#torch.tensordot "torch.tensordot") | Returns a contraction of a and b over multiple dimensions. |\
| [`threshold`](https://docs.pytorch.org/docs/2.15/generated/torch.threshold.html#torch.threshold "torch.threshold") |     |\
| [`threshold_`](https://docs.pytorch.org/docs/2.15/generated/torch.threshold_.html#torch.threshold_ "torch.threshold_") | In-place version of [`threshold()`](https://docs.pytorch.org/docs/2.15/generated/torch.threshold.html#torch.threshold "torch.threshold")<br>. |\
| [`trace`](https://docs.pytorch.org/docs/2.15/generated/torch.trace.html#torch.trace "torch.trace") | Returns the sum of the elements of the diagonal of the input 2-D matrix. |\
| [`tril`](https://docs.pytorch.org/docs/2.15/generated/torch.tril.html#torch.tril "torch.tril") | Returns the lower triangular part of the matrix (2-D tensor) or batch of matrices `input`, the other elements of the result tensor `out` are set to 0. |\
| [`tril_indices`](https://docs.pytorch.org/docs/2.15/generated/torch.tril_indices.html#torch.tril_indices "torch.tril_indices") | Returns the indices of the lower triangular part of a `row`\-by- `col` matrix in a 2-by-N Tensor, where the first row contains row coordinates of all indices and the second row contains column coordinates. |\
| [`triu`](https://docs.pytorch.org/docs/2.15/generated/torch.triu.html#torch.triu "torch.triu") | Returns the upper triangular part of a matrix (2-D tensor) or batch of matrices `input`, the other elements of the result tensor `out` are set to 0. |\
| [`triu_indices`](https://docs.pytorch.org/docs/2.15/generated/torch.triu_indices.html#torch.triu_indices "torch.triu_indices") | Returns the indices of the upper triangular part of a `row` by `col` matrix in a 2-by-N Tensor, where the first row contains row coordinates of all indices and the second row contains column coordinates. |\
| [`triplet_margin_loss`](https://docs.pytorch.org/docs/2.15/generated/torch.triplet_margin_loss.html#torch.triplet_margin_loss "torch.triplet_margin_loss") |     |\
| [`unflatten`](https://docs.pytorch.org/docs/2.15/generated/torch.unflatten.html#torch.unflatten "torch.unflatten") | Expands a dimension of the input tensor over multiple dimensions. |\
| [`vander`](https://docs.pytorch.org/docs/2.15/generated/torch.vander.html#torch.vander "torch.vander") | Generates a Vandermonde matrix. |\
| [`view_as_real`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real") | Returns a view of `input` as a real tensor. |\
| [`view_as_complex`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_complex.html#torch.view_as_complex "torch.view_as_complex") | Returns a view of `input` as a complex tensor. |\
| [`resolve_conj`](https://docs.pytorch.org/docs/2.15/generated/torch.resolve_conj.html#torch.resolve_conj "torch.resolve_conj") | Returns a new tensor with materialized conjugation if `input`'s conjugate bit is set to True, else returns `input`. |\
| [`resolve_neg`](https://docs.pytorch.org/docs/2.15/generated/torch.resolve_neg.html#torch.resolve_neg "torch.resolve_neg") | Returns a new tensor with materialized negation if `input`'s negative bit is set to True, else returns `input`. |\
\
### BLAS and LAPACK Operations[#](https://docs.pytorch.org/docs/2.15/torch.html#blas-and-lapack-operations "Link to this heading")\
\
|     |     |\
| --- | --- |\
| [`addbmm`](https://docs.pytorch.org/docs/2.15/generated/torch.addbmm.html#torch.addbmm "torch.addbmm") | Performs a batch matrix-matrix product of matrices stored in `batch1` and `batch2`, with a reduced add step (all matrix multiplications get accumulated along the first dimension). |\
| [`addmm`](https://docs.pytorch.org/docs/2.15/generated/torch.addmm.html#torch.addmm "torch.addmm") | Performs a matrix multiplication of the matrices `mat1` and `mat2`. |\
| [`addmv`](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html#torch.addmv "torch.addmv") | Performs a matrix-vector product of the matrix `mat` and the vector `vec`. |\
| [`addmv_`](https://docs.pytorch.org/docs/2.15/generated/torch.addmv_.html#torch.addmv_ "torch.addmv_") | In-place version of [`torch.addmv()`](https://docs.pytorch.org/docs/2.15/generated/torch.addmv.html#torch.addmv "torch.addmv") |\
| [`addr`](https://docs.pytorch.org/docs/2.15/generated/torch.addr.html#torch.addr "torch.addr") | Performs the outer-product of vectors `vec1` and `vec2` and adds it to the matrix `input`. |\
| [`baddbmm`](https://docs.pytorch.org/docs/2.15/generated/torch.baddbmm.html#torch.baddbmm "torch.baddbmm") | Performs a batch matrix-matrix product of matrices in `batch1` and `batch2`. |\
| [`bmm`](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html#torch.bmm "torch.bmm") | Performs a batch matrix-matrix product of matrices stored in `input` and `mat2`. |\
| [`chain_matmul`](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html#torch.chain_matmul "torch.chain_matmul") | Returns the matrix product of the NNN 2-D tensors. |\
| [`cholesky_inverse`](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_inverse.html#torch.cholesky_inverse "torch.cholesky_inverse") | Computes the inverse of a complex Hermitian or real symmetric positive-definite matrix given its Cholesky decomposition. |\
| [`cholesky_solve`](https://docs.pytorch.org/docs/2.15/generated/torch.cholesky_solve.html#torch.cholesky_solve "torch.cholesky_solve") | Computes the solution of a system of linear equations with complex Hermitian or real symmetric positive-definite lhs given its Cholesky decomposition. |\
| [`dot`](https://docs.pytorch.org/docs/2.15/generated/torch.dot.html#torch.dot "torch.dot") | Computes the dot product of two 1D tensors. |\
| [`dsmm`](https://docs.pytorch.org/docs/2.15/generated/torch.dsmm.html#torch.dsmm "torch.dsmm") |     |\
| [`geqrf`](https://docs.pytorch.org/docs/2.15/generated/torch.geqrf.html#torch.geqrf "torch.geqrf") | This is a low-level function for calling LAPACK's geqrf directly. |\
| [`ger`](https://docs.pytorch.org/docs/2.15/generated/torch.ger.html#torch.ger "torch.ger") | Alias of [`torch.outer()`](https://docs.pytorch.org/docs/2.15/generated/torch.outer.html#torch.outer "torch.outer")<br>. |\
| [`hsmm`](https://docs.pytorch.org/docs/2.15/generated/torch.hsmm.html#torch.hsmm "torch.hsmm") |     |\
| [`inner`](https://docs.pytorch.org/docs/2.15/generated/torch.inner.html#torch.inner "torch.inner") | Computes the dot product for 1D tensors. |\
| [`inverse`](https://docs.pytorch.org/docs/2.15/generated/torch.inverse.html#torch.inverse "torch.inverse") | Alias for [`torch.linalg.inv()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.inv.html#torch.linalg.inv "torch.linalg.inv") |\
| [`det`](https://docs.pytorch.org/docs/2.15/generated/torch.det.html#torch.det "torch.det") | Alias for [`torch.linalg.det()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.det.html#torch.linalg.det "torch.linalg.det") |\
| [`logdet`](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#torch.logdet "torch.logdet") | Calculates log determinant of a square matrix or batches of square matrices. |\
| [`slogdet`](https://docs.pytorch.org/docs/2.15/generated/torch.slogdet.html#torch.slogdet "torch.slogdet") | Alias for [`torch.linalg.slogdet()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.slogdet.html#torch.linalg.slogdet "torch.linalg.slogdet") |\
| [`lu`](https://docs.pytorch.org/docs/2.15/generated/torch.lu.html#torch.lu "torch.lu") | Computes the LU factorization of a matrix or batches of matrices `A`. |\
| [`lu_solve`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_solve.html#torch.lu_solve "torch.lu_solve") | Returns the LU solve of the linear system Ax\=bAx = bAx\=b using the partially pivoted LU factorization of A from [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")<br>. |\
| [`lu_unpack`](https://docs.pytorch.org/docs/2.15/generated/torch.lu_unpack.html#torch.lu_unpack "torch.lu_unpack") | Unpacks the LU decomposition returned by [`lu_factor()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor "torch.linalg.lu_factor")<br> into the P, L, U matrices. |\
| [`matmul`](https://docs.pytorch.org/docs/2.15/generated/torch.matmul.html#torch.matmul "torch.matmul") | Matrix product of two tensors. |\
| [`matrix_power`](https://docs.pytorch.org/docs/2.15/generated/torch.matrix_power.html#torch.matrix_power "torch.matrix_power") | Alias for [`torch.linalg.matrix_power()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_power.html#torch.linalg.matrix_power "torch.linalg.matrix_power") |\
| [`matrix_exp`](https://docs.pytorch.org/docs/2.15/generated/torch.matrix_exp.html#torch.matrix_exp "torch.matrix_exp") | Alias for [`torch.linalg.matrix_exp()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.matrix_exp.html#torch.linalg.matrix_exp "torch.linalg.matrix_exp")<br>. |\
| [`mm`](https://docs.pytorch.org/docs/2.15/generated/torch.mm.html#torch.mm "torch.mm") | Performs a matrix multiplication of the matrices `input` and `mat2`. |\
| [`mv`](https://docs.pytorch.org/docs/2.15/generated/torch.mv.html#torch.mv "torch.mv") | Performs a matrix-vector product of the matrix `input` and the vector `vec`. |\
| [`orgqr`](https://docs.pytorch.org/docs/2.15/generated/torch.orgqr.html#torch.orgqr "torch.orgqr") | Alias for [`torch.linalg.householder_product()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.householder_product.html#torch.linalg.householder_product "torch.linalg.householder_product")<br>. |\
| [`ormqr`](https://docs.pytorch.org/docs/2.15/generated/torch.ormqr.html#torch.ormqr "torch.ormqr") | Computes the matrix-matrix multiplication of a product of Householder matrices with a general matrix. |\
| [`outer`](https://docs.pytorch.org/docs/2.15/generated/torch.outer.html#torch.outer "torch.outer") | Outer product of `input` and `vec2`. |\
| [`pinverse`](https://docs.pytorch.org/docs/2.15/generated/torch.pinverse.html#torch.pinverse "torch.pinverse") | Alias for [`torch.linalg.pinv()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.pinv.html#torch.linalg.pinv "torch.linalg.pinv") |\
| [`saddmm`](https://docs.pytorch.org/docs/2.15/generated/torch.saddmm.html#torch.saddmm "torch.saddmm") |     |\
| [`spmm`](https://docs.pytorch.org/docs/2.15/generated/torch.spmm.html#torch.spmm "torch.spmm") |     |\
| [`svd`](https://docs.pytorch.org/docs/2.15/generated/torch.svd.html#torch.svd "torch.svd") | Computes the singular value decomposition of either a matrix or batch of matrices `input`. |\
| [`svd_lowrank`](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html#torch.svd_lowrank "torch.svd_lowrank") | Return the singular value decomposition `(U, S, V)` of a matrix, batches of matrices, or a sparse matrix AAA such that A≈Udiag⁡(S)VHA \\approx U \\operatorname{diag}(S) V^{\\text{H}}A≈Udiag(S)VH. |\
| [`pca_lowrank`](https://docs.pytorch.org/docs/2.15/generated/torch.pca_lowrank.html#torch.pca_lowrank "torch.pca_lowrank") | Performs linear Principal Component Analysis (PCA) on a low-rank matrix, batches of such matrices, or sparse matrix. |\
| [`lobpcg`](https://docs.pytorch.org/docs/2.15/generated/torch.lobpcg.html#torch.lobpcg "torch.lobpcg") | Find the k largest (or smallest) eigenvalues and the corresponding eigenvectors of a symmetric positive definite generalized eigenvalue problem using matrix-free LOBPCG methods. |\
| [`trapz`](https://docs.pytorch.org/docs/2.15/generated/torch.trapz.html#torch.trapz "torch.trapz") | Alias for [`torch.trapezoid()`](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html#torch.trapezoid "torch.trapezoid")<br>. |\
| [`trapezoid`](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html#torch.trapezoid "torch.trapezoid") | Computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)<br> along `dim`. |\
| [`cumulative_trapezoid`](https://docs.pytorch.org/docs/2.15/generated/torch.cumulative_trapezoid.html#torch.cumulative_trapezoid "torch.cumulative_trapezoid") | Cumulatively computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)<br> along `dim`. |\
| [`triangular_solve`](https://docs.pytorch.org/docs/2.15/generated/torch.triangular_solve.html#torch.triangular_solve "torch.triangular_solve") | Solves a system of equations with a square upper or lower triangular invertible matrix AAA and multiple right-hand sides bbb. |\
| [`vdot`](https://docs.pytorch.org/docs/2.15/generated/torch.vdot.html#torch.vdot "torch.vdot") | Computes the dot product of two 1D vectors along a dimension. |\
\
### Foreach Operations[#](https://docs.pytorch.org/docs/2.15/torch.html#foreach-operations "Link to this heading")\
\
You can find our foreach APIs at [`torch.foreach`](https://docs.pytorch.org/docs/2.15/foreach.html#module-torch.foreach "torch.foreach")\
. While the private `torch._foreach_*` APIs remain available to support backwards compatibility during migration, we recommend using the public APIs.\
\
Utilities[#](https://docs.pytorch.org/docs/2.15/torch.html#utilities "Link to this heading")\
\
---------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`autocast_decrement_nesting`](https://docs.pytorch.org/docs/2.15/generated/torch.autocast_decrement_nesting.html#torch.autocast_decrement_nesting "torch.autocast_decrement_nesting") |     |\
| [`autocast_increment_nesting`](https://docs.pytorch.org/docs/2.15/generated/torch.autocast_increment_nesting.html#torch.autocast_increment_nesting "torch.autocast_increment_nesting") |     |\
| [`clear_autocast_cache`](https://docs.pytorch.org/docs/2.15/generated/torch.clear_autocast_cache.html#torch.clear_autocast_cache "torch.clear_autocast_cache") |     |\
| [`compiled_with_cxx11_abi`](https://docs.pytorch.org/docs/2.15/generated/torch.compiled_with_cxx11_abi.html#torch.compiled_with_cxx11_abi "torch.compiled_with_cxx11_abi") | Returns whether PyTorch was built with \_GLIBCXX\_USE\_CXX11\_ABI=1 |\
| [`get_autocast_cpu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_autocast_cpu_dtype.html#torch.get_autocast_cpu_dtype "torch.get_autocast_cpu_dtype") |     |\
| [`get_autocast_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_autocast_dtype.html#torch.get_autocast_dtype "torch.get_autocast_dtype") |     |\
| [`get_autocast_gpu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_autocast_gpu_dtype.html#torch.get_autocast_gpu_dtype "torch.get_autocast_gpu_dtype") |     |\
| [`get_autocast_ipu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_autocast_ipu_dtype.html#torch.get_autocast_ipu_dtype "torch.get_autocast_ipu_dtype") |     |\
| [`get_autocast_xla_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.get_autocast_xla_dtype.html#torch.get_autocast_xla_dtype "torch.get_autocast_xla_dtype") |     |\
| [`get_device`](https://docs.pytorch.org/docs/2.15/generated/torch.get_device.html#torch.get_device "torch.get_device") |     |\
| [`get_device_module`](https://docs.pytorch.org/docs/2.15/generated/torch.get_device_module.html#torch.get_device_module "torch.get_device_module") | Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...). |\
| [`import_ir_module`](https://docs.pytorch.org/docs/2.15/generated/torch.import_ir_module.html#torch.import_ir_module "torch.import_ir_module") |     |\
| [`import_ir_module_from_buffer`](https://docs.pytorch.org/docs/2.15/generated/torch.import_ir_module_from_buffer.html#torch.import_ir_module_from_buffer "torch.import_ir_module_from_buffer") |     |\
| [`is_anomaly_check_nan_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_anomaly_check_nan_enabled.html#torch.is_anomaly_check_nan_enabled "torch.is_anomaly_check_nan_enabled") |     |\
| [`is_anomaly_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_anomaly_enabled.html#torch.is_anomaly_enabled "torch.is_anomaly_enabled") |     |\
| [`is_autocast_cache_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_autocast_cache_enabled.html#torch.is_autocast_cache_enabled "torch.is_autocast_cache_enabled") |     |\
| [`is_autocast_cpu_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_autocast_cpu_enabled.html#torch.is_autocast_cpu_enabled "torch.is_autocast_cpu_enabled") |     |\
| [`is_autocast_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_autocast_enabled.html#torch.is_autocast_enabled "torch.is_autocast_enabled") |     |\
| [`is_autocast_ipu_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_autocast_ipu_enabled.html#torch.is_autocast_ipu_enabled "torch.is_autocast_ipu_enabled") |     |\
| [`is_autocast_xla_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_autocast_xla_enabled.html#torch.is_autocast_xla_enabled "torch.is_autocast_xla_enabled") |     |\
| [`is_distributed`](https://docs.pytorch.org/docs/2.15/generated/torch.is_distributed.html#torch.is_distributed "torch.is_distributed") |     |\
| [`is_vulkan_available`](https://docs.pytorch.org/docs/2.15/generated/torch.is_vulkan_available.html#torch.is_vulkan_available "torch.is_vulkan_available") |     |\
| [`merge_type_from_type_comment`](https://docs.pytorch.org/docs/2.15/generated/torch.merge_type_from_type_comment.html#torch.merge_type_from_type_comment "torch.merge_type_from_type_comment") |     |\
| [`parse_ir`](https://docs.pytorch.org/docs/2.15/generated/torch.parse_ir.html#torch.parse_ir "torch.parse_ir") |     |\
| [`parse_schema`](https://docs.pytorch.org/docs/2.15/generated/torch.parse_schema.html#torch.parse_schema "torch.parse_schema") |     |\
| [`parse_type_comment`](https://docs.pytorch.org/docs/2.15/generated/torch.parse_type_comment.html#torch.parse_type_comment "torch.parse_type_comment") |     |\
| [`result_type`](https://docs.pytorch.org/docs/2.15/generated/torch.result_type.html#torch.result_type "torch.result_type") | Returns the [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")<br> that would result from performing an arithmetic operation on the provided input tensors. |\
| [`can_cast`](https://docs.pytorch.org/docs/2.15/generated/torch.can_cast.html#torch.can_cast "torch.can_cast") | Determines if a type conversion is allowed under PyTorch casting rules described in the type promotion [documentation](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#type-promotion-doc)<br>. |\
| [`promote_types`](https://docs.pytorch.org/docs/2.15/generated/torch.promote_types.html#torch.promote_types "torch.promote_types") | Returns the [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")<br> with the smallest size and scalar kind that is not smaller nor of lower kind than either type1 or type2. |\
| [`set_anomaly_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_anomaly_enabled.html#torch.set_anomaly_enabled "torch.set_anomaly_enabled") |     |\
| [`set_autocast_cache_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_cache_enabled.html#torch.set_autocast_cache_enabled "torch.set_autocast_cache_enabled") |     |\
| [`set_autocast_cpu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_cpu_dtype.html#torch.set_autocast_cpu_dtype "torch.set_autocast_cpu_dtype") |     |\
| [`set_autocast_cpu_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_cpu_enabled.html#torch.set_autocast_cpu_enabled "torch.set_autocast_cpu_enabled") |     |\
| [`set_autocast_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_dtype.html#torch.set_autocast_dtype "torch.set_autocast_dtype") |     |\
| [`set_autocast_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_enabled.html#torch.set_autocast_enabled "torch.set_autocast_enabled") |     |\
| [`set_autocast_gpu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_gpu_dtype.html#torch.set_autocast_gpu_dtype "torch.set_autocast_gpu_dtype") |     |\
| [`set_autocast_ipu_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_ipu_dtype.html#torch.set_autocast_ipu_dtype "torch.set_autocast_ipu_dtype") |     |\
| [`set_autocast_ipu_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_ipu_enabled.html#torch.set_autocast_ipu_enabled "torch.set_autocast_ipu_enabled") |     |\
| [`set_autocast_xla_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_xla_dtype.html#torch.set_autocast_xla_dtype "torch.set_autocast_xla_dtype") |     |\
| [`set_autocast_xla_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.set_autocast_xla_enabled.html#torch.set_autocast_xla_enabled "torch.set_autocast_xla_enabled") |     |\
| [`use_deterministic_algorithms`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms") | Sets whether PyTorch operations must use "deterministic" algorithms. |\
| [`are_deterministic_algorithms_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.are_deterministic_algorithms_enabled.html#torch.are_deterministic_algorithms_enabled "torch.are_deterministic_algorithms_enabled") | Returns True if the global deterministic flag is turned on. |\
| [`is_deterministic_algorithms_warn_only_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_deterministic_algorithms_warn_only_enabled.html#torch.is_deterministic_algorithms_warn_only_enabled "torch.is_deterministic_algorithms_warn_only_enabled") | Returns True if the global deterministic flag is set to warn only. |\
| [`set_deterministic_debug_mode`](https://docs.pytorch.org/docs/2.15/generated/torch.set_deterministic_debug_mode.html#torch.set_deterministic_debug_mode "torch.set_deterministic_debug_mode") | Sets the debug mode for deterministic operations. |\
| [`get_deterministic_debug_mode`](https://docs.pytorch.org/docs/2.15/generated/torch.get_deterministic_debug_mode.html#torch.get_deterministic_debug_mode "torch.get_deterministic_debug_mode") | Returns the current value of the debug mode for deterministic operations. |\
| [`set_float32_matmul_precision`](https://docs.pytorch.org/docs/2.15/generated/torch.set_float32_matmul_precision.html#torch.set_float32_matmul_precision "torch.set_float32_matmul_precision") | Sets the internal precision of float32 matrix multiplications. |\
| [`get_float32_matmul_precision`](https://docs.pytorch.org/docs/2.15/generated/torch.get_float32_matmul_precision.html#torch.get_float32_matmul_precision "torch.get_float32_matmul_precision") | Returns the current value of float32 matrix multiplication precision. |\
| [`set_warn_always`](https://docs.pytorch.org/docs/2.15/generated/torch.set_warn_always.html#torch.set_warn_always "torch.set_warn_always") | When this flag is False (default) then some PyTorch warnings may only appear once per process. |\
| [`is_warn_always_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.is_warn_always_enabled.html#torch.is_warn_always_enabled "torch.is_warn_always_enabled") | Returns True if the global warn\_always flag is turned on. |\
| [`vmap`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap") | vmap is the vectorizing map; `vmap(func)` returns a new function that maps `func` over some dimension of the inputs. |\
| [`_assert`](https://docs.pytorch.org/docs/2.15/generated/torch._assert.html#torch._assert "torch._assert") | A wrapper around Python's assert which is symbolically traceable. |\
| [`typename`](https://docs.pytorch.org/docs/2.15/generated/torch.typename.html#torch.typename "torch.typename") | String representation of the type of an object. |\
\
Type Information[#](https://docs.pytorch.org/docs/2.15/torch.html#type-information "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------\
\
_class_ torch.TensorType[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.TensorType "Link to this definition")\
\
Symbolic Numbers[#](https://docs.pytorch.org/docs/2.15/torch.html#symbolic-numbers "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------\
\
_class_ torch.SymInt(_node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L816)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "Link to this definition")\
\
Like an int (including magic methods), but redirects all operations on the wrapped node. This is used in particular to symbolically record operations in the symbolic shape workflow.\
\
as\_integer\_ratio()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L945)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt.as_integer_ratio "Link to this definition")\
\
Represent this int as an exact integer ratio\
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]\
\
_class_ torch.SymFloat(_node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L971)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "Link to this definition")\
\
Like a float (including magic methods), but redirects all operations on the wrapped node. This is used in particular to symbolically record operations in the symbolic shape workflow.\
\
as\_integer\_ratio()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1047)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat.as_integer_ratio "Link to this definition")\
\
Represent this float as an exact integer ratio\
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]\
\
conjugate()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1060)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat.conjugate "Link to this definition")\
\
Returns the complex conjugate of the float.\
\
Return type:\
\
[_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
\
hex()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1064)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat.hex "Link to this definition")\
\
Returns the hexadecimal representation of the float.\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
is\_integer()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1043)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat.is_integer "Link to this definition")\
\
Return True if the float is an integer.\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
_class_ torch.SymBool(_node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L1080)\
[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "Link to this definition")\
\
Like a bool (including magic methods), but redirects all operations on the wrapped node. This is used in particular to symbolically record operations in the symbolic shape workflow.\
\
Unlike regular bools, regular boolean operators will force extra guards instead of symbolically evaluate. Use the bitwise operators instead to handle this.\
\
|     |     |\
| --- | --- |\
| [`sym_constrain_range`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_constrain_range.html#torch.sym_constrain_range "torch.sym_constrain_range") |     |\
| [`sym_constrain_range_for_size`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_constrain_range_for_size.html#torch.sym_constrain_range_for_size "torch.sym_constrain_range_for_size") |     |\
| [`sym_float`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_float.html#torch.sym_float "torch.sym_float") | SymInt-aware utility for float casting. |\
| [`sym_fresh_size`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_fresh_size.html#torch.sym_fresh_size "torch.sym_fresh_size") |     |\
| [`sym_int`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_int.html#torch.sym_int "torch.sym_int") | SymInt-aware utility for int casting. |\
| [`sym_max`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_max.html#torch.sym_max "torch.sym_max") | SymInt-aware utility for max which avoids branching on a < b. |\
| [`sym_min`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_min.html#torch.sym_min "torch.sym_min") | SymInt-aware utility for min(). |\
| [`sym_not`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_not.html#torch.sym_not "torch.sym_not") | SymInt-aware utility for logical negation. |\
| [`sym_ite`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_ite.html#torch.sym_ite "torch.sym_ite") | SymInt-aware utility for ternary operator (`t if b else f`.) |\
| [`sym_sqrt`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_sqrt.html#torch.sym_sqrt "torch.sym_sqrt") |     |\
| [`sym_sum`](https://docs.pytorch.org/docs/2.15/generated/torch.sym_sum.html#torch.sym_sum "torch.sym_sum") | N-ary add which is faster to compute for long lists than iterated binary addition. |\
\
Export Path[#](https://docs.pytorch.org/docs/2.15/torch.html#export-path "Link to this heading")\
\
-------------------------------------------------------------------------------------------------\
\
Warning\
\
This feature is a prototype and may have compatibility breaking changes in the future.\
\
export generated/exportdb/index\
\
Control Flow[#](https://docs.pytorch.org/docs/2.15/torch.html#control-flow "Link to this heading")\
\
---------------------------------------------------------------------------------------------------\
\
Warning\
\
This feature is a prototype and may have compatibility breaking changes in the future.\
\
|     |     |\
| --- | --- |\
| [`cond`](https://docs.pytorch.org/docs/2.15/generated/torch.cond.html#torch.cond "torch.cond") | Conditionally applies true\_fn or false\_fn. |\
\
Optimizations[#](https://docs.pytorch.org/docs/2.15/torch.html#optimizations "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`compile`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile") | Optimizes given model/function using TorchDynamo and specified backend. |\
\
[torch.compile documentation](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler.html)\
\
Operator Tags[#](https://docs.pytorch.org/docs/2.15/torch.html#operator-tags "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------\
\
_class_ torch.Tag[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "Link to this definition")\
\
Members:\
\
core\
\
cudagraph\_unsafe\
\
data\_dependent\_output\
\
dynamic\_output\_shape\
\
flexible\_layout\
\
generated\
\
inplace\
\
inplace\_view\
\
maybe\_aliasing\_or\_mutating\
\
needs\_contiguous\_strides\
\
needs\_exact\_strides\
\
needs\_fixed\_stride\_order\
\
nondeterministic\_bitwise\
\
nondeterministic\_seeded\
\
out\
\
out\_variant\
\
pointwise\
\
pt2\_compliant\_tag\
\
reduction\
\
view\_copy\
\
_property_ name[#](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag.name "Link to this definition")\
\
|     |     |\
| --- | --- |\
| [`get_inline_skeleton`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.model_dump.get_inline_skeleton.html#torch.utils.model_dump.get_inline_skeleton "torch.utils.model_dump.get_inline_skeleton") | Get a fully-inlined skeleton of the frontend. |\
| [`get_model_info`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.model_dump.get_model_info.html#torch.utils.model_dump.get_model_info "torch.utils.model_dump.get_model_info") | Get JSON-friendly information about a model. |\
\
|     |     |\
| --- | --- |\
| [`StorageType`](https://docs.pytorch.org/docs/2.15/generated/torch.serialization.StorageType.html#torch.serialization.StorageType "torch.serialization.StorageType") |     |\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |