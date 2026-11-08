[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.where.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.where.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.where.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.where.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.where.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.where.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.where.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.where.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.where.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.where.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.where.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.where.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.where.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.where.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.where.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.where.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.where.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.where.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.where.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.where.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.where.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.where[#](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy-where "Link to this heading")

=====================================================================================================================

numpy.where(_condition_, \[_x_, _y_, \]_/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "Link to this definition")

Return elements chosen from _x_ or _y_ depending on _condition_.

Note

When only _condition_ is provided, this function is a shorthand for `np.asarray(condition).nonzero()`. Using [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
 directly should be preferred, as it behaves correctly for subclasses. The rest of this documentation covers only the case where all three arguments are provided.

Parameters:

**condition**array\_like, bool

Where True, yield _x_, otherwise yield _y_.

**x, y**array\_like

Values from which to choose. _x_, _y_ and _condition_ need to be broadcastable to some shape.

Returns:

**out**ndarray

An array with elements from _x_ where _condition_ is True, and elements from _y_ elsewhere.

See also

[`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")

[`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

The function that is called when x and y are omitted

Notes

If all the arrays are 1-D, [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
 is equivalent to:

\[xv if c else yv\
 for c, xv, yv in zip(condition, x, y)\]

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(10)
\>>> a
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> np.where(a < 5, a, 10\*a)
array(\[ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90\])

Copy to clipboard

This can be used on multidimensional arrays too:

\>>> np.where(\[\[True, False\], \[True, True\]\],
...          \[\[1, 2\], \[3, 4\]\],
...          \[\[9, 8\], \[7, 6\]\])
array(\[\[1, 8\],\
       \[3, 4\]\])

Copy to clipboard

The shapes of x, y, and the condition are broadcast together:

\>>> x, y \= np.ogrid\[:3, :4\]
\>>> np.where(x < y, x, 10 + y)  \# both x and 10+y are broadcast
array(\[\[10,  0,  0,  0\],\
       \[10, 11,  1,  1\],\
       \[10, 11, 12,  2\]\])

Copy to clipboard

\>>> a \= np.array(\[\[0, 1, 2\],\
...               \[0, 2, 4\],\
...               \[0, 3, 6\]\])
\>>> np.where(a < 4, a, \-1)  \# -1 is broadcast
array(\[\[ 0,  1,  2\],\
       \[ 0,  2, -1\],\
       \[ 0,  3, -1\]\])

Copy to clipboard

Go BackOpen In Tab

On this page