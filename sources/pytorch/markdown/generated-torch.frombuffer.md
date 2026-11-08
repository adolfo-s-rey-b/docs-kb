Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.frombuffer.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.frombuffer.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.frombuffer.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.frombuffer.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.frombuffer.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.frombuffer.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.frombuffer.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.frombuffer.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.frombuffer.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.frombuffer.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.frombuffer.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.frombuffer.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.frombuffer.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.frombuffer.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.frombuffer.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.frombuffer.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.frombuffer.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.frombuffer.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.frombuffer.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.frombuffer.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.frombuffer.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.frombuffer.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.frombuffer.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.frombuffer.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.frombuffer.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.frombuffer.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.frombuffer.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.frombuffer.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.frombuffer.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.frombuffer.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.frombuffer.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.frombuffer.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.frombuffer.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.frombuffer.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.frombuffer.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.frombuffer.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.frombuffer.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.frombuffer.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.frombuffer.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.frombuffer.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.frombuffer.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.frombuffer.html)

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

torch.frombuffer[#](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html#torch-frombuffer "Link to this heading")

================================================================================================================================

torch.frombuffer(_buffer_, _\*_, _dtype_, _count\=\-1_, _offset\=0_, _requires\_grad\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.frombuffer.html#torch.frombuffer "Link to this definition")

Creates a 1-dimensional [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 from an object that implements the Python buffer protocol.

Skips the first `offset` bytes in the buffer, and interprets the rest of the raw bytes as a 1-dimensional tensor of type [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 with `count` elements.

Note that either of the following must be true:

1\. `count` is a positive non-zero number, and the total number of bytes in the buffer is more than `offset` plus `count` times the size (in bytes) of [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
.

2\. `count` is negative, and the length (number of bytes) of the buffer subtracted by the `offset` is a multiple of the size (in bytes) of [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
.

The returned tensor and buffer share the same memory. Modifications to the tensor will be reflected in the buffer and vice versa. The returned tensor is not resizable.

Note

This function increments the reference count for the object that owns the shared memory. Therefore, such memory will not be deallocated before the returned tensor goes out of scope.

Warning

This function’s behavior is undefined when passed an object implementing the buffer protocol whose data is not on the CPU. Doing so is likely to cause a segmentation fault.

Warning

This function does not try to infer the [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 (hence, it is not optional). Passing a different [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 than its source may result in unexpected behavior.

Parameters:

**buffer** ([_object_](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
) – a Python object that exposes the buffer interface.

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the desired data type of returned tensor.
    
*   **count** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the number of desired elements to be read. If negative, all the elements (until the end of the buffer) will be read. Default: -1.
    
*   **offset** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the number of bytes to skip at the start of the buffer. Default: 0.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    

Example:

\>>> import array
\>>> a \= array.array('i', \[1, 2, 3\])
\>>> t \= torch.frombuffer(a, dtype\=torch.int32)
\>>> t
tensor(\[ 1,  2,  3\])
\>>> t\[0\] \= \-1
\>>> a
array(\[-1,  2,  3\])

\>>> \# Interprets the signed char bytes as 32-bit integers.
\>>> \# Each 4 signed char elements will be interpreted as
\>>> \# 1 signed 32-bit integer.
\>>> import array
\>>> a \= array.array('b', \[\-1, 0, 0, 0\])
\>>> torch.frombuffer(a, dtype\=torch.int32)
tensor(\[255\], dtype=torch.int32)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.frombuffer.rst.txt)

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