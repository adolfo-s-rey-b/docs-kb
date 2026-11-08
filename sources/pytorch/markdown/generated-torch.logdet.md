Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.logdet.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.logdet.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.logdet.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.logdet.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.logdet.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.logdet.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.logdet.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.logdet.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.logdet.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.logdet.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.logdet.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.logdet.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.logdet.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.logdet.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.logdet.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.logdet.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.logdet.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.logdet.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.logdet.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.logdet.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.logdet.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.logdet.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.logdet.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.logdet.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.logdet.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.logdet.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.logdet.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.logdet.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.logdet.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.logdet.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.logdet.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.logdet.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.logdet.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.logdet.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.logdet.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.logdet.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.logdet.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.logdet.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.logdet.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.logdet.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.logdet.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.logdet.html)

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

torch.logdet[#](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#torch-logdet "Link to this heading")

====================================================================================================================

torch.logdet(_input_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#torch.logdet "Link to this definition")

Calculates log determinant of a square matrix or batches of square matrices.

It returns `-inf` if the input has a determinant of zero, and `NaN` if it has a negative determinant.

Note

Backward through [`logdet()`](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#torch.logdet "torch.logdet")
 internally uses SVD results when `input` is not invertible. In this case, double backward through [`logdet()`](https://docs.pytorch.org/docs/2.15/generated/torch.logdet.html#torch.logdet "torch.logdet")
 will be unstable in when `input` doesn’t have distinct singular values. See [`torch.linalg.svd()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.svd.html#torch.linalg.svd "torch.linalg.svd")
 for details.

See also

[`torch.linalg.slogdet()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.slogdet.html#torch.linalg.slogdet "torch.linalg.slogdet")
 computes the sign (resp. angle) and natural logarithm of the absolute value of the determinant of real-valued (resp. complex) square matrices.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor of size `(*, n, n)` where `*` is zero or more batch dimensions.

Example:

\>>> A \= torch.randn(3, 3)
\>>> torch.det(A)
tensor(0.2611)
\>>> torch.logdet(A)
tensor(-1.3430)
\>>> A
tensor(\[\[\[ 0.9254, -0.6213\],\
         \[-0.5787,  1.6843\]\],\
\
        \[\[ 0.3242, -0.9665\],\
         \[ 0.4539, -0.0887\]\],\
\
        \[\[ 1.1336, -0.4025\],\
         \[-0.7089,  0.9032\]\]\])
\>>> A.det()
tensor(\[1.1990, 0.4099, 0.7386\])
\>>> A.det().log()
tensor(\[ 0.1815, -0.8917, -0.3031\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.logdet.rst.txt)

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