[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isposinf[#](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy-isposinf "Link to this heading")

==============================================================================================================================

numpy.isposinf(_x_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_ufunclike_impl.py#L75-L142)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf "Link to this definition")

Test element-wise for positive infinity, return result as bool array.

Parameters:

**x**array\_like

The input array.

**out**array\_like, optional

A location into which the result is stored. If provided, it must have a shape that the input broadcasts to. If not provided or None, a freshly-allocated boolean array is returned.

Returns:

**out**ndarray

A boolean array with the same dimensions as the input. If second argument is not supplied then a boolean array is returned with values True where the corresponding element of the input is positive infinity and values False where the element of the input is not positive infinity.

If a second argument is supplied the result is stored there. If the type of that array is a numeric type the result is represented as zeros and ones, if the type is boolean then as False and True. The return value _out_ is then a reference to that array.

See also

[`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")
, [`isneginf`](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf "numpy.isneginf")
, [`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")
, [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754).

Errors result if the second argument is also supplied when x is a scalar input, if first and second arguments have different shapes, or if the first argument has complex values

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.isposinf(np.inf)
True
\>>> np.isposinf(\-np.inf)
False
\>>> np.isposinf(\[\-np.inf, 0., np.inf\])
array(\[False, False,  True\])

Copy to clipboard

\>>> x \= np.array(\[\-np.inf, 0., np.inf\])
\>>> y \= np.array(\[2, 2, 2\])
\>>> np.isposinf(x, y)
array(\[0, 0, 1\])
\>>> y
array(\[0, 0, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page