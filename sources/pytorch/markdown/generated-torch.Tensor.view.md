Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.view.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.view.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.view.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.view.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.view.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.view.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.view.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.view.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.view.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.view.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.view.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.view.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.view.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.view.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.view.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.view.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.view.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.view.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.view.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.view.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.view.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.view.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.view.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.view.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.view.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.view.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.view.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.view.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.view.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.view.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.view.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.view.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.view.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.view.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.view.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.view.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.view.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.view.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.view.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.view.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.view.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.view.html)

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

torch.Tensor.view[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch-tensor-view "Link to this heading")

===================================================================================================================================

Tensor.view(_\*shape_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "Link to this definition")

Returns a new tensor with the same data as the `self` tensor but of a different [`shape`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.shape.html#torch.Tensor.shape "torch.Tensor.shape")
.

The returned tensor shares the same data and must have the same number of elements, but may have a different size. For a tensor to be viewed, the new view size must be compatible with its original size and stride, i.e., each new view dimension must either be a subspace of an original dimension, or only span across original dimensions d,d+1,…,d+kd, d+1, \\dots, d+kd,d+1,…,d+k that satisfy the following contiguity-like condition that ∀i\=d,…,d+k−1\\forall i = d, \\dots, d+k-1∀i\=d,…,d+k−1,

stride\[i\]\=stride\[i+1\]×size\[i+1\]\\text{stride}\[i\] = \\text{stride}\[i+1\] \\times \\text{size}\[i+1\]stride\[i\]\=stride\[i+1\]×size\[i+1\]

Otherwise, it will not be possible to view `self` tensor as [`shape`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.shape.html#torch.Tensor.shape "torch.Tensor.shape")
 without copying it (e.g., via [`contiguous()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous "torch.Tensor.contiguous")
). When it is unclear whether a [`view()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view")
 can be performed, it is advisable to use [`reshape()`](https://docs.pytorch.org/docs/2.15/generated/torch.reshape.html#torch.reshape "torch.reshape")
, which returns a view if the shapes are compatible, and copies (equivalent to calling [`contiguous()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous "torch.Tensor.contiguous")
) otherwise.

Parameters:

**shape** ([_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
 _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_..._) – the desired size

Example:

\>>> x \= torch.randn(4, 4)
\>>> x.size()
torch.Size(\[4, 4\])
\>>> y \= x.view(16)
\>>> y.size()
torch.Size(\[16\])
\>>> z \= x.view(\-1, 8)  \# the size -1 is inferred from other dimensions
\>>> z.size()
torch.Size(\[2, 8\])

\>>> a \= torch.randn(1, 2, 3, 4)
\>>> a.size()
torch.Size(\[1, 2, 3, 4\])
\>>> b \= a.transpose(1, 2)  \# Swaps 2nd and 3rd dimension
\>>> b.size()
torch.Size(\[1, 3, 2, 4\])
\>>> c \= a.view(1, 3, 2, 4)  \# Does not change tensor layout in memory
\>>> c.size()
torch.Size(\[1, 3, 2, 4\])
\>>> torch.equal(b, c)
False

Copy to clipboard

view(_dtype_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Returns a new tensor with the same data as the `self` tensor but of a different [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
.

If the element size of [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 is different than that of `self.dtype`, then the size of the last dimension of the output will be scaled proportionally. For instance, if [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 element size is twice that of `self.dtype`, then each pair of elements in the last dimension of `self` will be combined, and the size of the last dimension of the output will be half that of `self`. If [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 element size is half that of `self.dtype`, then each element in the last dimension of `self` will be split in two, and the size of the last dimension of the output will be double that of `self`. For this to be possible, the following conditions must be true:

> *   `self.dim()` must be greater than 0.
>     
> *   `self.stride(-1)` must be 1.
>     

Additionally, if the element size of [`dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 is greater than that of `self.dtype`, the following conditions must be true as well:

> *   `self.size(-1)` must be divisible by the ratio between the element sizes of the dtypes.
>     
> *   `self.storage_offset()` must be divisible by the ratio between the element sizes of the dtypes.
>     
> *   The strides of all dimensions, except the last dimension, must be divisible by the ratio between the element sizes of the dtypes.
>     

If any of the above conditions are not met, an error is thrown.

Warning

This overload is not supported by TorchScript, and using it in a Torchscript program will cause undefined behavior.

Warning

Viewing a tensor as `torch.bool` reinterprets its bytes without converting them. A `torch.bool` tensor must only contain the byte values `0` (`False`) and `1` (`True`). If any byte of the viewed data has another value, the behavior of operations on the returned tensor is undefined: depending on the operation, device and memory layout, such bytes may be preserved as-is or normalized to `1`, and eager mode and [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
 may give different results. To convert values to booleans, use [`bool()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.bool.html#torch.Tensor.bool "torch.Tensor.bool")
 (or `self != 0`) instead.

Parameters:

**dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
) – the desired dtype

Example:

\>>> x \= torch.randn(4, 4)
\>>> x
tensor(\[\[ 0.9482, -0.0310,  1.4999, -0.5316\],\
        \[-0.1520,  0.7472,  0.5617, -0.8649\],\
        \[-2.4724, -0.0334, -0.2976, -0.8499\],\
        \[-0.2109,  1.9913, -0.9607, -0.6123\]\])
\>>> x.dtype
torch.float32

\>>> y \= x.view(torch.int32)
\>>> y
tensor(\[\[ 1064483442, -1124191867,  1069546515, -1089989247\],\
        \[-1105482831,  1061112040,  1057999968, -1084397505\],\
        \[-1071760287, -1123489973, -1097310419, -1084649136\],\
        \[-1101533110,  1073668768, -1082790149, -1088634448\]\],
    dtype=torch.int32)
\>>> y\[0, 0\] \= 1000000000
\>>> x
tensor(\[\[ 0.0047, -0.0310,  1.4999, -0.5316\],\
        \[-0.1520,  0.7472,  0.5617, -0.8649\],\
        \[-2.4724, -0.0334, -0.2976, -0.8499\],\
        \[-0.2109,  1.9913, -0.9607, -0.6123\]\])

\>>> x.view(torch.cfloat)
tensor(\[\[ 0.0047-0.0310j,  1.4999-0.5316j\],\
        \[-0.1520+0.7472j,  0.5617-0.8649j\],\
        \[-2.4724-0.0334j, -0.2976-0.8499j\],\
        \[-0.2109+1.9913j, -0.9607-0.6123j\]\])
\>>> x.view(torch.cfloat).size()
torch.Size(\[4, 2\])

\>>> x.view(torch.uint8)
tensor(\[\[  0, 202, 154,  59, 182, 243, 253, 188, 185, 252, 191,  63, 240,  22,\
           8, 191\],\
        \[227, 165,  27, 190, 128,  72,  63,  63, 146, 203,  15,  63,  22, 106,\
          93, 191\],\
        \[205,  59,  30, 192, 112, 206,   8, 189,   7,  95, 152, 190,  12, 147,\
          89, 191\],\
        \[ 43, 246,  87, 190, 235, 226, 254,  63, 111, 240, 117, 191, 177, 191,\
          28, 191\]\], dtype=torch.uint8)
\>>> x.view(torch.uint8).size()
torch.Size(\[4, 16\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.view.rst.txt)

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