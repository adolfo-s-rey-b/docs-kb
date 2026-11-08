[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.greater.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.greater.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.greater.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.greater.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.greater.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.greater.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.greater.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.greater.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.greater.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.greater.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.greater.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.greater.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.greater.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.greater.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.greater.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.greater.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.greater.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.greater.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.greater.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.greater.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.greater[#](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html#numpy-char-greater "Link to this heading")

==========================================================================================================================================

char.greater(_x1_, _x2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/defchararray.py#L198-L229)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.greater.html#numpy.char.greater "Link to this definition")

Return (x1 > x2) element-wise.

Unlike [`numpy.greater`](https://numpy.org/doc/stable/reference/generated/numpy.greater.html#numpy.greater "numpy.greater")
, this comparison is performed by first stripping whitespace characters from the end of the string. This behavior is provided for backward-compatibility with numarray.

Parameters:

**x1, x2**array\_like of str or unicode

Input arrays of the same shape.

Returns:

**out**ndarray

Output array of bools.

See also

[`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")
, [`not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy.not_equal "numpy.not_equal")
, [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater_equal "numpy.greater_equal")
, [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html#numpy.less_equal "numpy.less_equal")
, [`less`](https://numpy.org/doc/stable/reference/generated/numpy.less.html#numpy.less "numpy.less")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x1 \= np.array(\['a', 'b', 'c'\])
\>>> np.char.greater(x1, 'b')
array(\[False, False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page