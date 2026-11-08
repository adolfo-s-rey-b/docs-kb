[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy-array-equal "Link to this heading")

========================================================================================================================================

numpy.array\_equal(_a1_, _a2_, _equal\_nan\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2470-L2553)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal "Link to this definition")

True if two arrays have the same shape and elements, False otherwise.

Parameters:

**a1, a2**array\_like

Input arrays.

**equal\_nan**bool

Whether to compare NaN’s as equal. If the dtype of a1 and a2 is complex, values will be considered equal if either the real or the imaginary component of a given value is `nan`.

Returns:

**b**bool

Returns True if the arrays are equal.

See also

[`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")

Returns True if two arrays are element-wise equal within a tolerance.

[`array_equiv`](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#numpy.array_equiv "numpy.array_equiv")

Returns True if input arrays are shape consistent and all elements equal.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.array\_equal(\[1, 2\], \[1, 2\])
True

Copy to clipboard

\>>> np.array\_equal(np.array(\[1, 2\]), np.array(\[1, 2\]))
True

Copy to clipboard

\>>> np.array\_equal(\[1, 2\], \[1, 2, 3\])
False

Copy to clipboard

\>>> np.array\_equal(\[1, 2\], \[1, 4\])
False

Copy to clipboard

\>>> a \= np.array(\[1, np.nan\])
\>>> np.array\_equal(a, a)
False

Copy to clipboard

\>>> np.array\_equal(a, a, equal\_nan\=True)
True

Copy to clipboard

When `equal_nan` is True, complex values with nan components are considered equal if either the real _or_ the imaginary components are nan.

\>>> a \= np.array(\[1 + 1j\])
\>>> b \= a.copy()
\>>> a.real \= np.nan
\>>> b.imag \= np.nan
\>>> np.array\_equal(a, b, equal\_nan\=True)
True

Copy to clipboard

Go BackOpen In Tab

On this page