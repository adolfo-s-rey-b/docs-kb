Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/special.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/special.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/special.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/special.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/special.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/special.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/special.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/special.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/special.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/special.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/special.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/special.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/special.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/special.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/special.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/special.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/special.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/special.html)
[v1.13](https://docs.pytorch.org/docs/1.13/special.html)
[v1.12](https://docs.pytorch.org/docs/1.12/special.html)
[v1.11](https://docs.pytorch.org/docs/1.11/special.html)
[v1.10](https://docs.pytorch.org/docs/1.10/special.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/special.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/special.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/special.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/special.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/special.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/special.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/special.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/special.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/special.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/special.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/special.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/special.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/special.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/special.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/special.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/special.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/special.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/special.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/special.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/special.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/special.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/special.html)

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

torch.special[#](https://docs.pytorch.org/docs/2.15/special.html#torch-special "Link to this heading")

=======================================================================================================

Created On: Mar 04, 2021 | Last Updated On: Jun 18, 2025

The torch.special module, modeled after SciPy’s [special](https://docs.scipy.org/doc/scipy/reference/special.html)
 module.

Functions[#](https://docs.pytorch.org/docs/2.15/special.html#functions "Link to this heading")

-----------------------------------------------------------------------------------------------

torch.special.airy\_ai(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L982)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.airy_ai "Link to this definition")

Airy function Ai(input)\\text{Ai}\\left(\\text{input}\\right)Ai(input).

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.bessel\_j0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L999)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.bessel_j0 "Link to this definition")

Bessel function of the first kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.bessel\_j1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1016)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.bessel_j1 "Link to this definition")

Bessel function of the first kind of order 111.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.bessel\_y0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1033)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.bessel_y0 "Link to this definition")

Bessel function of the second kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.bessel\_y1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1050)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.bessel_y1 "Link to this definition")

Bessel function of the second kind of order 111.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.chebyshev\_polynomial\_t(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1067)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.chebyshev_polynomial_t "Link to this definition")

Chebyshev polynomial of the first kind Tn(input)T\_{n}(\\text{input})Tn​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, input\\text{input}input is returned. If n<6n < 6n<6 or ∣input∣\>1|\\text{input}| > 1∣input∣\>1 the recursion:

Tn+1(input)\=2×input×Tn(input)−Tn−1(input)T\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times T\_{n}(\\text{input}) - T\_{n - 1}(\\text{input}) Tn+1​(input)\=2×input×Tn​(input)−Tn−1​(input)

is evaluated. Otherwise, the explicit trigonometric formula:

Tn(input)\=cos(n×arccos(x))T\_{n}(\\text{input}) = \\text{cos}(n \\times \\text{arccos}(x)) Tn​(input)\=cos(n×arccos(x))

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.chebyshev\_polynomial\_u(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1098)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.chebyshev_polynomial_u "Link to this definition")

Chebyshev polynomial of the second kind Un(input)U\_{n}(\\text{input})Un​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, 2×input2 \\times \\text{input}2×input is returned. If n<6n < 6n<6 or ∣input∣\>1|\\text{input}| > 1∣input∣\>1, the recursion:

Un+1(input)\=2×input×Un(input)−Un−1(input)U\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times U\_{n}(\\text{input}) - U\_{n - 1}(\\text{input}) Un+1​(input)\=2×input×Un​(input)−Un−1​(input)

is evaluated. Otherwise, the explicit trigonometric formula:

sin((n+1)×arccos(input))sin(arccos(input))\\frac{\\text{sin}((n + 1) \\times \\text{arccos}(\\text{input}))}{\\text{sin}(\\text{arccos}(\\text{input}))} sin(arccos(input))sin((n+1)×arccos(input))​

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.chebyshev\_polynomial\_v(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1130)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.chebyshev_polynomial_v "Link to this definition")

Chebyshev polynomial of the third kind Vn∗(input)V\_{n}^{\\ast}(\\text{input})Vn∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.chebyshev\_polynomial\_w(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1148)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.chebyshev_polynomial_w "Link to this definition")

Chebyshev polynomial of the fourth kind Wn∗(input)W\_{n}^{\\ast}(\\text{input})Wn∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.digamma(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L109)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.digamma "Link to this definition")

Computes the logarithmic derivative of the gamma function on input.

ϝ(x)\=ddxln⁡(Γ(x))\=Γ′(x)Γ(x)\\digamma(x) = \\frac{d}{dx} \\ln\\left(\\Gamma\\left(x\\right)\\right) = \\frac{\\Gamma'(x)}{\\Gamma(x)} ϝ(x)\=dxd​ln(Γ(x))\=Γ(x)Γ′(x)​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the tensor to compute the digamma function on

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Note

This function is similar to SciPy’s scipy.special.digamma.

Note

From PyTorch 1.8 onwards, the digamma function returns \-Inf for 0. Previously it returned NaN for 0.

Example:

\>>> a \= torch.tensor(\[1, 0.5\])
\>>> torch.special.digamma(a)
tensor(\[-0.5772, -1.9635\])

Copy to clipboard

torch.special.entr(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L67)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.entr "Link to this definition")

Computes the entropy on `input` (as defined below), elementwise.

entr(x)\={−x∗ln⁡(x)x\>00x\=0.0−∞x<0\\begin{align} \\text{entr(x)} = \\begin{cases} -x \* \\ln(x) & x > 0 \\\\ 0 & x = 0.0 \\\\ -\\infty & x < 0 \\end{cases} \\end{align} entr(x)\=⎩⎨⎧​−x∗ln(x)0−∞​x\>0x\=0.0x<0​​​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.arange(\-0.5, 1, 0.5)
\>>> a
tensor(\[-0.5000,  0.0000,  0.5000\])
\>>> torch.special.entr(a)
tensor(\[  -inf, 0.0000, 0.3466\])

Copy to clipboard

torch.special.erf(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L202)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erf "Link to this definition")

Computes the error function of `input`. The error function is defined as follows:

erf(x)\=2π∫0xe−t2dt\\mathrm{erf}(x) = \\frac{2}{\\sqrt{\\pi}} \\int\_{0}^{x} e^{-t^2} dt erf(x)\=π​2​∫0x​e−t2dt

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.erf(torch.tensor(\[0, \-1., 10.\]))
tensor(\[ 0.0000, -0.8427,  1.0000\])

Copy to clipboard

torch.special.erfc(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L226)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfc "Link to this definition")

Computes the complementary error function of `input`. The complementary error function is defined as follows:

erfc(x)\=1−2π∫0xe−t2dt\\mathrm{erfc}(x) = 1 - \\frac{2}{\\sqrt{\\pi}} \\int\_{0}^{x} e^{-t^2} dt erfc(x)\=1−π​2​∫0x​e−t2dt

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.erfc(torch.tensor(\[0, \-1., 10.\]))
tensor(\[ 1.0000, 1.8427,  0.0000\])

Copy to clipboard

torch.special.erfcx(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L251)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfcx "Link to this definition")

Computes the scaled complementary error function for each element of `input`. The scaled complementary error function is defined as follows:

erfcx(x)\=ex2erfc(x)\\mathrm{erfcx}(x) = e^{x^2} \\mathrm{erfc}(x) erfcx(x)\=ex2erfc(x)

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.erfcx(torch.tensor(\[0, \-1., 10.\]))
tensor(\[ 1.0000, 5.0090, 0.0561\])

Copy to clipboard

torch.special.erfinv(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L279)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.erfinv "Link to this definition")

Computes the inverse error function of `input`. The inverse error function is defined in the range (−1,1)(-1, 1)(−1,1) as:

erfinv(erf(x))\=x\\mathrm{erfinv}(\\mathrm{erf}(x)) = x erfinv(erf(x))\=x

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.erfinv(torch.tensor(\[0, 0.5, \-1.\]))
tensor(\[ 0.0000,  0.4769,    -inf\])

Copy to clipboard

torch.special.exp2(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L379)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.exp2 "Link to this definition")

Computes the base two exponential function of `input`.

yi\=2xiy\_{i} = 2^{x\_{i}} yi​\=2xi​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.exp2(torch.tensor(\[0, math.log2(2.), 3, 4\]))
tensor(\[ 1.,  2.,  8., 16.\])

Copy to clipboard

torch.special.expit(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L352)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expit "Link to this definition")

Computes the expit (also known as the logistic sigmoid function) of the elements of `input`.

outi\=11+e−inputi\\text{out}\_{i} = \\frac{1}{1 + e^{-\\text{input}\_{i}}} outi​\=1+e−inputi​1​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> t \= torch.randn(4)
\>>> t
tensor(\[ 0.9213,  1.0887, -0.8858, -1.7683\])
\>>> torch.special.expit(t)
tensor(\[ 0.7153,  0.7481,  0.2920,  0.1458\])

Copy to clipboard

torch.special.expm1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L404)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.expm1 "Link to this definition")

Computes the exponential of the elements minus 1 of `input`.

yi\=exi−1y\_{i} = e^{x\_{i}} - 1 yi​\=exi​−1

Note

This function provides greater precision than exp(x) - 1 for small values of x.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.expm1(torch.tensor(\[0, math.log(2.)\]))
tensor(\[ 0.,  1.\])

Copy to clipboard

torch.special.gammainc(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L885)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammainc "Link to this definition")

Computes the regularized lower incomplete gamma function:

outi\=1Γ(inputi)∫0otheritinputi−1e−tdt\\text{out}\_{i} = \\frac{1}{\\Gamma(\\text{input}\_i)} \\int\_0^{\\text{other}\_i} t^{\\text{input}\_i-1} e^{-t} dt outi​\=Γ(inputi​)1​∫0otheri​​tinputi​−1e−tdt

where both inputi\\text{input}\_iinputi​ and otheri\\text{other}\_iotheri​ are weakly positive and at least one is strictly positive. If both are zero or either is negative then outi\=nan\\text{out}\_i=\\text{nan}outi​\=nan. Γ(⋅)\\Gamma(\\cdot)Γ(⋅) in the equation above is the gamma function,

Γ(inputi)\=∫0∞t(inputi−1)e−tdt.\\Gamma(\\text{input}\_i) = \\int\_0^\\infty t^{(\\text{input}\_i-1)} e^{-t} dt. Γ(inputi​)\=∫0∞​t(inputi​−1)e−tdt.

See [`torch.special.gammaincc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaincc "torch.special.gammaincc")
 and [`torch.special.gammaln()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaln "torch.special.gammaln")
 for related functions.

Supports [broadcasting to a common shape](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 and float inputs.

Note

The backward pass with respect to `input` is not yet supported. Please open an issue on PyTorch’s Github to request it.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first non-negative input tensor
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second non-negative input tensor
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a1 \= torch.tensor(\[4.0\])
\>>> a2 \= torch.tensor(\[3.0, 4.0, 5.0\])
\>>> a \= torch.special.gammaincc(a1, a2)
tensor(\[0.3528, 0.5665, 0.7350\])
tensor(\[0.3528, 0.5665, 0.7350\])
\>>> b \= torch.special.gammainc(a1, a2) + torch.special.gammaincc(a1, a2)
tensor(\[1., 1., 1.\])

Copy to clipboard

torch.special.gammaincc(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L934)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaincc "Link to this definition")

Computes the regularized upper incomplete gamma function:

outi\=1Γ(inputi)∫otheri∞tinputi−1e−tdt\\text{out}\_{i} = \\frac{1}{\\Gamma(\\text{input}\_i)} \\int\_{\\text{other}\_i}^{\\infty} t^{\\text{input}\_i-1} e^{-t} dt outi​\=Γ(inputi​)1​∫otheri​∞​tinputi​−1e−tdt

where both inputi\\text{input}\_iinputi​ and otheri\\text{other}\_iotheri​ are weakly positive and at least one is strictly positive. If both are zero or either is negative then outi\=nan\\text{out}\_i=\\text{nan}outi​\=nan. Γ(⋅)\\Gamma(\\cdot)Γ(⋅) in the equation above is the gamma function,

Γ(inputi)\=∫0∞t(inputi−1)e−tdt.\\Gamma(\\text{input}\_i) = \\int\_0^\\infty t^{(\\text{input}\_i-1)} e^{-t} dt. Γ(inputi​)\=∫0∞​t(inputi​−1)e−tdt.

See [`torch.special.gammainc()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammainc "torch.special.gammainc")
 and [`torch.special.gammaln()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaln "torch.special.gammaln")
 for related functions.

Supports [broadcasting to a common shape](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
 and float inputs.

Note

The backward pass with respect to `input` is not yet supported. Please open an issue on PyTorch’s Github to request it.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the first non-negative input tensor
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the second non-negative input tensor
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a1 \= torch.tensor(\[4.0\])
\>>> a2 \= torch.tensor(\[3.0, 4.0, 5.0\])
\>>> a \= torch.special.gammaincc(a1, a2)
tensor(\[0.6472, 0.4335, 0.2650\])
\>>> b \= torch.special.gammainc(a1, a2) + torch.special.gammaincc(a1, a2)
tensor(\[1., 1., 1.\])

Copy to clipboard

torch.special.gammaln(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L140)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.gammaln "Link to this definition")

Computes the natural logarithm of the absolute value of the gamma function on `input`.

outi\=ln⁡Γ(∣inputi∣)\\text{out}\_{i} = \\ln \\Gamma(|\\text{input}\_{i}|) outi​\=lnΓ(∣inputi​∣)

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.arange(0.5, 2, 0.5)
\>>> torch.special.gammaln(a)
tensor(\[ 0.5724,  0.0000, -0.1208\])

Copy to clipboard

torch.special.hermite\_polynomial\_h(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1166)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.hermite_polynomial_h "Link to this definition")

Physicist’s Hermite polynomial Hn(input)H\_{n}(\\text{input})Hn​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, input\\text{input}input is returned. Otherwise, the recursion:

Hn+1(input)\=2×input×Hn(input)−Hn−1(input)H\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times H\_{n}(\\text{input}) - H\_{n - 1}(\\text{input}) Hn+1​(input)\=2×input×Hn​(input)−Hn−1​(input)

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.hermite\_polynomial\_he(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1192)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.hermite_polynomial_he "Link to this definition")

Probabilist’s Hermite polynomial Hen(input)He\_{n}(\\text{input})Hen​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, input\\text{input}input is returned. Otherwise, the recursion:

Hen+1(input)\=2×input×Hen(input)−Hen−1(input)He\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times He\_{n}(\\text{input}) - He\_{n - 1}(\\text{input}) Hen+1​(input)\=2×input×Hen​(input)−Hen−1​(input)

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.i0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L522)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i0 "Link to this definition")

Computes the zeroth order modified Bessel function of the first kind for each element of `input`.

outi\=I0(inputi)\=∑k\=0∞(inputi2/4)k(k!)2\\text{out}\_{i} = I\_0(\\text{input}\_{i}) = \\sum\_{k=0}^{\\infty} \\frac{(\\text{input}\_{i}^2/4)^k}{(k!)^2} outi​\=I0​(inputi​)\=k\=0∑∞​(k!)2(inputi2​/4)k​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.i0(torch.arange(5, dtype\=torch.float32))
tensor(\[ 1.0000,  1.2661,  2.2796,  4.8808, 11.3019\])

Copy to clipboard

torch.special.i0e(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L548)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i0e "Link to this definition")

Computes the exponentially scaled zeroth order modified Bessel function of the first kind (as defined below) for each element of `input`.

outi\=exp⁡(−∣x∣)∗i0(x)\=exp⁡(−∣x∣)∗∑k\=0∞(inputi2/4)k(k!)2\\text{out}\_{i} = \\exp(-|x|) \* i0(x) = \\exp(-|x|) \* \\sum\_{k=0}^{\\infty} \\frac{(\\text{input}\_{i}^2/4)^k}{(k!)^2} outi​\=exp(−∣x∣)∗i0(x)\=exp(−∣x∣)∗k\=0∑∞​(k!)2(inputi2​/4)k​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.i0e(torch.arange(5, dtype\=torch.float32))
tensor(\[1.0000, 0.4658, 0.3085, 0.2430, 0.2070\])

Copy to clipboard

torch.special.i1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L573)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i1 "Link to this definition")

Computes the first order modified Bessel function of the first kind (as defined below) for each element of `input`.

outi\=(inputi)2∗∑k\=0∞(inputi2/4)k(k!)∗(k+1)!\\text{out}\_{i} = \\frac{(\\text{input}\_{i})}{2} \* \\sum\_{k=0}^{\\infty} \\frac{(\\text{input}\_{i}^2/4)^k}{(k!) \* (k+1)!} outi​\=2(inputi​)​∗k\=0∑∞​(k!)∗(k+1)!(inputi2​/4)k​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.i1(torch.arange(5, dtype\=torch.float32))
tensor(\[0.0000, 0.5652, 1.5906, 3.9534, 9.7595\])

Copy to clipboard

torch.special.i1e(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L598)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.i1e "Link to this definition")

Computes the exponentially scaled first order modified Bessel function of the first kind (as defined below) for each element of `input`.

outi\=exp⁡(−∣x∣)∗i1(x)\=exp⁡(−∣x∣)∗(inputi)2∗∑k\=0∞(inputi2/4)k(k!)∗(k+1)!\\text{out}\_{i} = \\exp(-|x|) \* i1(x) = \\exp(-|x|) \* \\frac{(\\text{input}\_{i})}{2} \* \\sum\_{k=0}^{\\infty} \\frac{(\\text{input}\_{i}^2/4)^k}{(k!) \* (k+1)!} outi​\=exp(−∣x∣)∗i1(x)\=exp(−∣x∣)∗2(inputi​)​∗k\=0∑∞​(k!)∗(k+1)!(inputi2​/4)k​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.i1e(torch.arange(5, dtype\=torch.float32))
tensor(\[0.0000, 0.2079, 0.2153, 0.1968, 0.1788\])

Copy to clipboard

torch.special.laguerre\_polynomial\_l(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1218)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.laguerre_polynomial_l "Link to this definition")

Laguerre polynomial Ln(input)L\_{n}(\\text{input})Ln​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, input\\text{input}input is returned. Otherwise, the recursion:

Ln+1(input)\=2×input×Ln(input)−Ln−1(input)L\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times L\_{n}(\\text{input}) - L\_{n - 1}(\\text{input}) Ln+1​(input)\=2×input×Ln​(input)−Ln−1​(input)

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.legendre\_polynomial\_p(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1244)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.legendre_polynomial_p "Link to this definition")

Legendre polynomial Pn(input)P\_{n}(\\text{input})Pn​(input).

If n\=0n = 0n\=0, 111 is returned. If n\=1n = 1n\=1, input\\text{input}input is returned. Otherwise, the recursion:

Pn+1(input)\=2×input×Pn(input)−Pn−1(input)P\_{n + 1}(\\text{input}) = 2 \\times \\text{input} \\times P\_{n}(\\text{input}) - P\_{n - 1}(\\text{input}) Pn+1​(input)\=2×input×Pn​(input)−Pn−1​(input)

is evaluated.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.log1p(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L702)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.log1p "Link to this definition")

Alias for [`torch.log1p()`](https://docs.pytorch.org/docs/2.15/generated/torch.log1p.html#torch.log1p "torch.log1p")
.

torch.special.log\_ndtr(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L677)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.log_ndtr "Link to this definition")

Computes the log of the area under the standard Gaussian probability density function, integrated from minus infinity to `input`, elementwise.

log\_ndtr(x)\=log⁡(12π∫−∞xe−12t2dt)\\text{log\\\_ndtr}(x) = \\log\\left(\\frac{1}{\\sqrt{2 \\pi}}\\int\_{-\\infty}^{x} e^{-\\frac{1}{2}t^2} dt \\right) log\_ndtr(x)\=log(2π​1​∫−∞x​e−21​t2dt)

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.log\_ndtr(torch.tensor(\[\-3., \-2, \-1, 0, 1, 2, 3\]))
tensor(\[-6.6077 -3.7832 -1.841  -0.6931 -0.1728 -0.023  -0.0014\])

Copy to clipboard

torch.special.log\_softmax(_input_, _dim_, _\*_, _dtype\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L782)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.log_softmax "Link to this definition")

Computes softmax followed by a logarithm.

While mathematically equivalent to log(softmax(x)), doing these two operations separately is slower and numerically unstable. This function is computed as:

log\_softmax(xi)\=log⁡(exp⁡(xi)∑jexp⁡(xj))\\text{log\\\_softmax}(x\_{i}) = \\log\\left(\\frac{\\exp(x\_i) }{ \\sum\_j \\exp(x\_j)} \\right) log\_softmax(xi​)\=log(∑j​exp(xj​)exp(xi​)​)

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – input
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – A dimension along which log\_softmax will be computed.
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. If specified, the input tensor is cast to `dtype` before the operation is performed. This is useful for preventing data type overflows. Default: None.
    

Example:

\>>> t \= torch.ones(2, 2)
\>>> torch.special.log\_softmax(t, 0)
tensor(\[\[-0.6931, -0.6931\],\
        \[-0.6931, -0.6931\]\])

Copy to clipboard

torch.special.logit(_input_, _eps\=None_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L305)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.logit "Link to this definition")

Returns a new tensor with the logit of the elements of `input`. `input` is clamped to \[eps, 1 - eps\] when eps is not None. When eps is None and `input` < 0 or `input` > 1, the function will yield NaN.

yi\=ln⁡(zi1−zi)zi\={xiif eps is Noneepsif xi<epsxiif eps≤xi≤1−eps1−epsif xi\>1−eps\\begin{align} y\_{i} &= \\ln(\\frac{z\_{i}}{1 - z\_{i}}) \\\\ z\_{i} &= \\begin{cases} x\_{i} & \\text{if eps is None} \\\\ \\text{eps} & \\text{if } x\_{i} < \\text{eps} \\\\ x\_{i} & \\text{if } \\text{eps} \\leq x\_{i} \\leq 1 - \\text{eps} \\\\ 1 - \\text{eps} & \\text{if } x\_{i} > 1 - \\text{eps} \\end{cases} \\end{align} yi​zi​​\=ln(1−zi​zi​​)\=⎩⎨⎧​xi​epsxi​1−eps​if eps is Noneif xi​<epsif eps≤xi​≤1−epsif xi​\>1−eps​​​

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **eps** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – the epsilon for input clamp bound. Default: `None`
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.rand(5)
\>>> a
tensor(\[0.2796, 0.9331, 0.6486, 0.1523, 0.6516\])
\>>> torch.special.logit(a, eps\=1e-6)
tensor(\[-0.9466,  2.6352,  0.6131, -1.7169,  0.6261\])

Copy to clipboard

torch.special.logsumexp(_input_, _dim_, _keepdim\=False_, _\*_, _out\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L343)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.logsumexp "Link to this definition")

Alias for [`torch.logsumexp()`](https://docs.pytorch.org/docs/2.15/generated/torch.logsumexp.html#torch.logsumexp "torch.logsumexp")
.

torch.special.modified\_bessel\_i0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1270)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.modified_bessel_i0 "Link to this definition")

Modified Bessel function of the first kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.modified\_bessel\_i1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1287)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.modified_bessel_i1 "Link to this definition")

Modified Bessel function of the first kind of order 111.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.modified\_bessel\_k0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1304)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.modified_bessel_k0 "Link to this definition")

Modified Bessel function of the second kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.modified\_bessel\_k1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1321)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.modified_bessel_k1 "Link to this definition")

Modified Bessel function of the second kind of order 111.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.multigammaln(_input_, _p_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L848)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.multigammaln "Link to this definition")

Computes the [multivariate log-gamma function](https://en.wikipedia.org/wiki/Multivariate_gamma_function)
 with dimension ppp element-wise, given by

log⁡(Γp(a))\=C+∑i\=1plog⁡(Γ(a−i−12))\\log(\\Gamma\_{p}(a)) = C + \\displaystyle \\sum\_{i=1}^{p} \\log\\left(\\Gamma\\left(a - \\frac{i - 1}{2}\\right)\\right) log(Γp​(a))\=C+i\=1∑p​log(Γ(a−2i−1​))

where C\=log⁡(π)⋅p(p−1)4C = \\log(\\pi) \\cdot \\frac{p (p - 1)}{4}C\=log(π)⋅4p(p−1)​ and Γ(−)\\Gamma(-)Γ(−) is the Gamma function.

All elements must be greater than p−12\\frac{p - 1}{2}2p−1​, otherwise the behavior is undefined.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the tensor to compute the multivariate log-gamma function
    
*   **p** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of dimensions
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.empty(2, 3).uniform\_(1, 2)
\>>> a
tensor(\[\[1.6835, 1.8474, 1.1929\],\
        \[1.0475, 1.7162, 1.4180\]\])
\>>> torch.special.multigammaln(a, 2)
tensor(\[\[0.3928, 0.4007, 0.7586\],\
        \[1.0311, 0.3901, 0.5049\]\])

Copy to clipboard

torch.special.ndtr(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L624)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.ndtr "Link to this definition")

Computes the area under the standard Gaussian probability density function, integrated from minus infinity to `input`, elementwise.

ndtr(x)\=12π∫−∞xe−12t2dt\\text{ndtr}(x) = \\frac{1}{\\sqrt{2 \\pi}}\\int\_{-\\infty}^{x} e^{-\\frac{1}{2}t^2} dt ndtr(x)\=2π​1​∫−∞x​e−21​t2dt

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.ndtr(torch.tensor(\[\-3., \-2, \-1, 0, 1, 2, 3\]))
tensor(\[0.0013, 0.0228, 0.1587, 0.5000, 0.8413, 0.9772, 0.9987\])

Copy to clipboard

torch.special.ndtri(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L649)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.ndtri "Link to this definition")

Computes the argument, x, for which the area under the Gaussian probability density function (integrated from minus infinity to x) is equal to `input`, elementwise.

ndtri(p)\=2erf−1(2p−1)\\text{ndtri}(p) = \\sqrt{2}\\text{erf}^{-1}(2p - 1) ndtri(p)\=2​erf−1(2p−1)

Note

Also known as quantile function for Normal Distribution.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> torch.special.ndtri(torch.tensor(\[0, 0.25, 0.5, 0.75, 1\]))
tensor(\[   -inf, -0.6745,  0.0000,  0.6745,     inf\])

Copy to clipboard

torch.special.polygamma(_n_, _input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L166)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.polygamma "Link to this definition")

Computes the nthn^{th}nth derivative of the digamma function on `input`. n≥0n \\geq 0n≥0 is called the order of the polygamma function.

ψ(n)(x)\=d(n)dx(n)ψ(x)\\psi^{(n)}(x) = \\frac{d^{(n)}}{dx^{(n)}} \\psi(x) ψ(n)(x)\=dx(n)d(n)​ψ(x)

Note

This function is implemented only for nonnegative integers n≥0n \\geq 0n≥0.

Parameters:

*   **n** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the order of the polygamma function
    
*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> a \= torch.tensor(\[1, 0.5\])
\>>> torch.special.polygamma(1, a)
tensor(\[1.64493, 4.9348\])
\>>> torch.special.polygamma(2, a)
tensor(\[ -2.4041, -16.8288\])
\>>> torch.special.polygamma(3, a)
tensor(\[ 6.4939, 97.4091\])
\>>> torch.special.polygamma(4, a)
tensor(\[ -24.8863, -771.4742\])

Copy to clipboard

torch.special.psi(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L100)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.psi "Link to this definition")

Alias for [`torch.special.digamma()`](https://docs.pytorch.org/docs/2.15/special.html#torch.special.digamma "torch.special.digamma")
.

torch.special.round(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L743)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.round "Link to this definition")

Alias for [`torch.round()`](https://docs.pytorch.org/docs/2.15/generated/torch.round.html#torch.round "torch.round")
.

torch.special.scaled\_modified\_bessel\_k0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1338)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.scaled_modified_bessel_k0 "Link to this definition")

Scaled modified Bessel function of the second kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.scaled\_modified\_bessel\_k1(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1355)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.scaled_modified_bessel_k1 "Link to this definition")

Scaled modified Bessel function of the second kind of order 111.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.shifted\_chebyshev\_polynomial\_t(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1372)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.shifted_chebyshev_polynomial_t "Link to this definition")

Chebyshev polynomial of the first kind Tn∗(input)T\_{n}^{\\ast}(\\text{input})Tn∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.shifted\_chebyshev\_polynomial\_u(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1390)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.shifted_chebyshev_polynomial_u "Link to this definition")

Chebyshev polynomial of the second kind Un∗(input)U\_{n}^{\\ast}(\\text{input})Un∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.shifted\_chebyshev\_polynomial\_v(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1408)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.shifted_chebyshev_polynomial_v "Link to this definition")

Chebyshev polynomial of the third kind Vn∗(input)V\_{n}^{\\ast}(\\text{input})Vn∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.shifted\_chebyshev\_polynomial\_w(_input_, _n_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1426)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.shifted_chebyshev_polynomial_w "Link to this definition")

Chebyshev polynomial of the fourth kind Wn∗(input)W\_{n}^{\\ast}(\\text{input})Wn∗​(input).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **n** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Degree of the polynomial.
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.sinc(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L711)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.sinc "Link to this definition")

Computes the normalized sinc of `input.`

outi\={1,if inputi\=0sin⁡(πinputi)/(πinputi),otherwise\\text{out}\_{i} = \\begin{cases} 1, & \\text{if}\\ \\text{input}\_{i}=0 \\\\ \\sin(\\pi \\text{input}\_{i}) / (\\pi \\text{input}\_{i}), & \\text{otherwise} \\end{cases} outi​\={1,sin(πinputi​)/(πinputi​),​if inputi​\=0otherwise​

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> t \= torch.randn(4)
\>>> t
tensor(\[ 0.2252, -0.2948,  1.0267, -1.1566\])
\>>> torch.special.sinc(t)
tensor(\[ 0.9186,  0.8631, -0.0259, -0.1300\])

Copy to clipboard

torch.special.softmax(_input_, _dim_, _\*_, _dtype\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L752)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.softmax "Link to this definition")

Computes the softmax function.

Softmax is defined as:

Softmax(xi)\=exp⁡(xi)∑jexp⁡(xj)\\text{Softmax}(x\_{i}) = \\frac{\\exp(x\_i)}{\\sum\_j \\exp(x\_j)}Softmax(xi​)\=∑j​exp(xj​)exp(xi​)​

It is applied to all slices along dim, and will re-scale them so that the elements lie in the range \[0, 1\] and sum to 1.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – input
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – A dimension along which softmax will be computed.
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. If specified, the input tensor is cast to `dtype` before the operation is performed. This is useful for preventing data type overflows. Default: None.
    

Examples::

\>>> t \= torch.ones(2, 2)
\>>> torch.special.softmax(t, 0)
tensor(\[\[0.5000, 0.5000\],\
        \[0.5000, 0.5000\]\])

Copy to clipboard

torch.special.spherical\_bessel\_j0(_input_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L1444)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.spherical_bessel_j0 "Link to this definition")

Spherical Bessel function of the first kind of order 000.

Parameters:

**input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the input tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

torch.special.xlog1py(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L432)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.xlog1py "Link to this definition")

Computes `input * log1p(other)` with the following cases.

outi\={NaNif otheri\=NaN0if inputi\=0.0 and otheri!\=NaNinputi∗log1p(otheri)otherwise\\text{out}\_{i} = \\begin{cases} \\text{NaN} & \\text{if } \\text{other}\_{i} = \\text{NaN} \\\\ 0 & \\text{if } \\text{input}\_{i} = 0.0 \\text{ and } \\text{other}\_{i} != \\text{NaN} \\\\ \\text{input}\_{i} \* \\text{log1p}(\\text{other}\_{i})& \\text{otherwise} \\end{cases} outi​\=⎩⎨⎧​NaN0inputi​∗log1p(otheri​)​if otheri​\=NaNif inputi​\=0.0 and otheri​!\=NaNotherwise​

Similar to SciPy’s scipy.special.xlog1py.

Parameters:

*   **input** (_Number_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Multiplier
    
*   **other** (_Number_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Argument
    

Note

At least one of `input` or `other` must be a tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> x \= torch.zeros(5,)
\>>> y \= torch.tensor(\[\-1, 0, 1, float('inf'), float('nan')\])
\>>> torch.special.xlog1py(x, y)
tensor(\[0., 0., 0., 0., nan\])
\>>> x \= torch.tensor(\[1, 2, 3\])
\>>> y \= torch.tensor(\[3, 2, 1\])
\>>> torch.special.xlog1py(x, y)
tensor(\[1.3863, 2.1972, 2.0794\])
\>>> torch.special.xlog1py(x, 4)
tensor(\[1.6094, 3.2189, 4.8283\])
\>>> torch.special.xlog1py(2, y)
tensor(\[2.7726, 2.1972, 1.3863\])

Copy to clipboard

torch.special.xlogy(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L477)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.xlogy "Link to this definition")

Computes `input * log(other)` with the following cases.

outi\={NaNif otheri\=NaN0if inputi\=0.0inputi∗log⁡(otheri)otherwise\\text{out}\_{i} = \\begin{cases} \\text{NaN} & \\text{if } \\text{other}\_{i} = \\text{NaN} \\\\ 0 & \\text{if } \\text{input}\_{i} = 0.0 \\\\ \\text{input}\_{i} \* \\log{(\\text{other}\_{i})} & \\text{otherwise} \\end{cases} outi​\=⎩⎨⎧​NaN0inputi​∗log(otheri​)​if otheri​\=NaNif inputi​\=0.0otherwise​

Similar to SciPy’s scipy.special.xlogy.

Parameters:

*   **input** (_Number_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Multiplier
    
*   **other** (_Number_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Argument
    

Note

At least one of `input` or `other` must be a tensor.

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> x \= torch.zeros(5,)
\>>> y \= torch.tensor(\[\-1, 0, 1, float('inf'), float('nan')\])
\>>> torch.special.xlogy(x, y)
tensor(\[0., 0., 0., 0., nan\])
\>>> x \= torch.tensor(\[1, 2, 3\])
\>>> y \= torch.tensor(\[3, 2, 1\])
\>>> torch.special.xlogy(x, y)
tensor(\[1.0986, 1.3863, 0.0000\])
\>>> torch.special.xlogy(x, 4)
tensor(\[1.3863, 2.7726, 4.1589\])
\>>> torch.special.xlogy(2, y)
tensor(\[2.1972, 1.3863, 0.0000\])

Copy to clipboard

torch.special.zeta(_input_, _other_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/special/__init__.py#L814)
[#](https://docs.pytorch.org/docs/2.15/special.html#torch.special.zeta "Link to this definition")

Computes the Hurwitz zeta function, elementwise.

ζ(x,q)\=∑k\=0∞1(k+q)x\\zeta(x, q) = \\sum\_{k=0}^{\\infty} \\frac{1}{(k + q)^x} ζ(x,q)\=k\=0∑∞​(k+q)x1​

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor corresponding to x.
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor corresponding to q.
    

Note

The Riemann zeta function corresponds to the case when q = 1

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example:

\>>> x \= torch.tensor(\[2., 4.\])
\>>> torch.special.zeta(x, 1)
tensor(\[1.6449, 1.0823\])
\>>> torch.special.zeta(x, torch.tensor(\[1., 2.\]))
tensor(\[1.6449, 0.0823\])
\>>> torch.special.zeta(2, torch.tensor(\[1., 2.\]))
tensor(\[1.6449, 0.6449\])

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/special.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/special.md.txt)

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