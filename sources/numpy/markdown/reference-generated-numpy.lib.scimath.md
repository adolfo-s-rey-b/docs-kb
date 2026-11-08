[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.scimath.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.scimath.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.scimath.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.scimath.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.scimath.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.scimath.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.scimath.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.scimath.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.scimath.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.scimath.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.scimath.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.scimath.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.scimath.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.scimath.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.scimath.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.scimath.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.scimath.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.scimath.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.scimath.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.scimath.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.scimath[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.html#module-numpy.lib.scimath "Link to this heading")

==============================================================================================================================================

Wrapper functions to more user-friendly calling of certain math functions whose output data-type is different than the input data-type in certain domains of the input.

For example, for functions like [`log`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.log.html#numpy.lib.scimath.log "numpy.lib.scimath.log")
 with branch cuts, the versions in this module provide the mathematically valid answers in the complex plane:

\>>> import math
\>>> np.emath.log(\-math.exp(1)) \== (1+1j\*math.pi)
True

Copy to clipboard

Similarly, [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.sqrt.html#numpy.lib.scimath.sqrt "numpy.lib.scimath.sqrt")
, other base logarithms, [`power`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html#numpy.lib.scimath.power "numpy.lib.scimath.power")
 and trig functions are correctly handled. See their respective docstrings for specific examples.

Functions

|     |     |
| --- | --- |
| [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arccos.html#numpy.lib.scimath.arccos "numpy.lib.scimath.arccos")<br>(x) | Compute the inverse cosine of x. |
| [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arcsin.html#numpy.lib.scimath.arcsin "numpy.lib.scimath.arcsin")<br>(x) | Compute the inverse sine of x. |
| [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arctanh.html#numpy.lib.scimath.arctanh "numpy.lib.scimath.arctanh")<br>(x) | Compute the inverse hyperbolic tangent of _x_. |
| [`log`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.log.html#numpy.lib.scimath.log "numpy.lib.scimath.log")<br>(x) | Compute the natural logarithm of _x_. |
| [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.log10.html#numpy.lib.scimath.log10 "numpy.lib.scimath.log10")<br>(x) | Compute the logarithm base 10 of _x_. |
| [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.log2.html#numpy.lib.scimath.log2 "numpy.lib.scimath.log2")<br>(x) | Compute the logarithm base 2 of _x_. |
| [`logn`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.logn.html#numpy.lib.scimath.logn "numpy.lib.scimath.logn")<br>(n, x) | Take log base n of x. |
| [`power`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html#numpy.lib.scimath.power "numpy.lib.scimath.power")<br>(x, p) | Return x to the power p, (x\*\*p). |
| [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.sqrt.html#numpy.lib.scimath.sqrt "numpy.lib.scimath.sqrt")<br>(x) | Compute the square root of x. |