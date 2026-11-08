Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.corrcoef.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.corrcoef.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.corrcoef.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.corrcoef.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.corrcoef.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.corrcoef.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.corrcoef.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.corrcoef.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.corrcoef.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.corrcoef.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.corrcoef.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.corrcoef.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.corrcoef.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.corrcoef.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.corrcoef.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.corrcoef.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.corrcoef.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.corrcoef.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.corrcoef.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.corrcoef.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.corrcoef.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.corrcoef.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.corrcoef.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.corrcoef.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.corrcoef.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.corrcoef.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.corrcoef.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.corrcoef.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.corrcoef.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.corrcoef.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.corrcoef.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.corrcoef.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.corrcoef.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.corrcoef.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.corrcoef.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.corrcoef.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.corrcoef.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.corrcoef.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.corrcoef.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.corrcoef.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.corrcoef.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.corrcoef.html)

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

torch.corrcoef[#](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html#torch-corrcoef "Link to this heading")

==========================================================================================================================

torch.corrcoef(_input_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html#torch.corrcoef "Link to this definition")

Estimates the Pearson product-moment correlation coefficient matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations.

Note

The correlation coefficient matrix R is computed using the covariance matrix C as given by Rij\=CijCii∗CjjR\_{ij} = \\frac{ C\_{ij} } { \\sqrt{ C\_{ii} \* C\_{jj} } }Rij​\=Cii​∗Cjj​​Cij​​

Note

Due to floating point rounding, the resulting array may not be Hermitian and its diagonal elements may not be 1. The real and imaginary values are clipped to the interval \[-1, 1\] in an attempt to improve this situation.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – A 2D matrix containing multiple variables and observations, or a Scalar or 1D vector representing a single variable.

Returns:

(Tensor) The correlation coefficient matrix of the variables.

See also

[`torch.cov()`](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html#torch.cov "torch.cov")
 covariance matrix.

Example:

\>>> x \= torch.tensor(\[\[0, 1, 2\], \[2, 1, 0\]\])
\>>> torch.corrcoef(x)
tensor(\[\[ 1., -1.\],\
        \[-1.,  1.\]\])
\>>> x \= torch.randn(2, 4)
\>>> x
tensor(\[\[-0.2678, -0.0908, -0.3766,  0.2780\],\
        \[-0.5812,  0.1535,  0.2387,  0.2350\]\])
\>>> torch.corrcoef(x)
tensor(\[\[1.0000, 0.3582\],\
        \[0.3582, 1.0000\]\])
\>>> torch.corrcoef(x\[0\])
tensor(1.)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.corrcoef.rst.txt)

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