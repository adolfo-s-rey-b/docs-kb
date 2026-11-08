[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndarray.fill.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.fill.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.fill.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.fill.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndarray.fill.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndarray.fill.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.fill.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndarray.fill.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndarray.fill.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndarray.fill.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndarray.fill.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndarray.fill.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndarray.fill.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndarray.fill.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.fill.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndarray.fill.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndarray.fill.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndarray.fill.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndarray.fill.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndarray.fill.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.fill[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy-ndarray-fill "Link to this heading")

==========================================================================================================================================

method

ndarray.fill(_value_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "Link to this definition")

Fill the array with a scalar value.

Parameters:

**value**scalar

All elements of _a_ will be assigned this value.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1, 2\])
\>>> a.fill(0)
\>>> a
array(\[0, 0\])
\>>> a \= np.empty(2)
\>>> a.fill(1)
\>>> a
array(\[1.,  1.\])

Copy to clipboard

Fill expects a scalar value and always behaves the same as assigning to a single array element. The following is a rare example where this distinction is important:

\>>> a \= np.array(\[None, None\], dtype\=np.object\_)
\>>> a\[0\] \= np.array(3)
\>>> a
array(\[array(3), None\], dtype=object)
\>>> a.fill(np.array(3))
\>>> a
array(\[array(3), array(3)\], dtype=object)

Copy to clipboard

Where other forms of assignments will unpack the array being assigned:

\>>> a\[...\] \= np.array(3)
\>>> a
array(\[3, 3\], dtype=object)

Copy to clipboard

Go BackOpen In Tab

On this page