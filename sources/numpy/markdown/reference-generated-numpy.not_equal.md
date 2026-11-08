[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.not_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.not_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.not_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.not_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.not_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.not_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.not_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.not_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.not_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.not_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.not_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.not_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.not_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.not_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.not_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.not_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.not_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.not_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.not_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.not_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.not\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy-not-equal "Link to this heading")

==================================================================================================================================

numpy.not\_equal(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'not\_equal'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy.not_equal "Link to this definition")

Return (x1 != x2) element-wise.

Parameters:

**x1, x2**array\_like

Input arrays. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

Output array, element-wise comparison of _x1_ and _x2_. Typically of type bool, unless `dtype=np.object_` is passed. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")
, [`greater`](https://numpy.org/doc/stable/reference/generated/numpy.greater.html#numpy.greater "numpy.greater")
, [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater_equal "numpy.greater_equal")
, [`less`](https://numpy.org/doc/stable/reference/generated/numpy.less.html#numpy.less "numpy.less")
, [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html#numpy.less_equal "numpy.less_equal")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.not\_equal(\[1.,2.\], \[1., 3.\])
array(\[False,  True\])
\>>> np.not\_equal(\[1, 2\], \[\[1, 3\],\[1, 4\]\])
array(\[\[False,  True\],\
       \[False,  True\]\])

Copy to clipboard

The `!=` operator can be used as a shorthand for `np.not_equal` on ndarrays.

\>>> a \= np.array(\[1., 2.\])
\>>> b \= np.array(\[1., 3.\])
\>>> a != b
array(\[False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page