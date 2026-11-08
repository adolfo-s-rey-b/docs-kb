Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.tensor.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.tensor.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.tensor.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.tensor.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.tensor.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.tensor.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.tensor.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.tensor.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.tensor.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.tensor.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.tensor.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.tensor.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.tensor.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.tensor.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.tensor.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.tensor.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.tensor.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.tensor.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.tensor.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.tensor.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.tensor.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.tensor.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.tensor.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.tensor.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.tensor.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.tensor.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.tensor.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.tensor.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.tensor.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.tensor.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.tensor.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.tensor.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.tensor.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.tensor.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.tensor.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.tensor.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.tensor.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.tensor.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.tensor.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.tensor.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.tensor.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.tensor.html)

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

torch.tensor[#](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch-tensor "Link to this heading")

====================================================================================================================

torch.tensor(_data_, _\*_, _dtype\=None_, _device\=None_, _requires\_grad\=False_, _pin\_memory\=False_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch.tensor "Link to this definition")

Constructs a tensor with no autograd history (also known as a “leaf tensor”, see [Autograd mechanics](https://docs.pytorch.org/docs/2.15/notes/autograd.html)
) by copying `data`.

Warning

When working with tensors prefer using [`torch.Tensor.clone()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.clone.html#torch.Tensor.clone "torch.Tensor.clone")
, [`torch.Tensor.detach()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.detach.html#torch.Tensor.detach "torch.Tensor.detach")
, and [`torch.Tensor.requires_grad_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_ "torch.Tensor.requires_grad_")
 for readability. Letting t be a tensor, `torch.tensor(t)` is equivalent to `t.detach().clone()`, and `torch.tensor(t, requires_grad=True)` is equivalent to `t.detach().clone().requires_grad_(True)`.

See also

[`torch.as_tensor()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_tensor.html#torch.as_tensor "torch.as_tensor")
 preserves autograd history and avoids copies where possible. [`torch.from_numpy()`](https://docs.pytorch.org/docs/2.15/generated/torch.from_numpy.html#torch.from_numpy "torch.from_numpy")
 creates a tensor that shares storage with a NumPy array.

Parameters:

**data** (_array\_like_) – Initial data for the tensor. Can be a list, tuple, NumPy `ndarray`, scalar, and other types.

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, infers data type from `data`.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the device of the constructed tensor. If None and data is a tensor then the device of data is used. If None and data is not a tensor then the result tensor is constructed on the current device.
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned tensor. Default: `False`.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    

Example:

\>>> torch.tensor(\[\[0.1, 1.2\], \[2.2, 3.1\], \[4.9, 5.2\]\])
tensor(\[\[ 0.1000,  1.2000\],\
        \[ 2.2000,  3.1000\],\
        \[ 4.9000,  5.2000\]\])

\>>> torch.tensor(\[0, 1\])  \# Type inference on data
tensor(\[ 0,  1\])

\>>> torch.tensor(\[\[0.11111, 0.222222, 0.3333333\]\],
...              dtype\=torch.float64,
...              device\=torch.device('cuda:0'))  \# creates a double tensor on a CUDA device
tensor(\[\[ 0.1111,  0.2222,  0.3333\]\], dtype=torch.float64, device='cuda:0')

\>>> torch.tensor(3.14159)  \# Create a zero-dimensional (scalar) tensor
tensor(3.1416)

\>>> torch.tensor(\[\])  \# Create an empty tensor (of size (0,))
tensor(\[\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.tensor.rst.txt)

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