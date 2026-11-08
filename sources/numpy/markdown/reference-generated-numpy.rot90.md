[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rot90.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rot90.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rot90.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rot90.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rot90.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rot90.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rot90.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rot90.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rot90.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rot90.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rot90.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rot90.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rot90.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rot90.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rot90.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rot90.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rot90.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rot90.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rot90.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rot90.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rot90[#](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy-rot90 "Link to this heading")

=====================================================================================================================

numpy.rot90(_m_, _k\=1_, _axes\=(0, 1)_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L179-L276)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy.rot90 "Link to this definition")

Rotate an array by 90 degrees in the plane specified by axes.

Rotation direction is from the first towards the second axis. This means for a 2D array with the default _k_ and _axes_, the rotation will be counterclockwise.

Parameters:

**m**array\_like

Array of two or more dimensions.

**k**integer

Number of times the array is rotated by 90 degrees.

**axes**(2,) array\_like

The array is rotated in the plane defined by the axes. Axes must be different.

Returns:

**y**ndarray

A rotated view of _m_.

See also

[`flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "numpy.flip")

Reverse the order of elements in an array along the given axis.

[`fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")

Flip an array horizontally.

[`flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")

Flip an array vertically.

Notes

`rot90(m, k=1, axes=(1,0))` is the reverse of `rot90(m, k=1, axes=(0,1))`

`rot90(m, k=1, axes=(1,0))` is equivalent to `rot90(m, k=-1, axes=(0,1))`

Examples

Try it in your browser!

\>>> import numpy as np
\>>> m \= np.array(\[\[1,2\],\[3,4\]\], int)
\>>> m
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> np.rot90(m)
array(\[\[2, 4\],\
       \[1, 3\]\])
\>>> np.rot90(m, 2)
array(\[\[4, 3\],\
       \[2, 1\]\])
\>>> m \= np.arange(8).reshape((2,2,2))
\>>> np.rot90(m, 1, (1,2))
array(\[\[\[1, 3\],\
        \[0, 2\]\],\
       \[\[5, 7\],\
        \[4, 6\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page