[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isfinite.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isfinite.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isfinite.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isfinite.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isfinite.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isfinite.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isfinite.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isfinite.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isfinite.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isfinite.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isfinite.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isfinite.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isfinite.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isfinite.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isfinite.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isfinite.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isfinite.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isfinite.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isfinite.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isfinite.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isfinite[#](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy-isfinite "Link to this heading")

==============================================================================================================================

numpy.isfinite(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'isfinite'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "Link to this definition")

Test element-wise for finiteness (not infinity and not Not a Number).

The result is returned as a boolean array.

Parameters:

**x**array\_like

Input values.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray, bool

True where `x` is not positive infinity, negative infinity, or NaN; false otherwise. This is a scalar if _x_ is a scalar.

See also

[`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")
, [`isneginf`](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf "numpy.isneginf")
, [`isposinf`](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf "numpy.isposinf")
, [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Notes

Not a Number, positive infinity and negative infinity are considered to be non-finite.

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity. Also that positive infinity is not equivalent to negative infinity. But infinity is equivalent to positive infinity. Errors result if the second argument is also supplied when _x_ is a scalar input, or if first and second arguments have different shapes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.isfinite(1)
True
\>>> np.isfinite(0)
True
\>>> np.isfinite(np.nan)
False
\>>> np.isfinite(np.inf)
False
\>>> np.isfinite(\-np.inf)
False
\>>> np.isfinite(\[np.log(\-1.),1.,np.log(0)\])
array(\[False,  True, False\])

Copy to clipboard

\>>> x \= np.array(\[\-np.inf, 0., np.inf\])
\>>> y \= np.array(\[2, 2, 2\])
\>>> np.isfinite(x, y)
array(\[0, 1, 0\])
\>>> y
array(\[0, 1, 0\])

Copy to clipboard

Go BackOpen In Tab

On this page