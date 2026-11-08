Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.kron.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.kron.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.kron.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.kron.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.kron.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.kron.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.kron.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.kron.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.kron.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.kron.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.kron.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.kron.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.kron.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.kron.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.kron.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.kron.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.kron.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.kron.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.kron.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.kron.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.kron.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.kron.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.kron.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.kron.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.kron.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.kron.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.kron.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.kron.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.kron.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.kron.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.kron.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.kron.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.kron.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.kron.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.kron.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.kron.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.kron.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.kron.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.kron.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.kron.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.kron.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.kron.html)

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

torch.kron[#](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html#torch-kron "Link to this heading")

==============================================================================================================

torch.kron(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.kron.html#torch.kron "Link to this definition")

Computes the Kronecker product, denoted by ⊗\\otimes⊗, of `input` and `other`.

If `input` is a (a0×a1×⋯×an)(a\_0 \\times a\_1 \\times \\dots \\times a\_n)(a0​×a1​×⋯×an​) tensor and `other` is a (b0×b1×⋯×bn)(b\_0 \\times b\_1 \\times \\dots \\times b\_n)(b0​×b1​×⋯×bn​) tensor, the result will be a (a0∗b0×a1∗b1×⋯×an∗bn)(a\_0\*b\_0 \\times a\_1\*b\_1 \\times \\dots \\times a\_n\*b\_n)(a0​∗b0​×a1​∗b1​×⋯×an​∗bn​) tensor with the following entries:

(input⊗other)k0,k1,…,kn\=inputi0,i1,…,in∗otherj0,j1,…,jn,(\\text{input} \\otimes \\text{other})\_{k\_0, k\_1, \\dots, k\_n} = \\text{input}\_{i\_0, i\_1, \\dots, i\_n} \* \\text{other}\_{j\_0, j\_1, \\dots, j\_n}, (input⊗other)k0​,k1​,…,kn​​\=inputi0​,i1​,…,in​​∗otherj0​,j1​,…,jn​​,

where kt\=it∗bt+jtk\_t = i\_t \* b\_t + j\_tkt​\=it​∗bt​+jt​ for 0≤t≤n0 \\leq t \\leq n0≤t≤n. If one tensor has fewer dimensions than the other it is unsqueezed until it has the same number of dimensions.

Supports real-valued and complex-valued inputs.

Note

This function generalizes the typical definition of the Kronecker product for two matrices to two tensors, as described above. When `input` is a (m×n)(m \\times n)(m×n) matrix and `other` is a (p×q)(p \\times q)(p×q) matrix, the result will be a (p∗m×q∗n)(p\*m \\times q\*n)(p∗m×q∗n) block matrix:

A⊗B\=\[a11B⋯a1nB⋮⋱⋮am1B⋯amnB\]\\mathbf{A} \\otimes \\mathbf{B}=\\begin{bmatrix} a\_{11} \\mathbf{B} & \\cdots & a\_{1 n} \\mathbf{B} \\\\ \\vdots & \\ddots & \\vdots \\\\ a\_{m 1} \\mathbf{B} & \\cdots & a\_{m n} \\mathbf{B} \\end{bmatrix} A⊗B\=​a11​B⋮am1​B​⋯⋱⋯​a1n​B⋮amn​B​​

where `input` is A\\mathbf{A}A and `other` is B\\mathbf{B}B.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) –
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) –
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – The output tensor. Ignored if `None`. Default: `None`

Examples:

\>>> mat1 \= torch.eye(2)
\>>> mat2 \= torch.ones(2, 2)
\>>> torch.kron(mat1, mat2)
tensor(\[\[1., 1., 0., 0.\],\
        \[1., 1., 0., 0.\],\
        \[0., 0., 1., 1.\],\
        \[0., 0., 1., 1.\]\])

\>>> mat1 \= torch.eye(2)
\>>> mat2 \= torch.arange(1, 5).reshape(2, 2)
\>>> torch.kron(mat1, mat2)
tensor(\[\[1., 2., 0., 0.\],\
        \[3., 4., 0., 0.\],\
        \[0., 0., 1., 2.\],\
        \[0., 0., 3., 4.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.kron.rst.txt)

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