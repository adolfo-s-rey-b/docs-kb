Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.chain_matmul.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.chain_matmul.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.chain_matmul.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.chain_matmul.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.chain_matmul.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.chain_matmul.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.chain_matmul.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.chain_matmul.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.chain_matmul.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.chain_matmul.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.chain_matmul.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.chain_matmul.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.chain_matmul.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.chain_matmul.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.chain_matmul.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.chain_matmul.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.chain_matmul.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.chain_matmul.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.chain_matmul.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.chain_matmul.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.chain_matmul.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.chain_matmul.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.chain_matmul.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.chain_matmul.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.chain_matmul.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.chain_matmul.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.chain_matmul.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.chain_matmul.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.chain_matmul.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.chain_matmul.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.chain_matmul.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.chain_matmul.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.chain_matmul.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.chain_matmul.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.chain_matmul.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.chain_matmul.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.chain_matmul.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.chain_matmul.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.chain_matmul.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.chain_matmul.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.chain_matmul.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.chain_matmul.html)

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

torch.chain\_matmul[#](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html#torch-chain-matmul "Link to this heading")

=======================================================================================================================================

torch.chain\_matmul(_\*matrices_, _out\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L2062)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html#torch.chain_matmul "Link to this definition")

Returns the matrix product of the NNN 2-D tensors. This product is efficiently computed using the matrix chain order algorithm which selects the order in which incurs the lowest cost in terms of arithmetic operations ([\[CLRS\]](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)
). Note that since this is a function to compute the product, NNN needs to be greater than or equal to 2; if equal to 2 then a trivial matrix-matrix product is returned. If NNN is 1, then this is a no-op - the original matrix is returned as is.

Warning

[`torch.chain_matmul()`](https://docs.pytorch.org/docs/2.15/generated/torch.chain_matmul.html#torch.chain_matmul "torch.chain_matmul")
 is deprecated and will be removed in a future PyTorch release. Use [`torch.linalg.multi_dot()`](https://docs.pytorch.org/docs/2.15/generated/torch.linalg.multi_dot.html#torch.linalg.multi_dot "torch.linalg.multi_dot")
 instead, which accepts a list of two or more tensors rather than multiple arguments.

Parameters:

*   **matrices** (_Tensors__..._) – a sequence of 2 or more 2-D tensors whose product is to be determined.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor. Ignored if `out` = `None`.
    

Returns:

if the ithi^{th}ith tensor was of dimensions pi×pi+1p\_{i} \\times p\_{i + 1}pi​×pi+1​, then the product would be of dimensions p1×pN+1p\_{1} \\times p\_{N + 1}p1​×pN+1​.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> a \= torch.randn(3, 4)
\>>> b \= torch.randn(4, 5)
\>>> c \= torch.randn(5, 6)
\>>> d \= torch.randn(6, 7)
\>>> \# will raise a deprecation warning
\>>> torch.chain\_matmul(a, b, c, d)
tensor(\[\[ -2.3375,  -3.9790,  -4.1119,  -6.6577,   9.5609, -11.5095,  -3.2614\],\
        \[ 21.4038,   3.3378,  -8.4982,  -5.2457, -10.2561,  -2.4684,   2.7163\],\
        \[ -0.9647,  -5.8917,  -2.3213,  -5.2284,  12.8615, -12.2816,  -2.5095\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.chain_matmul.rst.txt)

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