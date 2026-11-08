[Skip to main content](https://numpy.org/doc/stable/reference/routines.emath.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.emath.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.emath.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.emath.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.emath.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.emath.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.emath.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.emath.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.emath.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.emath.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.emath.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.emath.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.emath.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.emath.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.emath.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.emath.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.emath.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.emath.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.emath.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.emath.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.emath.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.emath.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Mathematical functions with automatic domain[#](https://numpy.org/doc/stable/reference/routines.emath.html#mathematical-functions-with-automatic-domain "Link to this heading")

================================================================================================================================================================================

Note

`numpy.emath` is a preferred alias for `numpy.lib.scimath`, available after [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
 is imported.

Wrapper functions to more user-friendly calling of certain math functions whose output data-type is different than the input data-type in certain domains of the input.

For example, for functions like [`log`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log.html#numpy.emath.log "numpy.emath.log")
 with branch cuts, the versions in this module provide the mathematically valid answers in the complex plane:

\>>> import numpy as np
\>>> import math
\>>> np.emath.log(\-math.exp(1)) \== (1+1j\*math.pi)
True

Copy to clipboard

Similarly, [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#numpy.emath.sqrt "numpy.emath.sqrt")
, other base logarithms, [`power`](https://numpy.org/doc/stable/reference/generated/numpy.emath.power.html#numpy.emath.power "numpy.emath.power")
 and trig functions are correctly handled. See their respective docstrings for specific examples.

Functions[#](https://numpy.org/doc/stable/reference/routines.emath.html#functions "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arccos.html#numpy.emath.arccos "numpy.emath.arccos")<br>(x) | Compute the inverse cosine of x. |
| [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arcsin.html#numpy.emath.arcsin "numpy.emath.arcsin")<br>(x) | Compute the inverse sine of x. |
| [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arctanh.html#numpy.emath.arctanh "numpy.emath.arctanh")<br>(x) | Compute the inverse hyperbolic tangent of _x_. |
| [`log`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log.html#numpy.emath.log "numpy.emath.log")<br>(x) | Compute the natural logarithm of _x_. |
| [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log2.html#numpy.emath.log2 "numpy.emath.log2")<br>(x) | Compute the logarithm base 2 of _x_. |
| [`logn`](https://numpy.org/doc/stable/reference/generated/numpy.emath.logn.html#numpy.emath.logn "numpy.emath.logn")<br>(n, x) | Take log base n of x. |
| [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html#numpy.emath.log10 "numpy.emath.log10")<br>(x) | Compute the logarithm base 10 of _x_. |
| [`power`](https://numpy.org/doc/stable/reference/generated/numpy.emath.power.html#numpy.emath.power "numpy.emath.power")<br>(x, p) | Return x to the power p, (x\*\*p). |
| [`sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#numpy.emath.sqrt "numpy.emath.sqrt")<br>(x) | Compute the square root of x. |

On this page