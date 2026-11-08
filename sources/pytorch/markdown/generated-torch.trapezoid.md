Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.trapezoid.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.trapezoid.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.trapezoid.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.trapezoid.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.trapezoid.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.trapezoid.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.trapezoid.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.trapezoid.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.trapezoid.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.trapezoid.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.trapezoid.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.trapezoid.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.trapezoid.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.trapezoid.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.trapezoid.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.trapezoid.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.trapezoid.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.trapezoid.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.trapezoid.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.trapezoid.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.trapezoid.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.trapezoid.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.trapezoid.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.trapezoid.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.trapezoid.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.trapezoid.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.trapezoid.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.trapezoid.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.trapezoid.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.trapezoid.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.trapezoid.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.trapezoid.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.trapezoid.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.trapezoid.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.trapezoid.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.trapezoid.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.trapezoid.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.trapezoid.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.trapezoid.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.trapezoid.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.trapezoid.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.trapezoid.html)

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

torch.trapezoid[#](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html#torch-trapezoid "Link to this heading")

=============================================================================================================================

torch.trapezoid(_y_, _x\=None_, _\*_, _dx\=None_, _dim\=\-1_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.trapezoid.html#torch.trapezoid "Link to this definition")

Computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
 along `dim`. By default the spacing between elements is assumed to be 1, but `dx` can be used to specify a different constant spacing, and `x` can be used to specify arbitrary spacing along `dim`. Only one of `x` or `dx` should be specified.

Assuming `y` is a one-dimensional tensor with elements y0,y1,...,yn{y\_0, y\_1, ..., y\_n}y0​,y1​,...,yn​, the default computation is

∑i\=1n12(yi+yi−1)\\begin{aligned} \\sum\_{i = 1}^{n} \\frac{1}{2} (y\_i + y\_{i-1}) \\end{aligned} i\=1∑n​21​(yi​+yi−1​)​

When `dx` is specified the computation becomes

∑i\=1nΔx2(yi+yi−1)\\begin{aligned} \\sum\_{i = 1}^{n} \\frac{\\Delta x}{2} (y\_i + y\_{i-1}) \\end{aligned} i\=1∑n​2Δx​(yi​+yi−1​)​

effectively multiplying the result by `dx`. When `x` is specified, assuming `x` is also a one-dimensional tensor with elements x0,x1,...,xn{x\_0, x\_1, ..., x\_n}x0​,x1​,...,xn​, the computation becomes

∑i\=1n(xi−xi−1)2(yi+yi−1)\\begin{aligned} \\sum\_{i = 1}^{n} \\frac{(x\_i - x\_{i-1})}{2} (y\_i + y\_{i-1}) \\end{aligned} i\=1∑n​2(xi​−xi−1​)​(yi​+yi−1​)​

When `x` and `y` have the same size, the computation is as described above and no broadcasting is needed. The broadcasting behavior of this function is as follows when their sizes are different. For both `x` and `y`, the function computes the difference between consecutive elements along dimension `dim`. This effectively creates two tensors, x\_diff and y\_diff, that have the same shape as the original tensors except their lengths along the dimension `dim` is reduced by 1. After that, those two tensors are broadcast together to compute final output as part of the trapezoidal rule. See the examples below for details.

Note

The trapezoidal rule is a technique for approximating the definite integral of a function by averaging its left and right Riemann sums. The approximation becomes more accurate as the resolution of the partition increases.

Parameters:

*   **y** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Values to use when computing the trapezoidal rule.
    
*   **x** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – If specified, defines spacing between values as specified above.
    

Keyword Arguments:

*   **dx** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – constant spacing between values. If neither `x` or `dx` are specified then this defaults to 1. Effectively multiplies the result by its value.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The dimension along which to compute the trapezoidal rule. The last (inner-most) dimension by default.
    

Examples:

\>>> \# Computes the trapezoidal rule in 1D, spacing is implicitly 1
\>>> y \= torch.tensor(\[1, 5, 10\])
\>>> torch.trapezoid(y)
tensor(10.5)

\>>> \# Computes the same trapezoidal rule directly to verify
\>>> (1 + 10 + 10) / 2
10.5

\>>> \# Computes the trapezoidal rule in 1D with constant spacing of 2
\>>> \# NOTE: the result is the same as before, but multiplied by 2
\>>> torch.trapezoid(y, dx\=2)
21.0

\>>> \# Computes the trapezoidal rule in 1D with arbitrary spacing
\>>> x \= torch.tensor(\[1, 3, 6\])
\>>> torch.trapezoid(y, x)
28.5

\>>> \# Computes the same trapezoidal rule directly to verify
\>>> ((3 \- 1) \* (1 + 5) + (6 \- 3) \* (5 + 10)) / 2
28.5

\>>> \# Computes the trapezoidal rule for each row of a 3x3 matrix
\>>> y \= torch.arange(9).reshape(3, 3)
tensor(\[\[0, 1, 2\],\
        \[3, 4, 5\],\
        \[6, 7, 8\]\])
\>>> torch.trapezoid(y)
tensor(\[ 2., 8., 14.\])

\>>> \# Computes the trapezoidal rule for each column of the matrix
\>>> torch.trapezoid(y, dim\=0)
tensor(\[ 6., 8., 10.\])

\>>> \# Computes the trapezoidal rule for each row of a 3x3 ones matrix
\>>> \#   with the same arbitrary spacing
\>>> y \= torch.ones(3, 3)
\>>> x \= torch.tensor(\[1, 3, 6\])
\>>> torch.trapezoid(y, x)
array(\[5., 5., 5.\])

\>>> \# Computes the trapezoidal rule for each row of a 3x3 ones matrix
\>>> \#   with different arbitrary spacing per row
\>>> y \= torch.ones(3, 3)
\>>> x \= torch.tensor(\[\[1, 2, 3\], \[1, 3, 5\], \[1, 4, 7\]\])
\>>> torch.trapezoid(y, x)
array(\[2., 4., 6.\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.trapezoid.rst.txt)

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