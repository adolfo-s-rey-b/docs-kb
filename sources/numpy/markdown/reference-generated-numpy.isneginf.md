[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isneginf.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isneginf.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isneginf.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isneginf.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isneginf.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isneginf.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isneginf.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isneginf.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isneginf.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isneginf.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isneginf.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isneginf.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isneginf.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isneginf.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isneginf.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isneginf.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isneginf.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isneginf.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isneginf.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isneginf.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isneginf[#](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy-isneginf "Link to this heading")

==============================================================================================================================

numpy.isneginf(_x_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_ufunclike_impl.py#L145-L212)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf "Link to this definition")

Test element-wise for negative infinity, return result as bool array.

Parameters:

**x**array\_like

The input array.

**out**array\_like, optional

A location into which the result is stored. If provided, it must have a shape that the input broadcasts to. If not provided or None, a freshly-allocated boolean array is returned.

Returns:

**out**ndarray

A boolean array with the same dimensions as the input. If second argument is not supplied then a numpy boolean array is returned with values True where the corresponding element of the input is negative infinity and values False where the element of the input is not negative infinity.

If a second argument is supplied the result is stored there. If the type of that array is a numeric type the result is represented as zeros and ones, if the type is boolean then as False and True. The return value _out_ is then a reference to that array.

See also

[`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")
, [`isposinf`](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf "numpy.isposinf")
, [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")
, [`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754).

Errors result if the second argument is also supplied when x is a scalar input, if first and second arguments have different shapes, or if the first argument has complex values.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.isneginf(\-np.inf)
True
\>>> np.isneginf(np.inf)
False
\>>> np.isneginf(\[\-np.inf, 0., np.inf\])
array(\[ True, False, False\])

Copy to clipboard

\>>> x \= np.array(\[\-np.inf, 0., np.inf\])
\>>> y \= np.array(\[2, 2, 2\])
\>>> np.isneginf(x, y)
array(\[1, 0, 0\])
\>>> y
array(\[1, 0, 0\])

Copy to clipboard

Go BackOpen In Tab

On this page