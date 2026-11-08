Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cov.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cov.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cov.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cov.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cov.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cov.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cov.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cov.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cov.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cov.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cov.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cov.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cov.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cov.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cov.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cov.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cov.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cov.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cov.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cov.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cov.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cov.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cov.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cov.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cov.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cov.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cov.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cov.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cov.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cov.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cov.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cov.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cov.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cov.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cov.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cov.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cov.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cov.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cov.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cov.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cov.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cov.html)

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

torch.cov[#](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html#torch-cov "Link to this heading")

===========================================================================================================

torch.cov(_input_, _\*_, _correction\=1_, _fweights\=None_, _aweights\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cov.html#torch.cov "Link to this definition")

Estimates the covariance matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations.

A covariance matrix is a square matrix giving the covariance of each pair of variables. The diagonal contains the variance of each variable (covariance of a variable with itself). By definition, if `input` represents a single variable (Scalar or 1D) then its variance is returned.

The sample covariance of the variables xxx and yyy is given by:

cov(x,y)\=∑i\=1N(xi−xˉ)(yi−yˉ)max⁡(0, N − δN)\\text{cov}(x,y) = \\frac{\\sum^{N}\_{i = 1}(x\_{i} - \\bar{x})(y\_{i} - \\bar{y})}{\\max(0,~N~-~\\delta N)} cov(x,y)\=max(0, N − δN)∑i\=1N​(xi​−xˉ)(yi​−yˉ​)​

where xˉ\\bar{x}xˉ and yˉ\\bar{y}yˉ​ are the simple means of the xxx and yyy respectively, and δN\\delta NδN is the `correction`.

If `fweights` and/or `aweights` are provided, the weighted covariance is calculated, which is given by:

covw(x,y)\=∑i\=1Nwi(xi−μx∗)(yi−μy∗)max⁡(0, ∑i\=1Nwi − ∑i\=1Nwiai∑i\=1Nwi δN)\\text{cov}\_w(x,y) = \\frac{\\sum^{N}\_{i = 1}w\_i(x\_{i} - \\mu\_x^\*)(y\_{i} - \\mu\_y^\*)} {\\max(0,~\\sum^{N}\_{i = 1}w\_i~-~\\frac{\\sum^{N}\_{i = 1}w\_ia\_i}{\\sum^{N}\_{i = 1}w\_i}~\\delta N)} covw​(x,y)\=max(0, ∑i\=1N​wi​ − ∑i\=1N​wi​∑i\=1N​wi​ai​​ δN)∑i\=1N​wi​(xi​−μx∗​)(yi​−μy∗​)​

where www denotes `fweights` or `aweights` (`f` and `a` for brevity) based on whichever is provided, or w\=f×aw = f \\times aw\=f×a if both are provided, and μx∗\=∑i\=1Nwixi∑i\=1Nwi\\mu\_x^\* = \\frac{\\sum^{N}\_{i = 1}w\_ix\_{i} }{\\sum^{N}\_{i = 1}w\_i}μx∗​\=∑i\=1N​wi​∑i\=1N​wi​xi​​ is the weighted mean of the variable. If not provided, `f` and/or `a` can be seen as a 1\\mathbb{1}1 vector of appropriate size.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – A 2D matrix containing multiple variables and observations, or a Scalar or 1D vector representing a single variable.

Keyword Arguments:

*   **correction** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – difference between the sample size and sample degrees of freedom. Defaults to Bessel’s correction, `correction = 1` which returns the unbiased estimate, even if both `fweights` and `aweights` are specified. `correction = 0` will return the simple average. Defaults to `1`.
    
*   **fweights** ([_tensor_](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch.tensor "torch.tensor")
    _,_ _optional_) – A Scalar or 1D tensor of observation vector frequencies representing the number of times each observation should be repeated. Its numel must equal the number of columns of `input`. Must have integral dtype. Ignored if `None`. Defaults to `None`.
    
*   **aweights** ([_tensor_](https://docs.pytorch.org/docs/2.15/generated/torch.tensor.html#torch.tensor "torch.tensor")
    _,_ _optional_) – A Scalar or 1D array of observation vector weights. These relative weights are typically large for observations considered “important” and smaller for observations considered less “important”. Its numel must equal the number of columns of `input`. Must have floating point dtype. Ignored if `None`. Defaults to `None`.
    

Returns:

(Tensor) The covariance matrix of the variables.

See also

[`torch.corrcoef()`](https://docs.pytorch.org/docs/2.15/generated/torch.corrcoef.html#torch.corrcoef "torch.corrcoef")
 normalized covariance matrix.

Example:

\>>> x \= torch.tensor(\[\[0, 2\], \[1, 1\], \[2, 0\]\]).T
\>>> x
tensor(\[\[0, 1, 2\],\
        \[2, 1, 0\]\])
\>>> torch.cov(x)
tensor(\[\[ 1., -1.\],\
        \[-1.,  1.\]\])
\>>> torch.cov(x, correction\=0)
tensor(\[\[ 0.6667, -0.6667\],\
        \[-0.6667,  0.6667\]\])
\>>> fw \= torch.randint(1, 10, (3,))
\>>> fw
tensor(\[1, 6, 9\])
\>>> aw \= torch.rand(3)
\>>> aw
tensor(\[0.4282, 0.0255, 0.4144\])
\>>> torch.cov(x, fweights\=fw, aweights\=aw)
tensor(\[\[ 0.4169, -0.4169\],\
        \[-0.4169,  0.4169\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cov.rst.txt)

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