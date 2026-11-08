Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/tensor_attributes.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/tensor_attributes.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/tensor_attributes.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/tensor_attributes.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/tensor_attributes.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/tensor_attributes.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/tensor_attributes.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/tensor_attributes.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/tensor_attributes.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/tensor_attributes.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/tensor_attributes.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/tensor_attributes.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/tensor_attributes.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/tensor_attributes.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/tensor_attributes.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/tensor_attributes.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/tensor_attributes.html)
[v1.13](https://docs.pytorch.org/docs/1.13/tensor_attributes.html)
[v1.12](https://docs.pytorch.org/docs/1.12/tensor_attributes.html)
[v1.11](https://docs.pytorch.org/docs/1.11/tensor_attributes.html)
[v1.10](https://docs.pytorch.org/docs/1.10/tensor_attributes.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/tensor_attributes.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/tensor_attributes.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/tensor_attributes.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/tensor_attributes.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/tensor_attributes.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/tensor_attributes.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/tensor_attributes.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/tensor_attributes.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/tensor_attributes.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/tensor_attributes.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/tensor_attributes.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/tensor_attributes.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/tensor_attributes.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/tensor_attributes.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/tensor_attributes.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/tensor_attributes.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/tensor_attributes.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/tensor_attributes.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/tensor_attributes.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/tensor_attributes.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/tensor_attributes.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/tensor_attributes.html)

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

Tensor Attributes[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#tensor-attributes "Link to this heading")

=========================================================================================================================

Created On: May 08, 2026 | Last Updated On: Jun 15, 2026

Each `torch.Tensor` has a [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
, [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
, and [`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
.

torch.dtype[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch-dtype "Link to this heading")

-------------------------------------------------------------------------------------------------------------

_class_ torch.dtype[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "Link to this definition")

A [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 is an object that represents the data type of a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
. PyTorch has several different data types:

**Floating point dtypes**

| dtype | description |
| --- | --- |
| `torch.float32` or `torch.float` | 32-bit floating point, as defined in [https://en.wikipedia.org/wiki/IEEE\_754](https://en.wikipedia.org/wiki/IEEE_754) |
| `torch.float64` or `torch.double` | 64-bit floating point, as defined in [https://en.wikipedia.org/wiki/IEEE\_754](https://en.wikipedia.org/wiki/IEEE_754) |
| `torch.float16` or `torch.half` | 16-bit floating point, as defined in [https://en.wikipedia.org/wiki/IEEE\_754](https://en.wikipedia.org/wiki/IEEE_754)<br>, S-E-M 1-5-10 |
| `torch.bfloat16` | 16-bit floating point, sometimes referred to as Brain floating point, S-E-M 1-8-7 |
| `torch.complex32` or `torch.chalf` | 32-bit complex with two `float16` components |
| `torch.bcomplex32` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell) | 32-bit complex with two `bfloat16` components |
| `torch.complex64` or `torch.cfloat` | 64-bit complex with two `float32` components |
| `torch.complex128` or `torch.cdouble` | 128-bit complex with two `float64` components |
| `torch.float8_e4m3fn` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[1\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id20) | 8-bit floating point, S-E-M 1-4-3, from [https://arxiv.org/abs/2209.05433](https://arxiv.org/abs/2209.05433) |
| `torch.float8_e5m2` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell) | 8-bit floating point, S-E-M 1-5-2, from [https://arxiv.org/abs/2209.05433](https://arxiv.org/abs/2209.05433) |
| `torch.float8_e4m3fnuz` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[1\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id20) | 8-bit floating point, S-E-M 1-4-3, from [https://arxiv.org/pdf/2206.02915](https://arxiv.org/pdf/2206.02915) |
| `torch.float8_e5m2fnuz` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[1\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id20) | 8-bit floating point, S-E-M 1-5-2, from [https://arxiv.org/pdf/2206.02915](https://arxiv.org/pdf/2206.02915) |
| `torch.float8_e8m0fnu` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[1\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id20) | 8-bit floating point, S-E-M 0-8-0, from [https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf) |
| `torch.float4_e2m1fn_x2` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[1\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id20)<br> [\[3\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id22) | packed 4-bit floating point, S-E-M 1-2-1, from [https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf) |

**Integer dtypes**

| dtype | description |
| --- | --- |
| `torch.uint8` | 8-bit integer (unsigned) |
| `torch.int8` | 8-bit integer (signed) |
| `torch.uint16` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[2\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id21) | 16-bit integer (unsigned) |
| `torch.int16` or `torch.short` | 16-bit integer (signed) |
| `torch.uint32` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[2\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id21) | 32-bit integer (unsigned) |
| `torch.int32` or `torch.int` | 32-bit integer (signed) |
| `torch.uint64` [\[4\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#shell)<br> [\[2\]](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#id21) | 64-bit integer (unsigned) |
| `torch.int64` or `torch.long` | 64-bit integer (signed) |
| `torch.bool` | Boolean |

**Note**: legacy constructors such as `torch.*.FloatTensor`, `torch.*.DoubleTensor`, `torch.*.HalfTensor`, `torch.*.BFloat16Tensor`, `torch.*.ByteTensor`, `torch.*.CharTensor`, `torch.*.ShortTensor`, `torch.*.IntTensor`, `torch.*.LongTensor`, `torch.*.BoolTensor` only remain for backwards compatibility and should no longer be used.

To find out if a [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 is a floating point data type, the property [`is_floating_point`](https://docs.pytorch.org/docs/2.15/generated/torch.is_floating_point.html#torch.is_floating_point "torch.is_floating_point")
 can be used, which returns `True` if the data type is a floating point data type.

To find out if a [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 is a complex data type, the property [`is_complex`](https://docs.pytorch.org/docs/2.15/generated/torch.is_complex.html#torch.is_complex "torch.is_complex")
 can be used, which returns `True` if the data type is a complex data type.

Each [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 has an `abbr` property that returns a short abbreviation string for the dtype (e.g., `torch.float32.abbr` returns `"f32"`).

When the dtypes of inputs to an arithmetic operation (_add_, _sub_, _div_, _mul_) differ, we promote by finding the minimum dtype that satisfies the following rules:

*   If the type of a scalar operand is of a higher category than tensor operands (where complex > floating > integral > boolean), we promote to a type with sufficient size to hold all scalar operands of that category.
    
*   If a zero-dimension tensor operand has a higher category than dimensioned operands, we promote to a type with sufficient size and category to hold all zero-dim tensor operands of that category.
    
*   If there are no higher-category zero-dim operands, we promote to a type with sufficient size and category to hold all dimensioned operands.
    

A floating point scalar operand has dtype _torch.get\_default\_dtype()_ and an integral non-boolean scalar operand has dtype _torch.int64_. Unlike numpy, we do not inspect values when determining the minimum _dtypes_ of an operand. Complex types are not yet supported. Promotion for shell dtypes is not defined.

Promotion Examples:

\>>> float\_tensor \= torch.ones(1, dtype\=torch.float)
\>>> double\_tensor \= torch.ones(1, dtype\=torch.double)
\>>> complex\_float\_tensor \= torch.ones(1, dtype\=torch.complex64)
\>>> complex\_double\_tensor \= torch.ones(1, dtype\=torch.complex128)
\>>> int\_tensor \= torch.ones(1, dtype\=torch.int)
\>>> long\_tensor \= torch.ones(1, dtype\=torch.long)
\>>> uint\_tensor \= torch.ones(1, dtype\=torch.uint8)
\>>> bool\_tensor \= torch.ones(1, dtype\=torch.bool)
\# zero-dim tensors
\>>> long\_zerodim \= torch.tensor(1, dtype\=torch.long)
\>>> int\_zerodim \= torch.tensor(1, dtype\=torch.int)

\>>> torch.add(5, 5).dtype
torch.int64
\# 5 is an int64, but does not have higher category than int\_tensor so is not considered.
\>>> (int\_tensor + 5).dtype
torch.int32
\>>> (int\_tensor + long\_zerodim).dtype
torch.int32
\>>> (long\_tensor + int\_tensor).dtype
torch.int64
\>>> (bool\_tensor + long\_tensor).dtype
torch.int64
\>>> (bool\_tensor + uint\_tensor).dtype
torch.uint8
\>>> (float\_tensor + double\_tensor).dtype
torch.float64
\>>> (complex\_float\_tensor + complex\_double\_tensor).dtype
torch.complex128
\>>> (bool\_tensor + int\_tensor).dtype
torch.int32
\# Since long is a different kind than float, result dtype only needs to be large enough
\# to hold the float.
\>>> torch.add(long\_tensor, float\_tensor).dtype
torch.float32

Copy to clipboard

When the output tensor of an arithmetic operation is specified, we allow casting to its _dtype_ except that:

*   An integral output tensor cannot accept a floating point tensor.
    
*   A boolean output tensor cannot accept a non-boolean tensor.
    
*   A non-complex output tensor cannot accept a complex tensor
    

Casting Examples:

\# allowed:
\>>> float\_tensor \*= float\_tensor
\>>> float\_tensor \*= int\_tensor
\>>> float\_tensor \*= uint\_tensor
\>>> float\_tensor \*= bool\_tensor
\>>> float\_tensor \*= double\_tensor
\>>> int\_tensor \*= long\_tensor
\>>> int\_tensor \*= uint\_tensor
\>>> uint\_tensor \*= int\_tensor

\# disallowed (RuntimeError: result type can't be cast to the desired output type):
\>>> int\_tensor \*= float\_tensor
\>>> bool\_tensor \*= int\_tensor
\>>> bool\_tensor \*= uint\_tensor
\>>> float\_tensor \*= complex\_float\_tensor

Copy to clipboard

torch.device[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch-device "Link to this heading")

---------------------------------------------------------------------------------------------------------------

_class_ torch.device[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "Link to this definition")

A [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 is an object representing the device on which a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 is or will be allocated.

The [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 contains a device type (most commonly “cpu” or “cuda”, but also potentially [“mps”](https://docs.pytorch.org/docs/2.15/mps.html)
, [“xpu”](https://docs.pytorch.org/docs/2.15/xpu.html)
, [“xla”](https://github.com/pytorch/xla/)
 or [“meta”](https://docs.pytorch.org/docs/2.15/meta.html)
) and optional device ordinal for the device type. If the device ordinal is not present, this object will always represent the current device for the device type, even after [`torch.cuda.set_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.set_device.html#torch.cuda.set_device "torch.cuda.set_device")
 is called; e.g., a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 constructed with device `'cuda'` is equivalent to `'cuda:X'` where X is the result of [`torch.cuda.current_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.current_device.html#torch.cuda.current_device "torch.cuda.current_device")
.

A [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
’s device can be accessed via the [`Tensor.device`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.device.html#torch.Tensor.device "torch.Tensor.device")
 property.

A [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 can be constructed using:

*   A device string, which is a string representation of the device type and optionally the device ordinal.
    
*   A device type and a device ordinal.
    
*   A device ordinal, where the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
     type will be used.
    

Via a device string:

\>>> torch.device('cuda:0')
device(type='cuda', index=0)

\>>> torch.device('cpu')
device(type='cpu')

\>>> torch.device('mps')
device(type='mps')

\>>> torch.device('cuda')  \# implicit index is the "current device index"
device(type='cuda')

Copy to clipboard

Via a device type and a device ordinal:

\>>> torch.device('cuda', 0)
device(type='cuda', index=0)

\>>> torch.device('mps', 0)
device(type='mps', index=0)

\>>> torch.device('cpu', 0)
device(type='cpu', index=0)

Copy to clipboard

Via a device ordinal:

Note

This method will raise a RuntimeError if no accelerator is currently detected.

\>>> torch.device(0)  \# the current accelerator is cuda
device(type='cuda', index=0)

\>>> torch.device(1)  \# the current accelerator is xpu
device(type='xpu', index=1)

\>>> torch.device(0)  \# no current accelerator detected
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Cannot access accelerator device when none is available.

Copy to clipboard

The device object can also be used as a context manager to change the default device tensors are allocated on:

\>>> with torch.device('cuda:1'):
...     r \= torch.randn(2, 3)
\>>> r.device
device(type='cuda', index=1)

Copy to clipboard

This context manager has no effect if a factory function is passed an explicit, non-None device argument. To globally change the default device, see also [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
.

Warning

This function imposes a slight performance cost on every Python call to the torch API (not just factory functions). If this is causing problems for you, please comment on [pytorch/pytorch#92701](https://github.com/pytorch/pytorch/issues/92701)

Note

The [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 argument in functions can generally be substituted with a string. This allows for fast prototyping of code.

\>>> \# Example of a function that takes in a torch.device
\>>> cuda1 \= torch.device('cuda:1')
\>>> torch.randn((2,3), device\=cuda1)

Copy to clipboard

\>>> \# You can substitute the torch.device with a string
\>>> torch.randn((2,3), device\='cuda:1')

Copy to clipboard

Note

Methods which take a device will generally accept a (properly formatted) string or an integer device ordinal, i.e. the following are all equivalent:

\>>> torch.randn((2,3), device\=torch.device('cuda:1'))
\>>> torch.randn((2,3), device\='cuda:1')
\>>> torch.randn((2,3), device\=1)  \# equivalent to 'cuda:1' if the current accelerator is cuda

Copy to clipboard

Note

Tensors are never moved automatically between devices and require an explicit call from the user. Scalar Tensors (with tensor.dim()==0) are the only exception to this rule and they are automatically transferred from CPU to GPU when needed as this operation can be done “for free”. Example:

\>>> \# two scalars
\>>> torch.ones(()) + torch.ones(()).cuda()  \# OK, scalar auto-transferred from CPU to GPU
\>>> torch.ones(()).cuda() + torch.ones(())  \# OK, scalar auto-transferred from CPU to GPU

Copy to clipboard

\>>> \# one scalar (CPU), one vector (GPU)
\>>> torch.ones(()) + torch.ones(1).cuda()  \# OK, scalar auto-transferred from CPU to GPU
\>>> torch.ones(1).cuda() + torch.ones(())  \# OK, scalar auto-transferred from CPU to GPU

Copy to clipboard

\>>> \# one scalar (GPU), one vector (CPU)
\>>> torch.ones(()).cuda() + torch.ones(1)  \# Fail, scalar not auto-transferred from GPU to CPU and non-scalar not auto-transferred from CPU to GPU
\>>> torch.ones(1) + torch.ones(()).cuda()  \# Fail, scalar not auto-transferred from GPU to CPU and non-scalar not auto-transferred from CPU to GPU

Copy to clipboard

torch.layout[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch-layout "Link to this heading")

---------------------------------------------------------------------------------------------------------------

_class_ torch.layout[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "Link to this definition")

Warning

The `torch.layout` class is in beta and subject to change.

A [`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
 is an object that represents the memory layout of a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
. Currently, we support `torch.strided` (dense Tensors) and have beta support for `torch.sparse_coo` (sparse COO Tensors).

`torch.strided` represents dense Tensors and is the memory layout that is most commonly used. Each strided tensor has an associated `torch.Storage`, which holds its data. These tensors provide multi-dimensional, [strided](https://en.wikipedia.org/wiki/Stride_of_an_array)
 view of a storage. Strides are a list of integers: the k-th stride represents the jump in the memory necessary to go from one element to the next one in the k-th dimension of the Tensor. This concept makes it possible to perform many tensor operations efficiently.

Example:

\>>> x \= torch.tensor(\[\[1, 2, 3, 4, 5\], \[6, 7, 8, 9, 10\]\])
\>>> x.stride()
(5, 1)

\>>> x.t().stride()
(1, 5)

Copy to clipboard

For more information on `torch.sparse_coo` tensors, see [torch.sparse](https://docs.pytorch.org/docs/2.15/sparse.html#sparse-docs)
.

torch.memory\_format[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch-memory-format "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

_class_ torch.memory\_format[#](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "Link to this definition")

A [`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
 is an object representing the memory format on which a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 is or will be allocated.

Possible values are:

*   `torch.contiguous_format`: Tensor is or will be allocated in dense non-overlapping memory. Strides represented by values in decreasing order.
    
*   `torch.channels_last`: Tensor is or will be allocated in dense non-overlapping memory. Strides represented by values in `strides[0] > strides[2] > strides[3] > strides[1] == 1` aka NHWC order.
    
*   `torch.channels_last_3d`: Tensor is or will be allocated in dense non-overlapping memory. Strides represented by values in `strides[0] > strides[2] > strides[3] > strides[4] > strides[1] == 1` aka NDHWC order.
    
*   `torch.preserve_format`: Used in functions like _clone_ to preserve the memory format of the input tensor. If input tensor is allocated in dense non-overlapping memory, the output tensor strides will be copied from the input. Otherwise output strides will follow `torch.contiguous_format`
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/tensor_attributes.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/tensor_attributes.md.txt)

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