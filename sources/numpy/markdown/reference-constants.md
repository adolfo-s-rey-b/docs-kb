[Skip to main content](https://numpy.org/doc/stable/reference/constants.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/constants.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/constants.html)
[2.4](https://numpy.org/doc/2.4/reference/constants.html)
[2.3](https://numpy.org/doc/2.3/reference/constants.html)
[2.2](https://numpy.org/doc/2.2/reference/constants.html)
[2.1](https://numpy.org/doc/2.1/reference/constants.html)
[2.0](https://numpy.org/doc/2.0/reference/constants.html)
[1.26](https://numpy.org/doc/1.26/reference/constants.html)
[1.25](https://numpy.org/doc/1.25/reference/constants.html)
[1.24](https://numpy.org/doc/1.24/reference/constants.html)
[1.23](https://numpy.org/doc/1.23/reference/constants.html)
[1.22](https://numpy.org/doc/1.22/reference/constants.html)
[1.21](https://numpy.org/doc/1.21/reference/constants.html)
[1.20](https://numpy.org/doc/1.20/reference/constants.html)
[1.19](https://numpy.org/doc/1.19/reference/constants.html)
[1.18](https://numpy.org/doc/1.18/reference/constants.html)
[1.17](https://numpy.org/doc/1.17/reference/constants.html)
[1.16](https://numpy.org/doc/1.16/reference/constants.html)
[1.15](https://numpy.org/doc/1.15/reference/constants.html)
[1.14](https://numpy.org/doc/1.14/reference/constants.html)
[1.13](https://numpy.org/doc/1.13/reference/constants.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Constants[#](https://numpy.org/doc/stable/reference/constants.html#constants "Link to this heading")

=====================================================================================================

NumPy includes several constants:

numpy.e[#](https://numpy.org/doc/stable/reference/constants.html#numpy.e "Link to this definition")

Euler’s number, base of natural logarithms, Napier’s constant.

`e = 2.71828182845904523536028747135266249775724709369995...`

See Also

exp : Exponential function log : Natural logarithm

References

[https://en.wikipedia.org/wiki/E\_%28mathematical\_constant%29](https://en.wikipedia.org/wiki/E_%28mathematical_constant%29)

numpy.euler\_gamma[#](https://numpy.org/doc/stable/reference/constants.html#numpy.euler_gamma "Link to this definition")

`γ = 0.5772156649015328606065120900824024310421...`

References

[https://en.wikipedia.org/wiki/Euler%27s\_constant](https://en.wikipedia.org/wiki/Euler%27s_constant)

numpy.inf[#](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "Link to this definition")

IEEE 754 floating point representation of (positive) infinity.

Returns

yfloat

A floating point representation of positive infinity.

See Also

isinf : Shows which elements are positive or negative infinity

isposinf : Shows which elements are positive infinity

isneginf : Shows which elements are negative infinity

isnan : Shows which elements are Not a Number

isfinite : Shows which elements are finite (not one of Not a Number, positive infinity and negative infinity)

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity. Also that positive infinity is not equivalent to negative infinity. But infinity is equivalent to positive infinity.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.inf
inf
\>>> np.array(\[1\]) / 0.
array(\[inf\])

Copy to clipboard

Go BackOpen In Tab

numpy.nan[#](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "Link to this definition")

IEEE 754 floating point representation of Not a Number (NaN).

Returns

y : A floating point representation of Not a Number.

See Also

isnan : Shows which elements are Not a Number.

isfinite : Shows which elements are finite (not one of Not a Number, positive infinity and negative infinity)

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.nan
nan
\>>> np.log(\-1)
np.float64(nan)
\>>> np.log(\[\-1, 1, 2\])
array(\[       nan, 0.        , 0.69314718\])

Copy to clipboard

Go BackOpen In Tab

numpy.newaxis[#](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "Link to this definition")

A convenient alias for None, useful for indexing arrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.newaxis is None
True
\>>> x \= np.arange(3)
\>>> x
array(\[0, 1, 2\])
\>>> x\[:, np.newaxis\]
array(\[\[0\],\
\[1\],\
\[2\]\])
\>>> x\[:, np.newaxis, np.newaxis\]
array(\[\[\[0\]\],\
\[\[1\]\],\
\[\[2\]\]\])
\>>> x\[:, np.newaxis\] \* x
array(\[\[0, 0, 0\],\
    \[0, 1, 2\],\
    \[0, 2, 4\]\])

Copy to clipboard

Outer product, same as `outer(x, y)`:

\>>> y \= np.arange(3, 6)
\>>> x\[:, np.newaxis\] \* y
array(\[\[ 0,  0,  0\],\
    \[ 3,  4,  5\],\
    \[ 6,  8, 10\]\])

Copy to clipboard

`x[np.newaxis, :]` is equivalent to `x[np.newaxis]` and `x[None]`:

\>>> x\[np.newaxis, :\].shape
(1, 3)
\>>> x\[np.newaxis\].shape
(1, 3)
\>>> x\[None\].shape
(1, 3)
\>>> x\[:, np.newaxis\].shape
(3, 1)

Copy to clipboard

Go BackOpen In Tab

numpy.pi[#](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "Link to this definition")

`pi = 3.1415926535897932384626433...`

References

[https://en.wikipedia.org/wiki/Pi](https://en.wikipedia.org/wiki/Pi)

On this page